# Make a gui in pyqt6
import sys

from PySide6.QtGui import Qt

from ao.widgets import MainWindow

from PySide6.QtWidgets import QApplication

import qtmodern.styles
import qtmodern.windows

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    app.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    qtmodern.styles.dark(app)
    app.setStyleSheet("QLabel{font-size: 18pt;}")

    window = MainWindow()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())
