import sys

from PyQt5.QtCore import QSize

from PyQt5.QtGui import QImage, QPalette, QBrush

from PyQt5.QtWidgets import *

import src.testinggrounds as test

class MainWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self)
        self.setFixedSize(500, 375)
        self.setGeometry(500, 100, 500, 375)

        self.button = QPushButton("Create Custom Soundfile", self)
        self.button.setStyleSheet("padding:10px; width:160px;")
        self.button.move(50, 330)

        self.button.clicked.connect(self.on_click)

        self.show()

    def on_click(self):
        test.clicked()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    oMainwindow = MainWindow()

    sys.exit(app.exec_())