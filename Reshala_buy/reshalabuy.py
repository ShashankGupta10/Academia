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
# from pymongo import MongoClient

# client = MongoClient("mongodb+srv://shashankgupta2003:Shashank10@cluster0.x6bsdlb.mongodb.net/test")
# db = client['IOP']


# resultProductName = db.Re_Shala.find_one({"price": "200"}, {"productName": 1})
# resultPrice = db.Re_Shala.find_one({"price": "200"}, {"price": 1})
# resultDescription = db.Re_Shala.find_one({"price": "200"}, {"description": 1})
# resultPhone = db.Re_Shala.find_one({"price": "200"}, {"phone_number": 1})
# resultEmail = db.Re_Shala.find_one({"price": "200"}, {"email": 1})
# resultImage = db.Re_Shala.find_one({"price": "200"}, {"image": 1})
# imageData = resultImage['image']

class Announcements(QMainWindow):            
    def __init__(self):
        super().__init__()
        
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

        self.panel1.setGeometry(150,130,700,350)
        self.panel1.setStyleSheet("QLabel{ background: white;  border-radius: 20px; padding: 10px;}")
  
        bgimg1 = QLabel(self.panel1)
        pixmap1 = QPixmap()
        # pixmap.loadFromData(imageData)
        bgimg1.setPixmap(pixmap1)  
        bgimg1.setGeometry(0,0,300,350)
        bgimg1.setStyleSheet("QLabel{ background: #82C3EC}")
  

        productnametxt1 = QLabel(self.panel1)
        productnametxt1.setText("Product Name :")
        productnametxt1.setGeometry(300, 2,200,50) 
        productnametxt1.setStyleSheet("background-color: transparent;")
        productnametxt1.setFont(QFont('Times', 12))


        productpricetxt1 = QLabel(self.panel1)
        productpricetxt1.setText("Price :")
        productpricetxt1.setGeometry(300, 60,200,50)  
        productpricetxt1.setStyleSheet("background-color: transparent;")
        productpricetxt1.setFont(QFont('Times', 12))

        productDescriptiontxt1 = QLabel(self.panel1)
        productDescriptiontxt1.setText("Description : ")
        productDescriptiontxt1.setGeometry(300, 118,200,50) 
        productDescriptiontxt1.setStyleSheet("background-color: transparent;")
        productDescriptiontxt1.setFont(QFont('Times', 12))

        Emailtxt1 = QLabel(self.panel1)
        Emailtxt1.setText("Email :")
        Emailtxt1.setGeometry(300, 200,200,50)  
        Emailtxt1.setStyleSheet("background-color: transparent;")
        Emailtxt1.setFont(QFont('Times', 12))

        MobileNumbertxt1 = QLabel(self.panel1)
        MobileNumbertxt1.setText("Phone Number:")
        MobileNumbertxt1.setGeometry(300, 258,200,50)  
        MobileNumbertxt1.setStyleSheet("background-color: transparent;")
        MobileNumbertxt1.setFont(QFont('Times', 12))



        productnm1 = QLabel(self.panel1)
        # productnm1.setText(resultProductName["productName"])
        productnm1.setGeometry(450,10,220,50)
        productnm1.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        price1 =QLabel(self.panel1)
        # price1.setText(resultPrice["price"])
        price1.setGeometry(450,70,220,50)
        price1.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        describ1 =QLabel(self.panel1)
        # describ1.setText(resultDescription["description"])
        describ1.setGeometry(450,130,220,70)
        describ1.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        mail1 = QLabel(self.panel1)
        # mail1.setText(resultEmail["email"])
        mail1.setGeometry(450,210,220,50)
        mail1.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        num1 = QLabel(self.panel1)
        # num1.setText(resultPhone["phone_number"])
        num1.setGeometry(450,270,220,50)
        num1.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")
        
        #-------------------------------
        
        self.panel2 = QLabel(self)
        self.panel2.setGeometry(880,130,700,350)
        self.panel2.setStyleSheet("QLabel{ background: white;  border-radius: 20px; padding: 10px;}")

        bgimg2 = QLabel(self.panel2)
        pixmap2 = QPixmap()
        # pixmap.loadFromData(imageData)
        bgimg2.setPixmap(pixmap2)  
        bgimg2.setGeometry(0,0,300,350)
        bgimg2.setStyleSheet("QLabel{ background: #82C3EC}")
        
          

        productnametxt2 = QLabel(self.panel2)
        productnametxt2.setText("Product Name :")
        productnametxt2.setGeometry(300, 2,200,50) 
        productnametxt2.setStyleSheet("background-color: transparent;")
        productnametxt2.setFont(QFont('Times', 12))


        productpricetxt2 = QLabel(self.panel2)
        productpricetxt2.setText("Price :")
        productpricetxt2.setGeometry(300, 60,200,50)  
        productpricetxt2.setStyleSheet("background-color: transparent;")
        productpricetxt2.setFont(QFont('Times', 12))

        productDescriptiontxt2 = QLabel(self.panel2)
        productDescriptiontxt2.setText("Description : ")
        productDescriptiontxt2.setGeometry(300, 118,200,50) 
        productDescriptiontxt2.setStyleSheet("background-color: transparent;")
        productDescriptiontxt2.setFont(QFont('Times', 12))

        Emailtxt2 = QLabel(self.panel2)
        Emailtxt2.setText("Email :")
        Emailtxt2.setGeometry(300, 200,200,50)  
        Emailtxt2.setStyleSheet("background-color: transparent;")
        Emailtxt2.setFont(QFont('Times', 12))

        MobileNumbertxt2 = QLabel(self.panel2)
        MobileNumbertxt2.setText("Phone Number:")
        MobileNumbertxt2.setGeometry(300, 258,200,50)  
        MobileNumbertxt2.setStyleSheet("background-color: transparent;")
        MobileNumbertxt2.setFont(QFont('Times', 12))



        productnm2 = QLabel(self.panel2)
        # productnm2.setText(resultProductName["productName"])
        productnm2.setGeometry(450,10,220,50)
        productnm2.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        price2 =QLabel(self.panel2)
        # price2.setText(resultPrice["price"])
        price2.setGeometry(450,70,220,50)
        price2.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        describ2 =QLabel(self.panel2)
        # describ2.setText(resultDescription["description"])
        describ2.setGeometry(450,130,220,70)
        describ2.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        mail2 = QLabel(self.panel2)
        # mail2.setText(resultEmail["email"])
        mail2.setGeometry(450,210,220,50)
        mail2.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        num2 = QLabel(self.panel2)
        # num2.setText(resultPhone["phone_number"])
        num2.setGeometry(450,270,220,50)
        num2.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        #-------------------------------
        
        self.panel3 = QLabel(self)
        self.panel3.setGeometry(150,500,700,350)
        self.panel3.setStyleSheet("QLabel{ background: white;  border-radius: 20px; padding: 10px;}")

        bgimg3 = QLabel(self.panel3)
        pixmap3 = QPixmap()
        # pixmap.loadFromData(imageData)
        bgimg3.setPixmap(pixmap3)  
        bgimg3.setGeometry(0,0,300,350)
        bgimg3.setStyleSheet("QLabel{ background: #82C3EC}")
        
          

        productnametxt3 = QLabel(self.panel3)
        productnametxt3.setText("Product Name :")
        productnametxt3.setGeometry(300, 2,200,50) 
        productnametxt3.setStyleSheet("background-color: transparent;")
        productnametxt3.setFont(QFont('Times', 12))


        productpricetxt3 = QLabel(self.panel3)
        productpricetxt3.setText("Price :")
        productpricetxt3.setGeometry(300, 60,200,50)  
        productpricetxt3.setStyleSheet("background-color: transparent;")
        productpricetxt3.setFont(QFont('Times', 12))

        productDescriptiontxt3 = QLabel(self.panel3)
        productDescriptiontxt3.setText("Description : ")
        productDescriptiontxt3.setGeometry(300, 118,200,50) 
        productDescriptiontxt3.setStyleSheet("background-color: transparent;")
        productDescriptiontxt3.setFont(QFont('Times', 12))

        Emailtxt3 = QLabel(self.panel3)
        Emailtxt3.setText("Email :")
        Emailtxt3.setGeometry(300, 200,200,50)  
        Emailtxt3.setStyleSheet("background-color: transparent;")
        Emailtxt3.setFont(QFont('Times', 12))

        MobileNumbertxt3 = QLabel(self.panel3)
        MobileNumbertxt3.setText("Phone Number:")
        MobileNumbertxt3.setGeometry(300, 258,200,50)  
        MobileNumbertxt3.setStyleSheet("background-color: transparent;")
        MobileNumbertxt3.setFont(QFont('Times', 12))



        productnm3 = QLabel(self.panel3)
        # productnm3.setText(resultProductName["productName"])
        productnm3.setGeometry(450,10,220,50)
        productnm3.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        price3 =QLabel(self.panel3)
        # price3.setText(resultPrice["price"])
        price3.setGeometry(450,70,220,50)
        price3.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        describ3 =QLabel(self.panel3)
        # describ3.setText(resultDescription["description"])
        describ3.setGeometry(450,130,220,70)
        describ3.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        mail3 = QLabel(self.panel3)
        # mail3.setText(resultEmail["email"])
        mail3.setGeometry(450,210,220,50)
        mail3.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        num3 = QLabel(self.panel3)
        # num3.setText(resultPhone["phone_number"])
        num3.setGeometry(450,270,220,50)
        num3.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        #-------------------------------
        
        self.panel4 = QLabel(self)
        self.panel4.setGeometry(880,500,700,350)
        self.panel4.setStyleSheet("QLabel{ background: white;  border-radius: 20px; padding: 10px;}")

        bgimg4 = QLabel(self.panel4)
        pixmap4 = QPixmap()
        # pixmap.loadFromData(imageData)
        bgimg4.setPixmap(pixmap4)  
        bgimg4.setGeometry(0,0,300,350)
        bgimg4.setStyleSheet("QLabel{ background: #82C3EC}")
        
          

        productnametxt4 = QLabel(self.panel4)
        productnametxt4.setText("Product Name :")
        productnametxt4.setGeometry(300, 2,200,50) 
        productnametxt4.setStyleSheet("background-color: transparent;")
        productnametxt4.setFont(QFont('Times', 12))

        productpricetxt4 = QLabel(self.panel4)
        productpricetxt4.setText("Price :")
        productpricetxt4.setGeometry(300, 60,200,50)  
        productpricetxt4.setStyleSheet("background-color: transparent;")
        productpricetxt4.setFont(QFont('Times', 12))

        productDescriptiontxt4 = QLabel(self.panel4)
        productDescriptiontxt4.setText("Description : ")
        productDescriptiontxt4.setGeometry(300, 118,200,50) 
        productDescriptiontxt4.setStyleSheet("background-color: transparent;")
        productDescriptiontxt4.setFont(QFont('Times', 12))

        Emailtxt4 = QLabel(self.panel4)
        Emailtxt4.setText("Email :")
        Emailtxt4.setGeometry(300, 200,200,50)  
        Emailtxt4.setStyleSheet("background-color: transparent;")
        Emailtxt4.setFont(QFont('Times', 12))

        MobileNumbertxt4 = QLabel(self.panel4)
        MobileNumbertxt4.setText("Phone Number:")
        MobileNumbertxt4.setGeometry(300, 258,200,50)  
        MobileNumbertxt4.setStyleSheet("background-color: transparent;")
        MobileNumbertxt4.setFont(QFont('Times', 12))



        productnm4 = QLabel(self.panel4)
        # productnm4.setText(resultProductName["productName"])
        productnm4.setGeometry(450,10,220,50)
        productnm4.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        price4 =QLabel(self.panel4)
        # price4.setText(resultPrice["price"])
        price4.setGeometry(450,70,220,50)
        price4.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        describ4 =QLabel(self.panel4)
        # describ4.setText(resultDescription["description"])
        describ4.setGeometry(450,130,220,70)
        describ4.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        mail4 = QLabel(self.panel4)
        # mail4.setText(resultEmail["email"])
        mail4.setGeometry(450,210,220,50)
        mail4.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        num4 = QLabel(self.panel4)
        # num4.setText(resultPhone["phone_number"])
        num4.setGeometry(450,270,220,50)
        num4.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

    

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
