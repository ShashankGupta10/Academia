from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QGraphicsOpacityEffect
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from urllib import *
import sys,os
from pymongo import MongoClient

client = MongoClient("mongodb+srv://shashankgupta2003:Shashank10@cluster0.x6bsdlb.mongodb.net/test")
db = client['IOP']

class InstituteAddStudent(QMainWindow):            
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
        logo.setGeometry(30, 15, 80, 80)
        logocon = QIcon("All icons\logo.png")
        logo.setStyleSheet("background: transparent")
        logo.setIcon(logocon)
        logo.setIconSize(siz)

        navbarbtn1 = QPushButton("Home", self)
        navbarbtn1.setGeometry(1200, 31, 100, 40)
        navbarbtn1.setStyleSheet("QPushButton{ background: Black; position: fixed;border-radius:15px;color: white;}")
        navbarbtn1.setFont(QFont('Times', 20))
        navbarbtn1.clicked.connect(self.back)

        navbarbtn2= QPushButton("Add Student", self)
        navbarbtn2.setGeometry(1360, 31, 200, 40)
        navbarbtn2.setStyleSheet("QPushButton{ background: Black; position: fixed;border-radius:15px;color: white;}")
        navbarbtn2.setFont(QFont('Times', 20))
        navbarbtn2.clicked.connect(self.addstudent)
        
        navbarbtn3= QPushButton("About", self)
        navbarbtn3.setGeometry(1600, 31, 150, 40)
        navbarbtn3.setStyleSheet("QPushButton{ background: Black; position: fixed;border-radius:15px;color: white;}")
        navbarbtn3.setFont(QFont('Times', 20))


        icon = QIcon("images\homepageimage1bgrm.png")
        self.btn10 = QPushButton("" ,self)
        self.btn10.setGeometry(1800, 0, 100, 100)
        self.btn10.setStyleSheet("background : black;")
        self.btn10.setIcon(icon)
        size = QSize(100, 100)
        self.btn10.setIconSize(size)
        # self.btn10.clicked.connect(self.)
        
        # ************************MAIN CODE****************************

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
        
        proficon = QIcon('All icons\\profile.png')
        profile = QPushButton(sidebar)
        profile.setGeometry(20, 700, 60, 60)
        profile.setStyleSheet("border : 0px solid black")
        profile.setIcon(proficon)
        profile.setIconSize(size)

        addStudent = QLabel(self)
        addStudent.setText("Add Student")
        addStudent.setGeometry(835, 200, 400, 75) 
        addStudent.setStyleSheet("background-color: transparent; font-weight: bold;")
        addStudent.setFont(QFont('Times', 25))

        studentPanel = QLabel(self)
        studentPanel.setGeometry(450, 300, 1000, 450)
        studentPanel.setStyleSheet("background-color: white; border-radius: 20%")

        studentUsername = QLabel(self)
        studentUsername.setText(" Student Username  :")
        studentUsername.setGeometry(500, 350, 350, 50) 
        studentUsername.setStyleSheet("background-color: transparent; font-weight: bold;")
        studentUsername.setFont(QFont('Times', 12))


        self.studentUsernameText = QLineEdit(self)
        self.studentUsernameText.setGeometry(800,350,600,40)
        self.studentUsernameText.setStyleSheet("QLineEdit{ background: #EDE3FF;border; border-color: black; border-radius: 20px; padding: 10px;}")
        self.studentUsernameText.setFont(QFont('Times', 10))

        studentPassword = QLabel(self)
        studentPassword.setText(" Student Password   :")
        studentPassword.setGeometry(500, 450, 350, 50) 
        studentPassword.setStyleSheet("background-color: transparent; font-weight: bold;")
        studentPassword.setFont(QFont('Times', 12))

        self.studentPasswordText = QLineEdit(self)
        self.studentPasswordText.setGeometry(800,450,600,40)
        self.studentPasswordText.setStyleSheet("QLineEdit{ background: #EDE3FF; border-color: black; border-radius: 20px; padding: 10px;}")
        self.studentPasswordText.setFont(QFont('Times', 10))

        studentEmail = QLabel(self)
        studentEmail.setText(" Student Email          :")
        studentEmail.setGeometry(500, 550, 350, 50) 
        studentEmail.setStyleSheet("background-color: transparent; font-weight: bold;")
        studentEmail.setFont(QFont('Times', 12))

        self.studentEmailText = QLineEdit(self)
        self.studentEmailText.setGeometry(800,550,600,40)
        self.studentEmailText.setStyleSheet("QLineEdit{ background: #EDE3FF; border-color: black; border-radius: 20px; padding: 10px;}")
        self.studentEmailText.setFont(QFont('Times', 10))

        addStudentButton = QPushButton(self)
        addStudentButton.setText("Add Student")
        addStudentButton.setGeometry(850,650,200,40)
        addStudentButton.setStyleSheet("QPushButton{ background: #3E54AC; border-color: black; border-radius: 20px; padding: 10px; color: white}")
        addStudentButton.setFont(QFont('Times', 12))
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
    def announcement(self):
        window.close()
        os.system("python Announcements.py &")
    def attendence(self):
        window.close()
        os.system("python AttendanceFaculty.py &")
    def assignment(self):
        window.close()
        os.system("python AssignmentFaculty.py &")        
    def addstudent(self):
        window.close()
        os.system("python Instituteaddstudent.py &")
    def back(self):
        window.close()
        os.system("python Institutedashboard.py &") 

    def on_click_addStudentButton(self):
        newStudentUsername = self.studentUsernameText.text()
        newStudentPassword = self.studentPasswordText.text()
        newStudentEmail = self.studentEmailText.text()

        db.Student_Data.insert_one({
            "username": newStudentUsername,
            "password": newStudentPassword,
            "email": newStudentEmail
        })
        window.close()
        os.system("python Institutedashboard.py &")  
   
App = QApplication(sys.argv)
App.setStyleSheet("QMainWindow{background-color: #EBC7E6 }")
window = InstituteAddStudent()
sys.exit(App.exec())
