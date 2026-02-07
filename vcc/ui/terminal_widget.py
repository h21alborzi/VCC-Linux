"""
Embedded terminal widget - a dark themed text area mimicking a console.
"""

from PyQt6.QtWidgets import QPlainTextEdit
from PyQt6.QtGui import QFont, QTextCursor, QColor, QPalette
from PyQt6.QtCore import Qt


class TerminalWidget(QPlainTextEdit):
    """Dark-themed read-only text widget that looks like a terminal."""

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setReadOnly(True)
        self.setMaximumBlockCount(10000)

        # Monospace font
        font = QFont("Consolas", 9)
        font.setStyleHint(QFont.StyleHint.Monospace)
        self.setFont(font)

        # Dark palette
        palette = self.palette()
        palette.setColor(QPalette.ColorRole.Base, QColor(30, 30, 30))
        palette.setColor(QPalette.ColorRole.Text, QColor(204, 204, 204))
        self.setPalette(palette)

        self.setStyleSheet("""
            QPlainTextEdit {
                background-color: #1e1e1e;
                color: #cccccc;
                border: 1px solid #3c3c3c;
                border-radius: 4px;
                padding: 4px;
                selection-background-color: #264f78;
            }
        """)

        self.setLineWrapMode(QPlainTextEdit.LineWrapMode.WidgetWidth)

    def append_text(self, text: str):
        """Append text and scroll to bottom."""
        self.moveCursor(QTextCursor.MoveOperation.End)
        self.insertPlainText(text)
        self.moveCursor(QTextCursor.MoveOperation.End)
        self.ensureCursorVisible()

    def clear_terminal(self):
        self.clear()
