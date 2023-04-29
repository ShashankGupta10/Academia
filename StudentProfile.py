import sys,os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
from pymongo import MongoClient

client = MongoClient("mongodb+srv://shashankgupta2003:Shashank10@cluster0.x6bsdlb.mongodb.net/test")
db = client.get_database("IOP")

result = db.Student_Data.find_one({"pin": "1234"})


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowTitle("Academia")

        self.header = QLabel(self)
        self.header.setGeometry(0, 0, 1920, 100)
        self.header.setStyleSheet("QLabel{ background: black; position: fixed;} ")



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
        
        lbl = QLabel("YOUR PROFILE",self)
        lbl.setGeometry(800, 100, 600, 100)
        lbl.setFont(QFont('Times', 30))
        lbl.setStyleSheet("color: ")
        
        self.bg = QLabel(self)
        self.bg.setGeometry(QRect(120,100,900,1000))
        
        backbtn = QToolButton(self.bg)
        backbtn.setArrowType(Qt.LeftArrow)        
        backbtn.setGeometry(0,0,50,50)
        backbtn.setStyleSheet("QToolButton{ background: transparent;color: #301E67}")
        backbtn.clicked.connect(self.back)
    
        nmlbl = QLabel("Full Name : ",self.bg)
        nmlbl.setGeometry(50,110,200,100)
        nmlbl.setFont(QFont('Times', 20))
        nmlbl.setStyleSheet("color: ")
        
        global nmtt
        nmtt = QLabel(self.bg)
        nmtt.setGeometry(270,120,400,70)
        nmtt.setText(result["name"])
        nmtt.setFont(QFont('Times', 20))
        nmtt.setStyleSheet("background: #FFA3FD; border-radius: 25px; padding: 10px")
        
        contactlbl = QLabel("Contact : ",self.bg)
        contactlbl.setGeometry(50,240,200,100)
        contactlbl.setFont(QFont('Times', 20))
        contactlbl.setStyleSheet("color: ")
        
        global contt
        contt = QLabel(self.bg)
        contt.setGeometry(270,270,400,70)
        contt.setText(result["contact_no"])
        contt.setFont(QFont('Times', 20))
        contt.setStyleSheet("background: #FFA3FD; border-radius: 25px; padding: 10px")
        
        addlbl = QLabel("Address : ",self.bg)
        addlbl.setGeometry(50,370,200,100)
        addlbl.setFont(QFont('Times', 20))
        addlbl.setStyleSheet("color: ")
        
        global addtt
        addtt = QLabel(self.bg)
        addtt.setGeometry(270,380,400,100)
        addtt.setText(result["address"])
        addtt.setFont(QFont('Times', 20))
        addtt.setStyleSheet("background: #FFA3FD; border-radius: 25px; padding: 10px")
        
        agelbl = QLabel("Age (in yrs) : ",self.bg)
        agelbl.setGeometry(50,500,200,100)
        agelbl.setFont(QFont('Times', 20))
        agelbl.setStyleSheet("color: ")
        
        global agett
        agett = QLabel(self.bg)
        agett.setGeometry(270,530,200,50)
        agett.setText(result["age"])
        agett.setFont(QFont('Times', 20))
        agett.setStyleSheet("background: #FFA3FD; border-radius: 25px; padding: 10px")
        
        bglbl = QLabel("Blood Group : ",self.bg)
        bglbl.setGeometry(50,600,200,100)
        bglbl.setFont(QFont('Times', 20))
        bglbl.setStyleSheet("color: ")

        global bglbltt
        bglbltt = QLabel("",self.bg)
        bglbltt.setGeometry(270,630,200,50)
        bglbltt.setText(result["Blood Group"])
        bglbltt.setFont(QFont('Times', 20))
        bglbltt.setStyleSheet("background: #FFA3FD; border-radius: 25px; padding: 10px")
    

        #------------------------------------------------------------#
        #-------------------------NEXT PAGE--------------------------#
        #------------------------------------------------------------#
        
        self.bg1 = QLabel(self)
        self.bg1.setGeometry(QRect(920,100,1000,1000))
                
        global proflbltt
        proflbltt = QLabel("Profile Photo",self.bg1)
        pixmap = QPixmap()
        pixmap.loadFromData(result["profile Picture"])
        proflbltt.setPixmap(pixmap)
        proflbltt.setGeometry(600,100,200,200)
        proflbltt.setStyleSheet("border-radius: 10px;border:2px solid black;color: black")
        proflbltt.setAlignment(Qt.AlignCenter)
        proflbltt.setScaledContents(True)
        
        clnmlbl = QLabel("College : ",self.bg1)
        clnmlbl.setGeometry(50,370,200,100)
        clnmlbl.setFont(QFont('Times', 20))
        clnmlbl.setStyleSheet("color: ")
        
        global clnmtt
        clnmtt = QLabel(self.bg1)
        clnmtt.setGeometry(270,380,500,70)
        clnmtt.setText(result["college"])
        clnmtt.setFont(QFont('Times', 20))
        clnmtt.setStyleSheet("background: #FFA3FD; border-radius: 25px; padding: 10px")
        
        divlbl = QLabel("Division : ",self.bg1)
        divlbl.setGeometry(50,270,200,100)
        divlbl.setFont(QFont('Times', 20))
        divlbl.setStyleSheet("color: ")

        global divtt
        divtt = QLabel(self.bg1)
        divtt.setGeometry(270,260,150,70)
        divtt.setText(result["division"])
        divtt.setFont(QFont('Times', 20))
        divtt.setStyleSheet("background: #FFA3FD; border-radius: 25px; padding: 10px")
        
        rollnbl = QLabel("Roll Number : ",self.bg1)
        rollnbl.setGeometry(50,100,200,100)
        rollnbl.setFont(QFont('Times', 20))
        rollnbl.setStyleSheet("color: ")

        global rollntt
        rollntt = QLabel(self.bg1)
        rollntt.setGeometry(270,110,200,70)
        rollntt.setText(result["Roll Number"])
        rollntt.setFont(QFont('Times', 20))
        rollntt.setStyleSheet("background: #FFA3FD; border-radius: 25px; padding: 10px")
        
        yrlbl = QLabel("Year : ",self.bg1)
        yrlbl.setGeometry(50,500,200,100)
        yrlbl.setFont(QFont('Times', 20))
        yrlbl.setStyleSheet("color: ")

        global yrtt
        yrtt = QLabel(self.bg1)
        yrtt.setGeometry(270,510,250,70)
        yrtt.setText(result["year"])
        yrtt.setFont(QFont('Times', 20))
        yrtt.setStyleSheet("background: #FFA3FD; border-radius: 25px; padding: 10px")
        
        dptlbl = QLabel("Department : ",self.bg1)
        dptlbl.setGeometry(50,600,200,100)
        dptlbl.setFont(QFont('Times', 20))
        dptlbl.setStyleSheet("color: ")
        

        dpttt = QLabel(self.bg1)
        dpttt.setGeometry(270,630,500,60)
        dpttt.setText(result["department"])
        dpttt.setFont(QFont('Times', 20))
        dpttt.setStyleSheet("background: #FFA3FD; border-radius: 25px; padding: 10px")
        
        resetbtn = QPushButton("Reset Password",self)
        resetbtn.setGeometry(850,820,200,50)
        resetbtn.setStyleSheet("QPushButton{ background: #3E54AC; color:white ;border-radius: 25px;}")
        resetbtn.setFont(QFont('Times', 12))
        resetbtn.clicked.connect(self.reset)
        
        shad = QGraphicsDropShadowEffect()
        shad.setBlurRadius(10)
        shad.setXOffset(5)
        shad.setYOffset(5)
        shad.setColor(Qt.black)

        resetbtn.setGraphicsEffect(shad)
        
        global passreset
        passreset = QLabel(self)
        passreset.setGeometry(710,240,600,600)
        passreset.setStyleSheet("background: white; border-radius: 20px")
        
        icon1 = QIcon("images/close-button.png")
        close_button1 = QPushButton("", passreset)
        close_button1.setGeometry(550, 10, 50, 50)
        close_button1.setStyleSheet("border: none;")
        close_button1.setIcon(icon1)
        size = QSize(50, 50)
        close_button1.setIconSize(size)
        close_button1.clicked.connect(lambda: passreset.setVisible(False))
        
        oldpass = QLabel("Current Password:",passreset)
        oldpass.setGeometry(80,80,190,50)
        oldpass.setFont(QFont('Times', 12))
        oldpass.setStyleSheet("QLabel{ border: 0px}")

        global oldpasstf
        oldpasstf = QLineEdit(passreset)
        oldpasstf.setGeometry(280,80,210,50)
        oldpasstf.setStyleSheet("QLineEdit{ background: white; border: 1px solid black}")
        oldpasstf.setMaxLength(8)
        
        checkbtn = QPushButton("Check",passreset)
        checkbtn.setGeometry(180,200,150,50)
        checkbtn.setStyleSheet("QPushButton{ background: lightblue; border-radius: 5px}")
        checkbtn.clicked.connect(self.chec)
        
        global newpass
        newpass = QLabel("New Password:", passreset)
        newpass.setGeometry(80,300,200,70)
        newpass.setStyleSheet("QLabel{ color: grey;  border: none; }")
        newpass.setFont(QFont('Times',12))
        
        global newpasstf
        newpasstf = QLineEdit(passreset)
        newpasstf.setGeometry(280,300,200,50)
        newpasstf.setStyleSheet("QLineEdit{ background: lightgrey;}")
        newpasstf.setMaxLength(8)
        
        global confirmpass
        confirmpass = QLabel("Confirm Password:", passreset)
        confirmpass.setGeometry(80,400,200,70)
        confirmpass.setStyleSheet("QLabel{ color: grey;border: 0px black}")
        confirmpass.setFont(QFont('Times', 12))
        
        global confirmpasstf
        confirmpasstf = QLineEdit(passreset)
        confirmpasstf.setGeometry(280,400,200,50)
        confirmpasstf.setStyleSheet("QLineEdit{ background: lightgrey;}")
        confirmpasstf.setMaxLength(8)
        
        ress = QPushButton("Reset", passreset)
        ress.setGeometry(250,500,100,50)
        ress.setStyleSheet("background: lightblue")
        ress.clicked.connect(self.confirm)
        
        newpasstf.setReadOnly(True)
        confirmpasstf.setReadOnly(True)
        passreset.hide()
        
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
        os.system("python Reshala\\reshalabuy.py &") 
    def sprofile(self):
        window.close()
        os.system("python profilestudent.py &")
    def back(self):
        window.close()
        os.system("python Studentdashboard.py &") 
    def backin(self):
        self.bg1.hide()
        self.bg.show()
        
    def reset(self):
        passreset.show()
        newpasstf.setReadOnly(False)
        confirmpasstf.setReadOnly(False)
        newpasstf.setStyleSheet("QLineEdit{ background: lightgrey; border: 0px}")
        confirmpasstf.setStyleSheet("QLineEdit{ background: lightgrey; border: 0px}")
        confirmpass.setStyleSheet("QLabel{ color: grey; border: 0px}")
        newpass.setStyleSheet("QLabel{ color: grey;  border: 0px}")
        
    def confirm(self):
        passreset.hide()
        if newpasstf.text() == confirmpasstf.text():
                db.Student_Data.update_one({"pin": "1234"}, {"$set": {"password": newpasstf.text()}})
        else:
            QMessageBox.information(self, "Error", "Please Enter The Same Password")

    def chec(self):
        
        if oldpasstf.text() == result["password"]:
            newpasstf.setReadOnly(False)
            confirmpasstf.setReadOnly(False)
            newpasstf.setStyleSheet("QLineEdit{ background: white; border: 1px solid black}")
            confirmpasstf.setStyleSheet("QLineEdit{ background:white; border: 1px solid black}")
            newpass.setStyleSheet("QLabel{ color: black; border: none;")
            confirmpass.setStyleSheet("QLabel{ color:black; border: 0px}")
            


app = QApplication(sys.argv)
app.setStyleSheet("QMainWindow{ background: white;}")
window = MainWindow()
window.show()
sys.exit(app.exec_())