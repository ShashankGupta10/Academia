
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

        self.loginbox = QLabel(self)
        self.loginbox.setGeometry(650,175,600,650)
        self.loginbox.setStyleSheet("background-color: #BFACE2; border-radius: 80%;")

        self.loglabel = QLabel("LOG IN", self.loginbox)
        self.loglabel.setGeometry(243, 40, 150, 50)
        self.loglabel.setFont(QFont('Times', 20))
        self.loglabel.setStyleSheet("font-weight: bold;")

        icon = QIcon('D:\\Pyfon MPR\\TkinterGUI\\images\\usernameicon.png')
        self.usernameicon = QPushButton("" ,self.loginbox)
        self.usernameicon.setGeometry(90,200, 40, 40)
        self.usernameicon.setIcon(icon)
        size = QSize(35, 35)
        self.usernameicon.setIconSize(size)

        icon = QIcon('D:\\Pyfon MPR\\TkinterGUI\\images\\passwordicon.png')
        self.passwordicon = QPushButton("" ,self.loginbox)
        self.passwordicon.setGeometry(90,300, 40, 40)
        self.passwordicon.setIcon(icon)
        size = QSize(35, 35)
        self.passwordicon.setIconSize(size)

        self.textfield1 = QLineEdit(self)
        self.textfield1.setGeometry(830, 375, 300, 40)
        self.textfield1.setFont(QFont('Times',15))
        self.textfield1.setStyleSheet("QLineEdit{background-color: black;color: white; border-radius: 20px; padding-left: 20px; padding-right: 20px}"
                                      "QLineEdit:hover{ border: 2px solid; background-color: #15133C}")
        

        self.textfield2 = QLineEdit(self)
        self.textfield2.setGeometry(830, 475, 300, 40)
        self.textfield2.setFont(QFont('Times',15))
        self.textfield2.setStyleSheet("QLineEdit{background-color: black;color: white; border-radius: 20px; padding-left: 20px; padding-right: 20px}"
                                      "QLineEdit:hover{ border: 2px solid; background-color: #15133C}")
        

        self.btn5 = QPushButton("Forgot Password" ,self.loginbox)
        self.btn5.setGeometry(310, 310, 200, 100)
        self.btn5.setStyleSheet("QPushButton{ background: #BFACE2; color: black;}")
        self.btn5.setFont(QFont('Times', 10))

        self.btn5 = QPushButton("Log in" ,self.loginbox)
        self.btn5.setGeometry(243, 435, 130, 70)
        self.btn5.setStyleSheet("QPushButton{ background: #645CBB; color: black; border-radius: 20px;}"
                                "QPushButton:hover{ background: #A084DC;border-radius: 10px;}")
        self.btn5.setFont(QFont('Times', 17))


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
App.setStyleSheet("QMainWindow{background-color: #EBC7E6 }")

window = HomePage()

sys.exit(App.exec())


