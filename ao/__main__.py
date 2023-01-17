# Make a gui in pyqt6
import sys
import os
import random
from PySide6 import QtCore, QtWidgets, QtGui
from ao.utils import ImageRecognizer

project_path = "/home/alan/dev/AO"  # Tylko na potrzeby testów, myślę o wrzuceniu do .env albo coś bo jak ../ dawałem to nie wykrywało


class MyWidget(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.img_paths = [
            os.path.join(
                project_path,
                "dataset/Landscape Classification/Testing Data/Coast/Coast-Test (131).jpeg",
            ),
        ]
        print(os.getcwd())
        self.imageRecognizer = ImageRecognizer(
            os.path.join(project_path, "Notebooks/LandscapeCNN.model")
        )
        self.button = QtWidgets.QPushButton("Check Image")
        self.text = QtWidgets.QLabel("Prediction", alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout(self)
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)

        self.button.clicked.connect(self.predict)

    @QtCore.Slot()
    def predict(self):
        img_path = random.choice(self.img_paths)
        pred_class, score = self.imageRecognizer.recognize(img_path)
        self.text.setText(f"Image: {img_path} is a {pred_class} for {score*100}%")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec())
