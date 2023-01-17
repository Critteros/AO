from ctypes import alignment
import os
import random

from PySide6 import QtCore, QtWidgets, QtGui
from ao.utils import ImageRecognizer



project_path = "/home/bard/AO"  # Tylko na potrzeby testów, myślę o wrzuceniu do .env albo coś bo jak ../ dawałem to nie wykrywało


def configureStyle(app):
    pass

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Rozpoznawanie krajobrazów - AO 2023 AGH")
        self.centralWidget = CentralWidget()

        self.setCentralWidget(self.centralWidget)


class CentralWidget(QtWidgets.QWidget):
    def __init__(self):
        sp = QtWidgets.QSizePolicy()
        sp.setHorizontalPolicy(QtWidgets.QSizePolicy.Policy.Expanding)
        sp.setVerticalPolicy(QtWidgets.QSizePolicy.Policy.Expanding)

        super().__init__()
        self.layout = QtWidgets.QVBoxLayout(self)
        
        self.setSizePolicy(sp)
        self.updateGeometry()

        print(os.getcwd())
        self.imageRecognizer = ImageRecognizer(
            os.path.join(project_path, "Notebooks/LandscapeCNN.model")
        )
        self.imageBox = QtWidgets.QGroupBox(self)


        self.imageBox.setSizePolicy(sp)
        self.imageBox.updateGeometry()


        imageLayout = QtWidgets.QGridLayout(self.imageBox)
        self.imageBox.layout = imageLayout
        
        
        self.button = QtWidgets.QPushButton("Load Image")

        self.promptOrImage = QtWidgets.QLabel("Aby rozpocząć, załaduj obrazek", alignment=QtCore.Qt.AlignCenter)

        self.imageBox.layout.addWidget(self.promptOrImage, 0,0,alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.imageBox.layout.addWidget(self.button,1,0,alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        
        self.resultBox = QtWidgets.QGroupBox(self)
        self.resultBox.setSizePolicy(sp)
        self.resultBox.updateGeometry()
        self.resultBox.layout = QtWidgets.QGridLayout(self.resultBox)

        self.resultText = QtWidgets.QLabel("", alignment=QtCore.Qt.AlignCenter)

        self.resultBox.layout.addWidget(self.resultText,0,0,alignment=QtCore.Qt.AlignmentFlag.AlignCenter)


        self.layout.addWidget(self.imageBox, 2, alignment=QtCore.Qt.AlignmentFlag.AlignCenter)
        self.layout.addWidget(self.resultBox, 1)
        self.button.clicked.connect(self.loadAndAnalyse)

        self.updateGeometry()

    def viewImage(self,img_path, verdict):

        self.button.setParent(None)
        self.imageMap = QtGui.QPixmap(img_path)
        self.imageMap = self.imageMap.scaled(QtCore.QSize(400,400),aspectMode=QtCore.Qt.AspectRatioMode.KeepAspectRatio)
        self.promptOrImage.text = img_path
        self.promptOrImage.setPixmap(self.imageMap)

        self.resultText.setText(f"Wynik: {verdict[0]}\nPewność: {verdict[1] * 100}%")
        self.resultText.update()

        self.promptOrImage.updateGeometry()

    @QtCore.Slot()
    def loadAndAnalyse(self):
        try:
            res = QtWidgets.QFileDialog.getOpenFileName(self,("Open Image"), "/home/bardel/ao/", ("Image Files (*.png *.jpg *.bmp)"))
            img_path = res[0]
            verdict = self.imageRecognizer.recognize(img_path)
            #self.text.setText(f"Image: {img_path} is a {pred_class} for {score*100}%")
            self.viewImage(img_path, verdict)
        except:
            return
            