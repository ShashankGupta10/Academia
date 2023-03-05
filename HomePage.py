
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,QtCore,QtGui

from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QGraphicsOpacityEffect
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from PyQt5.QtCore import QPropertyAnimation
from pathlib import Path
from tkinter import *

# from new import Shashank

from urllib import *
import sys
import os




class HomePage(QMainWindow):

    # def OpenWindow(self):
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = Shashank() 
    #     self.ui.www(self.window)

            
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Home Page")
        self.setGeometry(0,0,1920,1080)

        self.navbar = QLabel(self)
        self.navbar.setGeometry(0, 0, 1920, 100)
        self.navbar.setStyleSheet("QLabel{ background: black; position: fixed;} ")
        
        self.opacity_effect = QGraphicsOpacityEffect()
  
        self.opacity_effect.setOpacity(0.3)
  
        # self.navbar.graphicsEffect(self.opacity_effect)

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
        self.btn5.setGeometry(760, 640, 160, 85)
        self.btn5.setStyleSheet("QPushButton{ background: #645CBB; color: white; border-radius: 20px; padding: 10px;}"
                                "QPushButton:hover{ background: #A084DC;border-radius: 10px;}")
        self.btn5.setFont(QFont('Times', 12))
        
        # self.btn5.clicked.connect(os.system('python new.py'))
        
        self.btn6 = QPushButton("Institute Login" ,self)
        self.btn6.setGeometry(990, 640, 160, 85)
        self.btn6.setStyleSheet("QPushButton{ background: #645CBB; color: white; border-radius: 20px; padding: 10px;}"
                                "QPushButton:hover{ background: #A084DC;border-radius: 10px;}")
        self.btn6.setFont(QFont('Times', 12))
        
        # self.btn6.clicked.connect(self.OpenWindow())
        
        
        # self.btn7 = QPushButton("Institute Login mod" ,self)
        # self.btn7.setGeometry(1000, 640, 160, 85)
        # self.btn7.setStyleSheet("QPushButton{ background: #645CBB; color: white; border-radius: 20px; padding: 10px;}"
        #                         "QPushButton:hover{ border-radius: 2px;padding: 0.2em 0.2em 0.3em 0.2em;border: 1px solid rgb(100, 100, 100);background: qlineargradient(x1:0, y1:0, x2:0, y2:1,stop:0 #f4f4f4, stop:0.1 #8F8F8F, stop:1  #7B7B7B);color: white;min-width: 70px;}")
        # self.btn7.setFont(QFont('Times', 12))

        # self.label1 = QLabel(self)
        # self.label1.setGeometry(75, 125, 600, 500)
        # self.movie = QMovie("homepageGIF.gif")
        # self.label1.setMovie(self.movie)
        # self.movie.start()


        self.label2 = QLabel(self)
        self.label2.setGeometry(1300, 450, 600, 500)
        self.pixmap = QPixmap('D:\Pyfon MPR\TkinterGUI\images\homepageimage4bgrm.png')
        self.label2.setPixmap(self.pixmap)

        self.label3 = QLabel(self)
        self.label3.setGeometry(725,250,500,200)
        self.label3.setStyleSheet("color: black; font-weight: bold;")
        self.label3.setText("ACADEMIA")
        self.label3.setFont(QFont('Cascadia', 50))

        self.label4 = QLabel(self)
        self.label4.setGeometry(75, 100, 600, 500)
        self.pixmap = QPixmap('D:\Pyfon MPR\TkinterGUI\images\homepageimage5bgrm.png')
        self.label4.setPixmap(self.pixmap)

        self.label5 = QLabel(self)
        self.label5.setGeometry(725, 400, 600, 200)
        self.label5.setText("A Better Learning Future Starts Here.\n\nDigitalizing the educational environment.")
        self.label5.setFont(QFont("Times", 15))
        self.label5.setStyleSheet("font-weight: bold; color: Black;")

        # self.label5 = QLabel(self)
        # self.label5.setGeometry(725, 400, 600, 200)
        # self.label5.setText("A Better Learning Future Starts Here.\nDigitalizing the educational environment.")
        # self.label5.setFont(QFont("Times", 15))
        # self.label5.setStyleSheet("font-weight: bold; color: #301E67;")

        icon = QIcon("D:\Pyfon MPR\TkinterGUI\images\homepageimage1bgrm.png")
        
        self.btn10 = QPushButton("" ,self)
        self.btn10.setGeometry(1800, 0, 100, 100)
        self.btn10.setStyleSheet("background : black;")
        self.btn10.setIcon(icon)
        size = QSize(100, 100)
        self.btn10.setIconSize(size)

        self.footer = QLabel(self)
        self.footer.setGeometry(0, 900, 1920, 100)
        self.footer.setStyleSheet("QLabel{ background: black; position: fixed;} ")

        self.label6 = QPushButton(self.footer)
        self.label6.setGeometry(1750,0,150,100)
        self.label6.setStyleSheet("color: white; background: black;")
        self.label6.setText("@Academia 2023")
        self.label6.setFont(QFont('Times', 10))

        self.label7 = QPushButton(self.footer)
        self.label7.setGeometry(1575,0,150,100)
        self.label7.setStyleSheet("color: white; background: black;")
        self.label7.setText("Terms of Use")
        self.label7.setFont(QFont('Times', 10))

        self.label8 = QPushButton(self.footer)
        self.label8.setGeometry(1400,0,150,100)
        self.label8.setStyleSheet("color: white; background: black;")
        self.label8.setText("Privacy Policy")
        self.label8.setFont(QFont('Times', 10))
                                
        self.label9 = QPushButton(self.footer)
        self.label9.setGeometry(50,0,500,100)
        self.label9.setStyleSheet("color: white; background: black;")
        self.label9.setText("Copyright © 2023 Academia Inc. All rights reserved.")
        self.label9.setFont(QFont('Times', 10))
    
        self.showMaximized()
        self.show()

App = QApplication(sys.argv)
# App.setStyleSheet("background: url('https://www.shutterstock.com/image-photo/old-brick-black-color-wall-260nw-1605128917.jpg')")
# App.setStyleSheet(Path('login.qss').read_text())
# qss="/programs/homepage.qss"
# with open(qss) as fh: 
#     App.setStyleSheet(fh.read())
App.setStyleSheet("QMainWindow{background-color: #EBC7E6 }")

window = HomePage()

sys.exit(App.exec())




        # self.anim = QPropertyAnimation(self.child, b"pos")
        # self.anim.setEndValue(QPoint(800, 600))
        # self.anim.setDuration(3000)
        # self.anim.start()

