# Make a gui in pyqt6
import sys

from PySide6.QtWidgets import QApplication

from .window import MainWindow


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
