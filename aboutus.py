from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5.QtCore import *

import sys
import os

class Aboutus(QMainWindow):            
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Academia")
        self.setGeometry(0,0,1920,1080)

        pixmap = QPixmap('/aboutus.jpg')

        bg = QLabel(self)
        bg.setGeometry(0,0,1920,1080)
        # bg.setStyleSheet("QLabel{ background-image: url('aboutus.jpg)}")
        bg.setPixmap(pixmap)
        bg.setScaledContents(True)
        self.resize(pixmap.width(),pixmap.height())

        self.setCentralWidget(bg)
        self.showMaximized()


        
App = QApplication(sys.argv)
window = Aboutus()
sys.exit(App.exec())