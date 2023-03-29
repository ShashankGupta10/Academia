import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setGeometry(0, 0, 1366, 768)
        self.setWindowTitle("Academia")

        self.header = QLabel(self)
        self.header.setGeometry(0, 0, 1920, 100)
        self.header.setStyleSheet("QLabel{ background: black; position: fixed;} ")

        self.label4 = QLabel(self)
        self.label4.setGeometry(20, 20, 80, 70)
        self.pixmap = QPixmap("D:\python mpr final\Python-MPR-\Homepage\Ellipse 1.png")
        self.label4.setPixmap(self.pixmap)
        self.pixmap = self.pixmap.scaled(100, 200)

        

        #header buttons
        self.button3 = QPushButton("Home", self)
        self.button3.setGeometry(1000, 31, 150, 40)
        # self.button3.clicked.connect(self.nextImage)
        self.button3.setStyleSheet("QPushButton{ background: Black; position: fixed;border-radius:15px;color: white;}")
        self.button3.setFont(QFont('Times', 20))


        self.button4= QPushButton("About", self)
        self.button4.setGeometry(1200, 31, 150, 40)
        # self.button4.clicked.connect(self.nextImage)
        self.button4.setStyleSheet("QPushButton{ background: Black; position: fixed;border-radius:15px;color: white;}")
        self.button4.setFont(QFont('Times', 20))
        
        self.button6= QPushButton("Reshaala", self)
        self.button6.setGeometry(1400, 31, 150, 40)
        # self.button4.clicked.connect(self.nextImage)
        self.button6.setStyleSheet("QPushButton{ background: Black; position: fixed;border-radius:15px;color: white;}")
        self.button6.setFont(QFont('Times', 20))

        self.button5= QPushButton("whatever", self)
        self.button5.setGeometry(1600, 31, 150, 40)
        # self.button4.clicked.connect(self.nextImage)
        self.button5.setStyleSheet("QPushButton{ background: Black; position: fixed;border-radius:15px;color: white;}")
        self.button5.setFont(QFont('Times', 20))

        icon = QIcon("D:\Pyfon MPR\TkinterGUI\images\homepageimage1bgrm.png")
        self.btn10 = QPushButton("" ,self)
        self.btn10.setGeometry(1800, 0, 100, 100)
        self.btn10.setStyleSheet("background : black;")
        self.btn10.setIcon(icon)
        size = QSize(100, 100)
        self.btn10.setIconSize(size)
        
    
        self.button6 = QPushButton("Student", self)
        self.button6.setGeometry(710, 700, 200, 50)
        self.button6.setStyleSheet("QPushButton{ background: #C47AFF; position: fixed;border-radius:15px;color: black;border-radius:24px;}"
                                   "QPushButton:hover {border-radius:20px;}")
        self.button6.setFont(QFont('Times', 20))

        self.button7 = QPushButton("Institute", self)
        self.button7.setGeometry(1010, 700, 200, 50)
        self.button7.setStyleSheet("QPushButton{ background: #C47AFF; position: fixed;border-radius:15px;color: black;border-radius:24px;} "
                                   "QPushButton:hover {border-radius:20px;}")
        self.button7.setFont(QFont('Times', 20))

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

        # Apply the shadow effect to the push button
        self.button6.setGraphicsEffect(shadow)
        self.button7.setGraphicsEffect(shadow1)
        
        # Set up the image label

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
        self.tagline.setGeometry(75,250,700,300)
        self.tagline.setStyleSheet("color: black")
        self.tagline.setText("A Better Learning Future Starts Here.")
        self.tagline.setFont(QFont('Helvetica', 20))



        self.image_label = QLabel(self)
        self.image_label.setGeometry(1100, 125, 700, 500)
        self.image_label.setPixmap(QPixmap("D:\python mpr final\Python-MPR-\Homepage\homepageimage4bgrm.png"))
        self.image_label.setScaledContents(True)
        
        # Set up the button
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


        # Set up the current image index
        
        
        
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
        # Update the image label based on the slider value
        if value == 0:
            self.image_label.setPixmap(QPixmap("D:\python mpr final\Python-MPR-\Homepage\homepagebanner1.png"))
            self.current_image = 0
        elif value == 1:
            self.image_label.setPixmap(QPixmap("D:\python mpr final\Python-MPR-\Homepage\homapage banners2.jpg.png"))
            self.current_image = 1
        elif value == 2:
            self.image_label.setPixmap(QPixmap("D:\python mpr final\Python-MPR-\Homepage\homepageimage4bgrm.png"))
            self.current_image = 2

    
    def nextImage(self):
        # Increment the current image index and update the image label
        self.current_image = (self.current_image + 1) % 3
        # self.slider.setValue(self.current_image)
        self.updateImage(self.current_image)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())