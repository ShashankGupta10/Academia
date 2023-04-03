
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import QFont,QPixmap
from urllib import *
import sys,os
from pymongo import MongoClient

client = MongoClient("mongodb+srv://shashankgupta2003:Shashank10@cluster0.x6bsdlb.mongodb.net/test")
db = client.get_database("IOP")
coll = db.Student_Data

class Studentlogin(QMainWindow):
    def __init__(self):
        global p
        p = QProcess()
        super().__init__()
        self.setWindowTitle("Home Page")
        self.setGeometry(0,0,1366,768)

        self.panel1 = QLabel(self)
        self.panel1.setGeometry(660,150,600,700)
        self.panel1.setStyleSheet("QLabel{ background: white;  border-radius: 40px; padding: 20px;}")
        
        loginAs = QLabel(self.panel1)
        loginAs.setText("STUDENT LOGIN")
        loginAs.setGeometry(200, 100, 250, 100) 
        loginAs.setStyleSheet("background-color: transparent; font-weight: bold;")
        loginAs.setFont(QFont('Times', 12))
        
        username = QLabel(self.panel1)
        username.setText("Username :")
        username.setGeometry(100, 250, 150, 100) 
        username.setStyleSheet("background-color: transparent;")
        username.setFont(QFont('Times', 12))

        self.textEdit1 = QLineEdit(self.panel1)
        self.textEdit1.setGeometry(250,280,250,40)
        self.textEdit1.setStyleSheet("QLineEdit{ background: #EDE3FF; border-color: black; border-radius: 20px; padding: 10px;}")
        self.textEdit1.setFont(QFont('Times', 10))

        password = QLabel(self.panel1)
        password.setText("Password : ")
        password.setGeometry(100, 350, 150, 100) 
        password.setStyleSheet("background-color: transparent;")
        password.setFont(QFont('Times', 12))
        
        self.textEdit2 = QLineEdit(self.panel1)
        self.textEdit2.setGeometry(250,380,250,40)
        self.textEdit2.setStyleSheet("QLineEdit{ background: #EDE3FF; border-color: black; border-radius: 20px; padding: 10px;}")
        self.textEdit2.setFont(QFont('Times', 10))
        self.textEdit2.setEchoMode(QLineEdit.Password)
        self.textEdit2.setMaxLength(8)

        self.btn6 = QPushButton("Login" ,self.panel1)
        self.btn6.setGeometry(250, 525, 100, 50)
        self.btn6.setStyleSheet("QPushButton{ background: #580599; color: white; border-radius: 20px; padding: 10px;}"
                                "QPushButton:hover{ background: #A084DC;border-radius: 10px;}")
        self.btn6.setFont(QFont('Times', 12))
        self.btn6.clicked.connect(self.on_click)

        self.label2 = QLabel(self.panel1)
        self.pixmap = QPixmap("D:\python mpr final\Python-MPR-\loginpage\smalllogo.png")
        self.label2.setGeometry(250, 10, 100, 100)

        self.showMaximized()
        self.show()


    def on_click(self):
        usernameent = self.textEdit1.text()
        passwordent = self.textEdit2.text()
        if(not usernameent or not passwordent):
            QMessageBox.information(self, "Error", "Please fill all the fields")

        else:

            record = coll.find_one({"username": usernameent})
            if(not record):
                QMessageBox.information(self, "Error", "Invalid details")

            password = coll.find_one({"username": usernameent})["password"]


            if(record and password == passwordent):
                window.close()
                os.system("python Studentdashboard.py &")     
            else:
                QMessageBox.information(self, "Error", "Invalid password")




App = QApplication(sys.argv)
App.setStyleSheet("QMainWindow{background-color: #BFACE2 }")

window = Studentlogin()

sys.exit(App.exec())