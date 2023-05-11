from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from urllib import *
import sys,os

class DashboardInstitute(QMainWindow):        
    def __init__(self):       
        super().__init__()
        
        self.setWindowTitle("Home Page")
        self.setGeometry(0,0,1366,768)

        self.header = QLabel(self)
        self.header.setGeometry(0, 0, 1920, 100)
        self.header.setStyleSheet("QLabel{ background: black; position: fixed;} ")

        siz = QSize(80,80)
        logo = QPushButton(self)
        logo.setGeometry(30, 15, 80, 80)
        logocon = QIcon("All icons\logo.png")
        logo.setStyleSheet("background: transparent")
        logo.setIcon(logocon)
        logo.setIconSize(siz)
        logo.clicked.connect(self.logout)

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
        navbarbtn3.clicked.connect(self.about)


        icon = QIcon("images\homepageimage1bgrm.png")
        self.btn10 = QPushButton("" ,self)
        self.btn10.setGeometry(1800, 0, 100, 100)
        self.btn10.setStyleSheet("background : black;")
        self.btn10.setIcon(icon)
        size = QSize(100, 100)
        self.btn10.setIconSize(size)
        # self.btn10.clicked.connect(self.)
        
        sidebar = QLabel(self)
        sidebar.setGeometry(0,100,450,1920)
        sidebar.setStyleSheet("background-color: #3E54AC;")
        
        size = QSize(60, 60)
        
        anicon = QIcon('All icons\\announcement.png')
        announce = QPushButton(sidebar)
        announce.setGeometry(20,30, 60, 60)
        announce.setStyleSheet("border : 0px solid black")
        announce.setIcon(anicon)
        announce.setIconSize(size)
        announce.clicked.connect(self.announcement)
        
        announce_btn = QPushButton("Announcements", sidebar)
        announce_btn.setGeometry(120, 30, 300, 60)
        announce_btn.setStyleSheet("border: none; color: white; text-align: left")
        announce_btn.setFont(QFont('Times', 20))
        announce_btn.clicked.connect(self.announcement)
        
        aticon = QIcon('All icons\\attendence.png')        
        attend = QPushButton(sidebar)
        attend.setGeometry(20,150, 60, 60)
        attend.setStyleSheet("border : 0px solid black")
        attend.setIcon(aticon)
        attend.setIconSize(size)
        attend.clicked.connect(self.attendence)
        
        attend_btn = QPushButton("Attendance", sidebar)
        attend_btn.setGeometry(120, 150, 300, 60)
        attend_btn.setStyleSheet("border: none; color: white; text-align: left")
        attend_btn.setFont(QFont('Times', 20))
        attend_btn.clicked.connect(self.attendence)

        asicon = QIcon('All icons\\assignment.png')
        assign = QPushButton(sidebar)
        assign.setGeometry(25, 270, 60, 60)
        assign.setStyleSheet("border : 0px solid black")
        assign.setIcon(asicon)
        assign.setIconSize(size)
        assign.clicked.connect(self.assignment)
        
        assign_btn = QPushButton("Assignments", sidebar)
        assign_btn.setGeometry(120, 270, 300, 60)
        assign_btn.setStyleSheet("border: none; color: white; text-align: left")
        assign_btn.setFont(QFont('Times', 20))
        assign_btn.clicked.connect(self.assignment)
        
        proficon = QIcon('All icons\\profile.png')
        profile = QPushButton(sidebar)
        profile.setGeometry(20, 700, 60, 60)
        profile.setStyleSheet("border : 0px solid black")
        profile.setIcon(proficon)
        profile.setIconSize(size)
        
        profile_btn = QPushButton("Profile", sidebar)
        profile_btn.setGeometry(120, 700, 300, 60)
        profile_btn.setStyleSheet("border: none; color: white; text-align: left")
        profile_btn.setFont(QFont('Times', 20))

        self.panel1 = QPushButton(self)
        self.panel1.setGeometry(500,350,675,400)
        self.panel1.setStyleSheet("QPushButton{ background: #BFACE2;  border-radius: 20px;}")
        self.panel1.clicked.connect(self.addstudent)
        
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setColor(QColor("black"))
        shadow.setXOffset(5)
        shadow.setYOffset(5)
        shadow.setColor(Qt.black)

        f = QFont('Times',15)
        f.setBold(True)
        add = QLabel(self.panel1)
        add.setText("Add Student")
        add.setGeometry(410, 80, 250, 250)
        add.setFont(f)
        self.panel1.setGraphicsEffect(shadow)

        addicon = QPixmap("images\\add-student-removebg.png")
        addlbl = QLabel(self.panel1)
        addlbl.setGeometry(20, 20, 350, 350)
        addlbl.setPixmap(addicon)
        addlbl.setScaledContents(True)
        
        self.panel2 = QPushButton(self)
        self.panel2.setGeometry(1200,350,675,400)
        self.panel2.setStyleSheet("QPushButton{ background: #BFACE2;  border-radius: 20px;}")
        self.panel2.clicked.connect(self.assignment)

        shadow1 = QGraphicsDropShadowEffect()
        shadow1.setBlurRadius(10)
        shadow1.setColor(QColor("black"))
        shadow1.setXOffset(5)
        shadow1.setYOffset(5)
        shadow1.setColor(Qt.black)
        
        ass = QLabel(self.panel2)
        ass.setText("Assignments")
        ass.setGeometry(450, 80, 200, 250)
        ass.setFont(f)

        assicon = QPixmap("images\\assignmentsdashboard.png")
        asslbl = QLabel(self.panel2)
        asslbl.setGeometry(0,0, 410, 400)
        asslbl.setPixmap(assicon)
        self.panel2.setGraphicsEffect(shadow1)
        
        hello = QLabel(self)
        hello.setGeometry(1000, 150, 500, 100)
        hello.setText("WELCOME TSEC")
        hello.setStyleSheet("QLabel{ background: white; font-weight: bold;}")
        hello.setFont(QFont('Times', 25))

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
    def back(Self):
        window.close()
        os.system("python Institutedashboard.py &")
    def logout(self):
        msgb = QMessageBox(self)
        msgb.setWindowTitle("LOGOUT!")
        msgb.setText("Are you sure you want to logout?")
        msgb.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgb.exec()
        if returnValue == QMessageBox.Ok:
            window.close()
            os.system("python homepage.py &")
    def about(self):
        window.close()
        os.system("python aboutus.py &")

App = QApplication(sys.argv)
App.setStyleSheet("QMainWindow{background-color: white }")

window = DashboardInstitute()

sys.exit(App.exec())
