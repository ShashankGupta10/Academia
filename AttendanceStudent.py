from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
import sys
import os

class AssignmentStudent(QMainWindow):            
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

        reicon = QIcon('All icons\\reshaala.png')
        reshaala = QPushButton(sidebar)
        reshaala.setGeometry(5,390, 60, 60)
        reshaala.setStyleSheet("border : 0px solid black")
        reshaala.setIcon(reicon)
        reshaala.setIconSize(size)
        reshaala.clicked.connect(self.reshaala)
        
        proficon = QIcon('All icons\\profile.png')
        profile = QPushButton(sidebar)
        profile.setGeometry(10,600, 60, 60)
        profile.setStyleSheet("border : 0px solid black")
        profile.setIcon(proficon)
        profile.setIconSize(size)
        profile.clicked.connect(self.sprofile)
            
        self.panel1 = QLabel(self)
        self.panel1.setGeometry(200,140,400,450)
        self.panel1.setStyleSheet("QLabel{background: white;  border-radius: 20px; padding: 10px;}")
  

        self.Name = QLineEdit(self.panel1)
        self.Name.setGeometry(150,10,220,50)
        self.Name.setStyleSheet("background: #EDE3FF; border-color: black; border-radius: 20px; padding: 10px;")
        self.Name.setFont(QFont('Times', 12))

        self.rollno = QLineEdit(self.panel1)
        self.rollno.setGeometry(150,80,220,50)
        self.rollno.setStyleSheet("background: #EDE3FF; border-color: black; border-radius: 20px; padding: 10px;")
        self.rollno.setFont(QFont('Times', 12))

        self.Subject = QLineEdit(self.panel1)
        self.Subject.setGeometry(150,150,220,50)
        self.Subject.setStyleSheet("background: #EDE3FF; border-color: black; border-radius: 20px; padding: 10px;")
        self.Subject.setFont(QFont('Times', 12))
        
        self.filename = QLineEdit(self.panel1)
        self.filename.setGeometry(150, 220, 220, 50)
        self.filename.setStyleSheet("background: #EDE3FF; border-color: black; border-radius: 20px; padding: 10px;")
        self.filename.setReadOnly(True)
        self.filename.setFont(QFont('Times', 12))
        
        self.upload_btn = QPushButton("Browse...", self.panel1)
        self.upload_btn.setGeometry(150, 280, 100, 40)
        self.upload_btn.setStyleSheet("background: #EDE3FF; border-color: black; border-radius: 20px; padding: 5px;")       
        self.upload_btn.clicked.connect(self.browseFiles)
        self.upload_btn.setFont(QFont('Times', 12))

        self.submit_btn = QPushButton("Submit" ,self.panel1)
        self.submit_btn .setGeometry(150, 350, 100, 50)
        self.submit_btn .setStyleSheet("QPushButton{ background: #580599; color: white; border-radius: 20px; padding: 10px;}"
                                "QPushButton:hover{ background: #A084DC;border-radius: 10px;}")
        self.submit_btn .setFont(QFont('Times', 12))
        
  
        Nametxt= QLabel(self.panel1)
        Nametxt.setText("Name :")
        Nametxt.setGeometry(10, 12,200,50) 
        Nametxt.setStyleSheet("background-color: transparent;")
        Nametxt.setFont(QFont('Times', 12))


        rolltxt = QLabel(self.panel1)
        rolltxt.setText("Roll No :")
        rolltxt.setGeometry(10, 80,200,50)  
        rolltxt.setStyleSheet("background-color: transparent;")
        rolltxt.setFont(QFont('Times', 12))

        Subjecttxt = QLabel(self.panel1)
        Subjecttxt.setText("Subject : ")
        Subjecttxt.setGeometry(10, 148,200,50) 
        Subjecttxt.setStyleSheet("background-color: transparent;")
        Subjecttxt.setFont(QFont('Times', 12))

        UploadAssignmenttxt = QLabel(self.panel1)
        UploadAssignmenttxt.setText("Upload file : ")
        UploadAssignmenttxt.setGeometry(10, 218,200,50) 
        UploadAssignmenttxt.setStyleSheet("background-color: transparent;")
        UploadAssignmenttxt.setFont(QFont('Times', 12))


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
        
    def browseFiles(self):
        fname = QFileDialog.getOpenFileName(self.panel1, 'Open File', '.')
        self.filename.setText(fname[0].rsplit('/', 1)[-1])
        return
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
        
App = QApplication(sys.argv)
App.setStyleSheet("QMainWindow{background-color: #EBC7E6 }")
window = AssignmentStudent()
sys.exit(App.exec())
