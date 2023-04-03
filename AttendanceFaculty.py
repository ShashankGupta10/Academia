from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QTabWidget, QTableWidgetItem
from PyQt5.QtWidgets import QGraphicsOpacityEffect
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from PyQt5.QtCore import QPropertyAnimation
from pathlib import Path
from urllib import *
import sys
import time
from pymongo import MongoClient

client = MongoClient("mongodb+srv://shashankgupta2003:Shashank10@cluster0.x6bsdlb.mongodb.net/test")
db = client['IOP']

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
        
        self.panel1 = QPushButton("SE S1", self)
        self.panel1.setStyleSheet("background-color: #3E54AC; color: white; border: none; border-radius: 20px;")
        self.panel1.setGeometry(310, 200, 600, 300)
        self.panel1.setFont(QFont('Times', 20))
        self.panel1.clicked.connect(lambda: self.se_s1.setVisible(True))
        
        self.panel2 = QPushButton("SE S2", self)
        self.panel2.setStyleSheet("background-color: #3E54AC; color: white; border: none; border-radius: 20px")
        self.panel2.setGeometry(1070, 200, 600, 300)
        self.panel2.setFont(QFont('Times', 20))
        self.panel2.clicked.connect(lambda: self.se_s2.setVisible(True))
            
        self.panel3 = QPushButton("TE T1", self)
        self.panel3.setStyleSheet("background-color: #3E54AC; color: white; border: none; border-radius: 20px")
        self.panel3.setGeometry(310, 550, 600, 300)
        self.panel3.setFont(QFont('Times', 20))
        self.panel3.clicked.connect(lambda: self.te_t1.setVisible(True))
        
        self.panel4 = QPushButton("TE T2", self)
        self.panel4.setStyleSheet("background-color: #3E54AC; color: white; border: none; border-radius: 20px")
        self.panel4.setGeometry(1070, 550, 600, 300)
        self.panel4.setFont(QFont('Times', 20))
        self.panel4.clicked.connect(lambda: self.te_t2.setVisible(True))
        
        icon = QIcon('images/close-button.png')
        size = QSize(50, 50)
        
        self.se_s1 = QLabel("", self)
        self.se_s1.setGeometry(120, 100, 1800, 900)
        self.se_s1.setStyleSheet("background-color: white; color: black")
        self.se_s1.setVisible(False)
        
        self.se_s1.header1 = QLabel("SE S1 Attendance", self.se_s1)
        self.se_s1.header1.setGeometry(700, 0, 500, 80)
        self.se_s1.header1.setFont(QFont('Times', 20))
        
        self.se_s1.close_button1 = QPushButton("", self.se_s1)
        self.se_s1.close_button1.setGeometry(1720, 10, 50, 50)
        self.se_s1.close_button1.setStyleSheet("border: none;")
        self.se_s1.close_button1.setIcon(icon)
        self.se_s1.close_button1.setIconSize(size)
        self.se_s1.close_button1.clicked.connect(lambda: self.se_s1.setVisible(False))
        
        self.se_s1.table1 = QTableWidget(self.se_s1)
        self.se_s1.table1.setRowCount(16)
        self.se_s1.table1.setColumnCount(3)
        self.se_s1.table1.setGeometry(100, 100, 700, 650)
        self.se_s1.table1.setFont(QFont('Times', 15))
        self.se_s1.table1.horizontalHeader()
        self.se_s1.table1.setHorizontalHeaderLabels(['Roll No.', 'Name', 'Attendance %'])
        self.se_s1.table1.horizontalHeader().setStretchLastSection(True)  
        self.se_s1.table1.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        self.se_s1.studentName_label = QLabel("Student Name:", self.se_s1)
        self.se_s1.studentName_label.setGeometry(900, 80, 250, 80)
        self.se_s1.studentName_label.setFont(QFont('Times', 15))
        
        self.se_s1.studentName_textbox = QLineEdit(self.se_s1)
        self.se_s1.studentName_textbox.setFont(QFont('Times', 12))
        self.se_s1.studentName_textbox.setStyleSheet("background-color: lightblue; color: black; border-radius: 20px; padding: 10px")
        self.se_s1.studentName_textbox.setGeometry(900, 150, 500, 50)


        self.se_s1.conducted_label1 = QLabel("Lectures Conducted:", self.se_s1)
        self.se_s1.conducted_label1.setGeometry(900, 230, 250, 80)
        self.se_s1.conducted_label1.setFont(QFont('Times', 15))
        
        self.se_s1.conducted_textbox1 = QLineEdit(self.se_s1)
        self.se_s1.conducted_textbox1.setFont(QFont('Times', 12))
        self.se_s1.conducted_textbox1.setStyleSheet("background-color: lightblue; color: black; border-radius: 20px; padding: 10px")
        self.se_s1.conducted_textbox1.setGeometry(900, 300, 500, 50)
        
        self.se_s1.attended_label1 = QLabel("Lectures Attended:", self.se_s1)
        self.se_s1.attended_label1.setGeometry(900, 380, 250, 80)
        self.se_s1.attended_label1.setFont(QFont('Times', 15))
        
        self.se_s1.attended_textbox1 = QLineEdit(self.se_s1)
        self.se_s1.attended_textbox1.setFont(QFont('Times', 12))
        self.se_s1.attended_textbox1.setStyleSheet("background-color: lightblue; color: black; border-radius: 20px; padding: 10px")
        self.se_s1.attended_textbox1.setGeometry(900, 450, 500, 50)
        

        
        self.se_s1.date_label1 = QLabel("Date:", self.se_s1)
        self.se_s1.date_label1.setGeometry(900, 530, 250, 80)
        self.se_s1.date_label1.setFont(QFont('Times', 15))   
        
        self.se_s1.date_picker1 = QDateEdit(self.se_s1)
        self.se_s1.date_picker1.setGeometry(900, 600, 250, 50)
        self.se_s1.date_picker1.setStyleSheet("background-color: lightblue; color: black;")
        self.se_s1.date_picker1.setFont(QFont('Times', 15))
        self.se_s1.date_picker1.setDate(QDate.currentDate())

        self.se_s1.submit_attendance1 = QPushButton("Submit", self.se_s1)
        self.se_s1.submit_attendance1.setGeometry(900, 700, 200, 50)
        self.se_s1.submit_attendance1.setStyleSheet("background-color: #3E54AC; color: white; border-radius: 20px")
        self.se_s1.submit_attendance1.setFont(QFont('Times', 15))
        self.se_s1.submit_attendance1.clicked.connect(self.on_click_submit)


        self.se_s1.showTable = QPushButton("Show Table", self.se_s1)
        self.se_s1.showTable.setGeometry(1200, 700, 200, 50)
        self.se_s1.showTable.setStyleSheet("background-color: #3E54AC; color: white; border-radius: 20px")
        self.se_s1.showTable.setFont(QFont('Times', 15))
        self.se_s1.showTable.clicked.connect(self.on_click_show)
        
        self.se_s2 = QLabel("", self)
        self.se_s2.setGeometry(120, 100, 1800, 900)
        self.se_s2.setStyleSheet("background-color: white; color: black")
        self.se_s2.setVisible(False)
        
        self.se_s2.header2 = QLabel("SE S2 Attendance", self.se_s2)
        self.se_s2.header2.setGeometry(700, 0, 500, 80)
        self.se_s2.header2.setFont(QFont('Times', 20))
        
        self.se_s2.close_button2 = QPushButton("", self.se_s2)
        self.se_s2.close_button2.setGeometry(1720, 10, 50, 50)
        self.se_s2.close_button2.setStyleSheet("border: none;")
        self.se_s2.close_button2.setIcon(icon)
        self.se_s2.close_button2.setIconSize(size)
        self.se_s2.close_button2.clicked.connect(lambda: self.se_s2.setVisible(False))
        
        self.se_s2.table2 = QTableWidget(self.se_s2)
        self.se_s2.table2.setRowCount(16)
        self.se_s2.table2.setColumnCount(3)
        self.se_s2.table2.setGeometry(100, 100, 700, 650)
        self.se_s2.table2.setFont(QFont('Times', 15))
        self.se_s2.table2.horizontalHeader()
        self.se_s2.table2.setHorizontalHeaderLabels(['Roll No.', 'Name', 'Attendance %'])
        self.se_s2.table2.horizontalHeader().setStretchLastSection(True)  
        self.se_s2.table2.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        self.se_s2.studentName_label2 = QLabel("Student Name:", self.se_s2)
        self.se_s2.studentName_label2.setGeometry(900, 80, 250, 80)
        self.se_s2.studentName_label2.setFont(QFont('Times', 15))
        
        self.se_s2.studentName_textbox2 = QLineEdit(self.se_s2)
        self.se_s2.studentName_textbox2.setFont(QFont('Times', 12))
        self.se_s2.studentName_textbox2.setStyleSheet("background-color: lightblue; color: black; border-radius: 20px; padding: 10px")
        self.se_s2.studentName_textbox2.setGeometry(900, 150, 500, 50)


        self.se_s2.conducted_label2 = QLabel("Lectures Conducted:", self.se_s2)
        self.se_s2.conducted_label2.setGeometry(900, 230, 250, 80)
        self.se_s2.conducted_label2.setFont(QFont('Times', 15))
        
        self.se_s2.conducted_textbox2 = QLineEdit(self.se_s2)
        self.se_s2.conducted_textbox2.setFont(QFont('Times', 12))
        self.se_s2.conducted_textbox2.setStyleSheet("background-color: lightblue; color: black; border-radius: 20px; padding: 10px")
        self.se_s2.conducted_textbox2.setGeometry(900, 300, 500, 50)

        
        self.se_s2.attended_label2 = QLabel("Lectures Attended:", self.se_s2)
        self.se_s2.attended_label2.setGeometry(900, 380, 250, 80)
        self.se_s2.attended_label2.setFont(QFont('Times', 15))
        
        self.se_s2.attended_textbox2 = QLineEdit(self.se_s2)
        self.se_s2.attended_textbox2.setFont(QFont('Times', 12))
        self.se_s2.attended_textbox2.setStyleSheet("background-color: lightblue; color: black; border-radius: 20px; padding: 10px")
        self.se_s2.attended_textbox2.setGeometry(900, 450, 500, 50)
        

        
        self.se_s2.date_label2 = QLabel("Date:", self.se_s2)
        self.se_s2.date_label2.setGeometry(900, 530, 250, 80)
        self.se_s2.date_label2.setFont(QFont('Times', 15))   
        
        self.se_s2.date_picker2 = QDateEdit(self.se_s2)
        self.se_s2.date_picker2.setGeometry(900, 600, 250, 50)
        self.se_s2.date_picker2.setStyleSheet("background-color: lightblue; color: black;")
        self.se_s2.date_picker2.setFont(QFont('Times', 15))
        self.se_s2.date_picker2.setDate(QDate.currentDate())
        
        self.se_s2.submit_attendance2 = QPushButton("Submit", self.se_s2)
        self.se_s2.submit_attendance2.setGeometry(900, 700, 200, 50)
        self.se_s2.submit_attendance2.setStyleSheet("background-color: #3E54AC; color: white; border-radius: 20px")
        self.se_s2.submit_attendance2.setFont(QFont('Times', 15))
        self.se_s2.submit_attendance2.clicked.connect(self.on_click_submit2)

        self.se_s2.showTable2 = QPushButton("Show Table", self.se_s2)
        self.se_s2.showTable2.setGeometry(1200, 700, 200, 50)
        self.se_s2.showTable2.setStyleSheet("background-color: #3E54AC; color: white; border-radius: 20px")
        self.se_s2.showTable2.setFont(QFont('Times', 15))
        self.se_s2.showTable2.clicked.connect(self.on_click_show2)
        
        
        
        self.te_t1 = QLabel("", self)
        self.te_t1.setGeometry(120, 100, 1800, 900)
        self.te_t1.setStyleSheet("background-color: white; color: black")
        self.te_t1.setVisible(False)
        
        self.te_t1.header3 = QLabel("TE T1 Attendance", self.te_t1)
        self.te_t1.header3.setGeometry(700, 0, 500, 80)
        self.te_t1.header3.setFont(QFont('Times', 20))
        
        self.te_t1.close_button3 = QPushButton("", self.te_t1)
        self.te_t1.close_button3.setGeometry(1720, 10, 50, 50)
        self.te_t1.close_button3.setStyleSheet("border: none;")
        self.te_t1.close_button3.setIcon(icon)
        self.te_t1.close_button3.setIconSize(size)
        self.te_t1.close_button3.clicked.connect(lambda: self.te_t1.setVisible(False))
        
        self.te_t1.table3 = QTableWidget(self.te_t1)
        self.te_t1.table3.setRowCount(16)
        self.te_t1.table3.setColumnCount(3)
        self.te_t1.table3.setGeometry(100, 100, 700, 650)
        self.te_t1.table3.setFont(QFont('Times', 15))
        self.te_t1.table3.horizontalHeader()
        self.te_t1.table3.setHorizontalHeaderLabels(['Roll No.', 'Name', 'Attendance %'])
        self.te_t1.table3.horizontalHeader().setStretchLastSection(True)  
        self.te_t1.table3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        self.te_t1.studentName_label3 = QLabel("Student Name:", self.te_t1)
        self.te_t1.studentName_label3.setGeometry(900, 80, 250, 80)
        self.te_t1.studentName_label3.setFont(QFont('Times', 15))
        
        self.te_t1.studentName_textbox3 = QLineEdit(self.te_t1)
        self.te_t1.studentName_textbox3.setFont(QFont('Times', 12))
        self.te_t1.studentName_textbox3.setStyleSheet("background-color: lightblue; color: black; border-radius: 20px; padding: 10px")
        self.te_t1.studentName_textbox3.setGeometry(900, 150, 500, 50)


        self.te_t1.conducted_label3 = QLabel("Lectures Conducted:", self.te_t1)
        self.te_t1.conducted_label3.setGeometry(900, 230, 250, 80)
        self.te_t1.conducted_label3.setFont(QFont('Times', 15))
    
        self.te_t1.conducted_textbox3 = QLineEdit(self.te_t1)
        self.te_t1.conducted_textbox3.setFont(QFont('Times', 12))
        self.te_t1.conducted_textbox3.setStyleSheet("background-color: lightblue; color: black; border-radius: 20px; padding: 10px")
        self.te_t1.conducted_textbox3.setGeometry(900, 300, 500, 50)
        
        self.te_t1.attended_label3 = QLabel("Lectures Attended:", self.te_t1)
        self.te_t1.attended_label3.setGeometry(900, 380, 250, 80)
        self.te_t1.attended_label3.setFont(QFont('Times', 15))
        
        self.te_t1.attended_textbox3 = QLineEdit(self.te_t1)
        self.te_t1.attended_textbox3.setFont(QFont('Times', 12))
        self.te_t1.attended_textbox3.setStyleSheet("background-color: lightblue; color: black; border-radius: 20px; padding: 10px")
        self.te_t1.attended_textbox3.setGeometry(900, 450, 500, 50)
        
        
        self.te_t1.date_label3 = QLabel("Date:", self.te_t1)
        self.te_t1.date_label3.setGeometry(900, 530, 250, 80)
        self.te_t1.date_label3.setFont(QFont('Times', 15))   
        
        self.te_t1.date_picker3 = QDateEdit(self.te_t1)
        self.te_t1.date_picker3.setGeometry(900, 600, 250, 50)
        self.te_t1.date_picker3.setStyleSheet("background-color: lightblue; color: black;")
        self.te_t1.date_picker3.setFont(QFont('Times', 15))
        self.te_t1.date_picker3.setDate(QDate.currentDate())
        
        self.te_t1.submit_attendance3 = QPushButton("Submit", self.te_t1)
        self.te_t1.submit_attendance3.setGeometry(900, 700, 200, 50)
        self.te_t1.submit_attendance3.setStyleSheet("background-color: #3E54AC; color: white; border-radius: 20px")
        self.te_t1.submit_attendance3.setFont(QFont('Times', 15))
        self.te_t1.submit_attendance3.clicked.connect(self.on_click_submit3)


        self.te_t1.showTable3 = QPushButton("Show Table", self.te_t1)
        self.te_t1.showTable3.setGeometry(1200, 700, 200, 50)
        self.te_t1.showTable3.setStyleSheet("background-color: #3E54AC; color: white; border-radius: 20px")
        self.te_t1.showTable3.setFont(QFont('Times', 15))
        self.te_t1.showTable3.clicked.connect(self.on_click_show3)


        self.te_t2 = QLabel("", self)
        self.te_t2.setGeometry(120, 100, 1800, 900)
        self.te_t2.setStyleSheet("background-color: white; color: black")
        self.te_t2.setVisible(False)

        self.te_t2.header4 = QLabel("TE T2 Attendance", self.te_t2)
        self.te_t2.header4.setGeometry(700, 0, 500, 80)
        self.te_t2.header4.setFont(QFont('Times', 20))

        self.te_t2.close_button4 = QPushButton("", self.te_t2)
        self.te_t2.close_button4.setGeometry(1720, 10, 50, 50)
        self.te_t2.close_button4.setStyleSheet("border: none;")
        self.te_t2.close_button4.setIcon(icon)
        self.te_t2.close_button4.setIconSize(size)
        self.te_t2.close_button4.clicked.connect(lambda: self.te_t2.setVisible(False))
        
        self.te_t2.table4 = QTableWidget(self.te_t2)
        self.te_t2.table4.setRowCount(16)
        self.te_t2.table4.setColumnCount(3)
        self.te_t2.table4.setGeometry(100, 100, 700, 650)
        self.te_t2.table4.setFont(QFont('Times', 15))
        self.te_t2.table4.horizontalHeader()
        self.te_t2.table4.setHorizontalHeaderLabels(['Roll No.', 'Name', 'Attendance %'])
        self.te_t2.table4.horizontalHeader().setStretchLastSection(True)  
        self.te_t2.table4.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        self.te_t2.studentName_label4 = QLabel("Student Name:", self.te_t2)
        self.te_t2.studentName_label4.setGeometry(900, 80, 250, 80)
        self.te_t2.studentName_label4.setFont(QFont('Times', 15))
        
        self.te_t2.studentName_textbox4 = QLineEdit(self.te_t2)
        self.te_t2.studentName_textbox4.setFont(QFont('Times', 12))
        self.te_t2.studentName_textbox4.setStyleSheet("background-color: lightblue; color: black; border-radius: 20px; padding: 10px")
        self.te_t2.studentName_textbox4.setGeometry(900, 150, 500, 50)


        self.te_t2.conducted_label4 = QLabel("Lectures Conducted:", self.te_t2)
        self.te_t2.conducted_label4.setGeometry(900, 230, 250, 80)
        self.te_t2.conducted_label4.setFont(QFont('Times', 15))
        
        self.te_t2.conducted_textbox4 = QLineEdit(self.te_t2)
        self.te_t2.conducted_textbox4.setFont(QFont('Times', 12))
        self.te_t2.conducted_textbox4.setStyleSheet("background-color: lightblue; color: black; border-radius: 20px; padding: 10px")
        self.te_t2.conducted_textbox4.setGeometry(900, 300, 500, 50)
        
        self.te_t2.attended_label4 = QLabel("Lectures Attended:", self.te_t2)
        self.te_t2.attended_label4.setGeometry(900, 380, 250, 80)
        self.te_t2.attended_label4.setFont(QFont('Times', 15))
        
        self.te_t2.attended_textbox4 = QLineEdit(self.te_t2)
        self.te_t2.attended_textbox4.setFont(QFont('Times', 12))
        self.te_t2.attended_textbox4.setStyleSheet("background-color: lightblue; color: black; border-radius: 20px; padding: 10px")
        self.te_t2.attended_textbox4.setGeometry(900, 450, 500, 50)
    
        
        self.te_t2.date_label4 = QLabel("Date:", self.te_t2)
        self.te_t2.date_label4.setGeometry(900, 530, 250, 80)
        self.te_t2.date_label4.setFont(QFont('Times', 15))   
        
        self.te_t2.date_picker4 = QDateEdit(self.te_t2)
        self.te_t2.date_picker4.setGeometry(900, 600, 250, 50)
        self.te_t2.date_picker4.setStyleSheet("background-color: lightblue; color: black;")
        self.te_t2.date_picker4.setFont(QFont('Times', 15))
        self.te_t2.date_picker4.setDate(QDate.currentDate())
        
        self.te_t2.submit_attendance4 = QPushButton("Submit", self.te_t2)
        self.te_t2.submit_attendance4.setGeometry(900, 700, 200, 50)
        self.te_t2.submit_attendance4.setStyleSheet("background-color: #3E54AC; color: white; border-radius: 20px")
        self.te_t2.submit_attendance4.setFont(QFont('Times', 15))
        self.te_t2.submit_attendance4.clicked.connect(self.on_click_submit4)

        self.te_t2.showTable4 = QPushButton("Show Table", self.te_t2)
        self.te_t2.showTable4.setGeometry(1200, 700, 200, 50)
        self.te_t2.showTable4.setStyleSheet("background-color: #3E54AC; color: white; border-radius: 20px")
        self.te_t2.showTable4.setFont(QFont('Times', 15))
        self.te_t2.showTable4.clicked.connect(self.on_click_show4)

        

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
    
    def on_click_submit(self):
        global StudentName, lecturesAttended, lecturesConducted
        StudentName = self.se_s1.studentName_textbox.text()
        lecturesConducted= self.se_s1.conducted_textbox1.text()
        lecturesAttended = self.se_s1.attended_textbox1.text()

        fil = db.Student_Data.find_one({"name": StudentName})
        attendancePercent = str((int(lecturesAttended)/int(lecturesConducted))*100)
        updatedVals = {"$set": {"attendance": attendancePercent }}
        db.Student_Data.update_one(fil, updatedVals)


        

    def on_click_show(self):
        fil = db.Student_Data.find_one({"name": StudentName})
        rolll = str(107)
        namee = fil["name"]
        att = fil["attendance"]


        row_position = self.se_s1.table1.rowCount()
        self.se_s1.table1.insertRow(row_position)
        self.se_s1.table1.setItem(row_position, 0, QTableWidgetItem(rolll))
        self.se_s1.table1.setItem(row_position, 1, QTableWidgetItem(namee))
        self.se_s1.table1.setItem(row_position, 2, QTableWidgetItem(att))


    def on_click_submit2(self):
        global StudentName2, lecturesAttended2, lecturesConducted2
        StudentName2 = self.se_s2.studentName_textbox2.text()
        lecturesConducted2= self.se_s2.conducted_textbox2.text()
        lecturesAttended2 = self.se_s2.attended_textbox2.text()

        filt = db.Student_Data.find_one({"name": StudentName2})
        attendancePercent2 = str((int(lecturesAttended2)/int(lecturesConducted2))*100)
        updatedVals2 = {"$set": {"attendance": attendancePercent2 }}
        db.Student_Data.update_one(filt, updatedVals2)


        

    def on_click_show2(self):
        filt = db.Student_Data.find_one({"name": StudentName2})
        rolll2 = str(107)
        namee2 = filt["name"]
        att2 = filt["attendance"]


        row_position = self.se_s2.table2.rowCount()
        self.se_s2.table2.insertRow(row_position)
        self.se_s2.table2.setItem(row_position, 0, QTableWidgetItem(rolll2))
        self.se_s2.table2.setItem(row_position, 1, QTableWidgetItem(namee2))
        self.se_s2.table2.setItem(row_position, 2, QTableWidgetItem(att2))

    
    def on_click_submit3(self):
        global StudentName3, lecturesAttended3, lecturesConducted3
        StudentName3 = self.te_t1.studentName_textbox3.text()
        lecturesConducted3= self.te_t1.conducted_textbox3.text()
        lecturesAttended3 = self.te_t1.attended_textbox3.text()

        filt = db.Student_Data.find_one({"name": StudentName3})
        attendancePercent3 = str((int(lecturesAttended3)/int(lecturesConducted3))*100)
        updatedVals3 = {"$set": {"attendance": attendancePercent3 }}
        db.Student_Data.update_one(filt, updatedVals3)


        

    def on_click_show3(self):
        filt = db.Student_Data.find_one({"name": StudentName3})
        rolll3 = str(107)
        namee3 = filt["name"]
        att3 = filt["attendance"]


        row_position = self.te_t1.table3.rowCount()
        self.te_t1.table3.insertRow(row_position)
        self.te_t1.table3.setItem(row_position, 0, QTableWidgetItem(rolll3))
        self.te_t1.table3.setItem(row_position, 1, QTableWidgetItem(namee3))
        self.te_t1.table3.setItem(row_position, 2, QTableWidgetItem(att3))

    
    def on_click_submit4(self):
        global StudentName4, lecturesAttended4, lecturesConducted4
        StudentName4 = self.te_t2.studentName_textbox4.text()
        lecturesConducted4= self.te_t2.conducted_textbox4.text()
        lecturesAttended4 = self.te_t2.attended_textbox4.text()

        filt = db.Student_Data.find_one({"name": StudentName4})
        attendancePercent4 = str((int(lecturesAttended4)/int(lecturesConducted4))*100)
        updatedVals4 = {"$set": {"attendance": attendancePercent4 }}
        db.Student_Data.update_one(filt, updatedVals4)


        

    def on_click_show4(self):
        filt = db.Student_Data.find_one({"name": StudentName4})
        rolll4 = str(107)
        namee4 = filt["name"]
        att4 = filt["attendance"]


        row_position = self.te_t2.table4.rowCount()
        self.te_t2.table4.insertRow(row_position)
        self.te_t2.table4.setItem(row_position, 0, QTableWidgetItem(rolll4))
        self.te_t2.table4.setItem(row_position, 1, QTableWidgetItem(namee4))
        self.te_t2.table4.setItem(row_position, 2, QTableWidgetItem(att4))
        

        
        
App = QApplication(sys.argv)
App.setStyleSheet("QMainWindow{background-color: #EBC7E6 }")
window = Attendance()
sys.exit(App.exec())
