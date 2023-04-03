from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from pymongo import MongoClient
import sys,os

client = MongoClient("mongodb+srv://shashankgupta2003:Shashank10@cluster0.x6bsdlb.mongodb.net/test")
db = client['IOP']

class HomePage(QMainWindow):
            
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Home Page")
        self.setGeometry(0,0,1920,1080)


        self.header = QLabel(self)
        self.header.setGeometry(0, 0, 1920, 100)
        self.header.setStyleSheet("QLabel{ background: black; position: fixed;} ")

        backbtn = QToolButton(self)
        backbtn.setArrowType(Qt.LeftArrow)        
        backbtn.setGeometry(100,100,50,50)
        backbtn.setStyleSheet("QToolButton{ background:  #A459D1;color: #301E67}")
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


        navbarbtn2= QPushButton("Reshala", self)
        navbarbtn2.setGeometry(1400, 31, 150, 40)
        navbarbtn2.setStyleSheet("QPushButton{ background: Black; position: fixed;border-radius:15px;color: white;}")
        navbarbtn2.setFont(QFont('Times', 20))
        
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
        sidebar.setGeometry(0,100,120,1920)
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



        self.title = QLabel(self)
        self.title.setGeometry(300, 50, 200, 40)
        self.pixmap = QPixmap('images\RESHALA-removebg-preview.png')
        self.title.setPixmap(self.pixmap)


        self.photo = QLabel(self)
        self.photo.setGeometry(770, 50, 500, 500)
        self.pixmap = QPixmap('images\homepageimage5bgrm.png')
        self.photo.setPixmap(self.pixmap)


        self.panel1 = QLabel(self)
        self.panel1.setGeometry(610,200,800,600)
        self.panel1.setStyleSheet("QLabel{ background: white;  border-radius: 20px; padding: 10px;}")
  
        self.title = QLineEdit(self.panel1)
        self.title.setGeometry(200,50,220,50)
        self.title.setStyleSheet("QLineEdit{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        self.price = QLineEdit(self.panel1)
        self.price.setGeometry(200,125,220,50)
        self.price.setStyleSheet("QLineEdit{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        self.description = QLineEdit(self.panel1)
        self.description.setGeometry(200,200,220,70)
        self.description.setStyleSheet("QLineEdit{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        self.mail = QLineEdit(self.panel1)
        self.mail.setGeometry(200,325,220,50)
        self.mail.setStyleSheet("QLineEdit{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")

        self.number = QLineEdit(self.panel1)
        self.number.setGeometry(200,400,220,50)
        self.number.setStyleSheet("QLineEdit{ background: #EDE3FF; border-color: black; border-radius: 5px; padding: 10px;}")


        self.btn6 = QPushButton("Upload" ,self.panel1)
        self.btn6.setGeometry(350, 500, 100, 50)
        self.btn6.setStyleSheet("QPushButton{ background: #580599; color: white; border-radius: 20px; padding: 10px;}"
                                "QPushButton:hover{ background: #A084DC;border-radius: 10px;}")
        self.btn6.setFont(QFont('Times', 12))
        self.btn6.clicked.connect(self.on_click_upload)
        
  

        self.label2 = QLabel(self)
        self.pixmap = QPixmap('images\smalllogo.png')
        self.label2.setGeometry(230, 50, 50, 50)
        
        size = QSize(100, 100)
        self.label2.setPixmap(self.pixmap)



        productnametxt = QLabel(self.panel1)
        productnametxt.setText("Product Name :")
        productnametxt.setGeometry(10, 50,200,50) 
        productnametxt.setStyleSheet("background-color: transparent;")
        productnametxt.setFont(QFont('Times', 12))


        productpricetxt = QLabel(self.panel1)
        productpricetxt.setText("Price :")
        productpricetxt.setGeometry(10, 125,200,50)  
        productpricetxt.setStyleSheet("background-color: transparent;")
        productpricetxt.setFont(QFont('Times', 12))

        productDescriptiontxt = QLabel(self.panel1)
        productDescriptiontxt.setText("Description : ")
        productDescriptiontxt.setGeometry(10, 200,200,50) 
        productDescriptiontxt.setStyleSheet("background-color: transparent;")
        productDescriptiontxt.setFont(QFont('Times', 12))

        Emailtxt = QLabel(self.panel1)
        Emailtxt .setText("Email :")
        Emailtxt .setGeometry(10, 325,200,50)  
        Emailtxt .setStyleSheet("background-color: transparent;")
        Emailtxt .setFont(QFont('Times', 12))

        MobileNumbertxt = QLabel(self.panel1)
        MobileNumbertxt.setText("Phone Number:")
        MobileNumbertxt.setGeometry(10, 400,200,50)  
        MobileNumbertxt.setStyleSheet("background-color: transparent;")
        MobileNumbertxt.setFont(QFont('Times', 12))

      
        vbox = QVBoxLayout()
        vbox.setContentsMargins(100, 100, 500, 500)
        vbox.setSpacing(20)

        self.btn1 = QPushButton("Upload Image",self.panel1)
        self.btn1.clicked.connect(self.select_image)
        self.btn1.setGeometry(550,350,100,40)
        self.btn1.setStyleSheet("QPushButton{ background: #C47AFF; position: fixed;border-radius:15px;color: black;border-radius:20px;} QPushButton:hover borderradius:20px;")
        vbox.addWidget(self.btn1)

        self.label = QLabel("Upload product image",self.panel1)
        self.label.setGeometry(500,100,200,200)
        self.label.setStyleSheet("border:2px solid black;")
        self.label.setAlignment(Qt.AlignCenter)

        vbox.addWidget(self.label)
        self.setLayout(vbox)


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

    def announcement(self):
        window.close()
        os.system("python StudentAnnouncement.py &")   
    def attendence(self):
        window.close()
        os.system("python Attendencestudent.py &")
    def assignment(self):
        window.close()
        os.system("python AssignmentStudent.py &") 
    def reshaala(self):
        window.close()
        os.system("python Reshala\\reshalabuy.py &") 
    def sprofile(self):
        window.close()
        os.system("python profilestudent.py &")
    def back(Self):
        window.close()
        os.system("python Studentdashboard.py &")
    def back(Self):
        window.close()
        os.system("python Studentdashboard.py &")

    def select_image(self):
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            global fileName
            fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Image Files (*.png *.jpg *.jpeg)", options=options)
            if fileName:
                self.pixmap = QPixmap(fileName)
                self.label.setPixmap(self.pixmap)
                self.label.setFixedSize(200, 200)

            

    def on_click_upload(self):
        product_name = self.title.toPlainText()
        price = self.price.toPlainText()
        description = self.description.toPlainText()
        email = self.mail.toPlainText()
        phone_number = self.number.toPlainText()
        pixmap = QPixmap(fileName)
        with open(fileName, 'rb') as f:
            image_data = f.read()


        db.Re_Shala.insert_one({"productName": product_name,
                            "price": price,
                            "description": description,
                            "email": email,
                            "phone_number": phone_number,
                            "image": image_data
                            })


App = QApplication(sys.argv)
App.setStyleSheet("QMainWindow{background-color: #BFACE2}")

window = HomePage()

sys.exit(App.exec())

