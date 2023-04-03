from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QGraphicsOpacityEffect
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from urllib import *
import sys

class Attendance(QMainWindow):            
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

        
        self.loginbox = QLabel(self)
        self.loginbox.setGeometry(0,100,120,800)
        self.loginbox.setStyleSheet("background-color: #3E54AC;")
        
        sidebar = QLabel(self)
        sidebar.setGeometry(0,100,80,1920)
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
        
        
        self.attendance_label = QLabel("Attendance", self)
        self.attendance_label.setStyleSheet("border-bottom: 2px solid black")
        self.attendance_label.setGeometry(910, 110, 250, 80)
        self.attendance_label.setFont(QFont('Times', 20))
        
        self.panel1 = QPushButton("Overall Attendance", self)
        self.panel1.setStyleSheet("background-color: #3E54AC; color: white; border: none; border-radius: 20px;")
        self.panel1.setGeometry(310, 200, 600, 300)
        self.panel1.setFont(QFont('Times', 20))
        self.panel1.clicked.connect(lambda: self.overall_box.setVisible(True))
        
        self.panel2 = QPushButton("Subject Wise Attendance", self)
        self.panel2.setStyleSheet("background-color: #3E54AC; color: white; border: none; border-radius: 20px")
        self.panel2.setGeometry(1070, 200, 600, 300)
        self.panel2.setFont(QFont('Times', 20))
        self.panel2.clicked.connect(lambda: self.subject_box.setVisible(True))
            
        self.panel3 = QPushButton("Defaulter?", self)
        self.panel3.setStyleSheet("background-color: #3E54AC; color: white; border: none; border-radius: 20px")
        self.panel3.setGeometry(310, 550, 600, 300)
        self.panel3.setFont(QFont('Times', 20))
        self.panel3.clicked.connect(lambda: self.defaulter_box.setVisible(True))
        
        self.panel4 = QPushButton("Record", self)
        self.panel4.setStyleSheet("background-color: #3E54AC; color: white; border: none; border-radius: 20px")
        self.panel4.setGeometry(1070, 550, 600, 300)
        self.panel4.setFont(QFont('Times', 20))
        self.panel4.clicked.connect(lambda: self.records_box.setVisible(True))
        
        icon = QIcon('images/close-button.png')
        
        self.subject_box = QLabel("", self)
        self.subject_box.setGeometry(120, 100, 1800, 900)
        self.subject_box.setStyleSheet("background-color: white; color: black")
        self.subject_box.setVisible(False)
        
        self.subject_box.header2 = QLabel("Subject Wise Attendance", self.subject_box)
        # self.subject_box.header1.setStyleSheet("border-bottom: 2px solid black")
        self.subject_box.header2.setGeometry(700, 0, 500, 80)
        self.subject_box.header2.setFont(QFont('Times', 20))

        self.subject_box.close_button2 = QPushButton("", self.subject_box)
        self.subject_box.close_button2.setGeometry(1720, 10, 50, 50)
        self.subject_box.close_button2.setStyleSheet("border: none;")
        self.subject_box.close_button2.setIcon(icon)
        size = QSize(50, 50)
        self.subject_box.close_button2.setIconSize(size)
        self.subject_box.close_button2.clicked.connect(lambda: self.subject_box.setVisible(False))
        
        self.overall_box = QLabel("", self)
        self.overall_box.setGeometry(550, 300, 900, 400)
        self.overall_box.setStyleSheet("background-color: white; color: black")
        self.overall_box.setVisible(False)
        self.overall_box.close_button1 = QPushButton("", self.overall_box)
        
        self.overall_box.header1 = QLabel("Overall Attendance", self.overall_box)
        self.overall_box.header1.setGeometry(350, 0, 220, 80)
        self.overall_box.header1.setFont(QFont('Times', 15))
        
        self.overall_box.close_button1.setGeometry(840, 10, 50, 50)
        self.overall_box.close_button1.setStyleSheet("border: none;")
        self.overall_box.close_button1.setIcon(icon)
        size = QSize(50, 50)
        self.overall_box.close_button1.setIconSize(size)
        self.overall_box.close_button1.clicked.connect(lambda: self.overall_box.setVisible(False))
        
        self.defaulter_box = QLabel("", self)
        self.defaulter_box.setGeometry(550, 300, 900, 400)
        self.defaulter_box.setStyleSheet("background-color: white; color: black")
        self.defaulter_box.setVisible(False)
        
        self.defaulter_box.header3 = QLabel("Defaulter", self.defaulter_box)
        # self.defaulter_box.header3.setStyleSheet("border-bottom: 2px solid black")
        self.defaulter_box.header3.setGeometry(400, 0, 220, 80)
        self.defaulter_box.header3.setFont(QFont('Times', 15))
        
        self.defaulter_box.close_button3 = QPushButton("", self.defaulter_box)
        self.defaulter_box.close_button3.setGeometry(840, 10, 50, 50)
        self.defaulter_box.close_button3.setStyleSheet("border: none;")
        self.defaulter_box.close_button3.setIcon(icon)
        size = QSize(50, 50)
        self.defaulter_box.close_button3.setIconSize(size)
        self.defaulter_box.close_button3.clicked.connect(lambda: self.defaulter_box.setVisible(False))
        
        self.records_box = QLabel("", self)
        self.records_box.setGeometry(120, 100, 1800, 900)
        self.records_box.setStyleSheet("background-color: white; color: black")
        self.records_box.setVisible(False)
        
        self.records_box.header4 = QLabel("Record", self.records_box)
        # self.records_box.header4.setStyleSheet("border-bottom: 2px solid black")
        self.records_box.header4.setGeometry(800, 0, 275, 80)
        self.records_box.header4.setFont(QFont('Times', 20))
        
        self.records_box.close_button4 = QPushButton("", self.records_box)
        self.records_box.close_button4.setGeometry(1720, 10, 50, 50)
        self.records_box.close_button4.setStyleSheet("border: none;")
        self.records_box.close_button4.setIcon(icon)
        size = QSize(50, 50)
        self.records_box.close_button4.setIconSize(size)
        self.records_box.close_button4.clicked.connect(lambda: self.records_box.setVisible(False))
        

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
        
        
App = QApplication(sys.argv)
App.setStyleSheet("QMainWindow{background-color: #EBC7E6 }")
window = Attendance()
sys.exit(App.exec())
