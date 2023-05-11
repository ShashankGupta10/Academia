import socket
import threading
from PyQt5.QtWidgets import *
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
import sys
import os

HOST = socket.gethostbyname(socket.gethostname())
PORT = 5555



class Announcements(QMainWindow):            
    def __init__(self):
        super().__init__()
        
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
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


        icon = QIcon("D:\Pyfon MPR\TkinterGUI\images\homepageimage1bgrm.png")
        self.btn10 = QPushButton("" ,self)
        self.btn10.setGeometry(1800, 0, 100, 100)
        self.btn10.setStyleSheet("background : black;")
        self.btn10.setIcon(icon)
        size = QSize(100, 100)
        self.btn10.setIconSize(size)
        
        
        self.loginbox = QLabel(self)
        self.loginbox.setGeometry(0,100,120,800)
        self.loginbox.setStyleSheet("background-color: #3E54AC;")
        
        sidebar = QLabel(self)
        sidebar.setGeometry(0,100,80,1920)
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

        
        self.chatbox = QLabel(self)
        self.chatbox.setGeometry(120,100,400,800)
        self.chatbox.setStyleSheet("background-color: #fff; border-right: 1px solid;")
        
        self.announcements = QLabel("Announcements", self)
        self.announcements.setStyleSheet("border-bottom: 2px solid black")
        self.announcements.setGeometry(200, 120, 250, 80)
        self.announcements.setFont(QFont('Times', 20))
        
        backbtn = QToolButton(self.chatbox)
        backbtn.setArrowType(Qt.LeftArrow)        
        backbtn.setGeometry(0,40,50,50)
        backbtn.setStyleSheet("QToolButton{ background:  transparent; color: #301E67}")
        backbtn.clicked.connect(self.back)
        
        self.active_chat = 0
        
        self.chat1 = QPushButton("IT Department", self)
        self.chat1.setStyleSheet("QPushButton { border: 1px solid black; border-left: none;}"
                                 "QPushButton:hover{ background: lightblue; border: 1px solid black;}")
        self.chat1.setGeometry(120, 200, 400, 100)
        self.chat1.setFont(QFont('Times', 12))
        self.chat1.clicked.connect(lambda: self.switchChat(0))
        
        
        
        self.chat2 = QPushButton("S1 IT", self)
        self.chat2.setStyleSheet("QPushButton { border: 1px solid black; border-left: none;}"
                                 "QPushButton:hover{ background: lightblue; border: 1px solid black;}")
        self.chat2.setGeometry(120, 300, 400, 100)
        self.chat2.setFont(QFont('Times', 12))
        # self.chat2.clicked.connect(lambda: self.switchChat(1))
        # self.chat2.clicked.connect(self.connect)
        
        # self.chat3 = QPushButton("S2 IT", self)
        # self.chat3.setStyleSheet("QPushButton { border: 1px solid black; border-left: none;}"
        #                          "QPushButton:hover{ background: lightblue; border-left: 1px solid black;}")
        # self.chat3.setGeometry(120, 400, 400, 100)
        # self.chat3.setFont(QFont('Times', 12))
        # self.chat3.clicked.connect(lambda: self.switchChat(2))
        # self.chat3.clicked.connect(self.connect)
        
        
        chat_icon = QIcon('images/chat-user.png')
        self.principal_icon = QPushButton("" ,self)
        self.principal_icon.setStyleSheet("border: none")
        self.principal_icon.setGeometry(150,210, 80, 80)
        self.principal_icon.setIcon(chat_icon)
        size = QSize(50, 50)
        self.principal_icon.setIconSize(size)
        
        self.hod_icon = QPushButton("" ,self)
        self.hod_icon.setStyleSheet("border: none")
        self.hod_icon.setGeometry(150,310, 80, 80)
        self.hod_icon.setIcon(chat_icon)
        size = QSize(50, 50)
        self.hod_icon.setIconSize(size)
        
        # self.teacher_icon = QPushButton("" ,self)
        # self.teacher_icon.setStyleSheet("border: none")
        # self.teacher_icon.setGeometry(150,410, 80, 80)
        # self.teacher_icon.setIcon(chat_icon)
        # size = QSize(50, 50)
        # self.teacher_icon.setIconSize(size)



        # Messages displayed here
        self.message_box = QTextEdit(self)
        self.message_box.setFont(QFont('Times', 15))
        self.message_box.setStyleSheet("background-color: #ECF2FF; color: black")
        self.message_box.setGeometry(520, 100, 1400, 800)
        self.message_box.setReadOnly(True)
        # self.message_box.setVisible(True)
        
        self.message_box1 = QTextEdit(self)
        self.message_box1.setFont(QFont('Times', 15))
        self.message_box1.setStyleSheet("background-color: #ECF2FF; color: black")
        self.message_box1.setGeometry(520, 100, 1400, 800)
        self.message_box1.setReadOnly(True)
        self.message_box1.setVisible(False)
        
        # self.message_box2 = QTextEdit(self)
        # self.message_box2.setFont(QFont('Times', 15))
        # self.message_box2.setStyleSheet("background-color: white; color: black")
        # self.message_box2.setGeometry(520, 200, 1400, 550)
        # self.message_box2.setReadOnly(True)
        # self.message_box2.setVisible(False)

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

        
        self.showMaximized()
        self.show()
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((HOST, PORT))
        print("ghdfghgs")
        def receive():
            while True:
                # receive data from the server
                data = s.recv(1024)
                print("mo")
                if not data:
                    break
                print(data.decode())
                self.add_message(data.decode())

        # start a separate thread to receive messages
        threading.Thread(target=receive).start()
        
    def switchChat(self, chat_num):
        global username
        chat_boxes = [self.message_box]
        for i, box in enumerate(chat_boxes):
            if i == chat_num:
                box.setVisible(True)
                return
            else:
                box.setVisible(False)

        self.active_chat = chat_num


        

        # self.username_button.setDisabled(False)


        
        
    def add_message(self, message):
        if self.active_chat == 0:
            message_box = self.message_box
        else:
            return
          
        message_box.moveCursor(QTextCursor.End)
        message_box.insertPlainText(message + '\n')
        message_box.moveCursor(QTextCursor.End)

        
    # def send_message(self):
    #     message = self.message_textbox.text()
    #     if message != '':
    #         if self.active_chat == 0:
    #             self.client.sendall(message.encode('utf-8'))
    #         elif self.active_chat == 1:
    #             self.client.sendall(message.encode('utf-8'))
    #         elif self.active_chat == 2:
    #             self.client.sendall(message.encode('utf-8'))
    #         self.message_textbox.clear()
    #     else:
    #         QMessageBox.critical(self, "Empty message", "Message cannot be empty")

            
    # def listen_for_messages_from_server(self, client):
    #     while True:
    #         message = client.recv(2048).decode('utf-8')
    #         print(f"Received message from client: {message}")
    #         if message != '':
    #             username = message
    #             content = message
    #             print(f"Username: {username}, Content: {content}")
    #             self.add_message(f"  {content}")
    #         else:
    #             QMessageBox.critical(self, "Error", "Message received from client is empty")
    #             break

    # create a socket objecthgsjdgfsj

        # create a socket object


   
                    
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
        os.system("python reshalasell.py &") 
    def sprofile(self):
        window.close()
        os.system("python profilestudent.py &")
    def back(self):
        window.close()
        os.system("python Studentdashboard.py &") 

App = QApplication(sys.argv)
window = Announcements()
sys.exit(App.exec())