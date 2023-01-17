# Make a gui in pyqt6
import sys
from PySide6 import QtWidgets, QtGui
from ao.widgets import *

from PySide6.QtWidgets import QApplication
from .window import MainWindow

import qtmodern.styles
import qtmodern.windows

if __name__ == "__main__":
    app = QApplication(sys.argv)

    qtmodern.styles.dark(app)
    
    window = MainWindow()
    window.resize(800, 600)
    mw = qtmodern.windows.ModernWindow(window)
    mw.show()
    #window.show()

    sys.exit(app.exec())
