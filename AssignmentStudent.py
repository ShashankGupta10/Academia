from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
import sys
import os
from pymongo import MongoClient


client = MongoClient("")
db = client.get_database("IOP")

class AssignmentStudent(QMainWindow):            
    def __init__(self):
        super().__init__()
        global i
        i = "1"
        
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
        profile.setGeometry(10,700, 60, 60)
        profile.setStyleSheet("border : 0px solid black")
        profile.setIcon(proficon)
        profile.setIconSize(size)
        profile.clicked.connect(self.sprofile)
        
        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setColor(QColor("black"))
        shadow.setXOffset(5)
        shadow.setYOffset(5)
        shadow.setColor(Qt.black)
            
        self.panel1 = QLabel(self)
        self.panel1.setGeometry(500,200,1000,600)
        self.panel1.setStyleSheet("QLabel{ background: white;  border-radius: 20px; padding: 10px;}")
        self.panel1.setGraphicsEffect(shadow)
  
        assgn_img = QLabel(self.panel1)
        assgn_img.pixmap = QPixmap('images\\assgn-img-removebg.png')
        assgn_img.setGeometry(500, 50, 500, 500)
        assgn_img.setPixmap(assgn_img.pixmap)

        global Name
        Name = QLineEdit(self.panel1)
        Name.setGeometry(200,50,300,50)
        Name.setStyleSheet("background: #EDE3FF; border-color: black; border-radius: 25px; padding: 10px;")
        Name.setFont(QFont('Times', 12))

        global rollno
        rollno = QLineEdit(self.panel1)
        rollno.setGeometry(200,130,300,50)
        rollno.setStyleSheet("background: #EDE3FF; border-color: black; border-radius: 25px; padding: 10px;")
        rollno.setFont(QFont('Times', 12))

        global Subject
        Subject = QLineEdit(self.panel1)
        Subject.setGeometry(200,210,300,50)
        Subject.setStyleSheet("background: #EDE3FF; border-color: black; border-radius: 25px; padding: 10px;")
        Subject.setFont(QFont('Times', 12))
        
        global filename
        filename = QLineEdit(self.panel1)
        filename.setGeometry(200, 290, 300, 50)

        filename.setStyleSheet("background: #EDE3FF; border-color: black; border-radius: 25px; padding: 10px;")
        filename.setReadOnly(True)
        filename.setFont(QFont('Times', 12))
        
        self.upload_btn = QPushButton("Browse", self.panel1)
        self.upload_btn.setGeometry(300, 360, 100, 40)
        self.upload_btn.setStyleSheet("background: #EDE3FF; border-color: black; border-radius: 20px; padding: 5px;")       
        self.upload_btn.clicked.connect(self.select_image)
        self.upload_btn.setFont(QFont('Times', 12))

        self.submit_btn = QPushButton("Submit" ,self.panel1)
        self.submit_btn .setGeometry(250, 450, 200, 50)
        self.submit_btn .setStyleSheet("QPushButton{ background: #580599; color: white; border-radius: 25px; padding: 10px;}")
        self.submit_btn .setFont(QFont('Times', 15))
        self.submit_btn.clicked.connect(self.on_click)
        
  
        Nametxt= QLabel(self.panel1)
        Nametxt.setText("Name :")
        Nametxt.setGeometry(10, 50,200,50) 
        Nametxt.setStyleSheet("background-color: transparent;")
        Nametxt.setFont(QFont('Times', 15))


        rolltxt = QLabel(self.panel1)
        rolltxt.setText("Roll No :")
        rolltxt.setGeometry(10, 130,200,50)  
        rolltxt.setStyleSheet("background-color: transparent;")
        rolltxt.setFont(QFont('Times', 15))

        Subjecttxt = QLabel(self.panel1)
        Subjecttxt.setText("Subject : ")
        Subjecttxt.setGeometry(10, 210,200,50) 
        Subjecttxt.setStyleSheet("background-color: transparent;")
        Subjecttxt.setFont(QFont('Times', 15))

        UploadAssignmenttxt = QLabel(self.panel1)
        UploadAssignmenttxt.setText("Upload file : ")
        UploadAssignmenttxt.setGeometry(10, 290,200,50) 
        UploadAssignmenttxt.setStyleSheet("background-color: transparent;")
        UploadAssignmenttxt.setFont(QFont('Times', 15))

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
        
    def select_image(self):
            options = QFileDialog.Options()
            options |= QFileDialog.DontUseNativeDialog
            global fileName
            fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Image Files (*.png *.jpg *.jpeg)", options=options)
            with open(fileName, 'rb') as f:
                global image_data
                image_data = f.read()

            

        
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
        os.system("python reshalasell.py &") 
    def sprofile(self):
        window.close()
        os.system("python profilestudent.py &")
    def back(self):
        window.close()
        os.system("python Studentdashboard.py &")
    def on_click(self):
        db.Assignments.insert_one({"id": "1", "name": Name.text(), "roll No": rollno.text(), "subject": Subject.text(), "UploadFile": image_data })
        QMessageBox.information(self, "GG", "Assignment Submitted")

App = QApplication(sys.argv)
App.setStyleSheet("QMainWindow{background-color: #EBC7E6 }")
window = AssignmentStudent()
sys.exit(App.exec())