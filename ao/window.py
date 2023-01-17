import os

from PySide6.QtCore import Qt, Slot
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (
    QLabel,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QFileDialog,
)

from ._i18n import _
from .utils import ImageRecognizer


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.analyzer = ImageRecognizer(
            os.path.join(os.path.dirname(__file__), "../LandscapeCNN.model")
        )

        self.resize(800, 600)
        self.setStyleSheet("background-color: #2d2d2d; color: #ffffff;")

        self.title = QLabel()

        self.title = QLabel(_("Postcard from holidays"))
        self.title.setStyleSheet(
            "font-size: 40px; font-weight: bold; font-style: italic;"
        )
        self.default_view()

    def default_view(self):
        # self.title.setText(_("Postcard from holidays"))
        # self.setCentralWidget(widget)
        widget = QWidget()
        self.setCentralWidget(widget)
        layout = QVBoxLayout(widget)

        self.title.setText(_("Postcard from holidays"))
        button = QPushButton(_("Load image"))
        button.setStyleSheet("font-size: 50px; padding: 10px;")
        button.clicked.connect(self.show_file_dialog)

        layout.addWidget(self.title, alignment=Qt.AlignCenter)
        layout.addWidget(button, alignment=Qt.AlignCenter)

    def analyse_view(self, filename):
        center_widget = QWidget()
        layout = QVBoxLayout(center_widget)
        image = QLabel()
        pixmap = QPixmap(filename)
        pixmap = pixmap.scaled(600, 600, Qt.KeepAspectRatio)
        image.setPixmap(pixmap)
        image.setStyleSheet("width: 10px; height: 10px;")

        recognition = self.analyzer.recognize(filename)

        self.title.setText(f'{_("Result:")} {recognition[0]} ({recognition[1] * 100})%')

        layout.addWidget(self.title, alignment=Qt.AlignCenter)

        layout.addWidget(
            image,
            alignment=Qt.AlignCenter,
        )

        back_button = QPushButton(_("Back"))
        back_button.setStyleSheet("font-size: 50px; padding: 10px;")
        back_button.clicked.connect(self.default_view)
        layout.addWidget(back_button, alignment=Qt.AlignCenter)
        self.setCentralWidget(center_widget)

    @Slot()
    def show_file_dialog(self):
        # Open a file dialog using PySide6.QtWidgets.QFileDialog
        # and then call self.imageRecognizer.recognize(img_path)
        # to get the prediction
        result = QFileDialog.getOpenFileName(
            self, "Open File", "", "Image Files (*.png *.jpg *.bmp *.jpeg)"
        )
        if result[0]:
            self.analyse_view(result[0])
