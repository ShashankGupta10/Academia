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


        self.header = QLabel(self)
        self.header.setGeometry(0, 0, 1920, 100)
        self.header.setStyleSheet("QLabel{ background: black; position: fixed;} ")

        logo = QLabel(self)
        logo.setGeometry(30, 20, 80, 70)
        self.pixmap = QPixmap("D:\python mpr final\Python-MPR-\loginpage\smalllogo.png")
        logo.setPixmap(self.pixmap)
        logo.setScaledContents(True)
        self.pixmap = self.pixmap.scaled(100, 200)

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
        
        # ************************MAIN CODE****************************

        sidebar = QLabel(self)
        sidebar.setGeometry(0,100,120,1920)
        sidebar.setStyleSheet("background-color: #3E54AC;")
        
        size = QSize(60, 60)
        
        anicon = QIcon('Python-MPR-\\images\\announcements.png.jpg')
        announce = QPushButton(sidebar)
        announce.setGeometry(20,30, 60, 60)
        announce.setStyleSheet("border : 0px solid black")
        announce.setIcon(anicon)
        announce.setIconSize(size)
        
        
        aticon = QIcon('D:\\python mpr final\\Python-MPR-\\images\\attendance.png')
        attend = QPushButton(sidebar)
        attend.setGeometry(20,150, 60, 60)
        attend.setStyleSheet("border : 0px solid black")
        attend.setIcon(aticon)
        attend.setIconSize(size)

        asicon = QIcon('D:\\python mpr final\\Python-MPR-\\images\\assignment.png.jpg')
        assign = QPushButton(sidebar)
        assign.setGeometry(25, 270, 60, 60)
        assign.setStyleSheet("border : 0px solid black")
        assign.setIcon(asicon)
        assign.setIconSize(size)

        reicon = QIcon('D:\\python mpr final\\Python-MPR-\\images\\reshala.png')
        reshaala = QPushButton(sidebar)
        reshaala.setGeometry(20,390, 60, 60)
        reshaala.setStyleSheet("border : 0px solid black")
        reshaala.setIcon(reicon)
        reshaala.setIconSize(size)
        
        proficon = QIcon('D:\python mpr final\Python-MPR-\images\profile.png-removebg-preview.png')
        profile = QPushButton(sidebar)
        profile.setGeometry(20, 700, 60, 60)
        profile.setStyleSheet("border : 0px solid black")
        profile.setIcon(proficon)
        profile.setIconSize(size)

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

        footerlbl1 = QPushButton(self.footer)
        footerlbl1.setGeometry(100,0,150,100)
        footerlbl1.setStyleSheet("color: white; background: black;")
        footerlbl1.setText("@Academia 2023")
        footerlbl1.setFont(QFont('Times', 10))

        footerlbl2 = QPushButton(self.footer)
        footerlbl2.setGeometry(300,0,150,100)
        footerlbl2.setStyleSheet("color: white; background: black;")
        footerlbl2.setText("Terms of Use")
        footerlbl2.setFont(QFont('Times', 10))

        footerlbl3 = QPushButton(self.footer)
        footerlbl3.setGeometry(500,0,200,100)
        footerlbl3.setStyleSheet("color: white; background: black;")
        footerlbl3.setText("Privacy Policy")
        footerlbl3.setFont(QFont('Times', 10))
                                
        footerlbl4 = QPushButton(self.footer)
        footerlbl4.setGeometry(1400,0,500,100)
        footerlbl4.setStyleSheet("color: white; background: black;")
        footerlbl4.setText("Copyright © 2023 Academia Inc. All rights reserved.")
        footerlbl4.setFont(QFont('Times', 10))
        
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
