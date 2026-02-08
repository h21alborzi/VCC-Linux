"""
GPU encoder detection for VCC.

Probes FFmpeg to discover which hardware-accelerated video encoders
are available on the current system (NVIDIA NVENC, AMD AMF, Intel QSV).
"""

import os
import glob
import shutil
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import dataclass, field


@dataclass
class GpuEncoder:
    """Metadata for a single GPU-accelerated encoder."""
    name: str               # FFmpeg encoder name, e.g. "h264_nvenc"
    vendor: str             # "NVIDIA", "AMD", or "Intel"
    codec_family: str       # "H.264", "H.265", or "AV1"
    display_name: str       # Human-readable, e.g. "H.264 (NVIDIA NVENC)"
    container: str          # Default output container
    quality_param: str      # The param that replaces CRF, e.g. "cq"
    quality_default: int    # Sensible default for quality param
    quality_min: int
    quality_max: int
    quality_label: str      # Label shown in UI, e.g. "CQ (Quality)"
    quality_tooltip: str    # Tooltip for the quality parameter
    preset_key: str         # FFmpeg flag name, e.g. "preset" or "-quality"
    preset_type: str        # "choice" or "int"
    preset_values: list = field(default_factory=list)
    preset_default: str | int = ""
    preset_tooltip: str = ""
    hwaccel_flag: str = ""  # e.g. "cuda", "d3d11va", "qsv" for input decoding
    max_bit_depth: int = 10  # Max bit depth the encoder supports (8 or 10)


# ── NVIDIA NVENC ──────────────────────────────────────────────────────

_NVENC_QUALITY_TOOLTIP = (
    "Constant Quality (CQ) — NVENC equivalent of CRF.\n\n"
    "Lower value (0) = HIGHEST quality, LARGEST file.\n"
    "Higher value (51) = LOWEST quality, SMALLEST file.\n\n"
    "Recommended: 24-30 for good quality.\n"
    "Visually transparent: ~20-25."
)
_NVENC_PRESET_TOOLTIP = (
    "NVENC performance/quality trade-off preset.\n\n"
    "p1 = FASTEST encoding, LOWEST quality.\n"
    "p7 = SLOWEST encoding, HIGHEST quality.\n\n"
    "Recommended: p4-p5 for a good balance.\n"
    "p6-p7 for archival or high quality."
)

_NVENC_H264 = GpuEncoder(
    name="h264_nvenc", vendor="NVIDIA", codec_family="H.264",
    display_name="H.264 (NVIDIA NVENC)",
    container="mkv",
    quality_param="cq", quality_default=28, quality_min=0, quality_max=51,
    quality_label="CQ (Quality)", quality_tooltip=_NVENC_QUALITY_TOOLTIP,
    preset_key="preset", preset_type="choice",
    preset_values=["p1", "p2", "p3", "p4", "p5", "p6", "p7"],
    preset_default="p4", preset_tooltip=_NVENC_PRESET_TOOLTIP,
    hwaccel_flag="cuda",
    max_bit_depth=8,  # H.264 NVENC does NOT support 10-bit
)

_NVENC_HEVC = GpuEncoder(
    name="hevc_nvenc", vendor="NVIDIA", codec_family="H.265",
    display_name="H.265/HEVC (NVIDIA NVENC)",
    container="mkv",
    quality_param="cq", quality_default=28, quality_min=0, quality_max=51,
    quality_label="CQ (Quality)", quality_tooltip=_NVENC_QUALITY_TOOLTIP,
    preset_key="preset", preset_type="choice",
    preset_values=["p1", "p2", "p3", "p4", "p5", "p6", "p7"],
    preset_default="p4", preset_tooltip=_NVENC_PRESET_TOOLTIP,
    hwaccel_flag="cuda",
)

_NVENC_AV1 = GpuEncoder(
    name="av1_nvenc", vendor="NVIDIA", codec_family="AV1",
    display_name="AV1 (NVIDIA NVENC)",
    container="mkv",
    quality_param="cq", quality_default=28, quality_min=0, quality_max=51,
    quality_label="CQ (Quality)", quality_tooltip=_NVENC_QUALITY_TOOLTIP,
    preset_key="preset", preset_type="choice",
    preset_values=["p1", "p2", "p3", "p4", "p5", "p6", "p7"],
    preset_default="p4", preset_tooltip=_NVENC_PRESET_TOOLTIP,
    hwaccel_flag="cuda",
)

# ── AMD AMF ───────────────────────────────────────────────────────────

_AMF_QUALITY_TOOLTIP = (
    "Quantization Parameter — AMF equivalent of CRF.\n\n"
    "Lower value (0) = HIGHEST quality, LARGEST file.\n"
    "Higher value (51) = LOWEST quality, SMALLEST file.\n\n"
    "Recommended: 22-30 for good quality."
)
_AMF_PRESET_TOOLTIP = (
    "AMF encoding quality/speed trade-off.\n\n"
    "speed    = FASTEST encoding, LOWEST quality.\n"
    "balanced = Good balance of speed and quality.\n"
    "quality  = SLOWER encoding, BETTER quality.\n\n"
    "Recommended: balanced or quality."
)

_AMF_H264 = GpuEncoder(
    name="h264_amf", vendor="AMD", codec_family="H.264",
    display_name="H.264 (AMD AMF)",
    container="mkv",
    quality_param="qp_i", quality_default=26, quality_min=0, quality_max=51,
    quality_label="QP (Quality)", quality_tooltip=_AMF_QUALITY_TOOLTIP,
    preset_key="quality", preset_type="choice",
    preset_values=["speed", "balanced", "quality"],
    preset_default="balanced", preset_tooltip=_AMF_PRESET_TOOLTIP,
    hwaccel_flag="d3d11va",
    max_bit_depth=8,  # H.264 AMF does NOT support 10-bit
)

_AMF_HEVC = GpuEncoder(
    name="hevc_amf", vendor="AMD", codec_family="H.265",
    display_name="H.265/HEVC (AMD AMF)",
    container="mkv",
    quality_param="qp_i", quality_default=28, quality_min=0, quality_max=51,
    quality_label="QP (Quality)", quality_tooltip=_AMF_QUALITY_TOOLTIP,
    preset_key="quality", preset_type="choice",
    preset_values=["speed", "balanced", "quality"],
    preset_default="balanced", preset_tooltip=_AMF_PRESET_TOOLTIP,
    hwaccel_flag="d3d11va",
)

_AMF_AV1 = GpuEncoder(
    name="av1_amf", vendor="AMD", codec_family="AV1",
    display_name="AV1 (AMD AMF)",
    container="mkv",
    quality_param="qp_i", quality_default=28, quality_min=0, quality_max=51,
    quality_label="QP (Quality)", quality_tooltip=_AMF_QUALITY_TOOLTIP,
    preset_key="quality", preset_type="choice",
    preset_values=["speed", "balanced", "quality", "high_quality"],
    preset_default="balanced",
    preset_tooltip=(
        "AMF encoding quality/speed trade-off.\n\n"
        "speed        = FASTEST encoding.\n"
        "balanced     = Good balance.\n"
        "quality      = Better quality.\n"
        "high_quality = BEST quality, SLOWEST.\n\n"
        "Recommended: balanced or quality."
    ),
    hwaccel_flag="d3d11va",
)

# ── Intel QSV ─────────────────────────────────────────────────────────

_QSV_QUALITY_TOOLTIP = (
    "Global Quality — Intel QSV equivalent of CRF.\n\n"
    "Lower value (1) = HIGHEST quality, LARGEST file.\n"
    "Higher value (51) = LOWEST quality, SMALLEST file.\n\n"
    "Recommended: 22-30 for good quality."
)
_QSV_PRESET_TOOLTIP = (
    "QSV speed preset.\n\n"
    "veryfast = FASTEST encoding, WORST quality.\n"
    "veryslow = SLOWEST encoding, BEST quality.\n\n"
    "Recommended: medium or slow."
)

_QSV_H264 = GpuEncoder(
    name="h264_qsv", vendor="Intel", codec_family="H.264",
    display_name="H.264 (Intel QSV)",
    container="mkv",
    quality_param="global_quality", quality_default=25, quality_min=1, quality_max=51,
    quality_label="Global Quality", quality_tooltip=_QSV_QUALITY_TOOLTIP,
    preset_key="preset", preset_type="choice",
    preset_values=["veryfast", "faster", "fast", "medium", "slow", "veryslow"],
    preset_default="medium", preset_tooltip=_QSV_PRESET_TOOLTIP,
    hwaccel_flag="qsv",
    max_bit_depth=8,  # H.264 QSV does NOT support 10-bit
)

_QSV_HEVC = GpuEncoder(
    name="hevc_qsv", vendor="Intel", codec_family="H.265",
    display_name="H.265/HEVC (Intel QSV)",
    container="mkv",
    quality_param="global_quality", quality_default=28, quality_min=1, quality_max=51,
    quality_label="Global Quality", quality_tooltip=_QSV_QUALITY_TOOLTIP,
    preset_key="preset", preset_type="choice",
    preset_values=["veryfast", "faster", "fast", "medium", "slow", "veryslow"],
    preset_default="medium", preset_tooltip=_QSV_PRESET_TOOLTIP,
    hwaccel_flag="qsv",
)

_QSV_AV1 = GpuEncoder(
    name="av1_qsv", vendor="Intel", codec_family="AV1",
    display_name="AV1 (Intel QSV)",
    container="mkv",
    quality_param="global_quality", quality_default=28, quality_min=1, quality_max=51,
    quality_label="Global Quality", quality_tooltip=_QSV_QUALITY_TOOLTIP,
    preset_key="preset", preset_type="choice",
    preset_values=["veryfast", "faster", "fast", "medium", "slow", "veryslow"],
    preset_default="medium", preset_tooltip=_QSV_PRESET_TOOLTIP,
    hwaccel_flag="qsv",
)

# -- All known GPU encoders (in display order) --------------------------

ALL_GPU_ENCODERS: list[GpuEncoder] = [
    _NVENC_H264, _NVENC_HEVC, _NVENC_AV1,
    _AMF_H264,   _AMF_HEVC,   _AMF_AV1,
    _QSV_H264,   _QSV_HEVC,   _QSV_AV1,
]

_GPU_ENCODER_MAP: dict[str, GpuEncoder] = {e.name: e for e in ALL_GPU_ENCODERS}


# ── FFmpeg location (reuse from encoder.py) ────────────────────────────

def _find_ffmpeg() -> str | None:
    """Locate ffmpeg executable."""
    path = shutil.which("ffmpeg")
    if path:
        return path

    winget_links = os.path.expandvars(
        r"%LOCALAPPDATA%\Microsoft\WinGet\Links\ffmpeg.exe"
    )
    if os.path.isfile(winget_links):
        return winget_links

    winget_pkgs = os.path.expandvars(
        r"%LOCALAPPDATA%\Microsoft\WinGet\Packages"
    )
    for pattern in [
        os.path.join(winget_pkgs, "Gyan.FFmpeg*", "ffmpeg-*", "bin", "ffmpeg.exe"),
        os.path.join(winget_pkgs, "Gyan.FFmpeg*", "ffmpeg.exe"),
    ]:
        matches = glob.glob(pattern)
        if matches:
            return matches[0]

    for candidate in [
        r"C:\ffmpeg\bin\ffmpeg.exe",
        r"C:\Program Files\ffmpeg\bin\ffmpeg.exe",
        r"C:\Program Files (x86)\ffmpeg\bin\ffmpeg.exe",
    ]:
        if os.path.isfile(candidate):
            return candidate

    return None


# ── Probing ────────────────────────────────────────────────────────────

_cached_result: list[GpuEncoder] | None = None


def probe_available_gpu_encoders(force: bool = False) -> list[GpuEncoder]:
    """Query FFmpeg for which GPU encoders are actually available.

    First checks if FFmpeg was compiled with each encoder, then does a
    real hardware test-encode to verify the GPU actually supports it.
    Results are cached so repeated calls are fast.
    Pass *force=True* to re-probe (e.g. after changing FFmpeg path).
    """
    global _cached_result
    if _cached_result is not None and not force:
        return _cached_result

    ffmpeg = _find_ffmpeg()
    if not ffmpeg:
        _cached_result = []
        return _cached_result

    # Step 1: check which encoders FFmpeg was compiled with
    try:
        result = subprocess.run(
            [ffmpeg, "-hide_banner", "-encoders"],
            capture_output=True, text=True, timeout=10,
            creationflags=0x08000000 if os.name == "nt" else 0,  # CREATE_NO_WINDOW
        )
        output = result.stdout
    except Exception:
        _cached_result = []
        return _cached_result

    candidates: list[GpuEncoder] = []
    for enc in ALL_GPU_ENCODERS:
        if f" {enc.name} " in output or f" {enc.name}\n" in output:
            candidates.append(enc)

    # Step 2: real hardware probe — test-encode in PARALLEL for speed
    available: list[GpuEncoder] = []
    with ThreadPoolExecutor(max_workers=len(candidates) or 1) as pool:
        futures = {
            pool.submit(_test_encoder, ffmpeg, enc.name): enc
            for enc in candidates
        }
        for future in as_completed(futures):
            if future.result():
                available.append(futures[future])

    # Preserve display order (same as ALL_GPU_ENCODERS)
    order = {e.name: i for i, e in enumerate(ALL_GPU_ENCODERS)}
    available.sort(key=lambda e: order.get(e.name, 999))

    _cached_result = available
    return _cached_result


def _test_encoder(ffmpeg: str, encoder_name: str) -> bool:
    """Run a tiny test encode to check if a GPU encoder actually works
    on the current hardware (not just compiled into FFmpeg)."""
    # Try without and with hwaccel init (NVENC may need CUDA context)
    for extra_args in [[], ["-hwaccel", "cuda"]]:
        try:
            cmd = [
                ffmpeg, "-hide_banner", "-loglevel", "error",
                *extra_args,
                "-f", "lavfi", "-i", "color=black:s=256x256:d=0.04:r=1",
                "-c:v", encoder_name, "-frames:v", "1",
                "-f", "null", "-",
            ]
            result = subprocess.run(
                cmd,
                capture_output=True, text=True, timeout=5,
                creationflags=0x08000000 if os.name == "nt" else 0,
            )
            if result.returncode == 0:
                return True
        except Exception:
            continue
    return False


def get_gpu_encoder(name: str) -> GpuEncoder | None:
    """Look up a GpuEncoder by its FFmpeg encoder name."""
    return _GPU_ENCODER_MAP.get(name)


def is_gpu_encoder(name: str) -> bool:
    """Return True if *name* is a known GPU encoder."""
    return name in _GPU_ENCODER_MAP
