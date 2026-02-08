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

<p>VCC supports both <b>CPU (software) encoders</b> and <b>GPU (hardware) encoders</b>.
This guide covers all available codecs, their parameters, and recommended settings.</p>

<p><b>Note:</b> VCC automatically filters the <b>Pixel Format</b> dropdown to show only
formats compatible with the selected codec. You will never see an incompatible option.</p>

<hr>

<h2>&#x2699;&#xFE0F; CPU Encoders (Software)</h2>

<h3>AV1 (SVT-AV1) &mdash; <code>libsvtav1</code> &nbsp;&#x2B50; Recommended</h3>
<p><b>Best overall choice for quality/size.</b> The fastest and most practical AV1 encoder.</p>
<ul>
<li><b>Pros:</b> Excellent compression (30-50% smaller than H.264 at same quality), royalty-free, \
fast encoder (SVT-AV1 is highly optimized), wide and growing playback support.</li>
<li><b>Cons:</b> Encoding is still slower than H.264/H.265, some older devices lack hardware decode.</li>
<li><b>Best for:</b> Archiving, streaming, general purpose when you want the best size/quality ratio.</li>
<li><b>Pixel formats:</b> <code>yuv420p</code>, <code>yuv420p10le</code> (10-bit recommended).</li>
</ul>
<table border="1" cellpadding="5" cellspacing="0" style="border-collapse:collapse;">
<tr><th>Parameter</th><th>Range</th><th>Default</th><th>Recommended</th><th>What It Does</th></tr>
<tr><td><b>Preset</b></td><td>0 &ndash; 13</td><td>10</td><td>6 &ndash; 8</td>
    <td>Speed vs compression. 0 = slowest/best, 13 = fastest/worst.</td></tr>
<tr><td><b>CRF</b></td><td>0 &ndash; 63</td><td>32</td><td>28 &ndash; 35</td>
    <td>Visual quality. 0 = lossless, 63 = worst. Transparent: ~23-28.</td></tr>
</table>

<h3>H.264 (x264) &mdash; <code>libx264</code></h3>
<p><b>Most compatible codec.</b> Plays everywhere &mdash; every phone, browser, TV, and device.</p>
<ul>
<li><b>Pros:</b> Universal hardware/software support, fast encoding, mature and well-optimized.</li>
<li><b>Cons:</b> Larger files compared to newer codecs at same quality, patented.</li>
<li><b>Best for:</b> Maximum compatibility, quick encodes, sharing on all devices.</li>
<li><b>Pixel formats:</b> <code>yuv420p</code> (widest support), <code>yuv420p10le</code>, \
<code>yuv422p</code>, <code>yuv444p</code>, and more. 8-bit <code>yuv420p</code> recommended for compatibility.</li>
</ul>
<table border="1" cellpadding="5" cellspacing="0" style="border-collapse:collapse;">
<tr><th>Parameter</th><th>Range</th><th>Default</th><th>Recommended</th><th>What It Does</th></tr>
<tr><td><b>Preset</b></td><td>ultrafast &ndash; placebo</td><td>medium</td><td>medium / slow</td>
    <td>Speed vs compression trade-off. Slower = smaller file, same quality.</td></tr>
<tr><td><b>CRF</b></td><td>0 &ndash; 51</td><td>23</td><td>18 &ndash; 23</td>
    <td>Visual quality. 0 = lossless. Transparent: ~17-20.</td></tr>
<tr><td><b>Tune</b></td><td>(see below)</td><td>(none)</td><td>(none)</td>
    <td>Optimizes for specific content types.</td></tr>
</table>
<p><b>Tune options:</b></p>
<ul>
<li><b>film</b> &mdash; Live-action content with fine detail and subtle grain.</li>
<li><b>animation</b> &mdash; Cartoons/anime with flat areas and sharp edges.</li>
<li><b>grain</b> &mdash; Preserves film grain texture (increases bitrate).</li>
<li><b>stillimage</b> &mdash; Slide shows or mostly static content.</li>
<li><b>fastdecode</b> &mdash; Disables CABAC and some filters for faster decoding (low-power devices).</li>
<li><b>zerolatency</b> &mdash; No look-ahead. Essential for live streaming / real-time.</li>
<li><b>(blank)</b> &mdash; General-purpose. Best for most content.</li>
</ul>

<h3>H.265 / HEVC (x265) &mdash; <code>libx265</code></h3>
<p><b>Good balance of compression and compatibility.</b></p>
<ul>
<li><b>Pros:</b> ~30-40% better compression than H.264, widespread hardware decode on modern devices.</li>
<li><b>Cons:</b> Complex licensing, slower encoding than H.264, some web browsers don't support it.</li>
<li><b>Best for:</b> When you need better compression than H.264 but AV1 is too slow.</li>
<li><b>Pixel formats:</b> Very broad &mdash; <code>yuv420p</code>, <code>yuv420p10le</code> (recommended), \
<code>yuv422p</code>, <code>yuv444p</code>, and 10/12-bit variants, plus alpha formats.</li>
</ul>
<table border="1" cellpadding="5" cellspacing="0" style="border-collapse:collapse;">
<tr><th>Parameter</th><th>Range</th><th>Default</th><th>Recommended</th><th>What It Does</th></tr>
<tr><td><b>Preset</b></td><td>ultrafast &ndash; placebo</td><td>medium</td><td>medium / slow</td>
    <td>Speed vs compression. Same names as x264 but HEVC is slower per preset.</td></tr>
<tr><td><b>CRF</b></td><td>0 &ndash; 51</td><td>28</td><td>24 &ndash; 30</td>
    <td>Visual quality. Transparent: ~20-25. Note: CRF 28 in HEVC &asymp; CRF 23 in H.264.</td></tr>
<tr><td><b>Tune</b></td><td>(see below)</td><td>(none)</td><td>(none)</td>
    <td>Optimizes for specific content types.</td></tr>
</table>
<p><b>Tune options:</b></p>
<ul>
<li><b>grain</b> &mdash; Preserves film grain (recommended for grainy sources).</li>
<li><b>animation</b> &mdash; Flat areas with sharp edges (cartoons/anime).</li>
<li><b>fastdecode</b> &mdash; Faster decoding at slight quality cost.</li>
<li><b>zerolatency</b> &mdash; Real-time streaming, no look-ahead.</li>
</ul>

<h3>H.266 / VVC (vvenc) &mdash; <code>libvvenc</code> &nbsp;&#x1F195;</h3>
<p><b>Next-generation successor to H.265/HEVC.</b></p>
<ul>
<li><b>Pros:</b> ~30-50% better compression than H.265 at the same visual quality. \
Excellent for 4K/8K content. Newest video standard (finalized 2020).</li>
<li><b>Cons:</b> Very slow encoding. Very limited playback support \
(VLC 3.0.21+, some newer devices). Patented with complex licensing.</li>
<li><b>Best for:</b> Future-proofing archives, 4K/8K content where file size matters most.</li>
<li><b>Pixel formats:</b> Only <code>yuv420p10le</code>. Very limited format support.</li>
</ul>
<table border="1" cellpadding="5" cellspacing="0" style="border-collapse:collapse;">
<tr><th>Parameter</th><th>Range</th><th>Default</th><th>Recommended</th><th>What It Does</th></tr>
<tr><td><b>Preset</b></td><td>faster &ndash; slower</td><td>medium</td><td>medium / slow</td>
    <td>Speed vs compression. VVC is already slow; &ldquo;slower&rdquo; is impractical for large files.</td></tr>
<tr><td><b>QP</b></td><td>0 &ndash; 63</td><td>32</td><td>27 &ndash; 35</td>
    <td>Quantizer &mdash; behaves like CRF. Lower = better quality.</td></tr>
</table>

<h3>VP9 &mdash; <code>libvpx-vp9</code></h3>
<p><b>Google's royalty-free predecessor to AV1.</b></p>
<ul>
<li><b>Pros:</b> Royalty-free, good compression (~similar to HEVC), excellent browser support (YouTube uses it).</li>
<li><b>Cons:</b> Encoding is slow (single-threaded reference encoder), superseded by AV1.</li>
<li><b>Best for:</b> WebM files, web video where AV1 support is uncertain.</li>
<li><b>Pixel formats:</b> <code>yuv420p</code>, <code>yuv420p10le</code>, <code>yuv422p</code>, \
<code>yuv444p</code>, and more. Supports alpha (<code>yuva420p</code>).</li>
</ul>
<table border="1" cellpadding="5" cellspacing="0" style="border-collapse:collapse;">
<tr><th>Parameter</th><th>Range</th><th>Default</th><th>Recommended</th><th>What It Does</th></tr>
<tr><td><b>CPU Used</b></td><td>0 &ndash; 8</td><td>4</td><td>2 &ndash; 4</td>
    <td>Speed vs quality. 0 = slowest/best, 8 = fastest. Watch out: 0-1 are very slow.</td></tr>
<tr><td><b>CRF</b></td><td>0 &ndash; 63</td><td>31</td><td>25 &ndash; 35</td>
    <td>Quality. VCC automatically sets <code>-b:v 0</code> to enable CRF mode.</td></tr>
</table>

<h3>AV1 (libaom) &mdash; <code>libaom-av1</code></h3>
<p><b>Reference AV1 encoder &mdash; highest quality, extremely slow.</b></p>
<ul>
<li><b>Pros:</b> Best AV1 quality at low speed settings, reference implementation.</li>
<li><b>Cons:</b> EXTREMELY slow at low cpu-used values. Not practical for large files.</li>
<li><b>Best for:</b> Short clips where maximum quality matters and time is not a concern.</li>
<li><b>Pixel formats:</b> Same as VP9 &mdash; broad support.</li>
</ul>
<table border="1" cellpadding="5" cellspacing="0" style="border-collapse:collapse;">
<tr><th>Parameter</th><th>Range</th><th>Default</th><th>Recommended</th><th>What It Does</th></tr>
<tr><td><b>CPU Used</b></td><td>0 &ndash; 8</td><td>6</td><td>4 &ndash; 6</td>
    <td>Speed vs quality. Warning: 0-3 can be impractically slow (hours per minute).</td></tr>
<tr><td><b>CRF</b></td><td>0 &ndash; 63</td><td>30</td><td>25 &ndash; 35</td>
    <td>Quality. Lower = better.</td></tr>
</table>

<h3>AV1 (rav1e) &mdash; <code>librav1e</code></h3>
<p><b>Rust-based AV1 encoder &mdash; safe, experimental.</b></p>
<ul>
<li><b>Pros:</b> Memory-safe Rust implementation, royalty-free.</li>
<li><b>Cons:</b> Generally slower than SVT-AV1, less widespread, fewer features.</li>
<li><b>Best for:</b> When you want an alternative AV1 encoder or value memory safety.</li>
</ul>
<table border="1" cellpadding="5" cellspacing="0" style="border-collapse:collapse;">
<tr><th>Parameter</th><th>Range</th><th>Default</th><th>Recommended</th><th>What It Does</th></tr>
<tr><td><b>Speed</b></td><td>0 &ndash; 10</td><td>6</td><td>4 &ndash; 6</td>
    <td>Encoding speed. Lower = slower, better compression.</td></tr>
<tr><td><b>QP</b></td><td>0 &ndash; 255</td><td>100</td><td>80 &ndash; 120</td>
    <td>Quantizer. 0 = lossless, 255 = worst. Wider range than CRF.</td></tr>
</table>

<h3>MPEG-4 Part 2 &mdash; <code>mpeg4</code></h3>
<p><b>Legacy codec.</b> Not recommended for new encodes.</p>
<ul>
<li><b>Pros:</b> Very fast encoding, simple, legacy device support.</li>
<li><b>Cons:</b> Poor compression compared to any modern codec.</li>
</ul>
<table border="1" cellpadding="5" cellspacing="0" style="border-collapse:collapse;">
<tr><th>Parameter</th><th>Range</th><th>Default</th><th>Recommended</th><th>What It Does</th></tr>
<tr><td><b>Quality (q:v)</b></td><td>1 &ndash; 31</td><td>5</td><td>3 &ndash; 8</td>
    <td>Fixed quantizer. Lower = better quality, larger file.</td></tr>
</table>

<hr>

<h2>&#x1F3AE; GPU Encoders (Hardware)</h2>

<p>GPU encoders appear in the codec dropdown with a &#x1F3AE; icon when auto-detected.
They are <b>10&ndash;50&times; faster</b> than CPU encoders with near-zero CPU usage.
See Help &rarr; GPU Encoding for a full guide.</p>

<h3>NVIDIA NVENC &mdash; H.264, H.265/HEVC, AV1</h3>
<table border="1" cellpadding="5" cellspacing="0" style="border-collapse:collapse;">
<tr><th>Parameter</th><th>Range</th><th>Default</th><th>Recommended</th><th>What It Does</th></tr>
<tr><td><b>Preset</b></td><td>p1 &ndash; p7</td><td>p4</td><td>p4 &ndash; p5</td>
    <td>p1 = fastest, p7 = best quality. p4 is the sweet spot.</td></tr>
<tr><td><b>CQ</b></td><td>0 &ndash; 51</td><td>28</td><td>24 &ndash; 30</td>
    <td>Constant Quality &mdash; behaves like CRF. Lower = better.</td></tr>
</table>
<p><b>Bit depth:</b> H.264 NVENC supports <b>8-bit only</b>. H.265/AV1 NVENC support <b>8-bit and 10-bit</b>. \
FFmpeg auto-converts pixel formats (e.g. <code>yuv420p10le</code> &rarr; <code>p010le</code> internally).</p>

<h3>AMD AMF &mdash; H.264, H.265/HEVC, AV1</h3>
<table border="1" cellpadding="5" cellspacing="0" style="border-collapse:collapse;">
<tr><th>Parameter</th><th>Range</th><th>Default</th><th>Recommended</th><th>What It Does</th></tr>
<tr><td><b>Preset</b></td><td>speed / balanced / quality</td><td>balanced</td><td>balanced / quality</td>
    <td>Speed vs quality trade-off.</td></tr>
<tr><td><b>QP</b></td><td>0 &ndash; 51</td><td>26&ndash;28</td><td>22 &ndash; 30</td>
    <td>Quantization Parameter. Lower = better quality.</td></tr>
</table>
<p><b>Bit depth:</b> H.264 AMF = <b>8-bit only</b>. H.265/AV1 AMF = <b>8-bit and 10-bit</b>.</p>

<h3>Intel QSV &mdash; H.264, H.265/HEVC, AV1</h3>
<table border="1" cellpadding="5" cellspacing="0" style="border-collapse:collapse;">
<tr><th>Parameter</th><th>Range</th><th>Default</th><th>Recommended</th><th>What It Does</th></tr>
<tr><td><b>Preset</b></td><td>veryfast &ndash; veryslow</td><td>medium</td><td>medium / slow</td>
    <td>Same naming as x264. Slower = better compression.</td></tr>
<tr><td><b>Global Quality</b></td><td>1 &ndash; 51</td><td>25&ndash;28</td><td>22 &ndash; 30</td>
    <td>Quality level. Lower = better. Similar to CRF.</td></tr>
</table>
<p><b>Bit depth:</b> H.264 QSV = <b>8-bit only</b>. H.265/AV1 QSV = <b>8-bit and 10-bit</b>.</p>

<hr>

<h2>Which AV1 Encoder Should I Use?</h2>
<table border="1" cellpadding="6" cellspacing="0">
<tr><th>Encoder</th><th>Speed</th><th>Quality</th><th>Recommendation</th></tr>
<tr><td><b>SVT-AV1</b></td><td>&#x1F7E2; Fast</td><td>&#x1F7E2; Excellent</td>\
<td><b>&#x2B50; Use this one</b></td></tr>
<tr><td><b>libaom</b></td><td>&#x1F534; Very Slow</td><td>&#x1F7E2; Best (marginal)</td>\
<td>Small clips only</td></tr>
<tr><td><b>rav1e</b></td><td>&#x1F7E1; Moderate</td><td>&#x1F7E1; Good</td>\
<td>Niche/experimental</td></tr>
<tr><td><b>NVENC/AMF/QSV AV1</b></td><td>&#x1F7E2; Very Fast</td><td>&#x1F7E1; Good</td>\
<td>Speed priority (needs new GPU)</td></tr>
</table>
<p><b>TL;DR:</b> Use <b>SVT-AV1</b> for best quality/size. Use <b>GPU AV1</b> when speed matters.</p>

<hr>

<h2>Quick Recommendations</h2>
<table border="1" cellpadding="6" cellspacing="0" style="border-collapse:collapse;">
<tr><th>Goal</th><th>Codec</th><th>Settings</th></tr>
<tr><td><b>Best quality/size ratio</b></td><td>AV1 (SVT-AV1)</td><td>Preset 6-8, CRF 28-35, yuv420p10le</td></tr>
<tr><td><b>Maximum compatibility</b></td><td>H.264 (x264)</td><td>Preset medium, CRF 20-23, yuv420p</td></tr>
<tr><td><b>Good balance</b></td><td>H.265 (x265)</td><td>Preset medium, CRF 24-28, yuv420p10le</td></tr>
<tr><td><b>Future-proofing</b></td><td>H.266 (VVC)</td><td>Preset medium, QP 30-35</td></tr>
<tr><td><b>Fastest (GPU)</b></td><td>H.264/H.265 NVENC</td><td>Preset p4-p5, CQ 24-30</td></tr>
<tr><td><b>Fastest + good compression (GPU)</b></td><td>HEVC NVENC</td><td>Preset p5, CQ 26, yuv420p10le</td></tr>
</table>
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
