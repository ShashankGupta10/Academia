from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
import sys
import os

class DashboardInstitute(QMainWindow):      
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Home Page")
        self.setGeometry(0,0,1366,768)

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
        logo.clicked.connect(self.back)

        navbarbtn1 = QPushButton("Home", self)
        navbarbtn1.setGeometry(1200, 31, 100, 40)
        navbarbtn1.setStyleSheet("QPushButton{ background: Black; position: fixed;border-radius:15px;color: white;}")
        navbarbtn1.setFont(QFont('Times', 20))
        navbarbtn1.clicked.connect(self.back)

        navbarbtn2= QPushButton("Student Add", self)
        navbarbtn2.setGeometry(1400, 31, 150, 40)
        navbarbtn2.setStyleSheet("QPushButton{ background: Black; position: fixed;border-radius:15px;color: white;}")
        navbarbtn2.setFont(QFont('Times', 20))
        navbarbtn2.clicked.connect(self.addstudent)
        
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
        profile.setGeometry(10,600, 60, 60)
        profile.setStyleSheet("border : 0px solid black")
        profile.setIcon(proficon)
        profile.setIconSize(size)

        panel1 = QLabel(self)
        panel1.setGeometry(200,140,500,450)
        panel1.setStyleSheet("QLabel{ background: white;  border-radius: 20px; padding: 10px;}")
  

        assgn_no = QLineEdit(panel1)
        assgn_no.setGeometry(250,10,220,50)
        assgn_no.setStyleSheet("QLineEdit{ background: #EDE3FF; border-color: black; border-radius: 20px; padding: 10px;}")
        assgn_no.setFont(QFont('Times', 12))

        assgn_name = QLineEdit(panel1)
        assgn_name.setGeometry(250,80,220,50)
        assgn_name.setStyleSheet("QLineEdit{ background: #EDE3FF; border-color: black; border-radius: 20px; padding: 10px;}")
        assgn_name.setFont(QFont('Times', 12))

        subject = QLineEdit(panel1)
        subject.setGeometry(250,150,220,50)
        subject.setStyleSheet("QLineEdit{ background: #EDE3FF; border-color: black; border-radius: 20px; padding: 10px;}")
        subject.setFont(QFont('Times', 12))
        
        filename = QLineEdit(panel1)
        filename.setGeometry(250, 220, 220, 50)
        filename.setStyleSheet("QLineEdit{ background: #EDE3FF; border-color: black; border-radius: 20px; padding: 10px;}")
        filename.setReadOnly(True)
        filename.setFont(QFont('Times', 12))
        
        duedate = QLineEdit(panel1)
        duedate.setGeometry(250, 290, 220, 50)
        duedate.setStyleSheet("QLineEdit{ background: #EDE3FF; border-color: black; border-radius: 20px; padding: 10px;}")
        duedate.setReadOnly(True)
        duedate.setFont(QFont('Times', 12))
        

        submit_btn = QPushButton("Schedule", panel1)
        submit_btn .setGeometry(200, 370, 100, 50)
        submit_btn .setStyleSheet("QPushButton{ background: #580599; color: white; border-radius: 20px; padding: 10px;}"
                                  "QPushButton:hover{ background: #A084DC;border-radius: 10px;}")
        submit_btn .setFont(QFont('Times', 12))
        
  
        assgn_no_lbl= QLabel(panel1)
        assgn_no_lbl.setText("Assignment number :")
        assgn_no_lbl.setGeometry(10, 12,200,50) 
        assgn_no_lbl.setStyleSheet("background-color: transparent;")
        assgn_no_lbl.setFont(QFont('Times', 12))


        assgn_name_lbl = QLabel(panel1)
        assgn_name_lbl.setText("Name of Assignment  :")
        assgn_name_lbl.setGeometry(10, 80,200,50)  
        assgn_name_lbl.setStyleSheet("background-color: transparent;")
        assgn_name_lbl.setFont(QFont('Times', 12))

        subject_lbl = QLabel(panel1)
        subject_lbl.setText("Subject : ")
        subject_lbl.setGeometry(10, 148,200,50) 
        subject_lbl.setStyleSheet("background-color: transparent;")
        subject_lbl.setFont(QFont('Times', 12))

        class_lbl = QLabel(panel1)
        class_lbl.setText("Class /Div: ")
        class_lbl.setGeometry(10, 218,200,50) 
        class_lbl.setStyleSheet("background-color: transparent;")
        class_lbl.setFont(QFont('Times', 12))


        duedate_lbl = QLabel(panel1)
        duedate_lbl.setText("Due date : ")
        duedate_lbl.setGeometry(10, 278,200,50) 
        duedate_lbl.setStyleSheet("background-color: transparent;")
        duedate_lbl.setFont(QFont('Times', 12))

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



App = QApplication(sys.argv)
App.setStyleSheet("QMainWindow{background-color: white }")

window = DashboardInstitute()

sys.exit(App.exec())
