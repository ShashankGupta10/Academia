from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from PyQt5.QtCore import QVariantAnimation

from urllib import *
import sys
import requests

class HomePage(QMainWindow):
    def __init__(self):
        super().__init__()
            

        # self.child = QWidget(self)
        # self.child.setStyleSheet("background-color:red;border-radius:15px solid black;")
        # self.child.resize(50, 50)
        # self.anim = QPropertyAnimation(self.child, b"pos")
        # self.anim.setEndValue(QPoint(800, 600))
        # self.anim.setDuration(3000)
        # self.anim.start()

        self.setWindowTitle("Home Page")
        self.setGeometry(0,0,1920,1080)
        # self.label = QLabel("onichan",self)
        # self.label.setGeometry(0,0,1920,100)
        # self.label.setStyleSheet("background-color: Black; Border: 1px Black;")


        self.label1 = QLabel(self)
        self.label1.setGeometry(0,0,1920,1080)
        # url_image = 'https://www.shutterstock.com/image-photo/old-brick-black-color-wall-260nw-1605128917.jpg'
        
        # image = QImage()
        # image.loadFromData(requests.get(url_image).content)
        
        # self_label1 = QLabel()
        # self_label1.setPixmap(QPixmap(image))

        
        # stylesheet = 'border-image: url("https://www.shutterstock.com/image-photo/old-brick-black-color-wall-260nw-1605128917.jpg");'
        # self.label1.setStyleSheet(stylesheet)
        
        self.pixmap = QPixmap('D:\Pyfon MPR\TkinterGUI\programs\Screenshot 2023-02-24 195310.png')
        self.label1.setPixmap(self.pixmap)
        
        # url = 'https://www.shutterstock.com/image-photo/old-brick-black-color-wall-260nw-1605128917.jpg'    
        # data = urllib.urlopen(url).read()
        # pixmap = QPixmap()
        # pixmap.loadFromData(data)
        # self.label1.setPixmap(pixmap)
        
        
        
        btn = QComboBox(self)
        btn.addItem("Home")
        btn.addItem("Pear")
        btn.addItem("Lemon")

        btn.setGeometry(500,0,100,100)
        # btn.setStyleSheet("background-color: Black; Border: 1px Black; color:white")
        btn.setFont(QFont('Arial', 13))
        
        self.btn1 = QPushButton("Click meas", self)
        self.btn1.setGeometry(700,0,100,100)
        self.btn1.setStyleSheet("Border: 1px Black; color:white; background-color: #4CAF50; color: white;  padding: 16px 32px;  text-align: center;  text-decoration: none;  display: inline-block;  font-size: 16px;  margin: 4px 2px;  transition-duration: 0.4s;cursor: pointer;}"
                                "QpushButton{background-color: white;color: black;border: 2px solid #4CAF50;}"
                                "QpushButton:hover{background-color: #4CAF50;color: white;}"
                                )
        self.btn1.setFont(QFont('Times', 10))
        
        self.btn2 = QPushButton("Whatever", self)
        self.btn2.setGeometry(900,0,100,100)
        self.btn2.setStyleSheet("background-color: Black; Border: 1px Black; color:white")
        self.btn2.setFont(QFont('Times', 10))
        
        self.btn3 = QPushButton("Re-Shaala", self)
        self.btn3.setGeometry(1100,0,100,100)
        self.btn3.setStyleSheet("background-color: Black; Border: 1px Black; color:white")
        self.btn3.setFont(QFont('Times', 10))
        
        self.btn4 = QPushButton("About Us", self)
        self.btn4.setGeometry(1300,0,100,100)
        # self.btn4.setStyleSheet("QPushButton:hover { background-color:rgba(0,0,255,1); transition: 0.2s;}"
        #                         "QPushButton{background-color:rgba(0,0,255,0.1);}")
        self.btn4.setStyleSheet("QPushButton{ opacity: 0.1; background-color: green; transition-property: background-color; transition-duration: 2s;}"
                                "QPushButton:hover{rgb(0,0,255);}"
                                )
        self.btn4.setFont(QFont('Times', 10))
        
        cbstyle =  "QComboBox{ border: 1px solid black;background: black;color: White ;selection-background-color: purple}" 
        btn.setStyleSheet(cbstyle)

  
        self.show()

App = QApplication(sys.argv)
# App.setStyleSheet("background: url('https://www.shutterstock.com/image-photo/old-brick-black-color-wall-260nw-1605128917.jpg')")
  
window = HomePage()

sys.exit(App.exec())        











