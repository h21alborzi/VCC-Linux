"""
Pixel format definitions and help text for VCC.
"""

import glob
import os
import re
import shutil
import subprocess

PIXEL_FORMATS = [
    # (ffmpeg_name, display_label, bit_depth, chroma_subsampling, has_alpha, description)
    ("yuv420p",      "YUV 4:2:0  8-bit",         8,  "4:2:0", False, "Standard 8-bit. Most compatible. Good for general video."),
    ("yuv420p10le",  "YUV 4:2:0 10-bit",         10, "4:2:0", False, "10-bit color depth. Reduces banding, slightly larger. Recommended for AV1/HEVC."),
    ("yuv422p",      "YUV 4:2:2  8-bit",         8,  "4:2:2", False, "Higher chroma resolution. Used in professional/broadcast."),
    ("yuv422p10le",  "YUV 4:2:2 10-bit",         10, "4:2:2", False, "Professional 10-bit with full chroma. Broadcast quality."),
    ("yuv444p",      "YUV 4:4:4  8-bit",         8,  "4:4:4", False, "Full chroma resolution. Best color accuracy, larger files."),
    ("yuv444p10le",  "YUV 4:4:4 10-bit",         10, "4:4:4", False, "Maximum color accuracy. Very large files. Professional grading."),
    ("yuva420p",     "YUVA 4:2:0  8-bit (Alpha)", 8,  "4:2:0", True,  "8-bit with alpha transparency channel."),
    ("yuva420p10le", "YUVA 4:2:0 10-bit (Alpha)", 10, "4:2:0", True,  "10-bit with alpha transparency channel."),
    ("nv12",         "NV12 (Semi-planar 4:2:0)",   8, "4:2:0", False, "Hardware-friendly semi-planar format. Used by GPU encoders."),
    ("p010le",       "P010 (Semi-planar 10-bit)",  10,"4:2:0", False, "10-bit semi-planar. Used by hardware encoders (NVENC/QSV)."),
    ("gray",         "Grayscale 8-bit",            8, "N/A",   False, "Monochrome / black-and-white video."),
    ("gray10le",     "Grayscale 10-bit",           10,"N/A",   False, "10-bit monochrome."),
    ("rgb24",        "RGB 24-bit",                 8, "4:4:4", False, "Direct RGB. Not typical for video compression. Large files."),
    ("gbrp",         "GBR Planar 8-bit",           8, "4:4:4", False, "Planar RGB used internally by some encoders."),
    ("gbrp10le",     "GBR Planar 10-bit",          10,"4:4:4", False, "10-bit planar RGB."),
]

PIXEL_FORMAT_HELP_TEXT = """\
<h2>Pixel Formats &amp; Color Models</h2>

<h3>What is a Pixel Format?</h3>
<p>The pixel format defines how color information is stored for each pixel in a video frame.
It determines the <b>color model</b> (YUV vs RGB), <b>chroma subsampling</b> (how much color
detail is kept), <b>bit depth</b> (precision of each color value), and whether an
<b>alpha (transparency) channel</b> is included.</p>

<hr>

<h3>Color Models</h3>

<h4>YUV (YCbCr)</h4>
<p>The standard for video. Separates brightness (Y / luma) from color (U,V / chroma).
Human eyes are more sensitive to brightness than color, so we can reduce color
information without noticeable quality loss &mdash; this is the basis of chroma subsampling.</p>

<h4>RGB</h4>
<p>Red, Green, Blue channels. Used in displays and image editing. Not efficient for
video compression because all three channels carry equal weight, making files larger.
Generally only used for special workflows (screen recording, compositing).</p>

<hr>

<h3>Chroma Subsampling</h3>
<table border="1" cellpadding="6" cellspacing="0" style="border-collapse:collapse;">
<tr><th>Subsampling</th><th>Color Resolution</th><th>Use Case</th><th>File Size</th></tr>
<tr><td><b>4:4:4</b></td><td>Full color for every pixel</td>
    <td>Professional grading, text/graphics overlay</td><td>Largest</td></tr>
<tr><td><b>4:2:2</b></td><td>Half horizontal color resolution</td>
    <td>Broadcast, professional video</td><td>Medium</td></tr>
<tr><td><b>4:2:0</b></td><td>Half horizontal &amp; half vertical color</td>
    <td>Consumer video, streaming, Blu-ray</td><td>Smallest</td></tr>
</table>
<p><b>Recommendation:</b> 4:2:0 is the standard for virtually all consumer video.
Choose 4:2:2 or 4:4:4 only for professional workflows.</p>

<hr>

<h3>Bit Depth</h3>
<table border="1" cellpadding="6" cellspacing="0" style="border-collapse:collapse;">
<tr><th>Depth</th><th>Values per Channel</th><th>Effect</th></tr>
<tr><td><b>8-bit</b></td><td>256</td>
    <td>Standard. May show <i>banding</i> in smooth gradients (e.g., skies, dark scenes).</td></tr>
<tr><td><b>10-bit</b></td><td>1024</td>
    <td>Greatly reduces banding. Better for HDR and modern codecs (AV1, HEVC). \
Slightly larger files but <b>often encodes more efficiently</b> in modern codecs.</td></tr>
<tr><td><b>12-bit</b></td><td>4096</td>
    <td>Professional / cinema. Rarely needed for consumer content.</td></tr>
</table>
<p><b>Lower bit depth (8-bit):</b> Smaller files, more compatible, may show color banding.<br>
<b>Higher bit depth (10-bit):</b> Smoother gradients, better for modern codecs. \
<b>Recommended for AV1 and HEVC.</b></p>

<hr>

<h3>Alpha Channel</h3>
<p>An alpha channel stores <b>transparency information</b> per pixel (0 = fully transparent,
max = fully opaque). This is used for:</p>
<ul>
<li>Overlays, lower thirds, motion graphics</li>
<li>Green-screen keying output</li>
<li>Compositing in video editors</li>
</ul>
<p>Formats with alpha (e.g., <code>yuva420p</code>) produce larger files. Most consumer video
does <b>not</b> need alpha. Only codecs like VP9 and AV1 support alpha in video;
H.264 and H.265 do <b>not</b>.</p>

<hr>

<h3>Codec Compatibility</h3>
<p>VCC <b>automatically filters</b> the pixel format dropdown based on the selected codec.
You will only see formats that the encoder actually supports, so you cannot pick an
incompatible combination.</p>

<table border="1" cellpadding="5" cellspacing="0" style="border-collapse:collapse;">
<tr><th>Codec</th><th>8-bit</th><th>10-bit</th><th>Best Choice</th></tr>
<tr><td><b>AV1 (SVT-AV1)</b></td><td>yuv420p</td><td>yuv420p10le</td>
    <td>&#x2B50; yuv420p10le (10-bit helps AV1 compress better)</td></tr>
<tr><td><b>H.264 (x264)</b></td><td>yuv420p + many</td><td>yuv420p10le + more</td>
    <td>yuv420p for compatibility, yuv420p10le for quality</td></tr>
<tr><td><b>H.265 (x265)</b></td><td>yuv420p + many</td><td>yuv420p10le + many</td>
    <td>&#x2B50; yuv420p10le (10-bit recommended for HEVC)</td></tr>
<tr><td><b>H.266 (VVC)</b></td><td>&mdash;</td><td>yuv420p10le only</td>
    <td>yuv420p10le (only option)</td></tr>
<tr><td><b>VP9</b></td><td>yuv420p + many</td><td>yuv420p10le + more</td>
    <td>yuv420p for web, yuv420p10le for quality</td></tr>
</table>

<h4>GPU Encoder Pixel Formats</h4>
<p>GPU encoders have simpler pixel format support. FFmpeg <b>auto-converts</b> between
format names transparently (e.g. <code>yuv420p10le</code> is internally mapped to
<code>p010le</code> for hardware encoders), so you can pick any shown format normally.</p>

<table border="1" cellpadding="5" cellspacing="0" style="border-collapse:collapse;">
<tr><th>GPU Encoder</th><th>Bit Depth</th><th>Best Choice</th></tr>
<tr><td><b>H.264 NVENC / AMF / QSV</b></td><td><b>8-bit only</b></td>
    <td>yuv420p or nv12</td></tr>
<tr><td><b>H.265 NVENC / AMF / QSV</b></td><td>8-bit and 10-bit</td>
    <td>&#x2B50; yuv420p10le (auto-converted to p010le)</td></tr>
<tr><td><b>AV1 NVENC / AMF / QSV</b></td><td>8-bit and 10-bit</td>
    <td>&#x2B50; yuv420p10le</td></tr>
</table>

<p><b>Important:</b> H.264 (all vendors) does <b>not</b> support 10-bit encoding.
VCC hides 10-bit formats when an H.264 GPU encoder is selected.</p>

<hr>

<h3>Recommendations</h3>
<p><b>General consumer video:</b> <code>yuv420p</code> (8-bit) or <code>yuv420p10le</code> (10-bit).<br>
<b>Best quality/size for modern codecs (AV1, HEVC):</b> <code>yuv420p10le</code> &mdash; 10-bit \
actually helps the encoder produce smaller files with fewer artifacts.<br>
<b>Maximum compatibility:</b> <code>yuv420p</code> (works everywhere).<br>
<b>Professional / broadcast:</b> <code>yuv422p10le</code>.<br>
<b>Need transparency:</b> <code>yuva420p</code> with VP9 or AV1.<br>
<b>GPU encoding:</b> For H.264 GPU use <code>yuv420p</code>; for H.265/AV1 GPU use <code>yuv420p10le</code>.</p>
"""


# ---------------------------------------------------------------------------
# Query FFmpeg for per-encoder pixel format support
# ---------------------------------------------------------------------------

def _find_ffmpeg() -> str | None:
    """Locate ffmpeg executable (lightweight duplicate to avoid circular imports)."""
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


_pix_fmt_cache: dict[str, list[str] | None] = {}


def query_encoder_pix_fmts(encoder_name: str) -> list[str] | None:
    """Query FFmpeg for the pixel formats supported by *encoder_name*.

    Returns a list of FFmpeg pix_fmt names that the encoder accepts,
    or ``None`` if the query fails (in which case the caller should
    show all formats).  Results are cached.
    """
    if encoder_name in _pix_fmt_cache:
        return _pix_fmt_cache[encoder_name]

    ffmpeg = _find_ffmpeg()
    if not ffmpeg:
        _pix_fmt_cache[encoder_name] = None
        return None

    try:
        result = subprocess.run(
            [ffmpeg, "-hide_banner", "-h", f"encoder={encoder_name}"],
            capture_output=True, text=True, timeout=10,
            creationflags=0x08000000 if os.name == "nt" else 0,
        )
        m = re.search(r"Supported pixel formats:\s*(.+)", result.stdout)
        if m:
            fmts = m.group(1).split()
            _pix_fmt_cache[encoder_name] = fmts
            return fmts
    except Exception:
        pass

    _pix_fmt_cache[encoder_name] = None
    return None
