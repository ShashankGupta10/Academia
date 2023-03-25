
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
        self.setGeometry(0,0,1366,768)
        self.title = QLabel(self)
        self.title.setGeometry(300, 50, 200, 40)
        self.pixmap = QPixmap('images\RESHALA-removebg-preview.png')
        self.title.setPixmap(self.pixmap)


        self.photo = QLabel(self)
        self.photo.setGeometry(770, 50, 500, 500)
        self.pixmap = QPixmap('images\homepageimage5bgrm.png')
        self.photo.setPixmap(self.pixmap)


        self.panel1 = QLabel(self)
        self.panel1.setGeometry(100,140,700,450)
        self.panel1.setStyleSheet("QLabel{background: white;  border-radius: 20px; padding: 10px;}")
  
        self.title = QTextEdit(self.panel1)
        self.title.setGeometry(150,10,220,50)
        self.title.setStyleSheet("QTextEdit{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        self.price = QTextEdit(self.panel1)
        self.price.setGeometry(150,70,220,50)
        self.price.setStyleSheet("QTextEdit{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        self.description = QTextEdit(self.panel1)
        self.description.setGeometry(150,130,220,70)
        self.description.setStyleSheet("QTextEdit{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        self.mail = QTextEdit(self.panel1)
        self.mail.setGeometry(150,210,220,50)
        self.mail.setStyleSheet("QTextEdit{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        self.number = QTextEdit(self.panel1)
        self.number.setGeometry(150,270,220,50)
        self.number.setStyleSheet("QTextEdit{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")


        self.btn6 = QPushButton("Upload" ,self)
        self.btn6.setGeometry(300, 500, 100, 50)
        self.btn6.setStyleSheet("QPushButton{ background: #580599; color: white; border-radius: 20px; padding: 10px;}"
                                "QPushButton:hover{ background: #A084DC;border-radius: 10px;}")
        self.btn6.setFont(QFont('Times', 12))
        
  

        self.label2 = QLabel(self)
        self.pixmap = QPixmap('images\smalllogo.png')
        self.label2.setGeometry(230, 50, 50, 50)
        
        size = QSize(100, 100)
        self.label2.setPixmap(self.pixmap)



        productnametxt = QLabel(self.panel1)
        productnametxt.setText("Product Name :")
        productnametxt.setGeometry(10, 2,200,50) 
        productnametxt.setStyleSheet("background-color: transparent;")
        productnametxt.setFont(QFont('Times', 12))


        productpricetxt = QLabel(self.panel1)
        productpricetxt.setText("Price :")
        productpricetxt.setGeometry(10, 60,200,50)  
        productpricetxt.setStyleSheet("background-color: transparent;")
        productpricetxt.setFont(QFont('Times', 12))

        productDescriptiontxt = QLabel(self.panel1)
        productDescriptiontxt.setText("Description : ")
        productDescriptiontxt.setGeometry(10, 118,200,50) 
        productDescriptiontxt.setStyleSheet("background-color: transparent;")
        productDescriptiontxt.setFont(QFont('Times', 12))

        Emailtxt = QLabel(self.panel1)
        Emailtxt .setText("Email :")
        Emailtxt .setGeometry(10, 200,200,50)  
        Emailtxt .setStyleSheet("background-color: transparent;")
        Emailtxt .setFont(QFont('Times', 12))

        MobileNumbertxt = QLabel(self.panel1)
        MobileNumbertxt.setText("Phone Number:")
        MobileNumbertxt.setGeometry(10, 258,200,50)  
        MobileNumbertxt.setStyleSheet("background-color: transparent;")
        MobileNumbertxt.setFont(QFont('Times', 12))



       


      
        vbox = QVBoxLayout()
        vbox.setContentsMargins(100, 100, 500, 500)
        vbox.setSpacing(20)

        self.btn1 = QPushButton("Upload  Image",self.panel1)
        self.btn1.clicked.connect(self.getImage)
        # self.btn1.setFixedSize(100, 100)
        self.btn1.setGeometry(450,300,100,40)
        self.btn1.setStyleSheet("QPushButton{background: #C47AFF; position: fixed;border-radius:15px;color: black;border-radius:20px;} QPushButton:hover borderradius:20px;")
       
        vbox.addWidget(self.btn1)

        self.label = QLabel("Upload product image",self)
        self.label.setGeometry(500,200,200,200)
        self.label.setStyleSheet("border:2px solid black;")
        self.label.setAlignment(QtCore.Qt.AlignCenter)

        vbox.addWidget(self.label)

        self.setLayout(vbox)

        
    
        self.showMaximized()
        self.show()

    def getImage(self):
        fname = QFileDialog.getOpenFileName(self, 'Open file')

        imagePath = fname[0]
        pixmap = QPixmap(imagePath)
        
        self.label.setPixmap(QPixmap(pixmap))
        self.label.setFixedSize(200,200)
        self.label.setGeometry(500,200,200,200)
        self.label.setStyleSheet("border:2px solid black;object-fit:contain;")

        # self.resize(50,50)



App = QApplication(sys.argv)
App.setStyleSheet("QMainWindow{background-color: #BFACE2}")

window = HomePage()

sys.exit(App.exec())

