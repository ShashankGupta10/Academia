from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QGraphicsOpacityEffect
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from urllib import *
import sys
from pymongo import MongoClient

client = MongoClient("mongodb+srv://shashankgupta2003:Shashank10@cluster0.x6bsdlb.mongodb.net/test")
db = client['IOP']


# resultProductName = db.Re_Shala.find_one({"price": "200"}, {"productName": 1})
# resultPrice = db.Re_Shala.find_one({"price": "200"}, {"price": 1})
# resultDescription = db.Re_Shala.find_one({"price": "200"}, {"description": 1})
# resultPhone = db.Re_Shala.find_one({"price": "200"}, {"phone_number": 1})
# resultEmail = db.Re_Shala.find_one({"price": "200"}, {"email": 1})
# resultImage = db.Re_Shala.find_one({"price": "200"}, {"image": 1})
# imageData = resultImage['image']



class InstituteAddStudent(QMainWindow):            
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
        
        # ************************MAIN CODE****************************


        addStudent = QLabel(self)
        addStudent.setText("ADD STUDENT")
        addStudent.setGeometry(835, 200, 250, 75) 
        addStudent.setStyleSheet("background-color: transparent; font-weight: bold;")
        addStudent.setFont(QFont('Times', 20))

        studentPanel = QLabel(self)
        studentPanel.setGeometry(450, 300, 1000, 450)
        studentPanel.setStyleSheet("background-color: #ECF2FF; border-radius: 20%")

        studentUsername = QLabel(self)
        studentUsername.setText("Enter new Student Username  :")
        studentUsername.setGeometry(500, 350, 350, 50) 
        studentUsername.setStyleSheet("background-color: transparent; font-weight: bold;")
        studentUsername.setFont(QFont('Times', 12))


        self.studentUsernameText = QLineEdit(self)
        self.studentUsernameText.setGeometry(900,350,500,40)
        self.studentUsernameText.setStyleSheet("QLineEdit{ background: #EDE3FF; border-color: black; border-radius: 20px; padding: 10px;}")
        self.studentUsernameText.setFont(QFont('Times', 10))

        studentPassword = QLabel(self)
        studentPassword.setText("Enter new Student Password   :")
        studentPassword.setGeometry(500, 450, 350, 50) 
        studentPassword.setStyleSheet("background-color: transparent; font-weight: bold;")
        studentPassword.setFont(QFont('Times', 12))

        self.studentPasswordText = QLineEdit(self)
        self.studentPasswordText.setGeometry(900,450,500,40)
        self.studentPasswordText.setStyleSheet("QLineEdit{ background: #EDE3FF; border-color: black; border-radius: 20px; padding: 10px;}")
        self.studentPasswordText.setFont(QFont('Times', 10))

        studentEmail = QLabel(self)
        studentEmail.setText("Enter new Student Email          :")
        studentEmail.setGeometry(500, 550, 350, 50) 
        studentEmail.setStyleSheet("background-color: transparent; font-weight: bold;")
        studentEmail.setFont(QFont('Times', 12))

        self.studentEmailText = QLineEdit(self)
        self.studentEmailText.setGeometry(900,550,500,40)
        self.studentEmailText.setStyleSheet("QLineEdit{ background: #EDE3FF; border-color: black; border-radius: 20px; padding: 10px;}")
        self.studentEmailText.setFont(QFont('Times', 10))

        addStudentButton = QPushButton(self)
        addStudentButton.setText("ADD STUDENT")
        addStudentButton.setGeometry(850,650,200,40)
        addStudentButton.setStyleSheet("QPushButton{ background: #3E54AC; border-color: black; border-radius: 20px; padding: 10px; color: white}")
        addStudentButton.setFont(QFont('Times', 10))
        addStudentButton.clicked.connect(self.on_click_addStudentButton)

        # ******FOOTER*******        
       
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
    

    def on_click_addStudentButton(self):
        newStudentUsername = self.studentUsernameText.text()
        newStudentPassword = self.studentPasswordText.text()
        newStudentEmail = self.studentEmailText.text()

        db.Student_Data.insert_one({
            "username": newStudentUsername,
            "password": newStudentPassword,
            "email": newStudentEmail
        })
   
App = QApplication(sys.argv)
App.setStyleSheet("QMainWindow{background-color: #EBC7E6 }")
window = InstituteAddStudent()
sys.exit(App.exec())
