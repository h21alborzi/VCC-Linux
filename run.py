"""
Entry point for Video Codec Converter (VCC).
"""

import sys
import traceback
from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtGui import QFont
from vcc.ui.main_window import MainWindow


def _global_exception_handler(exc_type, exc_value, exc_tb):
    """Catch unhandled exceptions so the window stays open."""
    # Format the traceback for display
    tb_text = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    sys.stderr.write(tb_text)
    try:
        QMessageBox.critical(
            None,
            "Unexpected Error",
            f"An unexpected error occurred:\n\n{exc_value}\n\n"
            f"The application will continue running.\n\n"
            f"Details:\n{tb_text[-1500:]}",
        )
    except Exception:
        pass  # If even the dialog fails, at least we don't crash


def main():
    # Install global exception handler to prevent silent crashes
    sys.excepthook = _global_exception_handler

    app = QApplication(sys.argv)
    app.setApplicationName("Video Codec Converter")
    app.setOrganizationName("VCC")

    # Set a clean default font
    font = QFont("Segoe UI", 10)
    app.setFont(font)

    # Apply global stylesheet for polished look
    app.setStyleSheet("""
        QWidget {
            font-family: 'Segoe UI', sans-serif;
        }
        QSpinBox, QComboBox, QLineEdit {
            padding: 4px 6px;
            border: 1px solid #c0c0c0;
            border-radius: 4px;
            background: #fff;
        }
        QSpinBox:focus, QComboBox:focus, QLineEdit:focus {
            border-color: #4a90d9;
        }
        QPushButton {
            padding: 5px 14px;
            border: 1px solid #bbb;
            border-radius: 4px;
            background: #f5f5f5;
        }
        QPushButton:hover {
            background: #e8e8e8;
            border-color: #999;
        }
        QPushButton:pressed {
            background: #ddd;
        }
        QCheckBox {
            spacing: 6px;
        }
    """)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
