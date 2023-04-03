import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import subprocess,os


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1366, 768)
        self.setWindowTitle("Academia")
        global process
        process = QProcess()
        
    #-----------------------------HEADER--------------------------------------#
    
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
        
    #------------------BODY---------------------------------#
    
        self.welcomeGreeting = QLabel(self)
        self.welcomeGreeting.setGeometry(75,150,700,300)
        self.welcomeGreeting.setStyleSheet("color: black; font-weight: bold;")
        self.welcomeGreeting.setText("WELCOME TO ACADEMIA")
        self.welcomeGreeting.setFont(QFont('Times', 33))

        self.line = QLabel(self)
        self.line.setGeometry(75,160,700,300)
        self.line.setStyleSheet("color: black; font-weight: bold;")
        self.line.setText("________________________________________________")
        self.line.setFont(QFont('Times', 33))
        
        self.tagline = QLabel(self)
        self.tagline.setGeometry(75,300,700,300)
        self.tagline.setStyleSheet("color: black")
        self.tagline.setText("A Better Learning Future Starts Here.")
        self.tagline.setFont(QFont('Helvetica', 20))
        
        self.tagline2 = QLabel(self)
        self.tagline2.setGeometry(70,350,700,300)
        self.tagline2.setStyleSheet("color: black;")
        self.tagline2.setText("The platform to fulfill all your eductaional needs.")
        self.tagline2.setFont(QFont('Helvetica', 20))
    
        self.button6 = QPushButton("Student", self)
        self.button6.setGeometry(710, 700, 200, 50)
        self.button6.setStyleSheet("QPushButton{ background: #C47AFF; position: fixed;border-radius:15px;color: black;border-radius:24px;}"
                                   "QPushButton:hover {border-radius:20px;}")
        self.button6.setFont(QFont('Times', 20))
        self.button6.clicked.connect(self.student)

        self.button7 = QPushButton("Institute", self)
        self.button7.setGeometry(1010, 700, 200, 50)
        self.button7.setStyleSheet("QPushButton{ background: #C47AFF; position: fixed;border-radius:15px;color: black;border-radius:24px;} "
                                   "QPushButton:hover {border-radius:20px;}")
        self.button7.setFont(QFont('Times', 20))
        self.button7.clicked.connect(self.institute)

        shadow = QGraphicsDropShadowEffect()
        shadow.setBlurRadius(10)
        shadow.setColor(QColor("black"))
        shadow.setXOffset(5)
        shadow.setYOffset(5)
        shadow.setColor(Qt.black)

        shadow1 = QGraphicsDropShadowEffect()
        shadow1.setBlurRadius(10)
        shadow1.setXOffset(5)
        shadow1.setYOffset(5)
        shadow1.setColor(Qt.black)

        shadow2 = QGraphicsDropShadowEffect()
        shadow2.setBlurRadius(10)
        shadow2.setXOffset(5)
        shadow2.setYOffset(5)
        shadow2.setColor(Qt.black)

        self.button6.setGraphicsEffect(shadow)
        self.button7.setGraphicsEffect(shadow1)
        
    #-----------CAROUSEL---------#
        self.image_label = QLabel(self)
        self.image_label.setGeometry(1100, 125, 700, 500)
        self.image_label.setPixmap(QPixmap("D:\python mpr final\Python-MPR-\Homepage\homepageimage4bgrm.png"))
        self.image_label.setScaledContents(True)
        
        self.button = QPushButton("<", self)
        self.button.setGeometry(1050, 310, 40, 40)
        self.button.clicked.connect(self.nextImage)
        self.button.setStyleSheet("QPushButton{ background: transparent; position: fixed;border-radius:15px;color: black;}")
        self.button.setFont(QFont('Times', 25))


        self.button2 = QPushButton(">", self)
        self.button2.setGeometry(1800, 310, 60, 60)
        self.button2.clicked.connect(self.nextImage)
        self.button2.setStyleSheet("QPushButton{ background: transparent; position: fixed; color: black;}")
        self.button2.setFont(QFont('Times', 25))

    #-----------------------------FOOTER--------------------------------------#
    
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


        self.current_image = 0
        self.showMaximized()


    def updateImage(self, value):
        if value == 0:
            self.image_label.setPixmap(QPixmap("D:\python mpr final\Python-MPR-\Homepage\homepagebanner1.png"))
            self.current_image = 0
        elif value == 1:
            self.image_label.setPixmap(QPixmap("D:\python mpr final\Python-MPR-\images\homepageimage2bgrm.png"))
            self.current_image = 1
        elif value == 2:
            self.image_label.setPixmap(QPixmap("D:\python mpr final\Python-MPR-\Homepage\homepageimage4bgrm.png"))
            self.current_image = 2
        elif value == 3:
            self.image_label.setPixmap(QPixmap("D:\python mpr final\Python-MPR-\images\homepageimage5bgrm.png"))
            self.current_image = 3
    
    def nextImage(self):
        self.current_image = (self.current_image + 1) % 4
        self.updateImage(self.current_image)
    
    def institute(self):
        # subprocess.Popen(["python", "loginpage\institutelogin.py"])
        window.close()
        process.start("python", ["loginpage\institutelogin.py"])
        process.waitForFinished()
        process.close()
        
        # os.system("python loginpage\institutelogin.py &")
        # os.close(1)


    def student(self):
        window.close()
        process.start("python",["loginpage\studentlogin.py"])
        process.waitForFinished()
        process.close()
        

        



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())