import socket
import threading
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QGraphicsOpacityEffect
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from PyQt5.QtCore import QPropertyAnimation
from pathlib import Path
from urllib import *
import sys
import os

HOST = ''
PORT = 9999

class Announcements(QMainWindow):            
    def __init__(self):
        super().__init__()
        
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.setWindowTitle("Academia")
        self.setGeometry(0,0,1920,1080)

        self.navbar = QLabel(self)
        self.navbar.setGeometry(0, 0, 1920, 100)
        self.navbar.setStyleSheet("QLabel{ background: black; position: fixed;} ")
        
        self.opacity_effect = QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(0.3)
  
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
        self.loginbox.setGeometry(0,100,120,800)
        self.loginbox.setStyleSheet("background-color: #3E54AC;")


        #*********************#

        self.panel1 = QLabel(self)
        self.panel1.setGeometry(200,140,700,350)
        self.panel1.setStyleSheet("QLabel{background: white;  border-radius: 20px; padding: 10px;}")
  
        self.panel2 = QLabel(self.panel1)
        self.panel2.setGeometry(0,0,300,350)
        self.panel2.setStyleSheet("QLabel{background: #82C3EC}")
  

        productnametxt = QLabel(self.panel1)
        productnametxt.setText("Product Name :")
        productnametxt.setGeometry(300, 2,200,50) 
        productnametxt.setStyleSheet("background-color: transparent;")
        productnametxt.setFont(QFont('Times', 12))


        productpricetxt = QLabel(self.panel1)
        productpricetxt.setText("Price :")
        productpricetxt.setGeometry(300, 60,200,50)  
        productpricetxt.setStyleSheet("background-color: transparent;")
        productpricetxt.setFont(QFont('Times', 12))

        productDescriptiontxt = QLabel(self.panel1)
        productDescriptiontxt.setText("Description : ")
        productDescriptiontxt.setGeometry(300, 118,200,50) 
        productDescriptiontxt.setStyleSheet("background-color: transparent;")
        productDescriptiontxt.setFont(QFont('Times', 12))

        Emailtxt = QLabel(self.panel1)
        Emailtxt .setText("Email :")
        Emailtxt .setGeometry(300, 200,200,50)  
        Emailtxt .setStyleSheet("background-color: transparent;")
        Emailtxt .setFont(QFont('Times', 12))

        MobileNumbertxt = QLabel(self.panel1)
        MobileNumbertxt.setText("Phone Number:")
        MobileNumbertxt.setGeometry(300, 258,200,50)  
        MobileNumbertxt.setStyleSheet("background-color: transparent;")
        MobileNumbertxt.setFont(QFont('Times', 12))



        self.title = QLabel(self.panel1)
        self.title.setGeometry(450,10,220,50)
        self.title.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        self.price =QLabel(self.panel1)
        self.price.setGeometry(450,70,220,50)
        self.price.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        self.description =QLabel(self.panel1)
        self.description.setGeometry(450,130,220,70)
        self.description.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        self.mail = QLabel(self.panel1)
        self.mail.setGeometry(450,210,220,50)
        self.mail.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        self.number = QLabel(self.panel1)
        self.number.setGeometry(450,270,220,50)
        self.number.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")


       


    

        icon = QIcon('Reshala_buy\chaticon.png')
        self.usernameicon = QPushButton("" ,self)
        self.usernameicon.setGeometry(20,150, 80, 80)
        self.usernameicon.setIcon(icon)
        size = QSize(50, 50)
        self.usernameicon.setIconSize(size)
        
        self.usernameicon = QPushButton("" ,self)
        self.usernameicon.setGeometry(20,300, 80, 80)
        self.usernameicon.setIcon(icon)
        size = QSize(50, 50)
        self.usernameicon.setIconSize(size)
        
        self.usernameicon = QPushButton("" ,self)
        self.usernameicon.setGeometry(20,450, 80, 80)
        self.usernameicon.setIcon(icon)
        size = QSize(50, 50)
        self.usernameicon.setIconSize(size)
        
        self.usernameicon = QPushButton("" ,self)
        self.usernameicon.setGeometry(20,600, 80, 80)
        self.usernameicon.setIcon(icon)
        size = QSize(50, 50)
        self.usernameicon.setIconSize(size)
        
       
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
window = Announcements()
sys.exit(App.exec())