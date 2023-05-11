from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
import sys
import os
from pymongo import MongoClient
from io import BytesIO


client = MongoClient("")
db = client.get_database("IOP")

ass = db.Assignments.find_one({"id":"1"})
resultName = (ass['name'])
resultRoll = (ass['roll No'])
resultSubject = (ass['subject'])
resultFile = (ass['UploadFile'])

class AssignmentFac(QMainWindow):      
    def __init__(self):
        super().__init__()
        self.setWindowTitle("ACADEMIA")
        self.setGeometry(0,0,1920, 1080)

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
        logo.clicked.connect(self.back)

        navbarbtn1 = QPushButton("Home", self)
        navbarbtn1.setGeometry(1200, 31, 100, 40)
        navbarbtn1.setStyleSheet("QPushButton{ background: Black; position: fixed;border-radius:15px;color: white;}")
        navbarbtn1.setFont(QFont('Times', 20))
        navbarbtn1.clicked.connect(self.back)

        navbarbtn2= QPushButton("Add Student", self)
        navbarbtn2.setGeometry(1350, 31, 200, 40)
        navbarbtn2.setStyleSheet("QPushButton{ background: Black; position: fixed;border-radius:15px;color: white;}")
        navbarbtn2.setFont(QFont('Times', 20))
        navbarbtn2.clicked.connect(self.addstudent)
        
        navbarbtn3= QPushButton("About", self)
        navbarbtn3.setGeometry(1600, 31, 150, 40)
        navbarbtn3.setStyleSheet("QPushButton{ background: Black; position: fixed;border-radius:15px;color: white;}")
        navbarbtn3.setFont(QFont('Times', 20))
        navbarbtn3.clicked.connect(self.about)
        
        icon = QIcon("images\homepageimage1bgrm.png")
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
        announce.setGeometry(10,30, 60, 60)
        announce.setStyleSheet("border : 0px solid black")
        announce.setIcon(anicon)
        announce.setIconSize(size)
        announce.clicked.connect(self.announcement)
        
        aticon = QIcon('All icons\\attendence.png')
        attend = QPushButton(sidebar)
        attend.setGeometry(15,150, 60, 60)
        attend.setStyleSheet("border : 0px solid black")
        attend.setIcon(aticon)
        attend.setIconSize(size)
        attend.clicked.connect(self.attendence)

        asicon = QIcon('All icons\\assignment.png')
        assign = QPushButton(sidebar)
        assign.setGeometry(10,270, 60, 60)
        assign.setStyleSheet("border : 0px solid black")
        assign.setIcon(asicon)
        assign.setIconSize(size)
        assign.clicked.connect(self.assignment)
        
        proficon = QIcon('All icons\\profile.png')
        profile = QPushButton(sidebar)
        profile.setGeometry(10,700, 60, 60)
        profile.setStyleSheet("border : 0px solid black")
        profile.setIcon(proficon)
        profile.setIconSize(size)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setColor(QColor("black"))
        shadow.setXOffset(5)
        shadow.setYOffset(5)
        shadow.setColor(Qt.black)
        
        addAss = QLabel(self)
        addAss.setText("Recieved Assignment")
        addAss.setGeometry(780, 100, 500, 75) 
        addAss.setStyleSheet("background-color: transparent; font-weight: bold;")
        addAss.setFont(QFont('Times', 23))
        
        panel1 = QLabel(self)
        panel1.setGeometry(500,200,1000,600)
        panel1.setStyleSheet("QLabel{ background: white;  border-radius: 20px; padding: 10px;}")
        panel1.setGraphicsEffect(shadow)
  
        assgnfac_img = QLabel(panel1)
        assgnfac_img.pixmap = QPixmap('images\\assgnfac-img-removebg.png')
        assgnfac_img.setGeometry(500, 50, 500, 500)
        assgnfac_img.setPixmap(assgnfac_img.pixmap)

        global assgn_no
        assgn_no = QLabel(panel1)
        assgn_no.setText(resultName)
        assgn_no.setGeometry(250,50,220,50)
        assgn_no.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 20px; padding: 10px;}")
        assgn_no.setFont(QFont('Times', 12))

        global assgn_name
        assgn_name = QLabel(panel1)
        assgn_name.setText(resultRoll)
        assgn_name.setGeometry(250,130,220,50)
        assgn_name.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 20px; padding: 10px;}")
        assgn_name.setFont(QFont('Times', 12))

        global subject
        subject = QLabel(panel1)
        subject.setText(resultSubject)
        subject.setGeometry(250,210,220,50)
        subject.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 20px; padding: 10px;}")
        subject.setFont(QFont('Times', 12))
        
        global classStudent
        classStudent = QLabel(panel1)
        pixmap = QPixmap()
        pixmap.loadFromData(resultFile)
        classStudent.setPixmap(pixmap) 
        classStudent.setGeometry(250, 290, 200, 200)
        classStudent.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 20px; padding: 10px;}")
        classStudent.setFont(QFont('Times', 12))
        classStudent.setScaledContents(True)
        
        # global duedate
        # duedate = QLabel(panel1)
        # duedate.setGeometry(250, 370, 220, 50)
        # duedate.setStyleSheet("QLabel{ background: #EDE3FF; border-color: black; border-radius: 20px; padding: 10px;}")
        # duedate.setFont(QFont('Times', 12))
        

        global assgn_no_lbl
        assgn_no_lbl= QLabel(panel1)
        assgn_no_lbl.setText("Student Name :")
        assgn_no_lbl.setGeometry(10, 50,200,50) 
        assgn_no_lbl.setStyleSheet("background-color: transparent;")
        assgn_no_lbl.setFont(QFont('Times', 12))

        global assgn_name_lbl
        assgn_name_lbl = QLabel(panel1)
        assgn_name_lbl.setText("Roll no:")
        assgn_name_lbl.setGeometry(10, 120,200,50)  
        assgn_name_lbl.setStyleSheet("background-color: transparent;")
        assgn_name_lbl.setFont(QFont('Times', 12))

        global subject_lbl
        subject_lbl = QLabel(panel1)
        subject_lbl.setText("Subject : ")
        subject_lbl.setGeometry(10, 210,200,50) 
        subject_lbl.setStyleSheet("background-color: transparent;")
        subject_lbl.setFont(QFont('Times', 12))

        global class_lbl
        class_lbl = QLabel(panel1)
        class_lbl.setText("Uploaded File: ")
        class_lbl.setGeometry(10, 290,200,50) 
        class_lbl.setStyleSheet("background-color: transparent;")
        class_lbl.setFont(QFont('Times', 12))


        # duedate_lbl = QLabel(panel1)
        # duedate_lbl.setText("Due date : ")
        # duedate_lbl.setGeometry(10, 370,200,50) 
        # duedate_lbl.setStyleSheet("background-color: transparent;")
        # duedate_lbl.setFont(QFont('Times', 12))

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
    def about(self):
        window.close()
        os.system("python aboutus.py &")
    


        


App = QApplication(sys.argv)
App.setStyleSheet("QMainWindow{background-color: }")
window = AssignmentFac()
window.show()
sys.exit(App.exec())