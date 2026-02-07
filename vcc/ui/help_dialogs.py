"""
Help dialogs for VCC - Codec info and Pixel Format info.
"""

from PyQt6.QtWidgets import (
    QDialog, QVBoxLayout, QTextBrowser, QPushButton, QHBoxLayout,
)
from PyQt6.QtCore import Qt, QSize
from PyQt6.QtGui import QFont

from vcc.core.codecs import CODEC_HELP_TEXT, AUDIO_HELP_TEXT
from vcc.core.pixel_formats import PIXEL_FORMAT_HELP_TEXT

RESOLUTION_HELP_TEXT = """\
<h2>Video Resolutions Guide</h2>

<p>Resolution is the number of pixels in each dimension (Width &times; Height).
Higher resolution = more detail but larger files and longer encoding times.</p>

<hr>

<h3>Common Resolutions</h3>
<table border="1" cellpadding="6" cellspacing="0" style="border-collapse:collapse;">
<tr><th>Name</th><th>Width</th><th>Height</th><th>Aspect Ratio</th><th>Notes</th></tr>
<tr><td><b>8K UHD</b></td><td>7680</td><td>4320</td><td>16:9</td>
    <td>Ultra-high-end. Massive files. Very few displays support it.</td></tr>
<tr><td><b>4K UHD</b></td><td>3840</td><td>2160</td><td>16:9</td>
    <td>Standard 4K. Excellent detail. Common on modern TVs and monitors.</td></tr>
<tr><td><b>4K DCI</b></td><td>4096</td><td>2160</td><td>~1.9:1</td>
    <td>Cinema 4K. Slightly wider than UHD. Used in film production.</td></tr>
<tr><td><b>1440p (QHD)</b></td><td>2560</td><td>1440</td><td>16:9</td>
    <td>Quad HD. Popular for gaming monitors. Good middle ground.</td></tr>
<tr><td><b>1080p (Full HD)</b></td><td>1920</td><td>1080</td><td>16:9</td>
    <td>The standard for most content. Great balance of quality and size.</td></tr>
<tr><td><b>720p (HD)</b></td><td>1280</td><td>720</td><td>16:9</td>
    <td>HD ready. Good for saving space while keeping decent quality.</td></tr>
<tr><td><b>480p (SD)</b></td><td>854</td><td>480</td><td>~16:9</td>
    <td>Standard definition. Small files. Acceptable on small screens.</td></tr>
<tr><td><b>480p (4:3)</b></td><td>640</td><td>480</td><td>4:3</td>
    <td>Classic 4:3 SD. Old TV / VGA standard.</td></tr>
<tr><td><b>360p</b></td><td>640</td><td>360</td><td>16:9</td>
    <td>Low quality. Used for previews or very low bandwidth.</td></tr>
<tr><td><b>240p</b></td><td>426</td><td>240</td><td>~16:9</td>
    <td>Very low quality. Tiny files. Mobile on slow connections.</td></tr>
</table>

<hr>

<h3>Ultrawide Resolutions</h3>
<table border="1" cellpadding="6" cellspacing="0" style="border-collapse:collapse;">
<tr><th>Name</th><th>Width</th><th>Height</th><th>Aspect Ratio</th></tr>
<tr><td><b>UWQHD</b></td><td>3440</td><td>1440</td><td>21:9</td></tr>
<tr><td><b>UWHD</b></td><td>2560</td><td>1080</td><td>21:9</td></tr>
<tr><td><b>Super Ultrawide</b></td><td>5120</td><td>1440</td><td>32:9</td></tr>
</table>

<hr>

<h3>Vertical / Portrait (Mobile)</h3>
<table border="1" cellpadding="6" cellspacing="0" style="border-collapse:collapse;">
<tr><th>Name</th><th>Width</th><th>Height</th><th>Use Case</th></tr>
<tr><td><b>1080×1920</b></td><td>1080</td><td>1920</td><td>Instagram/TikTok Reels, Stories</td></tr>
<tr><td><b>720×1280</b></td><td>720</td><td>1280</td><td>Mobile vertical video</td></tr>
<tr><td><b>1080×1080</b></td><td>1080</td><td>1080</td><td>Instagram square posts</td></tr>
</table>

<hr>

<h3>How Resolution Affects File Size</h3>
<p>Doubling both width and height means <b>4&times; the pixels</b> and roughly 4&times; the file size
(at the same quality settings). For example:</p>
<ul>
<li>720p (921,600 pixels) &rarr; 1080p (2,073,600 pixels) = ~2.25&times; more pixels</li>
<li>1080p (2,073,600 pixels) &rarr; 4K (8,294,400 pixels) = ~4&times; more pixels</li>
</ul>

<h3>Recommendations</h3>
<p><b>Archiving / high quality:</b> Keep original resolution, or use 1080p/4K.<br>
<b>Saving disk space:</b> 720p offers significant savings with acceptable quality.<br>
<b>Sharing online:</b> 1080p is the sweet spot &mdash; universally supported and looks great.<br>
<b>Very small files:</b> 480p for mobile or slow networks.<br>
<b>Tip:</b> Always maintain the original aspect ratio to avoid stretching or black bars.</p>
"""


class HelpDialog(QDialog):
    """Scrollable HTML help dialog."""

    def __init__(self, title: str, html_content: str, parent=None):
        super().__init__(parent)
        self.setWindowTitle(title)
        self.setMinimumSize(QSize(700, 550))
        self.resize(780, 620)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(12, 12, 12, 12)

        browser = QTextBrowser()
        browser.setOpenExternalLinks(True)
        browser.setHtml(html_content)
        font = QFont("Segoe UI", 10)
        browser.setFont(font)
        browser.setStyleSheet("""
            QTextBrowser {
                background-color: #fafafa;
                border: 1px solid #d0d0d0;
                border-radius: 4px;
                padding: 8px;
            }
        """)
        layout.addWidget(browser)

        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        close_btn = QPushButton("Close")
        close_btn.setFixedWidth(100)
        close_btn.clicked.connect(self.close)
        btn_layout.addWidget(close_btn)
        layout.addLayout(btn_layout)


class CodecHelpDialog(HelpDialog):
    def __init__(self, parent=None):
        super().__init__("Codec Information", CODEC_HELP_TEXT, parent)


class PixelFormatHelpDialog(HelpDialog):
    def __init__(self, parent=None):
        super().__init__("Pixel Format Information", PIXEL_FORMAT_HELP_TEXT, parent)


class AudioHelpDialog(HelpDialog):
    def __init__(self, parent=None):
        super().__init__("Audio Codec Information", AUDIO_HELP_TEXT, parent)


class ResolutionHelpDialog(HelpDialog):
    def __init__(self, parent=None):
        super().__init__("Resolution Guide", RESOLUTION_HELP_TEXT, parent)


class AboutDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("About Video Codec Converter")
        self.setFixedSize(420, 260)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)

        browser = QTextBrowser()
        browser.setOpenExternalLinks(False)
        browser.setHtml("""
        <div style="text-align:center;">
        <h2>Video Codec Converter (VCC)</h2>
        <p>Version 1.0.0</p>
        <p>A graphical FFmpeg front-end for batch video transcoding.</p>
        <hr>
        <p style="color:#666;">Powered by FFmpeg<br>
        Built with Python &amp; PyQt6</p>
        </div>
        """)
        browser.setStyleSheet("QTextBrowser { border: none; background: transparent; }")
        layout.addWidget(browser)

        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        close_btn = QPushButton("Close")
        close_btn.setFixedWidth(100)
        close_btn.clicked.connect(self.close)
        btn_layout.addWidget(close_btn)
        layout.addLayout(btn_layout)
