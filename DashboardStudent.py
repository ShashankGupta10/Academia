from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,QtCore,QtGui

from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QGraphicsOpacityEffect
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from PyQt5.QtCore import QPropertyAnimation
from pathlib import Path
from tkinter import *

# from new import Shashank

from urllib import *
import sys
import os




class DashboardStudent(QMainWindow):

    # def OpenWindow(self):
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = Shashank() 
    #     self.ui.www(self.window)

            
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Home Page")
        self.setGeometry(0,0,1366,768)

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
        
        sidebar = QLabel(self)
        sidebar.setGeometry(0,100,450,1920)
        sidebar.setStyleSheet("background-color: #3E54AC;")
        
        size = QSize(60, 60)
        
        anicon = QIcon('announcement.png')
        announce = QPushButton(sidebar)
        announce.setGeometry(15,30, 60, 60)
        announce.setStyleSheet("border : 1px solid black")
        announce.setIcon(anicon)
        announce.setIconSize(size)
        
        announce_btn = QPushButton("Announcements", sidebar)
        announce_btn.setGeometry(120, 30, 300, 60)
        announce_btn.setStyleSheet("border: none; color: white; text-align: left")
        announce_btn.setFont(QFont('Times', 20))
        
        aticon = QIcon('attendence.png')
        attend = QPushButton(sidebar)
        attend.setGeometry(15,150, 60, 60)
        attend.setStyleSheet("border : 1px solid black")
        attend.setIcon(aticon)
        attend.setIconSize(size)
        
        attend_btn = QPushButton("Attendance", sidebar)
        attend_btn.setGeometry(120, 150, 300, 60)
        attend_btn.setStyleSheet("border: none; color: white; text-align: left")
        attend_btn.setFont(QFont('Times', 20))

        asicon = QIcon('assignment.png')
        assign = QPushButton(sidebar)
        assign.setGeometry(15,270, 60, 60)
        assign.setStyleSheet("border : 1px solid black")
        assign.setIcon(asicon)
        assign.setIconSize(size)
        
        assign_btn = QPushButton("Assignments", sidebar)
        assign_btn.setGeometry(120, 270, 300, 60)
        assign_btn.setStyleSheet("border: none; color: white; text-align: left")
        assign_btn.setFont(QFont('Times', 20))

        reicon = QIcon('reshaala.png')
        reshaala = QPushButton(sidebar)
        reshaala.setGeometry(15,390, 60, 60)
        reshaala.setStyleSheet("border : 1px solid black")
        reshaala.setIcon(reicon)
        reshaala.setIconSize(size)
        
        reshaala_btn = QPushButton("Reshaala", sidebar)
        reshaala_btn.setGeometry(120, 390, 300, 60)
        reshaala_btn.setStyleSheet("border: none; color: white; text-align: left")
        reshaala_btn.setFont(QFont('Times', 20))
        
        proficon = QIcon('profile.png')
        profile = QPushButton(sidebar)
        profile.setGeometry(15,720, 60, 60)
        profile.setStyleSheet("border : 1px solid black")
        profile.setIcon(proficon)
        profile.setIconSize(size)
        
        profile_btn = QPushButton("Profile", sidebar)
        profile_btn.setGeometry(120, 720, 300, 60)
        profile_btn.setStyleSheet("border: none; color: white; text-align: left")
        profile_btn.setFont(QFont('Times', 20))

        self.panel1 = QLabel(self)
        self.panel1.setGeometry(600,350,500,300)
        self.panel1.setText("Announcements")
        self.panel1.setStyleSheet("QLabel{background: #BFACE2;  border-radius: 20px; padding: 10px;}"
                                "QLabel:hover{ background:#3E54AC;border-radius: 20px;padding: 20px; color: white;}")
        self.panel1.setFont(QFont('Times', 20))
        self.panel1.setAlignment(Qt.AlignCenter)

        self.panel2 = QLabel(self)
        self.panel2.setGeometry(1200,350,500,300)
        self.panel2.setText("Assignments")
        self.panel2.setStyleSheet("QLabel{background: #BFACE2;  border-radius: 20px; padding: 10px;}"
                                "QLabel:hover{ background:#3E54AC; border-width: 50px;border-color: #1E90FF;border-radius: 20px;padding: 10px; color: white;}")
        self.panel2.setFont(QFont('Times', 20))
        self.panel2.setAlignment(Qt.AlignCenter)
        
        hello = QLabel(self)
        hello.setGeometry(900, 150, 500, 100)
        hello.setStyleSheet("QLabel{background: #BFACE2}")

        # self.textfield1 = QLineEdit(self)
        # self.textfield1.setGeometry(830, 375, 300, 40)
        # self.textfield1.setFont(QFont('Times',15))
        # self.textfield1.setStyleSheet("QLineEdit{background-color: black;color: white; border-radius: 20px; padding-left: 20px; padding-right: 20px}"
        #                               "QLineEdit:hover{ border: 2px solid; background-color: #15133C}")
        

        # self.textfield2 = QLineEdit(self)
        # self.textfield2.setGeometry(830, 475, 300, 40)
        # self.textfield2.setFont(QFont('Times',15))
        # self.textfield2.setStyleSheet("QLineEdit{background-color: black;color: white; border-radius: 20px; padding-left: 20px; padding-right: 20px}"
        #                               "QLineEdit:hover{ border: 2px solid; background-color: #15133C}")
        

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




App = QApplication(sys.argv)
App.setStyleSheet("QMainWindow{background-color: white }")

window2 = DashboardStudent()

sys.exit(App.exec())