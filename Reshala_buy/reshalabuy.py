from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from urllib import *
import sys,os
from pymongo import MongoClient

client = MongoClient("mongodb+srv://shashankgupta2003:Shashank10@cluster0.x6bsdlb.mongodb.net/test")
db = client['IOP']


resultProductName1 = db.Re_Shala.find_one({"price": "200"}, {"productName": 1})
resultPrice1 = db.Re_Shala.find_one({"price": "200"}, {"price": 1})
resultDescription1 = db.Re_Shala.find_one({"price": "200"}, {"description": 1})
resultPhone1 = db.Re_Shala.find_one({"price": "200"}, {"phone_number": 1})
resultEmail1 = db.Re_Shala.find_one({"price": "200"}, {"email": 1})
resultImage1 = db.Re_Shala.find_one({"price": "200"}, {"image": 1})
imageData1 = resultImage1['image']

resultProductName2 = db.Re_Shala.find_one({"price": "500"}, {"productName": 1})
resultPrice2 = db.Re_Shala.find_one({"price": "500"}, {"price": 1})
resultDescription2 = db.Re_Shala.find_one({"price": "500"}, {"description": 1})
resultPhone2 = db.Re_Shala.find_one({"price": "500"}, {"phone_number": 1})
resultEmail2 = db.Re_Shala.find_one({"price": "500"}, {"email": 1})
resultImage2 = db.Re_Shala.find_one({"price": "500"}, {"image": 1})
imageData2 = resultImage2['image']

resultProductName3 = db.Re_Shala.find_one({"price": "100"}, {"productName": 1})
resultPrice3 = db.Re_Shala.find_one({"price": "100"}, {"price": 1})
resultDescription3 = db.Re_Shala.find_one({"price": "100"}, {"description": 1})
resultPhone3 = db.Re_Shala.find_one({"price": "100"}, {"phone_number": 1})
resultEmail3 = db.Re_Shala.find_one({"price": "100"}, {"email": 1})
resultImage3 = db.Re_Shala.find_one({"price": "100"}, {"image": 1})
imageData3 = resultImage3['image']

resultProductName4 = db.Re_Shala.find_one({"price": "400"}, {"productName": 1})
resultPrice4 = db.Re_Shala.find_one({"price": "400"}, {"price": 1})
resultDescription4 = db.Re_Shala.find_one({"price": "400"}, {"description": 1})
resultPhone4 = db.Re_Shala.find_one({"price": "400"}, {"phone_number": 1})
resultEmail4 = db.Re_Shala.find_one({"price": "400"}, {"email": 1})
resultImage4 = db.Re_Shala.find_one({"price": "400"}, {"image": 1})
imageData4 = resultImage4['image']

class reshaalabuy(QMainWindow):            
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Academia")
        self.setGeometry(0,0,1920,1080)


        self.header = QLabel(self)
        self.header.setGeometry(0, 0, 1920, 100)
        self.header.setStyleSheet("QLabel{ background: black; position: fixed;} ")

        backbtn = QToolButton(self)
        backbtn.setArrowType(Qt.LeftArrow)        
        backbtn.setGeometry(100,100,50,50)
        backbtn.setStyleSheet("QToolButton{ background: transparent;color: #301E67}")
        backbtn.clicked.connect(self.back)

        siz = QSize(80,80)
        logo = QPushButton(self)
        logo.setGeometry(30, 20, 80, 80)
        logocon = QIcon("All icons\logo.png")
        logo.setStyleSheet("background: transparent")
        logo.setIcon(logocon)
        logo.setIconSize(siz)

        navbarbtn1 = QPushButton("Home", self)
        navbarbtn1.setGeometry(1200, 31, 100, 40)
        navbarbtn1.setStyleSheet("QPushButton{ background: Black; position: fixed;border-radius:15px;color: white;}")
        navbarbtn1.setFont(QFont('Times', 20))
        navbarbtn1.clicked.connect(self.back)


        navbarbtn2= QPushButton("Reshala", self)
        navbarbtn2.setGeometry(1400, 31, 150, 40)
        navbarbtn2.setStyleSheet("QPushButton{ background: Black; position: fixed;border-radius:15px;color: white;}")
        navbarbtn2.setFont(QFont('Times', 20))
        navbarbtn2.clicked.connect(self.reshaala)
        
        navbarbtn3= QPushButton("About", self)
        navbarbtn3.setGeometry(1600, 31, 150, 40)
        navbarbtn3.setStyleSheet("QPushButton{ background: Black; position: fixed;border-radius:15px;color: white;}")
        navbarbtn3.setFont(QFont('Times', 20))


        icon = QIcon("D:\Pyfon MPR\TkinterGUI\images\homepageimage1bgrm.png")
        self.btn10 = QPushButton("" ,self)
        self.btn10.setGeometry(1800, 0, 100, 100)
        self.btn10.setStyleSheet("background : black;")
        self.btn10.setIcon(icon)
        size = QSize(100, 100)
        self.btn10.setIconSize(size)
        
        sidebar = QLabel(self)
        sidebar.setGeometry(0,100,100,1920)
        sidebar.setStyleSheet("background-color: #3E54AC;")
        
        size = QSize(60, 60)
        
        anicon = QIcon('All icons\\announcement.png')
        announce = QPushButton(sidebar)
        announce.setGeometry(20,30, 60, 60)
        announce.setStyleSheet("border : 0px solid black")
        announce.setIcon(anicon)
        announce.setIconSize(size)
        announce.clicked.connect(self.announcement)
        
        aticon = QIcon('All icons\\attendence.png')
        attend = QPushButton(sidebar)
        attend.setGeometry(20,150, 60, 60)
        attend.setStyleSheet("border : 0px solid black")
        attend.setIcon(aticon)
        attend.setIconSize(size)
        attend.clicked.connect(self.attendence)

        asicon = QIcon('All icons\\assignment.png')
        assign = QPushButton(sidebar)
        assign.setGeometry(25, 270, 60, 60)
        assign.setStyleSheet("border : 0px solid black")
        assign.setIcon(asicon)
        assign.setIconSize(size)
        assign.clicked.connect(self.assignment)

        reicon = QIcon('All icons\\reshaala.png')
        reshaala = QPushButton(sidebar)
        reshaala.setGeometry(20,390, 60, 60)
        reshaala.setStyleSheet("border : 0px solid black")
        reshaala.setIcon(reicon)
        reshaala.setIconSize(size)
        reshaala.clicked.connect(self.reshaala)
        
        proficon = QIcon('All icons\\profile.png')
        profile = QPushButton(sidebar)
        profile.setGeometry(20, 700, 60, 60)
        profile.setStyleSheet("border : 0px solid black")
        profile.setIcon(proficon)
        profile.setIconSize(size)
        profile.clicked.connect(self.sprofile)
        
        
        #*********************#

        self.panel1 = QLabel(self)

        self.panel1.setGeometry(250,130,700,350)
        self.panel1.setStyleSheet("QLabel{ background: white;  border-radius: 20px; padding: 10px;}")
  
        bgimg1 = QLabel(self.panel1)
        pixmap1 = QPixmap()
        pixmap1.loadFromData(imageData1)
        bgimg1.setPixmap(pixmap1)  
        bgimg1.setGeometry(0,0,300,350)
        bgimg1.setStyleSheet("QLabel{ background: #82C3EC}")
        bgimg1.setScaledContents(True)
  
        productnametxt1 = QLabel(self.panel1)
        productnametxt1.setText("Product Name")
        productnametxt1.setGeometry(300, 2,200,50) 
        productnametxt1.setStyleSheet("background-color: transparent;")
        productnametxt1.setFont(QFont('Times', 12))

        productpricetxt1 = QLabel(self.panel1)
        productpricetxt1.setText("Price")
        productpricetxt1.setGeometry(300, 60,200,50)  
        productpricetxt1.setStyleSheet("background-color: transparent;")
        productpricetxt1.setFont(QFont('Times', 12))

        productDescriptiontxt1 = QLabel(self.panel1)
        productDescriptiontxt1.setText("Description")
        productDescriptiontxt1.setGeometry(300, 118,200,50) 
        productDescriptiontxt1.setStyleSheet("background-color: transparent;")
        productDescriptiontxt1.setFont(QFont('Times', 12))

        Emailtxt1 = QLabel(self.panel1)
        Emailtxt1.setText("Email")
        Emailtxt1.setGeometry(300, 200,200,50)  
        Emailtxt1.setStyleSheet("background-color: transparent;")
        Emailtxt1.setFont(QFont('Times', 12))

        MobileNumbertxt1 = QLabel(self.panel1)
        MobileNumbertxt1.setText("Phone Number")
        MobileNumbertxt1.setGeometry(300, 258,200,50)  
        MobileNumbertxt1.setStyleSheet("background-color: transparent;")
        MobileNumbertxt1.setFont(QFont('Times', 12))

        productnm1 = QLabel(self.panel1)
        productnm1.setText(resultProductName1["productName"])
        productnm1.setGeometry(450,10,220,50)
        productnm1.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        price1 =QLabel(self.panel1)
        price1.setText(resultPrice1["price"])
        price1.setGeometry(450,70,220,50)
        price1.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        describ1 =QLabel(self.panel1)
        describ1.setText(resultDescription1["description"])
        describ1.setGeometry(450,130,220,70)
        describ1.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        mail1 = QLabel(self.panel1)
        mail1.setText(resultEmail1["email"])
        mail1.setGeometry(450,210,220,50)
        mail1.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        num1 = QLabel(self.panel1)
        num1.setText(resultPhone1["phone_number"])
        num1.setGeometry(450,270,220,50)
        num1.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")
        
        #-------------------------------
        
        self.panel2 = QLabel(self)
        self.panel2.setGeometry(1070,130,700,350)
        self.panel2.setStyleSheet("QLabel{ background: white;  border-radius: 20px; padding: 10px;}")

        bgimg2 = QLabel(self.panel2)
        pixmap2 = QPixmap()
        pixmap2.loadFromData(imageData2)
        bgimg2.setPixmap(pixmap2)  
        bgimg2.setGeometry(0,0,300,350)
        bgimg2.setStyleSheet("QLabel{ background: #82C3EC}")
        bgimg2.setScaledContents(True)

        productnametxt2 = QLabel(self.panel2)
        productnametxt2.setText("Product Name")
        productnametxt2.setGeometry(300, 2,200,50) 
        productnametxt2.setStyleSheet("background-color: transparent;")
        productnametxt2.setFont(QFont('Times', 12))

        productpricetxt2 = QLabel(self.panel2)
        productpricetxt2.setText("Price")
        productpricetxt2.setGeometry(300, 60,200,50)  
        productpricetxt2.setStyleSheet("background-color: transparent;")
        productpricetxt2.setFont(QFont('Times', 12))

        productDescriptiontxt2 = QLabel(self.panel2)
        productDescriptiontxt2.setText("Description")
        productDescriptiontxt2.setGeometry(300, 118,200,50) 
        productDescriptiontxt2.setStyleSheet("background-color: transparent;")
        productDescriptiontxt2.setFont(QFont('Times', 12))

        Emailtxt2 = QLabel(self.panel2)
        Emailtxt2.setText("Email")
        Emailtxt2.setGeometry(300, 200,200,50)  
        Emailtxt2.setStyleSheet("background-color: transparent;")
        Emailtxt2.setFont(QFont('Times', 12))

        MobileNumbertxt2 = QLabel(self.panel2)
        MobileNumbertxt2.setText("Phone Number")
        MobileNumbertxt2.setGeometry(300, 258,200,50)  
        MobileNumbertxt2.setStyleSheet("background-color: transparent;")
        MobileNumbertxt2.setFont(QFont('Times', 12))

        productnm2 = QLabel(self.panel2)
        productnm2.setText(resultProductName2["productName"])
        productnm2.setGeometry(450,10,220,50)
        productnm2.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        price2 =QLabel(self.panel2)
        price2.setText(resultPrice2["price"])
        price2.setGeometry(450,70,220,50)
        price2.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        describ2 =QLabel(self.panel2)
        describ2.setText(resultDescription2["description"])
        describ2.setGeometry(450,130,220,70)
        describ2.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        mail2 = QLabel(self.panel2)
        mail2.setText(resultEmail2["email"])
        mail2.setGeometry(450,210,220,50)
        mail2.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        num2 = QLabel(self.panel2)
        num2.setText(resultPhone2["phone_number"])
        num2.setGeometry(450,270,220,50)
        num2.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        #-------------------------------
        
        self.panel3 = QLabel(self)
        self.panel3.setGeometry(250,500,700,350)
        self.panel3.setStyleSheet("QLabel{ background: white;  border-radius: 20px; padding: 10px;}")

        bgimg3 = QLabel(self.panel3)
        pixmap3 = QPixmap()
        pixmap3.loadFromData(imageData3)
        bgimg3.setPixmap(pixmap3)  
        bgimg3.setGeometry(0,0,300,350)
        bgimg3.setStyleSheet("QLabel{ background: #82C3EC}")
        bgimg3.setScaledContents(True)
        
        productnametxt3 = QLabel(self.panel3)
        productnametxt3.setText("Product Name")
        productnametxt3.setGeometry(300, 2,200,50) 
        productnametxt3.setStyleSheet("background-color: transparent;")
        productnametxt3.setFont(QFont('Times', 12))

        productpricetxt3 = QLabel(self.panel3)
        productpricetxt3.setText("Price")
        productpricetxt3.setGeometry(300, 60,200,50)  
        productpricetxt3.setStyleSheet("background-color: transparent;")
        productpricetxt3.setFont(QFont('Times', 12))

        productDescriptiontxt3 = QLabel(self.panel3)
        productDescriptiontxt3.setText("Description")
        productDescriptiontxt3.setGeometry(300, 118,200,50) 
        productDescriptiontxt3.setStyleSheet("background-color: transparent;")
        productDescriptiontxt3.setFont(QFont('Times', 12))

        Emailtxt3 = QLabel(self.panel3)
        Emailtxt3.setText("Email")
        Emailtxt3.setGeometry(300, 200,200,50)  
        Emailtxt3.setStyleSheet("background-color: transparent;")
        Emailtxt3.setFont(QFont('Times', 12))

        MobileNumbertxt3 = QLabel(self.panel3)
        MobileNumbertxt3.setText("Phone Number")
        MobileNumbertxt3.setGeometry(300, 258,200,50)  
        MobileNumbertxt3.setStyleSheet("background-color: transparent;")
        MobileNumbertxt3.setFont(QFont('Times', 12))

        productnm3 = QLabel(self.panel3)
        productnm3.setText(resultProductName3["productName"])
        productnm3.setGeometry(450,10,220,50)
        productnm3.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        price3 =QLabel(self.panel3)
        price3.setText(resultPrice3["price"])
        price3.setGeometry(450,70,220,50)
        price3.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        describ3 =QLabel(self.panel3)
        describ3.setText(resultDescription3["description"])
        describ3.setGeometry(450,130,220,70)
        describ3.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        mail3 = QLabel(self.panel3)
        mail3.setText(resultEmail3["email"])
        mail3.setGeometry(450,210,220,50)
        mail3.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        num3 = QLabel(self.panel3)
        num3.setText(resultPhone3["phone_number"])
        num3.setGeometry(450,270,220,50)
        num3.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        #-------------------------------
        
        self.panel4 = QLabel(self)
        self.panel4.setGeometry(1070,500,700,350)
        self.panel4.setStyleSheet("QLabel{ background: white;  border-radius: 20px; padding: 10px;}")

        bgimg4 = QLabel(self.panel4)
        pixmap4 = QPixmap()
        pixmap4.loadFromData(imageData4)
        bgimg4.setPixmap(pixmap4)  
        bgimg4.setGeometry(0,0,300,350)
        bgimg4.setStyleSheet("QLabel{ background: #82C3EC}")
        bgimg4.setScaledContents(True)
          

        productnametxt4 = QLabel(self.panel4)
        productnametxt4.setText("Product Name")
        productnametxt4.setGeometry(300, 2,200,50) 
        productnametxt4.setStyleSheet("background-color: transparent;")
        productnametxt4.setFont(QFont('Times', 12))

        productpricetxt4 = QLabel(self.panel4)
        productpricetxt4.setText("Price")
        productpricetxt4.setGeometry(300, 60,200,50)  
        productpricetxt4.setStyleSheet("background-color: transparent;")
        productpricetxt4.setFont(QFont('Times', 12))

        productDescriptiontxt4 = QLabel(self.panel4)
        productDescriptiontxt4.setText("Description")
        productDescriptiontxt4.setGeometry(300, 118,200,50) 
        productDescriptiontxt4.setStyleSheet("background-color: transparent;")
        productDescriptiontxt4.setFont(QFont('Times', 12))

        Emailtxt4 = QLabel(self.panel4)
        Emailtxt4.setText("Email")
        Emailtxt4.setGeometry(300, 200,200,50)  
        Emailtxt4.setStyleSheet("background-color: transparent;")
        Emailtxt4.setFont(QFont('Times', 12))

        MobileNumbertxt4 = QLabel(self.panel4)
        MobileNumbertxt4.setText("Phone Number")
        MobileNumbertxt4.setGeometry(300, 258,200,50)  
        MobileNumbertxt4.setStyleSheet("background-color: transparent;")
        MobileNumbertxt4.setFont(QFont('Times', 12))

        productnm4 = QLabel(self.panel4)
        productnm4.setText(resultProductName4["productName"])
        productnm4.setGeometry(450,10,220,50)
        productnm4.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        price4 =QLabel(self.panel4)
        price4.setText(resultPrice4["price"])
        price4.setGeometry(450,70,220,50)
        price4.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        describ4 =QLabel(self.panel4)
        describ4.setText(resultDescription4["description"])
        describ4.setGeometry(450,130,220,70)
        describ4.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        mail4 = QLabel(self.panel4)
        mail4.setText(resultEmail4["email"])
        mail4.setGeometry(450,210,220,50)
        mail4.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        num4 = QLabel(self.panel4)
        num4.setText(resultPhone4["phone_number"])
        num4.setGeometry(450,270,220,50)
        num4.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")
       
        self.footer = QLabel(self)
        self.footer.setGeometry(0, 900, 1920, 1080)
        self.footer.setStyleSheet("QLabel{ background: black; position: fixed;} ")

        self.label1 = QPushButton(self.footer)
        self.label1.setGeometry(100,0,150,100)
        self.label1.setStyleSheet("color: white; background: black;")
        self.label1.setText("@Academia 2023")
        self.label1.setFont(QFont('Times', 10))

        self.label2 = QPushButton(self.footer)
        self.label2.setGeometry(300,0,150,100)
        self.label2.setStyleSheet("color: white; background: black;")
        self.label2.setText("Terms of Use")
        self.label2.setFont(QFont('Times', 10))

        self.label3 = QPushButton(self.footer)
        self.label3.setGeometry(500,0,200,100)
        self.label3.setStyleSheet("color: white; background: black;")
        self.label3.setText("Privacy Policy")
        self.label3.setFont(QFont('Times', 10))
                                
        self.label4 = QPushButton(self.footer)
        self.label4.setGeometry(1400,0,500,100)
        self.label4.setStyleSheet("color: white; background: black;")
        self.label4.setText("Copyright © 2023 Academia Inc. All rights reserved.")
        self.label4.setFont(QFont('Times', 10))
        
        self.showMaximized()
        self.show()
    

    def sell(self):
        window.close()
        os.system("python Reshala_sell\\reshalasell.py &") 
    def announcement(self):
        window.close()
        os.system("python StudentAnnouncement.py &")   
    def attendence(self):
        window.close()
        os.system("python Attendancestudent.py &")
    def assignment(self):
        window.close()
        os.system("python AssignmentStudent.py &") 
    def reshaala(self):
        window.close()
        os.system("python Reshala_sell\\reshalasell.py &") 
    def sprofile(self):
        window.close()
        os.system("python profilestudent.py &")
    def back(self):
        window.close()
        os.system("python Studentdashboard.py &")

   
App = QApplication(sys.argv)
App.setStyleSheet("QMainWindow{background-color: #EBC7E6 }")
window = reshaalabuy()
sys.exit(App.exec())
