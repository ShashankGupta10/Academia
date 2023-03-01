
from PyQt5.QtWidgets import *

from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QGraphicsOpacityEffect
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from PyQt5.QtCore import QPropertyAnimation
from pathlib import Path

from urllib import *
import sys

class HomePage(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Home Page")
        self.setGeometry(0,0,1920,1080)

        self.navbar = QLabel(self)
        self.navbar.setGeometry(0, 0, 1920, 100)
        self.navbar.setStyleSheet("QLabel{ background: black; position: fixed;} ")
        
        self.opacity_effect = QGraphicsOpacityEffect()
  
        self.opacity_effect.setOpacity(0.3)
  
        self.navbar.graphicsEffect(self.opacity_effect)

        self.btn1 = QPushButton("Home" ,self.navbar)
        self.btn1.setGeometry(300, 0, 200, 100)
        self.btn1.setStyleSheet("QPushButton{ background: black; color: white; color: white}")
        self.btn1.setFont(QFont('Times', 20))

        self.btn2 = QPushButton("Nothing" ,self.navbar)
        self.btn2.setGeometry(600, 0, 200, 100)
        self.btn2.setStyleSheet("QPushButton{ background: black; color: white; color: white}")
        self.btn2.setFont(QFont('Times', 20))

        self.btn3 = QPushButton("About Us" ,self.navbar)
        self.btn3.setGeometry(900, 0, 200, 100)
        self.btn3.setStyleSheet("QPushButton{ background: black; color: white; color: #ECF2FF}")
        self.btn3.setFont(QFont('Times', 20))

        self.btn4 = QPushButton("Contact Us" ,self.navbar)
        self.btn4.setGeometry(1200, 0, 200, 100)
        self.btn4.setStyleSheet("QPushButton{ background: black; color: white; color: #ECF2FF}")
        self.btn4.setFont(QFont('Times', 20))



        self.btn5 = QPushButton("Student Login" ,self)
        self.btn5.setGeometry(550, 640, 160, 85)
        self.btn5.setStyleSheet("QPushButton{ background: #645CBB; color: white; border-radius: 20px; padding: 10px;}"
                                "QPushButton:hover{ background: #A084DC;border-radius: 10px;}")
        self.btn5.setFont(QFont('Times', 12))
        
        self.btn6 = QPushButton("Institute Login" ,self)
        self.btn6.setGeometry(800, 640, 160, 85)
        self.btn6.setStyleSheet("QPushButton{ background: #645CBB; color: white; border-radius: 20px; padding: 10px;}"
                                "QPushButton:hover{ background: #A084DC;border-radius: 10px;}")
        self.btn6.setFont(QFont('Times', 12))
        
        # self.btn7 = QPushButton("Institute Login mod" ,self)
        # self.btn7.setGeometry(1000, 640, 160, 85)
        # self.btn7.setStyleSheet("QPushButton{ background: #645CBB; color: white; border-radius: 20px; padding: 10px;}"
        #                         "QPushButton:hover{ border-radius: 2px;padding: 0.2em 0.2em 0.3em 0.2em;border: 1px solid rgb(100, 100, 100);background: qlineargradient(x1:0, y1:0, x2:0, y2:1,stop:0 #f4f4f4, stop:0.1 #8F8F8F, stop:1  #7B7B7B);color: white;min-width: 70px;}")
        # self.btn7.setFont(QFont('Times', 12))

        self.label1 = QLabel(self)
        self.label1.setGeometry(200, 100, 500, 500)
        self.pixmap = QPixmap('D:\Pyfon MPR\TkinterGUI\images\homepageimage1bgrm.png')
        self.label1.setPixmap(self.pixmap)

        self.label2 = QLabel(self)
        self.label2.setGeometry(1300, 200, 1000, 1000)
        self.pixmap = QPixmap('D:\Pyfon MPR\TkinterGUI\images\homepageimage4bgrm.png')
        self.label2.setPixmap(self.pixmap)
       


        self.showMaximized()
        self.show()



App = QApplication(sys.argv)
# App.setStyleSheet("background: url('https://www.shutterstock.com/image-photo/old-brick-black-color-wall-260nw-1605128917.jpg')")
# App.setStyleSheet(Path('login.qss').read_text())
# qss="/programs/homepage.qss"
# with open(qss) as fh: 
#     App.setStyleSheet(fh.read())
App.setStyleSheet("QMainWindow{background-color: #ECF2FF }")

window = HomePage()

sys.exit(App.exec())



        # self.anim = QPropertyAnimation(self.child, b"pos")
        # self.anim.setEndValue(QPoint(800, 600))
        # self.anim.setDuration(3000)
        # self.anim.start()






