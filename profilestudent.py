
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtGui
from pymongo import MongoClient


client = MongoClient("mongodb+srv://shashankgupta2003:Shashank10@cluster0.x6bsdlb.mongodb.net/test")
db = client['IOP']


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowTitle("Academia")

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
        sidebar.setGeometry(0,100,120,1920)
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


        
        self.bg = QLabel(self)
        self.bg.setGeometry(QRect(260,100,1400,1000))
        self.bg.setStyleSheet("background: #301E67")
        
        lbl = QLabel("COMPLETE YOUR PROFILE",self.bg)
        lbl.setGeometry(400, 0, 600, 100)
        lbl.setFont(QFont('Times', 30))
        lbl.setStyleSheet("color: white")
    
        nmlbl = QLabel("Full Name : ",self.bg)
        nmlbl.setGeometry(150,110,200,100)
        nmlbl.setFont(QFont('Times', 20))
        nmlbl.setStyleSheet("color: white")
        

        global nmtf
        nmtf = QLineEdit(self.bg)
        nmtf.setGeometry(400,120,800,70)
        nmtf.setPlaceholderText("Enter full name")
        nmtf.setFont(QFont('Times', 20))
        nmtf.setStyleSheet("background: #FFA3FD; border-radius: 10px;")
        nmtf.setMaxLength(50)
        
        contactlbl = QLabel("Contact : ",self.bg)
        contactlbl.setGeometry(150,240,200,100)
        contactlbl.setFont(QFont('Times', 20))
        contactlbl.setStyleSheet("color: white")
        

        global contf
        contf = QLineEdit(self.bg)
        contf.setGeometry(400,250,800,70)
        contf.setPlaceholderText("Enter Contact Number")
        contf.setFont(QFont('Times', 20))
        contf.setStyleSheet("background: #FFA3FD; border-radius: 10px;")
        
        re  = QRegExp("[0-9]{10}")                         
        intval = QtGui.QRegExpValidator(re)                            
        contf.setValidator(intval) 
        
        addlbl = QLabel("Address : ",self.bg)
        addlbl.setGeometry(150,370,200,100)
        addlbl.setFont(QFont('Times', 20))
        addlbl.setStyleSheet("color: white")
        

        global addtf
        addtf = QPlainTextEdit(self.bg)
        addtf.setGeometry(400,380,800,100)
        addtf.setPlaceholderText("Enter Address")
        addtf.setFont(QFont('Times', 20))
        addtf.setStyleSheet("background: #FFA3FD; border-radius: 10px;")
        
        agelbl = QLabel("Age (in yrs) : ",self.bg)
        agelbl.setGeometry(150,500,200,100)
        agelbl.setFont(QFont('Times', 20))
        agelbl.setStyleSheet("color: white")
        

        global agetf
        agetf = QLineEdit(self.bg)
        agetf.setGeometry(400,530,200,50)
        agetf.setPlaceholderText("Enter Age")
        agetf.setFont(QFont('Times', 20))
        agetf.setStyleSheet("background: #FFA3FD; border-radius: 10px;")
        re1 = QRegExp("[0-9]{3}")
        intval1 = QRegExpValidator(re1)
        agetf.setValidator(intval1)
        
        bglbl = QLabel("Blood Group : ",self.bg)
        bglbl.setGeometry(750,500,200,100)
        bglbl.setFont(QFont('Times', 20))
        bglbl.setStyleSheet("color: white")

        global bgcb,bg  
        bgcb = QComboBox(self.bg)
        bgcb.addItems(["A+", "B+","AB+","O+","A-","B-","AB-","O-","RH null"])
        bgcb.setGeometry(1000,530,100,50)
        bgcb.setStyleSheet("QComboBox { background: #FFA3FD; color: black; selection-background-color: #D27685; selection-color: black;Font-size:20px; border-radius: 10px;}"
                         "QListView{ background: #FFA3FD}")

        nextbtn = QPushButton("Next",self.bg)
        nextbtn.setGeometry(710,650,100,50)
        nextbtn.setStyleSheet("QPushButton{ background: #A555EC ;color:white;border-radius: 4px}"
                              "QPushButton:hover{ background: #D27685;}")
        nextbtn.setFont(QFont('Arial', 12))
        nextbtn.clicked.connect(self.nextpg)
        
        shad = QGraphicsDropShadowEffect()
        shad.setBlurRadius(10)
        shad.setXOffset(5)
        shad.setYOffset(5)
        shad.setColor(Qt.black)

        nextbtn.setGraphicsEffect(shad)

        #------------------------------------------------------------#
        #-------------------------NEXT PAGE--------------------------#
        #------------------------------------------------------------#
        
        self.bg1 = QLabel(self)
        self.bg1.setGeometry(QRect(260,100,1400,1000))
        self.bg1.setStyleSheet("background: #301E67")
        
        global proflbl
        proflbl = QLabel("Upload Profile Photo",self.bg1)
        proflbl.setGeometry(1100,180,230,230)
        proflbl.setStyleSheet("border-radius: 10px;border:2px solid White;color: White")
        proflbl.setAlignment(Qt.AlignCenter)
        
        uploadimg = QPushButton("Upload Image",self.bg1)
        uploadimg.setGeometry(1160,450,100,40)
        uploadimg.setStyleSheet("QPushButton{ background: #C47AFF; position: fixed;border-radius:15px;color: black;border-radius:20px;} QPushButton:hover borderradius:20px;")
        uploadimg.clicked.connect(self.getImage)

        backbtn= QToolButton(self.bg1)
        backbtn.setArrowType(Qt.LeftArrow)        
        backbtn.setGeometry(10,10,50,50)
        backbtn.setStyleSheet("QToolButton{ background:  #A459D1;color: #301E67}")
        backbtn.clicked.connect(self.back)
        
        lbl = QLabel("ADD DETAILS",self.bg1)
        lbl.setGeometry(450,0,500,100)
        lbl.setFont(QFont('Times', 30))
        lbl.setStyleSheet("color: white")
        
        
        clnmlbl = QLabel("College : ",self.bg1)
        clnmlbl.setGeometry(150,110,200,100)
        clnmlbl.setFont(QFont('Times', 20))
        clnmlbl.setStyleSheet("color: white")
        
        global clnmtf
        clnmtf = QLineEdit(self.bg1)
        clnmtf.setGeometry(350,120,650,70)
        clnmtf.setPlaceholderText("College Name:")
        clnmtf.setFont(QFont('Times', 20))
        clnmtf.setStyleSheet("background: #FFA3FD; border-radius: 10px;")
        
        divlbl = QLabel("Division : ",self.bg1)
        divlbl.setGeometry(150,280,200,100)
        divlbl.setFont(QFont('Times', 20))
        divlbl.setStyleSheet("color: white")

        global divtf
        divtf = QLineEdit(self.bg1)
        divtf.setGeometry(350,290,150,70)
        divtf.setPlaceholderText("Division")
        divtf.setFont(QFont('Times', 20))
        divtf.setStyleSheet("background: #FFA3FD; border-radius: 10px;")
        
        rollnbl = QLabel("Roll Number : ",self.bg1)
        rollnbl.setGeometry(530,280,200,100)
        rollnbl.setFont(QFont('Times', 20))
        rollnbl.setStyleSheet("color: white")

        global rollntf
        rollntf = QLineEdit(self.bg1)
        rollntf.setGeometry(760,290,240,70)
        rollntf.setPlaceholderText("Roll No")
        rollntf.setFont(QFont('Times', 20))
        rollntf.setStyleSheet("background: #FFA3FD; border-radius: 10px;")
        
        yrlbl = QLabel("Year : ",self.bg1)
        yrlbl.setGeometry(150,450,200,100)
        yrlbl.setFont(QFont('Times', 20))
        yrlbl.setStyleSheet("color: white")

        global yrcb
        yrcb = QComboBox(self.bg1)
        yrcb.addItems(["First Year", "Second Year","Third Year","Bachelor of Eng"])
        yrcb.setGeometry(350,475,150,50)
        yrcb.setStyleSheet("QComboBox { background: #FFA3FD; color: black; selection-background-color: #D27685; selection-color: black;Font-size:20px; border-radius: 10px;}"
                         "QListView{ background: #FFA3FD}")
        
        dptlbl = QLabel("Department : ",self.bg1)
        dptlbl.setGeometry(530,450,200,100)
        dptlbl.setFont(QFont('Times', 20))
        dptlbl.setStyleSheet("color: white")

        global dptcb
        dptcb = QComboBox(self.bg1)
        dptcb.addItems(["Information Technology", "Computer Science","Electronic & Telecom","AI & Data Science","Chemical"])
        dptcb.setGeometry(760,475,240,50)
        dptcb.setStyleSheet("QComboBox { background: #FFA3FD; color: black; selection-background-color: #D27685; selection-color: black;Font-size:20px; border-radius: 10px;}"
                         "QListView{ background: #FFA3FD}")
        
        subbtn = QPushButton("Submit",self.bg1)
        subbtn.setGeometry(650,650,100,50)
        subbtn.setStyleSheet("QPushButton{ background: #A555EC ;color:white;border-radius: 4px}"
                              "QPushButton:hover{ background: #D27685;}")
        subbtn.setFont(QFont('Arial', 12))
        shad1 = QGraphicsDropShadowEffect()
        shad1.setBlurRadius(10)
        shad1.setXOffset(5)
        shad1.setYOffset(5)
        shad1.setColor(Qt.black)
        subbtn.setGraphicsEffect(shad1)
        subbtn.clicked.connect(self.on_click_submit)

        
        self.bg1.hide()
        
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
        
    def getImage(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        global fileName
        fileName, _ = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()", "","All Files (*);;Image Files (*.png *.jpg *.jpeg)", options=options)
        if fileName:
            self.pixmap = QPixmap(fileName)
            proflbl.setPixmap(self.pixmap)
            proflbl.setFixedSize(200, 200)
    
    def back(self):
        self.bg1.hide()
        self.bg.show()
    
    def nextpg(self):
        self.bg.hide()
        self.bg1.show()

    def on_click_submit(self):
        file_name = fileName
        pixmap1 = QPixmap(file_name)
        with open(file_name, 'rb') as f:
            image_data = f.read()
        
        fullName = nmtf.text()
        contact = contf.text()
        address = addtf.toPlainText()
        age = agetf.text()
        bloodGroup = bgcb.currentText()
        college = clnmtf.text()
        division = divtf.text()
        rollNumber = rollntf.text()
        year = yrcb.currentText()
        department = dptcb.currentText()
        profilePic = image_data
        filterr = db.Student_Data.find_one({"name": fullName})
        
        

        updatedValues = {"$set":{"contact_no": contact, "address": address, "age": age, "Blood Group": bloodGroup, "college": college, "division": division, "Roll Number": rollNumber, "year": year, "department": department, "profile Picture": profilePic}}
        db.Student_Data.update_one(filterr, updatedValues)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyleSheet("QMainWindow{ background: #BFACE2}")
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

