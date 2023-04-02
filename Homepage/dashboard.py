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




class HomePage(QMainWindow):

    # def OpenWindow(self):
    #     self.window = QtWidgets.QMainWindow()
    #     self.ui = Shashank() 
    #     self.ui.www(self.window)

            
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Home Page")
        self.setGeometry(0,0,1366,768)

        self.navbar = QLabel(self)
        self.navbar.setGeometry(0, 0, 1366, 100)
        self.navbar.setStyleSheet("QLabel{ background: black; position: fixed;} ")


    #    # creating push button
    #     button = QPushButton("Geek Button", self)
  
    #     # setting geometry of the push button
    #     button.setGeometry(1000, 150, 100, 40)
  
    #     # setting background color to push button when mouse hover over it
    #     button.setStyleSheet("QPushButton::hover"
    #                          "{"
    #                          "background-color : lightgreen;"
    #                          "}")


        self.btn5 = QPushButton("Student Login" ,self)
        self.btn5.setGeometry(950, 150, 60, 85)
        self.btn5.setStyleSheet("QPushButton{ background: #645CBB; color: white; border-radius: 20px; padding: 10px;}"
                                "QPushButton:hover{ background: #A084DC;border-radius: 10px;}")
        self.btn5.setFont(QFont('Times', 12))
        
        # self.btn5.clicked.connect(os.system('python new.py'))
        
        self.btn6 = QPushButton("Institute Login" ,self)
        self.btn6.setGeometry(990, 640, 160, 85)
        self.btn6.setStyleSheet("QPushButton{ background: #645CBB; color: white; border-radius: 20px; padding: 10px;}"
                                "QPushButton:hover{ background: #A084DC;border-radius: 10px;}")
        self.btn6.setFont(QFont('Times', 12))
        
  
        self.label2 = QLabel(self)
        self.label2.setGeometry(850, 150, 600, 500)
        self.pixmap = QPixmap('images\homepageimage5bgrm.png')
        self.label2.setPixmap(self.pixmap)


        self.label5 = QLabel(self)
        self.label5.setGeometry(1000, 60, 600, 200)
        self.label5.setText("Hello Shagun !\n\nWelcome to Academia..")
        self.label5.setFont(QFont("Times", 15))
        self.label5.setStyleSheet("font-weight: bold; color: Black;")

        self.btn1 = QPushButton("Home" ,self.navbar)
        self.btn1.setGeometry(100, 0, 200, 100)
        self.btn1.setStyleSheet("QPushButton{ background: black; color: white; color: white}")
        self.btn1.setFont(QFont('Times', 20))

        self.btn2 = QPushButton("Nothing" ,self.navbar)
        self.btn2.setGeometry(400, 0, 200, 100)
        self.btn2.setStyleSheet("QPushButton{ background: black; color: white; color: white}")
        self.btn2.setFont(QFont('Times', 20))

        self.btn3 = QPushButton("About Us" ,self.navbar)
        self.btn3.setGeometry(700, 0, 200, 100)
        self.btn3.setStyleSheet("QPushButton{ background: black; color: white; color: white}")
        self.btn3.setFont(QFont('Times', 20))

        self.btn4 = QPushButton("Contact Us" ,self.navbar)
        self.btn4.setGeometry(1000, 0, 200, 100)
        self.btn4.setStyleSheet("QPushButton{ background: black; color: white; color: white}")
        self.btn4.setFont(QFont('Times', 20))

        self.loginbox = QLabel(self)
        self.loginbox.setGeometry(10,110,70,510)
        self.loginbox.setStyleSheet("background-color: #3E54AC; border-radius: 20%;")

        self.panel1 = QLabel(self)
        self.panel1.setGeometry(100,140,300,200)
        self.panel1.setStyleSheet("QLabel{background: #BFACE2;  border-radius: 20px; padding: 10px;}"
                                "QLabel:hover{ background:#3E54AC;;border-radius: 20px;padding: 10px;}")

        self.panel2 = QLabel(self)
        self.panel2.setGeometry(100,400,300,200)
        self.panel2.setStyleSheet("QLabel{background: #BFACE2;  border-radius: 20px; padding: 10px;}"
                                "QLabel:hover{ background:#3E54AC;;border-radius: 20px;padding: 10px;}")

        self.panel3 = QLabel(self)
        self.panel3.setGeometry(450,140,300,200)
        self.panel3.setStyleSheet("QLabel{background: #BFACE2;  border-radius: 20px; padding: 10px;}"
                                "QLabel:hover{ background:#3E54AC;border-radius: 20px;padding: 20px;}")

        self.panel4 = QLabel(self)
        self.panel4.setGeometry(450,400,300,200)
        self.panel4.setStyleSheet("QLabel{background: #BFACE2;  border-radius: 20px; padding: 10px;}"
                                "QLabel:hover{ background:#3E54AC; border-width: 50px;border-color: #1E90FF;border-radius: 20px;padding: 10px;}")





        self.loglabel = QLabel("LOG IN", self.loginbox)
        self.loglabel.setGeometry(243, 40, 150, 50)
        self.loglabel.setFont(QFont('Times', 20))
        self.loglabel.setStyleSheet("font-weight: bold;")

        icon = QIcon('images\homepageimage3bgrm.png')
        self.usernameicon = QPushButton("" ,self)
        self.usernameicon.setGeometry(20,150, 50, 50)
        self.usernameicon.setIcon(icon)
        size = QSize(50, 50)
        self.usernameicon.setIconSize(size)

        icon = QIcon('images\homepageimage3bgrm.png')
        self.usernameicon = QPushButton("" ,self)
        self.usernameicon.setGeometry(20,250, 50, 50)
        self.usernameicon.setIcon(icon)
        size = QSize(50, 50)
        self.usernameicon.setIconSize(size)

        icon = QIcon('images\homepageimage3bgrm.png')
        self.usernameicon = QPushButton("" ,self)
        self.usernameicon.setGeometry(20,350, 50, 50)
        self.usernameicon.setIcon(icon)
        size = QSize(50, 50)
        self.usernameicon.setIconSize(size)


        icon = QIcon('images\homepageimage3bgrm.png')
        self.usernameicon = QPushButton("" ,self)
        self.usernameicon.setGeometry(20,450, 50, 50)
        self.usernameicon.setIcon(icon)
        size = QSize(50, 50)
        self.usernameicon.setIconSize(size)



        icon = QIcon('images\homepageimage3bgrm.png')
        self.passwordicon = QPushButton("" ,self)
        self.passwordicon.setGeometry(20,550, 50, 50)
        self.passwordicon.setIcon(icon)
        size = QSize(50, 50)
        self.passwordicon.setIconSize(size)

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
        

        self.btn5 = QPushButton("Forgot Password" ,self.loginbox)
        self.btn5.setGeometry(310, 310, 200, 100)
        self.btn5.setStyleSheet("QPushButton{ background: #BFACE2; color: black;}")
        self.btn5.setFont(QFont('Times', 10))

        self.btn5 = QPushButton("Log in" ,self.loginbox)
        self.btn5.setGeometry(243, 435, 130, 70)
        self.btn5.setStyleSheet("QPushButton{ background: #645CBB; color: black; border-radius: 20px;}"
                                "QPushButton:hover{ background: #A084DC;border-radius: 10px;}")
        self.btn5.setFont(QFont('Times', 17))


        self.footer = QLabel(self)
        self.footer.setGeometry(0, 630, 1366, 100)
        self.footer.setStyleSheet("QLabel{ background: black; position: fixed;} ")

        self.label6 = QPushButton(self.footer)
        self.label6.setGeometry(1000,0,150,100)
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
App.setStyleSheet("QMainWindow{background-color: white }")

window2 = HomePage()

sys.exit(App.exec())