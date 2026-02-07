"""
Codec definitions, parameters, and help text for VCC.
Each codec has: ffmpeg name, display name, default params with tooltips, and description.
"""

CODECS = {
    "libsvtav1": {
        "display": "AV1 (SVT-AV1)",
        "container": "mkv",
        "params": {
            "preset": {
                "label": "Preset",
                "type": "int",
                "default": 10,
                "min": 0,
                "max": 13,
                "tooltip": (
                    "Controls encoding speed vs compression efficiency.\n\n"
                    "Lower value (0) = SLOWEST encoding, BEST compression (smaller file).\n"
                    "Higher value (13) = FASTEST encoding, WORST compression (larger file).\n\n"
                    "Recommended: 6-8 for a good balance."
                ),
            },
            "crf": {
                "label": "CRF (Quality)",
                "type": "int",
                "default": 32,
                "min": 0,
                "max": 63,
                "tooltip": (
                    "Constant Rate Factor - controls visual quality.\n\n"
                    "Lower value (0) = HIGHEST quality, LARGEST file.\n"
                    "Higher value (63) = LOWEST quality, SMALLEST file.\n\n"
                    "Recommended: 28-35 for good quality/size balance.\n"
                    "Visually transparent: ~23-28."
                ),
            },
        },
    },
    "libx264": {
        "display": "H.264 (x264)",
        "container": "mkv",
        "params": {
            "preset": {
                "label": "Preset",
                "type": "choice",
                "default": "medium",
                "choices": [
                    "ultrafast", "superfast", "veryfast", "faster", "fast",
                    "medium", "slow", "slower", "veryslow", "placebo",
                ],
                "tooltip": (
                    "Controls encoding speed vs compression efficiency.\n\n"
                    "ultrafast = FASTEST encoding, WORST compression.\n"
                    "veryslow  = SLOWEST encoding, BEST compression.\n"
                    "placebo   = Negligible gain over veryslow; not recommended.\n\n"
                    "Recommended: medium or slow."
                ),
            },
            "crf": {
                "label": "CRF (Quality)",
                "type": "int",
                "default": 23,
                "min": 0,
                "max": 51,
                "tooltip": (
                    "Constant Rate Factor - controls visual quality.\n\n"
                    "Lower value (0) = Lossless, LARGEST file.\n"
                    "Higher value (51) = LOWEST quality, SMALLEST file.\n\n"
                    "Recommended: 18-23 for high quality.\n"
                    "Visually transparent: ~17-20."
                ),
            },
            "tune": {
                "label": "Tune",
                "type": "choice",
                "default": "",
                "choices": [
                    "", "film", "animation", "grain", "stillimage",
                    "fastdecode", "zerolatency", "psnr", "ssim",
                ],
                "tooltip": (
                    "Optimizes encoding settings for specific content types.\n\n"
                    "film       - Live-action content with fine detail.\n"
                    "animation  - Cartoons/anime with flat areas and sharp edges.\n"
                    "grain      - Preserves film grain.\n"
                    "stillimage - Slide shows or mostly static content.\n"
                    "fastdecode - Faster decoding (for low-power devices).\n"
                    "zerolatency- Real-time streaming.\n\n"
                    "Leave blank for general-purpose encoding."
                ),
            },
        },
    },
    "libx265": {
        "display": "H.265 / HEVC (x265)",
        "container": "mkv",
        "params": {
            "preset": {
                "label": "Preset",
                "type": "choice",
                "default": "medium",
                "choices": [
                    "ultrafast", "superfast", "veryfast", "faster", "fast",
                    "medium", "slow", "slower", "veryslow", "placebo",
                ],
                "tooltip": (
                    "Controls encoding speed vs compression efficiency.\n\n"
                    "ultrafast = FASTEST encoding, WORST compression.\n"
                    "veryslow  = SLOWEST encoding, BEST compression.\n\n"
                    "Recommended: medium or slow."
                ),
            },
            "crf": {
                "label": "CRF (Quality)",
                "type": "int",
                "default": 28,
                "min": 0,
                "max": 51,
                "tooltip": (
                    "Constant Rate Factor - controls visual quality.\n\n"
                    "Lower value (0) = Lossless, LARGEST file.\n"
                    "Higher value (51) = LOWEST quality, SMALLEST file.\n\n"
                    "Recommended: 24-30 for good quality.\n"
                    "Visually transparent: ~20-25."
                ),
            },
            "tune": {
                "label": "Tune",
                "type": "choice",
                "default": "",
                "choices": ["", "grain", "animation", "fastdecode", "zerolatency"],
                "tooltip": (
                    "Optimizes encoding for specific content.\n\n"
                    "grain      - Preserves film grain.\n"
                    "animation  - Cartoons/anime.\n"
                    "fastdecode - Faster decoding.\n"
                    "zerolatency- Real-time streaming.\n\n"
                    "Leave blank for general use."
                ),
            },
        },
    },
    "libvpx-vp9": {
        "display": "VP9",
        "container": "webm",
        "params": {
            "cpu-used": {
                "label": "CPU Used (Speed)",
                "type": "int",
                "default": 4,
                "min": 0,
                "max": 8,
                "tooltip": (
                    "Controls encoding speed vs quality.\n\n"
                    "Lower value (0) = SLOWEST, BEST quality.\n"
                    "Higher value (8) = FASTEST, LOWER quality.\n\n"
                    "Recommended: 2-4."
                ),
            },
            "crf": {
                "label": "CRF (Quality)",
                "type": "int",
                "default": 31,
                "min": 0,
                "max": 63,
                "tooltip": (
                    "Constant Rate Factor - controls visual quality.\n\n"
                    "Lower value (0) = BEST quality, LARGEST file.\n"
                    "Higher value (63) = WORST quality, SMALLEST file.\n\n"
                    "Recommended: 25-35.\n"
                    "Note: VP9 CRF requires -b:v 0 to enable CRF mode."
                ),
            },
        },
    },
    "libaom-av1": {
        "display": "AV1 (libaom - reference)",
        "container": "mkv",
        "params": {
            "cpu-used": {
                "label": "CPU Used (Speed)",
                "type": "int",
                "default": 6,
                "min": 0,
                "max": 8,
                "tooltip": (
                    "Controls encoding speed vs quality.\n\n"
                    "Lower value (0) = EXTREMELY SLOW, BEST quality.\n"
                    "Higher value (8) = FASTEST, LOWER quality.\n\n"
                    "Warning: values 0-3 can be impractically slow.\n"
                    "Recommended: 4-6."
                ),
            },
            "crf": {
                "label": "CRF (Quality)",
                "type": "int",
                "default": 30,
                "min": 0,
                "max": 63,
                "tooltip": (
                    "Constant Rate Factor.\n\n"
                    "Lower value = HIGHER quality, larger file.\n"
                    "Higher value = LOWER quality, smaller file.\n\n"
                    "Recommended: 25-35."
                ),
            },
        },
    },
    "mpeg4": {
        "display": "MPEG-4 (Part 2)",
        "container": "mkv",
        "params": {
            "q:v": {
                "label": "Quality (q:v)",
                "type": "int",
                "default": 5,
                "min": 1,
                "max": 31,
                "tooltip": (
                    "Fixed quantizer scale.\n\n"
                    "Lower value (1) = BEST quality, LARGEST file.\n"
                    "Higher value (31) = WORST quality, SMALLEST file.\n\n"
                    "Recommended: 3-8."
                ),
            },
        },
    },
    "librav1e": {
        "display": "AV1 (rav1e)",
        "container": "mkv",
        "params": {
            "speed": {
                "label": "Speed",
                "type": "int",
                "default": 6,
                "min": 0,
                "max": 10,
                "tooltip": (
                    "Encoding speed.\n\n"
                    "Lower value (0) = SLOWEST, BEST compression.\n"
                    "Higher value (10) = FASTEST, WORST compression.\n\n"
                    "Recommended: 4-6."
                ),
            },
            "qp": {
                "label": "Quantizer (QP)",
                "type": "int",
                "default": 100,
                "min": 0,
                "max": 255,
                "tooltip": (
                    "Quantizer parameter.\n\n"
                    "Lower value (0) = BEST quality / lossless.\n"
                    "Higher value (255) = WORST quality.\n\n"
                    "Recommended: 80-120."
                ),
            },
        },
    },
    "libvvenc": {
        "display": "H.266 / VVC (vvenc)",
        "container": "mkv",
        "params": {
            "preset": {
                "label": "Preset",
                "type": "choice",
                "default": "medium",
                "choices": ["faster", "fast", "medium", "slow", "slower"],
                "tooltip": (
                    "Controls encoding speed vs compression efficiency.\n\n"
                    "faster  = FASTEST encoding, WORST compression.\n"
                    "slower  = SLOWEST encoding, BEST compression.\n\n"
                    "Recommended: medium or slow."
                ),
            },
            "qp": {
                "label": "QP (Quality)",
                "type": "int",
                "default": 32,
                "min": 0,
                "max": 63,
                "tooltip": (
                    "Quantizer Parameter - controls visual quality.\n\n"
                    "Lower value (0) = HIGHEST quality, LARGEST file.\n"
                    "Higher value (63) = LOWEST quality, SMALLEST file.\n\n"
                    "Recommended: 27-35 for good quality/size balance.\n"
                    "Note: VVC/H.266 achieves ~30-50% better compression\n"
                    "than H.265/HEVC at the same visual quality."
                ),
            },
        },
    },
}


CODEC_HELP_TEXT = """\
<h2>Video Codecs Overview</h2>

<h3>AV1 (SVT-AV1) &mdash; <code>libsvtav1</code></h3>
<p><b>Best overall choice for quality/size.</b></p>
<ul>
<li><b>Pros:</b> Excellent compression (30-50% smaller than H.264 at same quality), royalty-free, \
fast encoder (SVT-AV1 is highly optimized), wide and growing playback support.</li>
<li><b>Cons:</b> Encoding is still slower than H.264/H.265, some older devices lack hardware decode.</li>
<li><b>Best for:</b> Archiving, streaming, general purpose when you want the best size/quality ratio.</li>
<li><b>vs libaom:</b> Much faster (10-100x) with very similar quality. Use SVT-AV1 for practical encoding.</li>
<li><b>vs rav1e:</b> Faster and better optimized. SVT-AV1 is the recommended AV1 encoder.</li>
</ul>

<h3>H.264 (x264) &mdash; <code>libx264</code></h3>
<p><b>Most compatible codec.</b></p>
<ul>
<li><b>Pros:</b> Universal hardware/software support, fast encoding, mature and well-optimized.</li>
<li><b>Cons:</b> Larger files compared to newer codecs at same quality, patented (royalties for commercial use).</li>
<li><b>Best for:</b> Maximum compatibility, quick encodes, sharing on all devices.</li>
</ul>

<h3>H.265 / HEVC (x265) &mdash; <code>libx265</code></h3>
<p><b>Good middle ground.</b></p>
<ul>
<li><b>Pros:</b> ~30-40% better compression than H.264, widespread hardware decode on modern devices.</li>
<li><b>Cons:</b> Complex licensing/royalty situation, slower encoding than H.264, some web browsers don't support it.</li>
<li><b>Best for:</b> When you need better compression than H.264 but AV1 is too slow for your needs.</li>
</ul>

<h3>H.266 / VVC (vvenc) &mdash; <code>libvvenc</code> &nbsp;&#x1F195;</h3>
<p><b>Next-generation successor to H.265/HEVC.</b></p>
<ul>
<li><b>Pros:</b> ~30-50% better compression than H.265/HEVC at the same visual quality. \
Excellent for 4K/8K content. The newest video coding standard (finalized 2020).</li>
<li><b>Cons:</b> Very slow encoding (newer encoder, less optimized). Very limited playback support \
(VLC 3.0.21+, some newer devices). Only supports <code>yuv420p10le</code> pixel format. \
Patented with complex licensing.</li>
<li><b>Best for:</b> Future-proofing archives, 4K/8K content where file size matters most and \
you don't need immediate wide compatibility.</li>
<li><b>Note:</b> This is a cutting-edge codec. Playback support will grow over time.</li>
</ul>

<h3>VP9 &mdash; <code>libvpx-vp9</code></h3>
<p><b>Google's royalty-free predecessor to AV1.</b></p>
<ul>
<li><b>Pros:</b> Royalty-free, good compression (~similar to HEVC), excellent browser support (YouTube uses it).</li>
<li><b>Cons:</b> Encoding is slow (single-threaded reference encoder), superseded by AV1.</li>
<li><b>Best for:</b> Web video where AV1 support is uncertain.</li>
</ul>

<h3>AV1 (libaom) &mdash; <code>libaom-av1</code></h3>
<p><b>Reference AV1 encoder &mdash; highest quality, extremely slow.</b></p>
<ul>
<li><b>Pros:</b> Best AV1 quality at low speed settings, reference implementation, most feature-complete.</li>
<li><b>Cons:</b> EXTREMELY slow at low cpu-used values. Not practical for large files.</li>
<li><b>Best for:</b> Small clips where maximum quality matters and time is not a concern.</li>
<li><b>vs SVT-AV1:</b> libaom can produce very slightly better quality at very low speeds, but SVT-AV1 \
is 10-100x faster with nearly identical quality. For most users, SVT-AV1 is the better choice.</li>
</ul>

<h3>AV1 (rav1e) &mdash; <code>librav1e</code></h3>
<p><b>Rust-based AV1 encoder &mdash; safe, experimental.</b></p>
<ul>
<li><b>Pros:</b> Memory-safe Rust implementation, royalty-free.</li>
<li><b>Cons:</b> Generally slower than SVT-AV1, less widespread, fewer features.</li>
<li><b>Best for:</b> When you want an alternative AV1 encoder or value memory safety.</li>
<li><b>vs SVT-AV1:</b> SVT-AV1 is faster and more mature. rav1e is mainly of interest for \
Rust ecosystem integration.</li>
</ul>

<h3>MPEG-4 Part 2 &mdash; <code>mpeg4</code></h3>
<p><b>Legacy codec.</b></p>
<ul>
<li><b>Pros:</b> Very fast encoding, simple.</li>
<li><b>Cons:</b> Poor compression compared to modern codecs, dated quality.</li>
<li><b>Best for:</b> Legacy device compatibility only. Not recommended for new encodes.</li>
</ul>

<hr>
<h3>AV1 Encoders &mdash; Which One to Choose?</h3>
<p>VCC includes three AV1 encoders. Here's how they compare:</p>
<table border="1" cellpadding="6" cellspacing="0">
<tr><th>Encoder</th><th>Speed</th><th>Quality</th><th>Recommendation</th></tr>
<tr><td><b>SVT-AV1</b></td><td>&#x1F7E2; Fast</td><td>&#x1F7E2; Excellent</td>\
<td><b>&#x2B50; Use this one</b></td></tr>
<tr><td><b>libaom</b></td><td>&#x1F534; Very Slow</td><td>&#x1F7E2; Best (marginal)</td>\
<td>Small clips only</td></tr>
<tr><td><b>rav1e</b></td><td>&#x1F7E1; Moderate</td><td>&#x1F7E1; Good</td>\
<td>Niche/experimental</td></tr>
</table>
<p><b>TL;DR:</b> Use <b>SVT-AV1</b> unless you have a specific reason not to.</p>

<hr>
<h3>Recommendation</h3>
<p><b>For best quality/size ratio:</b> AV1 (SVT-AV1) with preset 6-8, CRF 28-35.<br>
<b>For fastest encoding with decent quality:</b> H.264 (x264) with preset medium, CRF 20-23.<br>
<b>For good balance of speed, quality, and size:</b> H.265 (x265) with preset medium, CRF 24-28.<br>
<b>For cutting-edge compression (future-proofing):</b> H.266/VVC with preset medium, QP 30-35.</p>
"""


AUDIO_HELP_TEXT = """\
<h2>Audio Codecs Overview</h2>

<h3>copy</h3>
<p><b>Stream copy (no re-encoding).</b></p>
<ul>
<li>Copies the original audio bitstream without any change.</li>
<li>Fastest option &mdash; no quality loss, no extra processing time.</li>
<li><b>Use this</b> when you only want to re-encode the video and keep audio as-is.</li>
</ul>

<h3>AAC &mdash; <code>aac</code></h3>
<p><b>Advanced Audio Coding. The most widely compatible lossy codec.</b></p>
<ul>
<li><b>Pros:</b> Universal support (every browser, phone, player, smart TV). Good quality at 128-256 kbps.</li>
<li><b>Cons:</b> FFmpeg's built-in AAC encoder is decent but not the best. Lossy compression.</li>
<li><b>Best for:</b> Maximum compatibility, MP4 containers, streaming.</li>
<li><b>Typical bitrate:</b> 128 kbps (stereo), 256-384 kbps (5.1 surround).</li>
</ul>

<h3>Opus &mdash; <code>libopus</code></h3>
<p><b>Modern, royalty-free, and the best lossy codec for quality-per-bitrate.</b></p>
<ul>
<li><b>Pros:</b> Superior quality at low bitrates (64-128 kbps sounds excellent). Great for both speech and \
music. Royalty-free. Supports up to 7.1 surround.</li>
<li><b>Cons:</b> Not supported in MP4 containers (use MKV or WebM). Some older devices lack support.</li>
<li><b>Best for:</b> MKV/WebM files, archiving at small sizes, VoIP, streaming.</li>
<li><b>Typical bitrate:</b> 96-128 kbps (stereo), 192-256 kbps (5.1 surround).</li>
</ul>

<h3>Vorbis &mdash; <code>libvorbis</code></h3>
<p><b>Open-source lossy codec, predecessor to Opus.</b></p>
<ul>
<li><b>Pros:</b> Royalty-free, good quality, widely supported in MKV/WebM.</li>
<li><b>Cons:</b> Surpassed by Opus in quality. Not supported in MP4.</li>
<li><b>Best for:</b> WebM video, open-source workflows, legacy compatibility.</li>
<li><b>Typical bitrate:</b> 128-192 kbps (stereo).</li>
</ul>

<h3>AC-3 (Dolby Digital) &mdash; <code>ac3</code></h3>
<p><b>Surround sound standard for DVDs and broadcast.</b></p>
<ul>
<li><b>Pros:</b> Excellent surround sound support (5.1), universally supported by home theater equipment \
and media players.</li>
<li><b>Cons:</b> Lossy, lower compression efficiency than modern codecs, max 640 kbps.</li>
<li><b>Best for:</b> Surround sound content, DVD/Blu-ray authoring, home theater playback.</li>
<li><b>Typical bitrate:</b> 384-640 kbps (5.1 surround).</li>
</ul>

<h3>FLAC &mdash; <code>flac</code></h3>
<p><b>Lossless audio compression.</b></p>
<ul>
<li><b>Pros:</b> Bit-perfect &mdash; no quality loss at all. Typically 50-70% of original PCM size. \
Well supported in MKV.</li>
<li><b>Cons:</b> Much larger files than lossy codecs. Not supported in MP4 containers.</li>
<li><b>Best for:</b> Archiving, professional workflows, when audio quality is paramount.</li>
<li><b>Typical bitrate:</b> 700-1400 kbps (stereo CD quality).</li>
</ul>

<h3>PCM (Uncompressed) &mdash; <code>pcm_s16le</code></h3>
<p><b>Raw uncompressed audio.</b></p>
<ul>
<li><b>Pros:</b> Zero processing, bit-perfect, no encoder artifacts.</li>
<li><b>Cons:</b> Very large files (1411 kbps for 16-bit/44.1kHz stereo). No compression at all.</li>
<li><b>Best for:</b> Intermediate editing, when you need truly raw audio.</li>
</ul>

<hr>
<h3>Recommendations</h3>
<p><b>Keep original audio:</b> Use <code>copy</code> &mdash; fastest, no quality loss.<br>
<b>Best quality per file size:</b> <code>libopus</code> at 128 kbps (MKV/WebM containers).<br>
<b>Maximum compatibility:</b> <code>aac</code> at 192-256 kbps.<br>
<b>Surround sound:</b> <code>ac3</code> at 384-640 kbps, or <code>libopus</code> at 256 kbps.<br>
<b>Lossless archiving:</b> <code>flac</code>.<br>
<b>General advice:</b> If you're only re-encoding video, just use <code>copy</code>.</p>
"""
