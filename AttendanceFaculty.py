from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from urllib import *
import sys
import os

class Attendance(QMainWindow):            
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
        
        
        self.attendance_label = QLabel("Attendance", self)
        self.attendance_label.setStyleSheet("border-bottom: 2px solid black")
        self.attendance_label.setGeometry(910, 110, 250, 80)
        self.attendance_label.setFont(QFont('Times', 20))
        
        self.panel1 = QPushButton("SE S1", self)
        self.panel1.setStyleSheet("background-color: #3E54AC; color: white; border: none; border-radius: 20px;")
        self.panel1.setGeometry(310, 200, 600, 300)
        self.panel1.setFont(QFont('Times', 20))
        self.panel1.clicked.connect(lambda: se_s1.setVisible(True))
        
        self.panel2 = QPushButton("SE S2", self)
        self.panel2.setStyleSheet("background-color: #3E54AC; color: white; border: none; border-radius: 20px")
        self.panel2.setGeometry(1070, 200, 600, 300)
        self.panel2.setFont(QFont('Times', 20))
        self.panel2.clicked.connect(lambda: se_s2.setVisible(True))
            
        self.panel3 = QPushButton("TE T1", self)
        self.panel3.setStyleSheet("background-color: #3E54AC; color: white; border: none; border-radius: 20px")
        self.panel3.setGeometry(310, 550, 600, 300)
        self.panel3.setFont(QFont('Times', 20))
        self.panel3.clicked.connect(lambda: te_t1.setVisible(True))
        
        self.panel4 = QPushButton("TE T2", self)
        self.panel4.setStyleSheet("background-color: #3E54AC; color: white; border: none; border-radius: 20px")
        self.panel4.setGeometry(1070, 550, 600, 300)
        self.panel4.setFont(QFont('Times', 20))
        self.panel4.clicked.connect(lambda: te_t2.setVisible(True))
        
        icon = QIcon('images/close-button.png')
        size = QSize(50, 50)
        
        se_s1 = QLabel("", self)
        se_s1.setGeometry(100, 100, 1820, 900)
        se_s1.setStyleSheet("background-color: white; color: black")
        se_s1.setVisible(False)
        
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
        
        coa_attend1 = QLineEdit(se_s1)
        coa_attend1.setGeometry(400, 220, 150, 50)
        coa_attend1.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        coa_attend1.setFont(QFont('Times', 12))
        
        coa_conduct1 = QLineEdit(se_s1)
        coa_conduct1.setGeometry(600, 220, 150, 50)
        coa_conduct1.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        coa_conduct1.setFont(QFont('Times', 12))

        cn_label = QLabel("Computer Networks:", se_s1)
        cn_label.setGeometry(100, 340, 250, 50)
        cn_label.setFont(QFont('Times', 15))
        
        cn_attend1 = QLineEdit(se_s1)
        cn_attend1.setGeometry(400, 340, 150, 50)
        cn_attend1.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        cn_attend1.setFont(QFont('Times', 12))
        
        cn_conduct1 = QLineEdit(se_s1)
        cn_conduct1.setGeometry(600, 340, 150, 50)
        cn_conduct1.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        cn_conduct1.setFont(QFont('Times', 12))
        
        at_label = QLabel("Automata Theory:", se_s1)
        at_label.setGeometry(100, 460, 250, 50)
        at_label.setFont(QFont('Times', 15))
        
        at_attend1 = QLineEdit(se_s1)
        at_attend1.setGeometry(400, 460, 150, 50)
        at_attend1.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        at_attend1.setFont(QFont('Times', 12))
        
        at_conduct1 = QLineEdit(se_s1)
        at_conduct1.setGeometry(600, 460, 150, 50)
        at_conduct1.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        at_conduct1.setFont(QFont('Times', 12))
        
        maths_label = QLabel("Engg. Maths-IV:", se_s1)
        maths_label.setGeometry(100, 580, 250, 50)
        maths_label.setFont(QFont('Times', 15))
        
        maths_attend1 = QLineEdit(se_s1)
        maths_attend1.setGeometry(400, 580, 150, 50)
        maths_attend1.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        maths_attend1.setFont(QFont('Times', 12))
        
        maths_conduct1 = QLineEdit(se_s1)
        maths_conduct1.setGeometry(600, 580, 150, 50)
        maths_conduct1.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        maths_conduct1.setFont(QFont('Times', 12))
        
        mpl_label = QLabel("Microprocessor Lab:", se_s1)
        mpl_label.setGeometry(900, 220, 250, 50)
        mpl_label.setFont(QFont('Times', 15))
        
        mpl_attend1 = QLineEdit(se_s1)
        mpl_attend1.setGeometry(1200, 220, 150, 50)
        mpl_attend1.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        mpl_attend1.setFont(QFont('Times', 12))
        
        mpl_conduct1 = QLineEdit(se_s1)
        mpl_conduct1.setGeometry(1400, 220, 150, 50)
        mpl_conduct1.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        mpl_conduct1.setFont(QFont('Times', 12))

        nt_label = QLabel("Networking Lab:", se_s1)
        nt_label.setGeometry(900, 340, 250, 50)
        nt_label.setFont(QFont('Times', 15))
        
        nt_attend1 = QLineEdit(se_s1)
        nt_attend1.setGeometry(1200, 340, 150, 50)
        nt_attend1.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        nt_attend1.setFont(QFont('Times', 12))
        
        nt_conduct1 = QLineEdit(se_s1)
        nt_conduct1.setGeometry(1400, 340, 150, 50)
        nt_conduct1.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        nt_conduct1.setFont(QFont('Times', 12))
        
        unix_label = QLabel("Unix Lab:", se_s1)
        unix_label.setGeometry(900, 460, 250, 50)
        unix_label.setFont(QFont('Times', 15))
        
        unix_attend1 = QLineEdit(se_s1)
        unix_attend1.setGeometry(1200, 460, 150, 50)
        unix_attend1.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        unix_attend1.setFont(QFont('Times', 12))
        
        unix_conduct1 = QLineEdit(se_s1)
        unix_conduct1.setGeometry(1400, 460, 150, 50)
        unix_conduct1.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        unix_conduct1.setFont(QFont('Times', 12))
        
        python_label = QLabel("Python Lab:", se_s1)
        python_label.setGeometry(900, 580, 250, 50)
        python_label.setFont(QFont('Times', 15))
        
        python_attend1 = QLineEdit(se_s1)
        python_attend1.setGeometry(1200, 580, 150, 50)
        python_attend1.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        python_attend1.setFont(QFont('Times', 12))
        
        python_conduct1 = QLineEdit(se_s1)
        python_conduct1.setGeometry(1400, 580, 150, 50)
        python_conduct1.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        python_conduct1.setFont(QFont('Times', 12))
        
        submit_attend1 = QPushButton("Submit", se_s1)
        submit_attend1.setGeometry(650, 700, 200, 50)
        submit_attend1.setStyleSheet("background-color: #3E54AC; color: white; border-radius: 25px; padding: 10px;")
        submit_attend1.setFont(QFont('Times', 15))
        
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
        
        table1 = QTableWidget(table_view1)
        table1.setGeometry(200, 150, 1400, 500)
        table1.setRowCount(1)
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
        
        coa_attend2 = QLineEdit(se_s2)
        coa_attend2.setGeometry(400, 220, 150, 50)
        coa_attend2.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        coa_attend2.setFont(QFont('Times', 12))
        
        coa_conduct2 = QLineEdit(se_s2)
        coa_conduct2.setGeometry(600, 220, 150, 50)
        coa_conduct2.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        coa_conduct2.setFont(QFont('Times', 12))

        cn_label = QLabel("Computer Networks:", se_s2)
        cn_label.setGeometry(100, 340, 250, 50)
        cn_label.setFont(QFont('Times', 15))
        
        cn_attend2 = QLineEdit(se_s2)
        cn_attend2.setGeometry(400, 340, 150, 50)
        cn_attend2.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        cn_attend2.setFont(QFont('Times', 12))
        
        cn_conduct2 = QLineEdit(se_s2)
        cn_conduct2.setGeometry(600, 340, 150, 50)
        cn_conduct2.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        cn_conduct2.setFont(QFont('Times', 12))
        
        at_label = QLabel("Automata Theory:", se_s2)
        at_label.setGeometry(100, 460, 250, 50)
        at_label.setFont(QFont('Times', 15))
        
        at_attend2 = QLineEdit(se_s2)
        at_attend2.setGeometry(400, 460, 150, 50)
        at_attend2.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        at_attend2.setFont(QFont('Times', 12))
        
        at_conduct2 = QLineEdit(se_s2)
        at_conduct2.setGeometry(600, 460, 150, 50)
        at_conduct2.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        at_conduct2.setFont(QFont('Times', 12))
        
        maths_label = QLabel("Engg. Maths-IV:", se_s2)
        maths_label.setGeometry(100, 580, 250, 50)
        maths_label.setFont(QFont('Times', 15))
        
        maths_attend2 = QLineEdit(se_s2)
        maths_attend2.setGeometry(400, 580, 150, 50)
        maths_attend2.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        maths_attend2.setFont(QFont('Times', 12))
        
        maths_conduct2 = QLineEdit(se_s2)
        maths_conduct2.setGeometry(600, 580, 150, 50)
        maths_conduct2.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        maths_conduct2.setFont(QFont('Times', 12))
        
        mpl_label = QLabel("Microprocessor Lab:", se_s2)
        mpl_label.setGeometry(900, 220, 250, 50)
        mpl_label.setFont(QFont('Times', 15))
        
        mpl_attend2 = QLineEdit(se_s2)
        mpl_attend2.setGeometry(1200, 220, 150, 50)
        mpl_attend2.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        mpl_attend2.setFont(QFont('Times', 12))
        
        mpl_conduct2 = QLineEdit(se_s2)
        mpl_conduct2.setGeometry(1400, 220, 150, 50)
        mpl_conduct2.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        mpl_conduct2.setFont(QFont('Times', 12))

        nt_label = QLabel("Networking Lab:", se_s2)
        nt_label.setGeometry(900, 340, 250, 50)
        nt_label.setFont(QFont('Times', 15))
        
        nt_attend2 = QLineEdit(se_s2)
        nt_attend2.setGeometry(1200, 340, 150, 50)
        nt_attend2.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        nt_attend2.setFont(QFont('Times', 12))
        
        nt_conduct2 = QLineEdit(se_s2)
        nt_conduct2.setGeometry(1400, 340, 150, 50)
        nt_conduct2.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        nt_conduct2.setFont(QFont('Times', 12))
        
        unix_label = QLabel("Unix Lab:", se_s2)
        unix_label.setGeometry(900, 460, 250, 50)
        unix_label.setFont(QFont('Times', 15))
        
        unix_attend2 = QLineEdit(se_s2)
        unix_attend2.setGeometry(1200, 460, 150, 50)
        unix_attend2.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        unix_attend2.setFont(QFont('Times', 12))
        
        unix_conduct2 = QLineEdit(se_s2)
        unix_conduct2.setGeometry(1400, 460, 150, 50)
        unix_conduct2.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        unix_conduct2.setFont(QFont('Times', 12))
        
        python_label = QLabel("Python Lab:", se_s2)
        python_label.setGeometry(900, 580, 250, 50)
        python_label.setFont(QFont('Times', 15))
        
        python_attend2 = QLineEdit(se_s2)
        python_attend2.setGeometry(1200, 580, 150, 50)
        python_attend2.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        python_attend2.setFont(QFont('Times', 12))
        
        python_conduct2 = QLineEdit(se_s2)
        python_conduct2.setGeometry(1400, 580, 150, 50)
        python_conduct2.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        python_conduct2.setFont(QFont('Times', 12))
        
        submit_attend2 = QPushButton("Submit", se_s2)
        submit_attend2.setGeometry(650, 700, 200, 50)
        submit_attend2.setStyleSheet("background-color: #3E54AC; color: white; border-radius: 25px; padding: 10px;")
        submit_attend2.setFont(QFont('Times', 15))
        
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
        
        table2 = QTableWidget(table_view2)
        table2.setGeometry(200, 150, 1400, 500)
        table2.setRowCount(1)
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
    def back(Self):
        window.close()
        os.system("python Institutedashboard.py &")        
            
        
App = QApplication(sys.argv)
App.setStyleSheet("QMainWindow{background-color: #EBC7E6 }")
window = Attendance()
sys.exit(App.exec())
