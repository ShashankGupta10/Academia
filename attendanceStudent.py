from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QGraphicsOpacityEffect
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from PyQt5.QtCore import QPropertyAnimation
from pathlib import Path
from urllib import *
import sys
import os

class Attendance(QMainWindow):            
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
        
        
        self.loginbox = QLabel(self)
        self.loginbox.setGeometry(0,100,120,800)
        self.loginbox.setStyleSheet("background-color: #3E54AC;")
        
        icon = QIcon('')
        self.usernameicon = QPushButton("" ,self)
        self.usernameicon.setGeometry(20,150, 80, 80)
        self.usernameicon.setIcon(icon)
        size = QSize(50, 50)
        self.usernameicon.setIconSize(size)
        
        self.usernameicon = QPushButton("" ,self)
        self.usernameicon.setGeometry(20,300, 80, 80)
        self.usernameicon.setIcon(icon)
        size = QSize(50, 50)
        self.usernameicon.setIconSize(size)
        
        self.usernameicon = QPushButton("" ,self)
        self.usernameicon.setGeometry(20,450, 80, 80)
        self.usernameicon.setIcon(icon)
        size = QSize(50, 50)
        self.usernameicon.setIconSize(size)
        
        self.usernameicon = QPushButton("" ,self)
        self.usernameicon.setGeometry(20,600, 80, 80)
        self.usernameicon.setIcon(icon)
        size = QSize(50, 50)
        self.usernameicon.setIconSize(size)
        
        
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
        
        icon = QIcon('D:\python mpr final\Python-MPR-\images\close-button.png')
        
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
        
        
App = QApplication(sys.argv)
App.setStyleSheet("QMainWindow{background-color: #EBC7E6 }")
window = Attendance()
sys.exit(App.exec())