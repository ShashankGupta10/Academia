from PyQt5.QtWidgets import QApplication, QWidget, QLabel
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5.QtCore import *

class Example(QWidget):

    def __init__(self):
        super().__init__()
        
        backbtn = QToolButton(self)
        backbtn.setArrowType(Qt.LeftArrow)        
        backbtn.setGeometry(100,100,50,50)
        backbtn.setStyleSheet("QToolButton{ background: transparent;color: #301E67}")
        backbtn.clicked.connect(self.back)
        
        # Set the background image
        self.background_label = QLabel(self)
        self.background_pixmap = QPixmap("images\\aboutus.png")
        self.background_label.setPixmap(self.background_pixmap)
        self.background_label.setGeometry(0, 0,1920, 1080)
        self.background_label.setAlignment(Qt.AlignCenter)
        self.background_label.lower()

        # Set the widget properties
        self.setGeometry(0,0,1920, 1080)
        self.setWindowTitle('Background Image Example')
        self.showMaximized()
        self.show()
    def back(self):
        ex.close()
        os.system("python Institutedashboard.py &") 

if __name__ == '__main__':
    app = QApplication([])
    ex = Example()
    app.exec_()
