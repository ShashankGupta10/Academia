from PyQt5.QtWidgets import QLabel, QPushButton, QMainWindow, QLineEdit, QApplication, QTableWidget, QHeaderView, QTableWidgetItem
from PyQt5.QtGui import QIcon, QFont, QPixmap
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import os
from pymongo import MongoClient

client = MongoClient("mongodb+srv://shashankgupta2003:Shashank10@cluster0.x6bsdlb.mongodb.net/test")
db = client['IOP']
coll = db['Student_Data']

student = db.Student_Data.find_one({"name": "aa" })
class Attendance(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Academia")
        self.setGeometry(0,0,1920,1080)

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


        icon = QIcon("images\homepageimage1bgrm.png")
        self.btn10 = QPushButton("" ,self)
        self.btn10.setGeometry(1800, 0, 100, 100)
        self.btn10.setStyleSheet("background : black;")
        self.btn10.setIcon(icon)
        size = QSize(100, 100)
        self.btn10.setIconSize(size)
        # self.btn10.clicked.connect(self.)
        
        
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
        # profile.clicked.connect(self.sprofile)
        
        
        self.attendance_label = QLabel("Attendance", self)
        self.attendance_label.setStyleSheet("border-bottom: 2px solid black;font-weight:bold;")
        self.attendance_label.setGeometry(910, 110, 300, 80)
        self.attendance_label.setFont(QFont('Times', 25))

        shadow1 = QGraphicsDropShadowEffect()
        shadow1.setBlurRadius(10)
        shadow1.setColor(QColor("black"))
        shadow1.setXOffset(5)
        shadow1.setYOffset(5)
        shadow1.setColor(Qt.black)
        
        self.panel1 = QPushButton("SE S1", self)
        self.panel1.setStyleSheet("background-color: #3E54AC; color: white; border: none; border-radius: 20px;")
        self.panel1.setGeometry(310, 200, 600, 300)
        self.panel1.setFont(QFont('Times', 20))
        self.panel1.clicked.connect(lambda: se_s1.setVisible(True))
        self.panel1.setGraphicsEffect(shadow1)
        
        shadow2 = QGraphicsDropShadowEffect()
        shadow2.setBlurRadius(10)
        shadow2.setColor(QColor("black"))
        shadow2.setXOffset(5)
        shadow2.setYOffset(5)
        shadow2.setColor(Qt.black)
        
        self.panel2 = QPushButton("SE S2", self)
        self.panel2.setStyleSheet("background-color: #3E54AC; color: white; border: none; border-radius: 20px")
        self.panel2.setGeometry(1070, 200, 600, 300)
        self.panel2.setFont(QFont('Times', 20))
        self.panel2.clicked.connect(lambda: se_s2.setVisible(True))
        self.panel2.setGraphicsEffect(shadow2)

        shadow3 = QGraphicsDropShadowEffect()
        shadow3.setBlurRadius(10)
        shadow3.setColor(QColor("black"))
        shadow3.setXOffset(5)
        shadow3.setYOffset(5)
        shadow3.setColor(Qt.black) 
            
        self.panel3 = QPushButton("TE T1", self)
        self.panel3.setStyleSheet("background-color: #3E54AC; color: white; border: none; border-radius: 20px")
        self.panel3.setGeometry(310, 550, 600, 300)
        self.panel3.setFont(QFont('Times', 20))
        self.panel3.clicked.connect(lambda: te_t1.setVisible(True))
        self.panel3.setGraphicsEffect(shadow3)
        
        shadow4 = QGraphicsDropShadowEffect()
        shadow4.setBlurRadius(10)
        shadow4.setColor(QColor("black"))
        shadow4.setXOffset(5)
        shadow4.setYOffset(5)
        shadow4.setColor(Qt.black)
        
        self.panel4 = QPushButton("TE T2", self)
        self.panel4.setStyleSheet("background-color: #3E54AC; color: white; border: none; border-radius: 20px")
        self.panel4.setGeometry(1070, 550, 600, 300)
        self.panel4.setFont(QFont('Times', 20))
        self.panel4.clicked.connect(lambda: te_t2.setVisible(True))
        self.panel4.setGraphicsEffect(shadow4)
        
        icon = QIcon('images/close-button.png')
        size = QSize(50, 50)
        
        se_s1 = QLabel("", self)
        se_s1.setGeometry(100, 100, 1820, 900)
        se_s1.setStyleSheet("background-color: white; color: black")
        se_s1.setVisible(False)
        
        re  = QRegExp("[0-9]{2}")                         
        intval = QRegExpValidator(re) 
        
        header1 = QLabel("SE S1 Attendance", se_s1)
        header1.setGeometry(700, 0, 500, 80)
        header1.setFont(QFont('Times', 20))
        
        close_button1 = QPushButton("", se_s1)
        close_button1.setGeometry(1720, 10, 50, 50)
        close_button1.setStyleSheet("border: none;")
        close_button1.setIcon(icon)
        close_button1.setIconSize(size)
        close_button1.clicked.connect(lambda: se_s1.setVisible(False))
        
        name_label = QLabel("Name:", se_s1)
        name_label.setGeometry(650, 80, 80, 50)
        name_label.setFont(QFont('Times', 15))
        

        global student_name1
        student_name1 = QLineEdit(se_s1)
        student_name1.setGeometry(750, 80, 250, 50)
        student_name1.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        student_name1.setFont(QFont('Times', 12))
        
        attend_label = QLabel("Attended", se_s1)
        attend_label.setGeometry(430, 150, 100, 50)
        attend_label.setFont(QFont('Times', 12))
        
        conduct_label = QLabel("Conducted", se_s1)
        conduct_label.setGeometry(625, 150, 100, 50)
        conduct_label.setFont(QFont('Times', 12))
        
        attend_label = QLabel("Attended", se_s1)
        attend_label.setGeometry(1230, 150, 100, 50)
        attend_label.setFont(QFont('Times', 12))
        
        conduct_label = QLabel("Conducted", se_s1)
        conduct_label.setGeometry(1425, 150, 100, 50)
        conduct_label.setFont(QFont('Times', 12))
        
        coa_label = QLabel("COA:", se_s1)
        coa_label.setGeometry(100, 220, 250, 50)
        coa_label.setFont(QFont('Times', 15))
        
        global coa_attend1
        coa_attend1 = QLineEdit(se_s1)
        coa_attend1.setGeometry(400, 220, 150, 50)
        coa_attend1.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        coa_attend1.setFont(QFont('Times', 12))                           
        coa_attend1.setValidator(intval) 
        

        global coa_conduct1
        coa_conduct1 = QLineEdit(se_s1)
        coa_conduct1.setGeometry(600, 220, 150, 50)
        coa_conduct1.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        coa_conduct1.setFont(QFont('Times', 12))
        coa_conduct1.setValidator(intval)

        cn_label = QLabel("Computer Networks:", se_s1)
        cn_label.setGeometry(100, 340, 250, 50)
        cn_label.setFont(QFont('Times', 15))
        
        global cn_attend1
        cn_attend1 = QLineEdit(se_s1)
        cn_attend1.setGeometry(400, 340, 150, 50)
        cn_attend1.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        cn_attend1.setFont(QFont('Times', 12))
        cn_attend1.setValidator(intval)
        
        global cn_conduct1
        cn_conduct1 = QLineEdit(se_s1)
        cn_conduct1.setGeometry(600, 340, 150, 50)
        cn_conduct1.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        cn_conduct1.setFont(QFont('Times', 12))
        cn_conduct1.setValidator(intval)
        
        at_label = QLabel("Automata Theory:", se_s1)
        at_label.setGeometry(100, 460, 250, 50)
        at_label.setFont(QFont('Times', 15))
        

        global at_attend1
        at_attend1 = QLineEdit(se_s1)
        at_attend1.setGeometry(400, 460, 150, 50)
        at_attend1.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        at_attend1.setFont(QFont('Times', 12))
        at_attend1.setValidator(intval)

        global at_conduct1
        at_conduct1 = QLineEdit(se_s1)
        at_conduct1.setGeometry(600, 460, 150, 50)
        at_conduct1.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        at_conduct1.setFont(QFont('Times', 12))
        at_conduct1.setValidator(intval)
        
        maths_label = QLabel("Engg. Maths-IV:", se_s1)
        maths_label.setGeometry(100, 580, 250, 50)
        maths_label.setFont(QFont('Times', 15))
        

        global maths_attend1
        maths_attend1 = QLineEdit(se_s1)
        maths_attend1.setGeometry(400, 580, 150, 50)
        maths_attend1.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        maths_attend1.setFont(QFont('Times', 12))
        maths_attend1.setValidator(intval)
        
        global maths_conduct1
        maths_conduct1 = QLineEdit(se_s1)
        maths_conduct1.setGeometry(600, 580, 150, 50)
        maths_conduct1.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        maths_conduct1.setFont(QFont('Times', 12))
        maths_conduct1.setValidator(intval)
        
        mpl_label = QLabel("Microprocessor Lab:", se_s1)
        mpl_label.setGeometry(900, 220, 250, 50)
        mpl_label.setFont(QFont('Times', 15))
        
        global mpl_attend1
        mpl_attend1 = QLineEdit(se_s1)
        mpl_attend1.setGeometry(1200, 220, 150, 50)
        mpl_attend1.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        mpl_attend1.setFont(QFont('Times', 12))
        mpl_attend1.setValidator(intval)
        
        global mpl_conduct1
        mpl_conduct1 = QLineEdit(se_s1)
        mpl_conduct1.setGeometry(1400, 220, 150, 50)
        mpl_conduct1.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        mpl_conduct1.setFont(QFont('Times', 12))
        mpl_conduct1.setValidator(intval)

        nt_label = QLabel("Networking Lab:", se_s1)
        nt_label.setGeometry(900, 340, 250, 50)
        nt_label.setFont(QFont('Times', 15))
        

        global nt_attend1
        nt_attend1 = QLineEdit(se_s1)
        nt_attend1.setGeometry(1200, 340, 150, 50)
        nt_attend1.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        nt_attend1.setFont(QFont('Times', 12))
        nt_attend1.setValidator(intval)

        global nt_conduct1
        nt_conduct1 = QLineEdit(se_s1)
        nt_conduct1.setGeometry(1400, 340, 150, 50)
        nt_conduct1.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        nt_conduct1.setFont(QFont('Times', 12))
        nt_conduct1.setValidator(intval)
        
        unix_label = QLabel("Unix Lab:", se_s1)
        unix_label.setGeometry(900, 460, 250, 50)
        unix_label.setFont(QFont('Times', 15))
        
        global unix_attend1
        unix_attend1 = QLineEdit(se_s1)
        unix_attend1.setGeometry(1200, 460, 150, 50)
        unix_attend1.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        unix_attend1.setFont(QFont('Times', 12))
        unix_attend1.setValidator(intval)

        global unix_conduct1
        unix_conduct1 = QLineEdit(se_s1)
        unix_conduct1.setGeometry(1400, 460, 150, 50)
        unix_conduct1.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        unix_conduct1.setFont(QFont('Times', 12))
        unix_conduct1.setValidator(intval)
        
        python_label = QLabel("Python Lab:", se_s1)
        python_label.setGeometry(900, 580, 250, 50)
        python_label.setFont(QFont('Times', 15))
        
        global python_attend1
        python_attend1 = QLineEdit(se_s1)
        python_attend1.setGeometry(1200, 580, 150, 50)
        python_attend1.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        python_attend1.setFont(QFont('Times', 12))
        python_attend1.setValidator(intval)

        global python_conduct1
        python_conduct1 = QLineEdit(se_s1)
        python_conduct1.setGeometry(1400, 580, 150, 50)
        python_conduct1.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        python_conduct1.setFont(QFont('Times', 12))
        python_conduct1.setValidator(intval)
        
        submit_attend1 = QPushButton("Submit", se_s1)
        submit_attend1.setGeometry(650, 700, 200, 50)
        submit_attend1.setStyleSheet("background-color: #3E54AC; color: white; border-radius: 25px; padding: 10px;")
        submit_attend1.setFont(QFont('Times', 15))
        submit_attend1.clicked.connect(self.on_click_se_s1)
        
        show_table1 = QPushButton("Show Table", se_s1)
        show_table1.setGeometry(950, 700, 200, 50)
        show_table1.setStyleSheet("background-color: #3E54AC; color: white; border-radius: 25px; padding: 10px;")
        show_table1.setFont(QFont('Times', 15))
        show_table1.clicked.connect(lambda: table_view1.setVisible(True))

        
        # show_table1 = QPushButton("Show Table", self)
        # show_table1.setGeometry(950, 700, 200, 50)
        # show_table1.setStyleSheet("background-color: #3E54AC; color: white; border-radius: 25px; padding: 10px;")
        # show_table1.setFont(QFont('Times', 15))
        # show_table1.clicked.connect(lambda: table_view1.setVisible(True))
        
        table_view1 = QLabel(se_s1)
        table_view1.setGeometry(0, 0, 1820, 900)
        table_view1.setStyleSheet("background-color: white; color: black")
        table_view1.setVisible(False)
        
        table_header1 = QLabel("Attendance Report", table_view1)
        table_header1.setGeometry(700, 0, 500, 80)
        table_header1.setFont(QFont('Times', 20))

        show_table1_button = QPushButton("Show Table", table_view1)
        show_table1_button.setGeometry(950, 700, 200, 50)
        show_table1_button.setStyleSheet("background-color: #3E54AC; color: white; border-radius: 25px; padding: 10px;")
        show_table1_button.setFont(QFont('Times', 15))
        show_table1_button.clicked.connect(self.on_click_se_s1_table)
        

        global table1
        table1 = QTableWidget(table_view1)
        table1.setGeometry(200, 150, 1400, 500)
        table1.setRowCount(3)
        table1.setColumnCount(10)
        table1.setHorizontalHeaderLabels(['Roll No.', 'Name', 'COA', 'CN', 'AT', 'EM-4', 'MPL', 'NT', 'UL', 'Python'])
        table1.horizontalHeader().setStretchLastSection(True)
        table1.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
        
        close_table1 = QPushButton("", table_view1)
        close_table1.setGeometry(1720, 10, 50, 50)
        close_table1.setStyleSheet("border: none;")
        close_table1.setIcon(icon)
        close_table1.setIconSize(size)
        close_table1.clicked.connect(lambda: table_view1.setVisible(False))
        
        
        se_s2 = QLabel("", self)
        se_s2.setGeometry(100, 100, 1820, 900)
        se_s2.setStyleSheet("background-color: white; color: black")
        se_s2.setVisible(False)
        
        header2 = QLabel("SE S2 Attendance", se_s2)
        header2.setGeometry(700, 0, 500, 80)
        header2.setFont(QFont('Times', 20))
        
        close_button2 = QPushButton("", se_s2)
        close_button2.setGeometry(1720, 10, 50, 50)
        close_button2.setStyleSheet("border: none;")
        close_button2.setIcon(icon)
        close_button2.setIconSize(size)
        close_button2.clicked.connect(lambda: se_s2.setVisible(False))
        
        name_label = QLabel("Name:", se_s2)
        name_label.setGeometry(650, 80, 80, 50)
        name_label.setFont(QFont('Times', 15))
        
        global student_name2
        student_name2 = QLineEdit(se_s2)
        student_name2.setGeometry(750, 80, 250, 50)
        student_name2.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        student_name2.setFont(QFont('Times', 12))
        
        attend_label = QLabel("Attended", se_s2)
        attend_label.setGeometry(430, 150, 100, 50)
        attend_label.setFont(QFont('Times', 12))
        
        conduct_label = QLabel("Conducted", se_s2)
        conduct_label.setGeometry(625, 150, 100, 50)
        conduct_label.setFont(QFont('Times', 12))
        
        attend_label = QLabel("Attended", se_s2)
        attend_label.setGeometry(1230, 150, 100, 50)
        attend_label.setFont(QFont('Times', 12))
        
        conduct_label = QLabel("Conducted", se_s2)
        conduct_label.setGeometry(1425, 150, 100, 50)
        conduct_label.setFont(QFont('Times', 12))
        
        coa_label = QLabel("COA:", se_s2)
        coa_label.setGeometry(100, 220, 250, 50)
        coa_label.setFont(QFont('Times', 15))
        
        global coa_attend2
        coa_attend2 = QLineEdit(se_s2)
        coa_attend2.setGeometry(400, 220, 150, 50)
        coa_attend2.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        coa_attend2.setFont(QFont('Times', 12))
        coa_attend2.setValidator(intval)
        
        global coa_conduct2
        coa_conduct2 = QLineEdit(se_s2)
        coa_conduct2.setGeometry(600, 220, 150, 50)
        coa_conduct2.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        coa_conduct2.setFont(QFont('Times', 12))
        coa_conduct2.setValidator(intval)

        cn_label = QLabel("Computer Networks:", se_s2)
        cn_label.setGeometry(100, 340, 250, 50)
        cn_label.setFont(QFont('Times', 15))
        
        global cn_attend2
        cn_attend2 = QLineEdit(se_s2)
        cn_attend2.setGeometry(400, 340, 150, 50)
        cn_attend2.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        cn_attend2.setFont(QFont('Times', 12))
        cn_attend2.setValidator(intval)
        
        global cn_conduct2
        cn_conduct2 = QLineEdit(se_s2)
        cn_conduct2.setGeometry(600, 340, 150, 50)
        cn_conduct2.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        cn_conduct2.setFont(QFont('Times', 12))
        cn_conduct2.setValidator(intval)
        
        at_label = QLabel("Automata Theory:", se_s2)
        at_label.setGeometry(100, 460, 250, 50)
        at_label.setFont(QFont('Times', 15))
        
        global at_attend2
        at_attend2 = QLineEdit(se_s2)
        at_attend2.setGeometry(400, 460, 150, 50)
        at_attend2.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        at_attend2.setFont(QFont('Times', 12))
        at_attend2.setValidator(intval)
        
        global at_conduct2
        at_conduct2 = QLineEdit(se_s2)
        at_conduct2.setGeometry(600, 460, 150, 50)
        at_conduct2.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        at_conduct2.setFont(QFont('Times', 12))
        at_conduct2.setValidator(intval)
        
        maths_label = QLabel("Engg. Maths-IV:", se_s2)
        maths_label.setGeometry(100, 580, 250, 50)
        maths_label.setFont(QFont('Times', 15))
        
        global maths_attend2
        maths_attend2 = QLineEdit(se_s2)
        maths_attend2.setGeometry(400, 580, 150, 50)
        maths_attend2.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        maths_attend2.setFont(QFont('Times', 12))
        maths_attend2.setValidator(intval)
        
        global maths_conduct2
        maths_conduct2 = QLineEdit(se_s2)
        maths_conduct2.setGeometry(600, 580, 150, 50)
        maths_conduct2.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        maths_conduct2.setFont(QFont('Times', 12))
        maths_conduct2.setValidator(intval)
        
        mpl_label = QLabel("Microprocessor Lab:", se_s2)
        mpl_label.setGeometry(900, 220, 250, 50)
        mpl_label.setFont(QFont('Times', 15))
        
        global mpl_attend2
        mpl_attend2 = QLineEdit(se_s2)
        mpl_attend2.setGeometry(1200, 220, 150, 50)
        mpl_attend2.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        mpl_attend2.setFont(QFont('Times', 12))
        mpl_attend2.setValidator(intval)
        
        global mpl_conduct2
        mpl_conduct2 = QLineEdit(se_s2)
        mpl_conduct2.setGeometry(1400, 220, 150, 50)
        mpl_conduct2.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        mpl_conduct2.setFont(QFont('Times', 12))
        mpl_conduct2.setValidator(intval)

        nt_label = QLabel("Networking Lab:", se_s2)
        nt_label.setGeometry(900, 340, 250, 50)
        nt_label.setFont(QFont('Times', 15))
        
        global nt_attend2
        nt_attend2 = QLineEdit(se_s2)
        nt_attend2.setGeometry(1200, 340, 150, 50)
        nt_attend2.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        nt_attend2.setFont(QFont('Times', 12))
        nt_attend2.setValidator(intval)
        
        global nt_conduct2
        nt_conduct2 = QLineEdit(se_s2)
        nt_conduct2.setGeometry(1400, 340, 150, 50)
        nt_conduct2.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        nt_conduct2.setFont(QFont('Times', 12))
        nt_conduct2.setValidator(intval)
        
        unix_label = QLabel("Unix Lab:", se_s2)
        unix_label.setGeometry(900, 460, 250, 50)
        unix_label.setFont(QFont('Times', 15))
        
        global unix_attend2
        unix_attend2 = QLineEdit(se_s2)
        unix_attend2.setGeometry(1200, 460, 150, 50)
        unix_attend2.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        unix_attend2.setFont(QFont('Times', 12))
        unix_attend2.setValidator(intval)
        
        global unix_conduct2
        unix_conduct2 = QLineEdit(se_s2)
        unix_conduct2.setGeometry(1400, 460, 150, 50)
        unix_conduct2.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        unix_conduct2.setFont(QFont('Times', 12))
        unix_conduct2.setValidator(intval)
        
        python_label = QLabel("Python Lab:", se_s2)
        python_label.setGeometry(900, 580, 250, 50)
        python_label.setFont(QFont('Times', 15))
        
        global python_attend2
        python_attend2 = QLineEdit(se_s2)
        python_attend2.setGeometry(1200, 580, 150, 50)
        python_attend2.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        python_attend2.setFont(QFont('Times', 12))
        python_attend2.setValidator(intval)
        
        global python_conduct2
        python_conduct2 = QLineEdit(se_s2)
        python_conduct2.setGeometry(1400, 580, 150, 50)
        python_conduct2.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        python_conduct2.setFont(QFont('Times', 12))
        unix_conduct2.setValidator(intval)
        
        submit_attend2 = QPushButton("Submit", se_s2)
        submit_attend2.setGeometry(650, 700, 200, 50)
        submit_attend2.setStyleSheet("background-color: #3E54AC; color: white; border-radius: 25px; padding: 10px;")
        submit_attend2.setFont(QFont('Times', 15))
        submit_attend2.clicked.connect(self.on_click_se_s2)
        
        show_table2 = QPushButton("Show Table", se_s2)
        show_table2.setGeometry(950, 700, 200, 50)
        show_table2.setStyleSheet("background-color: #3E54AC; color: white; border-radius: 25px; padding: 10px;")
        show_table2.setFont(QFont('Times', 15))
        show_table2.clicked.connect(lambda: table_view2.setVisible(True))
        
        # show_table1 = QPushButton("Show Table", self)
        # show_table1.setGeometry(950, 700, 200, 50)
        # show_table1.setStyleSheet("background-color: #3E54AC; color: white; border-radius: 25px; padding: 10px;")
        # show_table1.setFont(QFont('Times', 15))
        # show_table1.clicked.connect(lambda: table_view1.setVisible(True))
        
        table_view2 = QLabel(se_s2)
        table_view2.setGeometry(0, 0, 1820, 900)
        table_view2.setStyleSheet("background-color: white; color: black")
        table_view2.setVisible(False)
        
        table_header1 = QLabel("Attendance Report", table_view2)
        table_header1.setGeometry(700, 0, 500, 80)
        table_header1.setFont(QFont('Times', 20))

        show_table2_button = QPushButton("Show Table", table_view2)
        show_table2_button.setGeometry(860, 700, 200, 50)
        show_table2_button.setStyleSheet("background-color: #3E54AC; color: white; border-radius: 25px; padding: 10px;")
        show_table2_button.setFont(QFont('Times', 15))
        show_table2_button.clicked.connect(self.on_click_se_s2_table)
        
        global table2
        table2 = QTableWidget(table_view2)
        table2.setGeometry(200, 150, 1400, 500)
        table2.setRowCount(3)
        table2.setColumnCount(10)
        table2.setHorizontalHeaderLabels(['Roll No.', 'Name', 'COA', 'CN', 'AT', 'EM-4', 'MPL', 'NT', 'UL', 'Python'])
        table2.horizontalHeader().setStretchLastSection(True)
        table2.horizontalHeader().setSectionResizeMode(
            QHeaderView.Stretch)
        
        close_table2 = QPushButton("", table_view2)
        close_table2.setGeometry(1720, 10, 50, 50)
        close_table2.setStyleSheet("border: none;")
        close_table2.setIcon(icon)
        close_table2.setIconSize(size)
        close_table2.clicked.connect(lambda: table_view2.setVisible(False))
        
        
        te_t1 = QLabel("", self)
        te_t1.setGeometry(100, 100, 1820, 900)
        te_t1.setStyleSheet("background-color: white; color: black")
        te_t1.setVisible(False)
        
        header3 = QLabel("TE T1 Attendance", te_t1)
        header3.setGeometry(700, 0, 500, 80)
        header3.setFont(QFont('Times', 20))


        name_label3 = QLabel("Name:", te_t1)
        name_label3.setGeometry(650, 80, 80, 50)
        name_label3.setFont(QFont('Times', 15))
        
        global student_name3
        student_name3 = QLineEdit(te_t1)
        student_name3.setGeometry(750, 80, 250, 50)
        student_name3.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        student_name3.setFont(QFont('Times', 12))
        
        attend_label3 = QLabel("Attended", te_t1)
        attend_label3.setGeometry(430, 150, 100, 50)
        attend_label3.setFont(QFont('Times', 12))
        
        conduct_label3 = QLabel("Conducted", te_t1)
        conduct_label3.setGeometry(625, 150, 100, 50)
        conduct_label3.setFont(QFont('Times', 12))
        
        attend_label3 = QLabel("Attended", te_t1)
        attend_label3.setGeometry(1230, 150, 100, 50)
        attend_label3.setFont(QFont('Times', 12))
        
        conduct_label3 = QLabel("Conducted", te_t1)
        conduct_label3.setGeometry(1425, 150, 100, 50)
        conduct_label3.setFont(QFont('Times', 12))
        
        coa_label3 = QLabel("COA:", te_t1)
        coa_label3.setGeometry(100, 220, 250, 50)
        coa_label3.setFont(QFont('Times', 15))
        
        global coa_attend3
        coa_attend3 = QLineEdit(te_t1)
        coa_attend3.setGeometry(400, 220, 150, 50)
        coa_attend3.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        coa_attend3.setFont(QFont('Times', 12))
        coa_attend3.setValidator(intval)
        
        global coa_conduct3
        coa_conduct3 = QLineEdit(te_t1)
        coa_conduct3.setGeometry(600, 220, 150, 50)
        coa_conduct3.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        coa_conduct3.setFont(QFont('Times', 12))
        coa_conduct3.setValidator(intval)

        cn_label3 = QLabel("Computer Networks:", te_t1)
        cn_label3.setGeometry(100, 340, 250, 50)
        cn_label3.setFont(QFont('Times', 15))
        
        global cn_attend3
        cn_attend3 = QLineEdit(te_t1)
        cn_attend3.setGeometry(400, 340, 150, 50)
        cn_attend3.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        cn_attend3.setFont(QFont('Times', 12))
        cn_attend3.setValidator(intval)
        
        global cn_conduct3
        cn_conduct3 = QLineEdit(te_t1)
        cn_conduct3.setGeometry(600, 340, 150, 50)
        cn_conduct3.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        cn_conduct3.setFont(QFont('Times', 12))
        cn_conduct3.setValidator(intval)
        
        at_label3 = QLabel("Automata Theory:", te_t1)
        at_label3.setGeometry(100, 460, 250, 50)
        at_label3.setFont(QFont('Times', 15))
        
        global at_attend3
        at_attend3 = QLineEdit(te_t1)
        at_attend3.setGeometry(400, 460, 150, 50)
        at_attend3.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        at_attend3.setFont(QFont('Times', 12))
        at_attend3.setValidator(intval)
        
        global at_conduct3
        at_conduct3 = QLineEdit(te_t1)
        at_conduct3.setGeometry(600, 460, 150, 50)
        at_conduct3.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        at_conduct3.setFont(QFont('Times', 12))
        at_conduct3.setValidator(intval)
        
        maths_label3 = QLabel("Engg. Maths-IV:", te_t1)
        maths_label3.setGeometry(100, 580, 250, 50)
        maths_label3.setFont(QFont('Times', 15))
        
        global maths_attend3
        maths_attend3 = QLineEdit(te_t1)
        maths_attend3.setGeometry(400, 580, 150, 50)
        maths_attend3.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        maths_attend3.setFont(QFont('Times', 12))
        maths_attend3.setValidator(intval)
        
        global maths_conduct3
        maths_conduct3 = QLineEdit(te_t1)
        maths_conduct3.setGeometry(600, 580, 150, 50)
        maths_conduct3.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        maths_conduct3.setFont(QFont('Times', 12))
        maths_conduct3.setValidator(intval)
        
        mpl_label3 = QLabel("Microprocessor Lab:", te_t1)
        mpl_label3.setGeometry(900, 220, 250, 50)
        mpl_label3.setFont(QFont('Times', 15))
        
        global mpl_attend3
        mpl_attend3 = QLineEdit(te_t1)
        mpl_attend3.setGeometry(1200, 220, 150, 50)
        mpl_attend3.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        mpl_attend3.setFont(QFont('Times', 12))
        mpl_attend3.setValidator(intval)
        
        global mpl_conduct3
        mpl_conduct3 = QLineEdit(te_t1)
        mpl_conduct3.setGeometry(1400, 220, 150, 50)
        mpl_conduct3.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        mpl_conduct3.setFont(QFont('Times', 12))
        mpl_conduct3.setValidator(intval)
        
        nt_label3 = QLabel("Networking Lab:", te_t1)
        nt_label3.setGeometry(900, 340, 250, 50)
        nt_label3.setFont(QFont('Times', 15))
        
        global nt_attend3
        nt_attend3 = QLineEdit(te_t1)
        nt_attend3.setGeometry(1200, 340, 150, 50)
        nt_attend3.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        nt_attend3.setFont(QFont('Times', 12))
        nt_attend3.setValidator(intval)
        
        global nt_conduct3
        nt_conduct3 = QLineEdit(te_t1)
        nt_conduct3.setGeometry(1400, 340, 150, 50)
        nt_conduct3.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        nt_conduct3.setFont(QFont('Times', 12))
        nt_conduct3.setValidator(intval)
        
        unix_label3 = QLabel("Unix Lab:", te_t1)
        unix_label3.setGeometry(900, 460, 250, 50)
        unix_label3.setFont(QFont('Times', 15))
        
        global unix_attend3
        unix_attend3 = QLineEdit(te_t1)
        unix_attend3.setGeometry(1200, 460, 150, 50)
        unix_attend3.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        unix_attend3.setFont(QFont('Times', 12))
        unix_attend3.setValidator(intval)
        
        global unix_conduct3
        unix_conduct3 = QLineEdit(te_t1)
        unix_conduct3.setGeometry(1400, 460, 150, 50)
        unix_conduct3.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        unix_conduct3.setFont(QFont('Times', 12))
        unix_conduct3.setValidator(intval)
        
        python_label3 = QLabel("Python Lab:", te_t1)
        python_label3.setGeometry(900, 580, 250, 50)
        python_label3.setFont(QFont('Times', 15))
        
        global python_attend3
        python_attend3 = QLineEdit(te_t1)
        python_attend3.setGeometry(1200, 580, 150, 50)
        python_attend3.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        python_attend3.setFont(QFont('Times', 12))
        python_attend3.setValidator(intval)
        
        global python_conduct3
        python_conduct3 = QLineEdit(te_t1)
        python_conduct3.setGeometry(1400, 580, 150, 50)
        python_conduct3.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        python_conduct3.setFont(QFont('Times', 12))
        python_conduct3.setValidator(intval)
        
        submit_attend3 = QPushButton("Submit", te_t1)
        submit_attend3.setGeometry(650, 700, 200, 50)
        submit_attend3.setStyleSheet("background-color: #3E54AC; color: white; border-radius: 25px; padding: 10px;")
        submit_attend3.setFont(QFont('Times', 15))
        submit_attend3.clicked.connect(self.on_click_te_t1)
        
        show_table3 = QPushButton("Show Table", te_t1)
        show_table3.setGeometry(950, 700, 200, 50)
        show_table3.setStyleSheet("background-color: #3E54AC; color: white; border-radius: 25px; padding: 10px;")
        show_table3.setFont(QFont('Times', 15))
        show_table3.clicked.connect(lambda: table_view3.setVisible(True))
        
        # show_table1 = QPushButton("Show Table", self)
        # show_table1.setGeometry(950, 700, 200, 50)
        # show_table1.setStyleSheet("background-color: #3E54AC; color: white; border-radius: 25px; padding: 10px;")
        # show_table1.setFont(QFont('Times', 15))
        # show_table1.clicked.connect(lambda: table_view1.setVisible(True))
        
        table_view3 = QLabel(te_t1)
        table_view3.setGeometry(0, 0, 1820, 900)
        table_view3.setStyleSheet("background-color: white; color: black")
        table_view3.setVisible(False)
        
        table_header3 = QLabel("Attendance Report", table_view3)
        table_header3.setGeometry(700, 0, 500, 80)
        table_header3.setFont(QFont('Times', 20))

        show_table3_button = QPushButton("Show Table", table_view3)
        show_table3_button.setGeometry(860, 700, 200, 50)
        show_table3_button.setStyleSheet("background-color: #3E54AC; color: white; border-radius: 25px; padding: 10px;")
        show_table3_button.setFont(QFont('Times', 15))
        show_table3_button.clicked.connect(self.on_click_te_t1_table)
        
        global table3
        table3 = QTableWidget(table_view3)
        table3.setGeometry(200, 150, 1400, 500)
        table3.setRowCount(3)
        table3.setColumnCount(10)
        table3.setHorizontalHeaderLabels(['Roll No.', 'Name', 'COA', 'CN', 'AT', 'EM-4', 'MPL', 'NT', 'UL', 'Python'])
        table3.horizontalHeader().setStretchLastSection(True)
        table3.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        close_table3 = QPushButton("", table_view3)
        close_table3.setGeometry(1720, 10, 50, 50)
        close_table3.setStyleSheet("border: none;")
        close_table3.setIcon(icon)
        close_table3.setIconSize(size)
        close_table3.clicked.connect(lambda: table_view3.setVisible(False))
        
        close_button3 = QPushButton("", te_t1)
        close_button3.setGeometry(1720, 10, 50, 50)
        close_button3.setStyleSheet("border: none;")
        close_button3.setIcon(icon)
        close_button3.setIconSize(size)
        close_button3.clicked.connect(lambda: te_t1.setVisible(False))
        
        te_t2 = QLabel("", self)
        te_t2.setGeometry(100, 100, 1820, 900)
        te_t2.setStyleSheet("background-color: white; color: black")
        te_t2.setVisible(False)

        header4 = QLabel("TE T2 Attendance", te_t2)
        header4.setGeometry(700, 0, 500, 80)
        header4.setFont(QFont('Times', 20))

        name_label4 = QLabel("Name:", te_t2)
        name_label4.setGeometry(650, 80, 80, 50)
        name_label4.setFont(QFont('Times', 15))
        
        global student_name4
        student_name4 = QLineEdit(te_t2)
        student_name4.setGeometry(750, 80, 250, 50)
        student_name4.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        student_name4.setFont(QFont('Times', 12))
        
        attend_label4 = QLabel("Attended", te_t2)
        attend_label4.setGeometry(430, 150, 100, 50)
        attend_label4.setFont(QFont('Times', 12))
        
        conduct_label4 = QLabel("Conducted", te_t2)
        conduct_label4.setGeometry(625, 150, 100, 50)
        conduct_label4.setFont(QFont('Times', 12))
        
        attend_label4 = QLabel("Attended", te_t2)
        attend_label4.setGeometry(1230, 150, 100, 50)
        attend_label4.setFont(QFont('Times', 12))
        
        conduct_label4 = QLabel("Conducted", te_t2)
        conduct_label4.setGeometry(1425, 150, 100, 50)
        conduct_label4.setFont(QFont('Times', 12))
        
        coa_label4 = QLabel("COA:", te_t2)
        coa_label4.setGeometry(100, 220, 250, 50)
        coa_label4.setFont(QFont('Times', 15))
        
        global coa_attend4
        coa_attend4 = QLineEdit(te_t2)
        coa_attend4.setGeometry(400, 220, 150, 50)
        coa_attend4.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        coa_attend4.setFont(QFont('Times', 12))
        coa_attend4.setValidator(intval)
        
        global coa_conduct4
        coa_conduct4 = QLineEdit(te_t2)
        coa_conduct4.setGeometry(600, 220, 150, 50)
        coa_conduct4.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        coa_conduct4.setFont(QFont('Times', 12))
        coa_conduct4.setValidator(intval)

        cn_label4 = QLabel("Computer Networks:", te_t2)
        cn_label4.setGeometry(100, 340, 250, 50)
        cn_label4.setFont(QFont('Times', 15))
        
        global cn_attend4
        cn_attend4 = QLineEdit(te_t2)
        cn_attend4.setGeometry(400, 340, 150, 50)
        cn_attend4.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        cn_attend4.setFont(QFont('Times', 12))
        cn_attend4.setValidator(intval)
        
        global cn_conduct4
        cn_conduct4 = QLineEdit(te_t2)
        cn_conduct4.setGeometry(600, 340, 150, 50)
        cn_conduct4.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        cn_conduct4.setFont(QFont('Times', 12))
        cn_conduct4.setValidator(intval)
        
        at_label4 = QLabel("Automata Theory:", te_t2)
        at_label4.setGeometry(100, 460, 250, 50)
        at_label4.setFont(QFont('Times', 15))
        
        global at_attend4
        at_attend4 = QLineEdit(te_t2)
        at_attend4.setGeometry(400, 460, 150, 50)
        at_attend4.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        at_attend4.setFont(QFont('Times', 12))
        at_attend4.setValidator(intval)
        
        global at_conduct4
        at_conduct4 = QLineEdit(te_t2)
        at_conduct4.setGeometry(600, 460, 150, 50)
        at_conduct4.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        at_conduct4.setFont(QFont('Times', 12))
        at_conduct4.setValidator(intval)
        
        maths_label4 = QLabel("Engg. Maths-IV:", te_t2)
        maths_label4.setGeometry(100, 580, 250, 50)
        maths_label4.setFont(QFont('Times', 15))
        
        global maths_attend4
        maths_attend4 = QLineEdit(te_t2)
        maths_attend4.setGeometry(400, 580, 150, 50)
        maths_attend4.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        maths_attend4.setFont(QFont('Times', 12))
        maths_attend4.setValidator(intval)
        
        global maths_conduct4
        maths_conduct4 = QLineEdit(te_t2)
        maths_conduct4.setGeometry(600, 580, 150, 50)
        maths_conduct4.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        maths_conduct4.setFont(QFont('Times', 12))
        maths_conduct4.setValidator(intval)
        
        mpl_label4 = QLabel("Microprocessor Lab:", te_t2)
        mpl_label4.setGeometry(900, 220, 250, 50)
        mpl_label4.setFont(QFont('Times', 15))
        
        global mpl_attend4
        mpl_attend4 = QLineEdit(te_t2)
        mpl_attend4.setGeometry(1200, 220, 150, 50)
        mpl_attend4.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        mpl_attend4.setFont(QFont('Times', 12))
        mpl_attend4.setValidator(intval)
        
        global mpl_conduct4
        mpl_conduct4 = QLineEdit(te_t2)
        mpl_conduct4.setGeometry(1400, 220, 150, 50)
        mpl_conduct4.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        mpl_conduct4.setFont(QFont('Times', 12))
        mpl_conduct4.setValidator(intval)

        nt_label4 = QLabel("Networking Lab:", te_t2)
        nt_label4.setGeometry(900, 340, 250, 50)
        nt_label4.setFont(QFont('Times', 15))
        
        global nt_attend4
        nt_attend4 = QLineEdit(te_t2)
        nt_attend4.setGeometry(1200, 340, 150, 50)
        nt_attend4.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        nt_attend4.setFont(QFont('Times', 12))
        nt_attend4.setValidator(intval)
        
        global nt_conduct4
        nt_conduct4 = QLineEdit(te_t2)
        nt_conduct4.setGeometry(1400, 340, 150, 50)
        nt_conduct4.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        nt_conduct4.setFont(QFont('Times', 12))
        nt_conduct4.setValidator(intval)
        
        unix_label4 = QLabel("Unix Lab:", te_t2)
        unix_label4.setGeometry(900, 460, 250, 50)
        unix_label4.setFont(QFont('Times', 15))
        
        global unix_attend4
        unix_attend4 = QLineEdit(te_t2)
        unix_attend4.setGeometry(1200, 460, 150, 50)
        unix_attend4.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        unix_attend4.setFont(QFont('Times', 12))
        unix_attend4.setValidator(intval)
        
        global unix_conduct4
        unix_conduct4 = QLineEdit(te_t2)
        unix_conduct4.setGeometry(1400, 460, 150, 50)
        unix_conduct4.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        unix_conduct4.setFont(QFont('Times', 12))
        unix_conduct4.setValidator(intval)
        
        python_label4 = QLabel("Python Lab:", te_t2)
        python_label4.setGeometry(900, 580, 250, 50)
        python_label4.setFont(QFont('Times', 15))
        
        global python_attend4
        python_attend4 = QLineEdit(te_t2)
        python_attend4.setGeometry(1200, 580, 150, 50)
        python_attend4.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        python_attend4.setFont(QFont('Times', 12))
        python_attend4.setValidator(intval)
        
        global python_conduct4
        python_conduct4 = QLineEdit(te_t2)
        python_conduct4.setGeometry(1400, 580, 150, 50)
        python_conduct4.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        python_conduct4.setFont(QFont('Times', 12))
        python_conduct4.setValidator(intval)
        
        submit_attend4 = QPushButton("Submit", te_t2)
        submit_attend4.setGeometry(650, 700, 200, 50)
        submit_attend4.setStyleSheet("background-color: #3E54AC; color: white; border-radius: 25px; padding: 10px;")
        submit_attend4.setFont(QFont('Times', 15))
        submit_attend4.clicked.connect(self.on_click_te_t2)
        
        show_table4 = QPushButton("Show Table", te_t2)
        show_table4.setGeometry(950, 700, 200, 50)
        show_table4.setStyleSheet("background-color: #3E54AC; color: white; border-radius: 25px; padding: 10px;")
        show_table4.setFont(QFont('Times', 15))
        show_table4.clicked.connect(lambda: table_view4.setVisible(True))
        
        # show_table1 = QPushButton("Show Table", self)
        # show_table1.setGeometry(950, 700, 200, 50)
        # show_table1.setStyleSheet("background-color: #3E54AC; color: white; border-radius: 25px; padding: 10px;")
        # show_table1.setFont(QFont('Times', 15))
        # show_table1.clicked.connect(lambda: table_view1.setVisible(True))
        
        table_view4 = QLabel(te_t2)
        table_view4.setGeometry(0, 0, 1820, 900)
        table_view4.setStyleSheet("background-color: white; color: black")
        table_view4.setVisible(False)
        
        table_header4 = QLabel("Attendance Report", table_view4)
        table_header4.setGeometry(700, 0, 500, 80)
        table_header4.setFont(QFont('Times', 20))

        show_table4_button = QPushButton("Show Table", table_view4)
        show_table4_button.setGeometry(860, 700, 200, 50)
        show_table4_button.setStyleSheet("background-color: #3E54AC; color: white; border-radius: 25px; padding: 10px;")
        show_table4_button.setFont(QFont('Times', 15))
        show_table4_button.clicked.connect(self.on_click_te_t2_table)
        
        global table4
        table4 = QTableWidget(table_view4)
        table4.setGeometry(200, 150, 1400, 500)
        table4.setRowCount(3)
        table4.setColumnCount(10)
        table4.setHorizontalHeaderLabels(['Roll No.', 'Name', 'COA', 'CN', 'AT', 'EM-4', 'MPL', 'NT', 'UL', 'Python'])
        table4.horizontalHeader().setStretchLastSection(True)
        table4.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
        close_table4 = QPushButton("", table_view4)
        close_table4.setGeometry(1720, 10, 50, 50)
        close_table4.setStyleSheet("border: none;")
        close_table4.setIcon(icon)
        close_table4.setIconSize(size)
        close_table4.clicked.connect(lambda: table_view4.setVisible(False))

        close_button4 = QPushButton("", te_t2)
        close_button4.setGeometry(1720, 10, 50, 50)
        close_button4.setStyleSheet("border: none;")
        close_button4.setIcon(icon)
        close_button4.setIconSize(size)
        close_button4.clicked.connect(lambda: te_t2.setVisible(False))
        
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
    def logout(self):
        msgb = QMessageBox(self)
        msgb.setWindowTitle("LOGOUT!")
        msgb.setText("Are you sure you want to logout?")
        msgb.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        returnValue = msgb.exec()
        if returnValue == QMessageBox.Ok:
            window.close()
            os.system("python homepage.py &")
        
    def on_click_se_s1(self):
        studentName = student_name1.text()
        coaA = coa_attend1.text()
        coaC = coa_conduct1.text()
        cnA = cn_attend1.text()
        cnC = cn_conduct1.text()
        atA = at_attend1.text()
        atC = at_conduct1.text()
        mathsA = maths_attend1.text()
        mathsC = maths_conduct1.text()
        mplA = mpl_attend1.text()
        mplC = mpl_conduct1.text()
        ntA = nt_attend1.text()
        ntC = nt_conduct1.text()
        unixA = unix_attend1.text()
        unixC = unix_conduct1.text()
        pythonA = python_attend1.text()
        pythonC = python_conduct1.text()

        coa = str((int(coaA)/ int(coaC))*100)
        cn = str((int(cnA)/ int(cnC))*100)
        at = str((int(atA)/ int(atC))*100)
        maths = str((int(mathsA)/ int(mathsC))*100)
        mpl = str((int(mplA)/ int(mplC))*100)
        nt = str((int(ntA)/ int(ntC))*100)
        unix = str((int(unixA)/ int(unixC))*100)
        python = str((int(pythonA)/ int(pythonC))*100)

        global filterr
        filterr = db.Student_Data.find_one({"name": studentName})
        updatedVals = {"$set": {"COA_Attendance": coa, "CN_Attendance": cn, "At_Attendance": at, "Maths_Attendance": maths, "MPL_Attendance": mpl, "NT_Attendance": nt, "Unix_Attendance": unix, "Python_Attendance": python }}
        db.Student_Data.update_one({"name": filterr["name"]}, updatedVals)
    
    def on_click_se_s1_table(self):
        i = 2
        table1.setItem(i, 0, QTableWidgetItem(filterr['Roll Number']))
        table1.setItem(i, 1, QTableWidgetItem(filterr['name']))
        table1.setItem(i, 2, QTableWidgetItem(filterr['COA_Attendance']))
        table1.setItem(i, 3, QTableWidgetItem(filterr['CN_Attendance']))
        table1.setItem(i, 4, QTableWidgetItem(filterr['At_Attendance']))
        table1.setItem(i, 5, QTableWidgetItem(filterr['Maths_Attendance']))
        table1.setItem(i, 6, QTableWidgetItem(filterr['MPL_Attendance']))
        table1.setItem(i, 7, QTableWidgetItem(filterr['NT_Attendance']))
        table1.setItem(i, 8, QTableWidgetItem(filterr['Unix_Attendance']))
        table1.setItem(i, 9, QTableWidgetItem(filterr['Python_Attendance']))
        i = i + 1


    def on_click_se_s2(self):
        studentName2 = student_name2.text()
        coaA = coa_attend2.text()
        coaC = coa_conduct2.text()
        cnA = cn_attend2.text()
        cnC = cn_conduct2.text()
        atA = at_attend2.text()
        atC = at_conduct2.text()
        mathsA = maths_attend2.text()
        mathsC = maths_conduct2.text()
        mplA = mpl_attend2.text()
        mplC = mpl_conduct2.text()
        ntA = nt_attend2.text()
        ntC = nt_conduct2.text()
        unixA = unix_attend2.text()
        unixC = unix_conduct2.text()
        pythonA = python_attend2.text()
        pythonC = python_conduct2.text()

        coa2 = str((int(coaA)/ int(coaC))*100)
        cn2 = str((int(cnA)/ int(cnC))*100)
        at2 = str((int(atA)/ int(atC))*100)
        maths2 = str((int(mathsA)/ int(mathsC))*100)
        mpl2 = str((int(mplA)/ int(mplC))*100)
        nt2 = str((int(ntA)/ int(ntC))*100)
        unix2 = str((int(unixA)/ int(unixC))*100)
        python2 = str((int(pythonA)/ int(pythonC))*100)

        global filterr2
        filterr2 = db.Student_Data.find_one({"name": studentName2})
        updatedVals = {"$set": {"COA_Attendance": coa2, "CN_Attendance": cn2, "At_Attendance": at2, "Maths_Attendance": maths2, "MPL_Attendance": mpl2, "NT_Attendance": nt2, "Unix_Attendance": unix2, "Python_Attendance": python2 }}
        db.Student_Data.update_one({"name": filterr2["name"]}, updatedVals)
    
    def on_click_se_s2_table(self):
        global filterr2
        i = 2
        table2.setItem(i, 0, QTableWidgetItem(filterr2['Roll Number']))
        table2.setItem(i, 1, QTableWidgetItem(filterr2['name']))
        table2.setItem(i, 2, QTableWidgetItem(filterr2['COA_Attendance']))
        table2.setItem(i, 3, QTableWidgetItem(filterr2['CN_Attendance']))
        table2.setItem(i, 4, QTableWidgetItem(filterr2['At_Attendance']))
        table2.setItem(i, 5, QTableWidgetItem(filterr2['Maths_Attendance']))
        table2.setItem(i, 6, QTableWidgetItem(filterr2['MPL_Attendance']))
        table2.setItem(i, 7, QTableWidgetItem(filterr2['NT_Attendance']))
        table2.setItem(i, 8, QTableWidgetItem(filterr2['Unix_Attendance']))
        table2.setItem(i, 9, QTableWidgetItem(filterr2['Python_Attendance']))
        i = i + 1

    def on_click_te_t1(self):
        studentName3 = student_name3.text()
        coaA = coa_attend3.text()
        coaC = coa_conduct3.text()
        cnA = cn_attend3.text()
        cnC = cn_conduct3.text()
        atA = at_attend3.text()
        atC = at_conduct3.text()
        mathsA = maths_attend3.text()
        mathsC = maths_conduct3.text()
        mplA = mpl_attend3.text()
        mplC = mpl_conduct3.text()
        ntA = nt_attend3.text()
        ntC = nt_conduct3.text()
        unixA = unix_attend3.text()
        unixC = unix_conduct3.text()
        pythonA = python_attend3.text()
        pythonC = python_conduct3.text()

        coa3 = str((int(coaA)/ int(coaC))*100)
        cn3 = str((int(cnA)/ int(cnC))*100)
        at3 = str((int(atA)/ int(atC))*100)
        maths3 = str((int(mathsA)/ int(mathsC))*100)
        mpl3 = str((int(mplA)/ int(mplC))*100)
        nt3 = str((int(ntA)/ int(ntC))*100)
        unix3 = str((int(unixA)/ int(unixC))*100)
        python3 = str((int(pythonA)/ int(pythonC))*100)

        global filterr3
        filterr3 = db.Student_Data.find_one({"name": studentName3})
        updatedVals = {"$set": {"COA_Attendance": coa3, "CN_Attendance": cn3, "At_Attendance": at3, "Maths_Attendance": maths3, "MPL_Attendance": mpl3, "NT_Attendance": nt3, "Unix_Attendance": unix3, "Python_Attendance": python3 }}
        db.Student_Data.update_one({"name": filterr3["name"]}, updatedVals)

    def on_click_te_t1_table(self):
        global filterr3
        i = 2
        table3.setItem(i, 0, QTableWidgetItem(filterr3['Roll Number']))
        table3.setItem(i, 1, QTableWidgetItem(filterr3['name']))
        table3.setItem(i, 2, QTableWidgetItem(filterr3['COA_Attendance']))
        table3.setItem(i, 3, QTableWidgetItem(filterr3['CN_Attendance']))
        table3.setItem(i, 4, QTableWidgetItem(filterr3['At_Attendance']))
        table3.setItem(i, 5, QTableWidgetItem(filterr3['Maths_Attendance']))
        table3.setItem(i, 6, QTableWidgetItem(filterr3['MPL_Attendance']))
        table3.setItem(i, 7, QTableWidgetItem(filterr3['NT_Attendance']))
        table3.setItem(i, 8, QTableWidgetItem(filterr3['Unix_Attendance']))
        table3.setItem(i, 9, QTableWidgetItem(filterr3['Python_Attendance']))
        i = i + 1

    def on_click_te_t2(self):
        studentName4 = student_name4.text()
        coaA = coa_attend4.text()
        coaC = coa_conduct4.text()
        cnA = cn_attend4.text()
        cnC = cn_conduct4.text()
        atA = at_attend4.text()
        atC = at_conduct4.text()
        mathsA = maths_attend4.text()
        mathsC = maths_conduct4.text()
        mplA = mpl_attend4.text()
        mplC = mpl_conduct4.text()
        ntA = nt_attend4.text()
        ntC = nt_conduct4.text()
        unixA = unix_attend4.text()
        unixC = unix_conduct4.text()
        pythonA = python_attend4.text()
        pythonC = python_conduct4.text()

        coa4 = str((int(coaA)/ int(coaC))*100)
        cn4 = str((int(cnA)/ int(cnC))*100)
        at4 = str((int(atA)/ int(atC))*100)
        maths4 = str((int(mathsA)/ int(mathsC))*100)
        mpl4 = str((int(mplA)/ int(mplC))*100)
        nt4 = str((int(ntA)/ int(ntC))*100)
        unix4 = str((int(unixA)/ int(unixC))*100)
        python4 = str((int(pythonA)/ int(pythonC))*100)

        global filterr4
        filterr4 = db.Student_Data.find_one({"name": studentName4})
        updatedVals = {"$set": {"COA_Attendance": coa4, "CN_Attendance": cn4, "At_Attendance": at4, "Maths_Attendance": maths4, "MPL_Attendance": mpl4, "NT_Attendance": nt4, "Unix_Attendance": unix4, "Python_Attendance": python4 }}
        db.Student_Data.update_one({"name": filterr4["name"]}, updatedVals)

    def on_click_te_t2_table(self):
        global filterr3
        i = 2
        table4.setItem(i, 0, QTableWidgetItem(filterr4['Roll Number']))
        table4.setItem(i, 1, QTableWidgetItem(filterr4['name']))
        table4.setItem(i, 2, QTableWidgetItem(filterr4['COA_Attendance']))
        table4.setItem(i, 3, QTableWidgetItem(filterr4['CN_Attendance']))
        table4.setItem(i, 4, QTableWidgetItem(filterr4['At_Attendance']))
        table4.setItem(i, 5, QTableWidgetItem(filterr4['Maths_Attendance']))
        table4.setItem(i, 6, QTableWidgetItem(filterr4['MPL_Attendance']))
        table4.setItem(i, 7, QTableWidgetItem(filterr4['NT_Attendance']))
        table4.setItem(i, 8, QTableWidgetItem(filterr4['Unix_Attendance']))
        table4.setItem(i, 9, QTableWidgetItem(filterr4['Python_Attendance']))
        i = i + 1


        
App = QApplication(sys.argv)
App.setStyleSheet("QMainWindow{background-color: white }")
window = Attendance()
sys.exit(App.exec())
