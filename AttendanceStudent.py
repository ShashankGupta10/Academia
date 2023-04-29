from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from urllib import *
import sys
import os
from pymongo import MongoClient

client = MongoClient("mongodb+srv://shashankgupta2003:Shashank10@cluster0.x6bsdlb.mongodb.net/test")
db = client.get_database("IOP")
result = db.Student_Data.find_one({"pin": "1234"})
dbpin = result["pin"]

compAtt =str(int((float(result["At_Attendance"]) + float(result["CN_Attendance"]) + float(result["COA_Attendance"])  + float(result["MPL_Attendance"]) + float(result["Maths_Attendance"]) + float(result["NT_Attendance"]) + float(result["Python_Attendance"]) + float(result["Unix_Attendance"]))/8)) + "%"

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
        navbarbtn1.clicked.connect(self.back)

        navbarbtn2= QPushButton("Reshala", self)
        navbarbtn2.setGeometry(1400, 31, 150, 40)
        navbarbtn2.setStyleSheet("QPushButton{ background: Black; position: fixed;border-radius:15px;color: white;}")
        navbarbtn2.setFont(QFont('Times', 20))
        navbarbtn2.clicked.connect(self.reshaala)
        
        navbarbtn3= QPushButton("About", self)
        navbarbtn3.setGeometry(1600, 31, 150, 40)
        navbarbtn3.setStyleSheet("QPushButton{ background: Black; position: fixed;border-radius:15px;color: white;}")
        navbarbtn3.setFont(QFont('Times', 20))
        # navbarbtn3.clicked.connect(self.about)

        icon = QIcon("images\homepageimage1bgrm.png")
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
        announce.setGeometry(20,30, 60, 60)
        announce.setStyleSheet("border : 0px solid black")
        announce.setIcon(anicon)
        announce.setIconSize(size)
        announce.clicked.connect(self.announcement)
        
        aticon = QIcon('All icons\\attendence.png')
        attend = QPushButton(sidebar)
        attend.setGeometry(20,150, 60, 60)
        attend.setStyleSheet("border : 0px solid black")
        attend.setIcon(aticon)
        attend.setIconSize(size)
        attend.clicked.connect(self.attendence)

        asicon = QIcon('All icons\\assignment.png')
        assign = QPushButton(sidebar)
        assign.setGeometry(25, 270, 60, 60)
        assign.setStyleSheet("border : 0px solid black")
        assign.setIcon(asicon)
        assign.setIconSize(size)
        assign.clicked.connect(self.assignment)

        reicon = QIcon('All icons\\reshaala.png')
        reshaala = QPushButton(sidebar)
        reshaala.setGeometry(20,390, 60, 60)
        reshaala.setStyleSheet("border : 0px solid black")
        reshaala.setIcon(reicon)
        reshaala.setIconSize(size)
        reshaala.clicked.connect(self.reshaala)
        
        proficon = QIcon('All icons\\profile.png')
        profile = QPushButton(sidebar)
        profile.setGeometry(20, 700, 60, 60)
        profile.setStyleSheet("border : 0px solid black")
        profile.setIcon(proficon)
        profile.setIconSize(size)
        profile.clicked.connect(self.sprofile)
        global pin, pintf, pinbtn, panel1, panel2, panel3, panel4
        pin = QLabel(self)
        pin.setGeometry(710, 400, 225, 100)
        pin.setText("Enter Your Pin :")
        pin.setFont(QFont('Times', 20))

        pintf = QLineEdit(self)
        pintf.setGeometry(950, 425, 100, 50)
        pintf.setStyleSheet("background: white; border-radius: 10px; color: black; border: 2px solid black")
        pintf.setFont(QFont('Times', 20))


        pinbtn = QPushButton("Submit", self)
        pinbtn.setStyleSheet("background-color: #3E54AC; color: white; border: none; border-radius: 20px;")
        pinbtn.setGeometry(850, 500, 130, 70)
        pinbtn.setFont(QFont('Times', 20))
        pinbtn.clicked.connect(self.on_submit)
        
        
        attendance_label = QLabel("Attendance", self)
        attendance_label.setStyleSheet("border-bottom: 2px solid black")
        attendance_label.setGeometry(910, 110, 250, 80)
        attendance_label.setFont(QFont('Times', 20))
        
        panel1 = QPushButton("Overall Attendance", self)
        panel1.setStyleSheet("background-color: #3E54AC; color: white; border: none; border-radius: 20px;")
        panel1.setGeometry(310, 300, 600, 300)
        panel1.setFont(QFont('Times', 20))
        panel1.hide()
        panel1.clicked.connect(lambda: overall_box.setVisible(True))
        
        panel2 = QPushButton("Subject Wise Attendance", self)
        panel2.setStyleSheet("background-color: #3E54AC; color: white; border: none; border-radius: 20px")
        panel2.setGeometry(1070, 300, 600, 300)
        panel2.setFont(QFont('Times', 20))
        panel2.hide()
        panel2.clicked.connect(lambda: subject_box.setVisible(True))
            


        
        
        icon = QIcon('images/close-button.png')
        
        subject_box = QLabel(self)
        subject_box.setGeometry(100, 100, 1820, 900)
        subject_box.setStyleSheet("background-color: white; color: black")
        subject_box.setVisible(False)
        
        header2 = QLabel("Subject Wise Attendance", subject_box)
        header2.setGeometry(700, 0, 500, 80)
        header2.setFont(QFont('Times', 20))

        close_button2 = QPushButton("", subject_box)
        close_button2.setGeometry(1750, 10, 50, 50)
        close_button2.setStyleSheet("border: none;")
        close_button2.setIcon(icon)
        size = QSize(50, 50)
        close_button2.setIconSize(size)
        close_button2.clicked.connect(lambda: subject_box.setVisible(False))
        
        lecture1 = QLabel("Lectures", subject_box)
        lecture1.setGeometry(350, 100, 200, 50)
        lecture1.setFont(QFont('Times', 17))
        
        lecture2 = QLabel("Labs", subject_box)
        lecture2.setGeometry(1150, 100, 200, 50)
        lecture2.setFont(QFont('Times', 17))
        
        coa_label = QLabel("COA:", subject_box)
        coa_label.setGeometry(100, 220, 250, 50)
        coa_label.setFont(QFont('Times', 15))
        
        coa_attend = QLabel(subject_box)
        coa_attend.setGeometry(400, 220, 300, 50)
        coa_attend.setText(result["COA_Attendance"])
        coa_attend.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        coa_attend.setFont(QFont('Times', 15))

        cn_label = QLabel("Computer Networks:", subject_box)
        cn_label.setGeometry(100, 340, 250, 50)
        cn_label.setFont(QFont('Times', 15))
        
        cn_attend = QLabel(subject_box)
        cn_attend.setGeometry(400, 340, 300, 50)
        cn_attend.setText(result["CN_Attendance"])
        cn_attend.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        cn_attend.setFont(QFont('Times', 15))
        
        at_label = QLabel("Automata Theory:", subject_box)
        at_label.setGeometry(100, 460, 250, 50)
        at_label.setFont(QFont('Times', 15))
        
        at_attend = QLabel(subject_box)
        at_attend.setGeometry(400, 460, 300, 50)
        at_attend.setText(result["At_Attendance"])
        at_attend.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        at_attend.setFont(QFont('Times', 15))
        
        maths_label = QLabel("Engg. Maths-IV:", subject_box)
        maths_label.setGeometry(100, 580, 250, 50)
        maths_label.setFont(QFont('Times', 15))
        
        maths_attend = QLabel(subject_box)
        maths_attend.setText(result["Maths_Attendance"])
        maths_attend.setGeometry(400, 580, 300, 50)
        maths_attend.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        maths_attend.setFont(QFont('Times', 15))
        
        mpl_label = QLabel("Microprocessor Lab:", subject_box)
        mpl_label.setGeometry(900, 220, 250, 50)
        mpl_label.setFont(QFont('Times', 15))
        
        mpl_attend = QLabel(subject_box)
        mpl_attend.setGeometry(1200, 220, 300, 50)
        mpl_attend.setText(result["MPL_Attendance"])
        mpl_attend.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        mpl_attend.setFont(QFont('Times', 15))

        nt_label = QLabel("Networking Lab:", subject_box)
        nt_label.setGeometry(900, 340, 250, 50)
        nt_label.setFont(QFont('Times', 15))
        
        nt_attend = QLabel(subject_box)
        nt_attend.setGeometry(1200, 340, 300, 50)
        nt_attend.setText(result["NT_Attendance"])
        nt_attend.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        nt_attend.setFont(QFont('Times', 15))
        
        unix_label = QLabel("Unix Lab:", subject_box)
        unix_label.setGeometry(900, 460, 250, 50)
        unix_label.setFont(QFont('Times', 15))
        
        unix_attend = QLabel(subject_box)
        unix_attend.setGeometry(1200, 460, 300, 50)
        unix_attend.setText(result["Unix_Attendance"])
        unix_attend.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        unix_attend.setFont(QFont('Times', 15))
        
        python_label = QLabel("Python Lab:", subject_box)
        python_label.setGeometry(900, 580, 250, 50)
        python_label.setFont(QFont('Times', 15))
        
        python_attend = QLabel(subject_box)
        python_attend.setGeometry(1200, 580, 300, 50)
        python_attend.setText(result["Python_Attendance"])
        python_attend.setStyleSheet("background: lightblue; border-radius: 25px; padding: 10px")
        python_attend.setFont(QFont('Times', 15))
        
        overall_box = QLabel("", self)
        overall_box.setGeometry(550, 300, 900, 400)
        overall_box.setStyleSheet("background-color: white; color: black")
        overall_box.setVisible(False)
        
        header1 = QLabel("Overall Attendance", overall_box)
        header1.setGeometry(350, 0, 220, 80)
        header1.setFont(QFont('Times', 15))

        compAttendance = QLabel("", overall_box)
        compAttendance.setText(str(compAtt))
        compAttendance.setFont(QFont('Times', 50))
        compAttendance.setStyleSheet("font-weight: bold;")
        compAttendance.setGeometry(350, 125,800, 200)
        
        close_button1 = QPushButton("", overall_box)
        close_button1.setGeometry(840, 10, 50, 50)
        close_button1.setStyleSheet("border: none;")
        close_button1.setIcon(icon)
        size = QSize(50, 50)
        close_button1.setIconSize(size)
        close_button1.clicked.connect(lambda: overall_box.setVisible(False))
        
        defaulter_box = QLabel("", self)
        defaulter_box.setGeometry(550, 300, 900, 400)
        defaulter_box.setStyleSheet("background-color: white; color: black")
        defaulter_box.setVisible(False)
        
        header3 = QLabel("Defaulter", defaulter_box)
        header3.setGeometry(400, 0, 220, 80)
        header3.setFont(QFont('Times', 15))
        
        close_button3 = QPushButton("", defaulter_box)
        close_button3.setGeometry(840, 10, 50, 50)
        close_button3.setStyleSheet("border: none;")
        close_button3.setIcon(icon)
        size = QSize(50, 50)
        close_button3.setIconSize(size)
        close_button3.clicked.connect(lambda: defaulter_box.setVisible(False))
        
        records_box = QLabel("", self)
        records_box.setGeometry(100, 100, 1820, 900)
        records_box.setStyleSheet("background-color: white; color: black")
        records_box.setVisible(False)
        
        header4 = QLabel("Record", records_box)
        header4.setGeometry(800, 0, 275, 80)
        header4.setFont(QFont('Times', 20))
        
        close_button4 = QPushButton("", records_box)
        close_button4.setGeometry(1750, 10, 50, 50)
        close_button4.setStyleSheet("border: none;")
        close_button4.setIcon(icon)
        size = QSize(50, 50)
        close_button4.setIconSize(size)
        close_button4.clicked.connect(lambda: records_box.setVisible(False))
        

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
        os.system("python StudentAnnouncement.py &")   
    def attendence(self):
        window.close()
        os.system("python Attendancestudent.py &")
    def assignment(self):
        window.close()
        os.system("python AssignmentStudent.py &") 
    def reshaala(self):
        window.close()
        os.system("python Reshala_sell\\reshalasell.py &") 
    def sprofile(self):
        window.close()
        os.system("python profilestudent.py &")
    def back(self):
        window.close()
        os.system("python Studentdashboard.py &")

    def on_submit(self):
            if pintf.text() == dbpin:
                pin.hide()
                pintf.hide()
                pinbtn.hide()
                panel1.show()
                panel2.show()

            else:
                QMessageBox.information(self, "Error", "Invalid password")
        
        
App = QApplication(sys.argv)
App.setStyleSheet("QMainWindow{background-color: #EBC7E6 }")
window = Attendance()
sys.exit(App.exec())
