import socket
import threading
from PyQt5.QtWidgets import *
from PyQt5 import QtWidgets,QtCore,QtGui
from PyQt5.QtWidgets import QTabWidget
from PyQt5.QtWidgets import QGraphicsOpacityEffect
from PyQt5.QtGui import * 
from PyQt5.QtCore import *
from PyQt5.QtCore import QPropertyAnimation
from pathlib import Path
from urllib import *
import sys
import os

HOST = ''
PORT = 9999

class Announcements(QMainWindow):            
    def __init__(self):
        super().__init__()
        
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.setWindowTitle("Academia")
        self.setGeometry(0,0,1920,1080)

        self.navbar = QLabel(self)
        self.navbar.setGeometry(0, 0, 1920, 100)
        self.navbar.setStyleSheet("QLabel{ background: black; position: fixed;} ")
        
        self.opacity_effect = QGraphicsOpacityEffect()
        self.opacity_effect.setOpacity(0.3)
  
        self.btn1 = QPushButton("Home" ,self.navbar)
        self.btn1.setGeometry(300, 0, 200, 100)
        self.btn1.setStyleSheet("QPushButton{ background: black; color: white; color: white}")
        self.btn1.setFont(QFont('Times', 20))

        self.btn2 = QPushButton("Nothing" ,self.navbar)
        self.btn2.setGeometry(600, 0, 200, 100)
        self.btn2.setStyleSheet("QPushButton{ background: black; color: white; color: white}")
        self.btn2.setFont(QFont('Times', 20))

        self.btn3 = QPushButton("About Us" ,self.navbar)
        self.btn3.setGeometry(900, 0, 200, 100)
        self.btn3.setStyleSheet("QPushButton{ background: black; color: white; color: #ECF2FF}")
        self.btn3.setFont(QFont('Times', 20))

        self.btn4 = QPushButton("Contact Us" ,self.navbar)
        self.btn4.setGeometry(1200, 0, 200, 100)
        self.btn4.setStyleSheet("QPushButton{ background: black; color: white; color: #ECF2FF}")
        self.btn4.setFont(QFont('Times', 20))
        
        
        self.loginbox = QLabel(self)
        self.loginbox.setGeometry(0,100,120,800)
        self.loginbox.setStyleSheet("background-color: #3E54AC;")
        
        icon = QIcon('')
        self.usernameicon = QPushButton("" ,self)
        self.usernameicon.setGeometry(20,150, 80, 80)
        self.usernameicon.setIcon(icon)
        size = QSize(50, 50)
        self.usernameicon.setIconSize(size)
        
        self.usernameicon = QPushButton("" ,self)
        self.usernameicon.setGeometry(20,300, 80, 80)
        self.usernameicon.setIcon(icon)
        size = QSize(50, 50)
        self.usernameicon.setIconSize(size)
        
        self.usernameicon = QPushButton("" ,self)
        self.usernameicon.setGeometry(20,450, 80, 80)
        self.usernameicon.setIcon(icon)
        size = QSize(50, 50)
        self.usernameicon.setIconSize(size)
        
        self.usernameicon = QPushButton("" ,self)
        self.usernameicon.setGeometry(20,600, 80, 80)
        self.usernameicon.setIcon(icon)
        size = QSize(50, 50)
        self.usernameicon.setIconSize(size)
        
        self.chatbox = QLabel(self)
        self.chatbox.setGeometry(120,100,400,800)
        self.chatbox.setStyleSheet("background-color: #fff; border-right: 1px solid;")
        
        self.announcements = QLabel("Announcements", self)
        self.announcements.setStyleSheet("border-bottom: 2px solid black")
        self.announcements.setGeometry(200, 120, 250, 80)
        self.announcements.setFont(QFont('Times', 20))
        
        self.active_chat = 0
        
        self.chat1 = QPushButton("IT Department", self)
        self.chat1.setStyleSheet("QPushButton { border: 1px solid black; border-left: none;}"
                                 "QPushButton:hover{ background: lightblue; border: 1px solid black;}")
        self.chat1.setGeometry(120, 200, 400, 100)
        self.chat1.setFont(QFont('Times', 12))
        self.chat1.clicked.connect(lambda: self.switchChat(0))
        self.chat1.clicked.connect(self.connect)
        
        
        self.chat2 = QPushButton("S1 IT", self)
        self.chat2.setStyleSheet("QPushButton { border: 1px solid black; border-left: none;}"
                                 "QPushButton:hover{ background: lightblue; border: 1px solid black;}")
        self.chat2.setGeometry(120, 300, 400, 100)
        self.chat2.setFont(QFont('Times', 12))
        self.chat2.clicked.connect(lambda: self.switchChat(1))
        # self.chat2.clicked.connect(self.connect)
        
        self.chat3 = QPushButton("S2 IT", self)
        self.chat3.setStyleSheet("QPushButton { border: 1px solid black; border-left: none;}"
                                 "QPushButton:hover{ background: lightblue; border-left: 1px solid black;}")
        self.chat3.setGeometry(120, 400, 400, 100)
        self.chat3.setFont(QFont('Times', 12))
        self.chat3.clicked.connect(lambda: self.switchChat(2))
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
        
        self.teacher_icon = QPushButton("" ,self)
        self.teacher_icon.setStyleSheet("border: none")
        self.teacher_icon.setGeometry(150,410, 80, 80)
        self.teacher_icon.setIcon(chat_icon)
        size = QSize(50, 50)
        self.teacher_icon.setIconSize(size)
        
        
        # self.username_label = QLabel("Username", self)
        # self.username_label.setGeometry(540, 150, 150, 40)
        # self.username_label.setFont(QFont('Times', 15))

        # self.username_textbox = QLineEdit(self)
        # self.username_textbox.setStyleSheet("background-color: white; color: black; border-radius: 5px")
        # self.username_textbox.setGeometry(700, 150, 300, 40)
        # self.username_textbox.setFont(QFont('Times', 12))

        self.username_button = QPushButton("Make an Announcement", self)
        self.username_button.setFont(QFont('Times', 12))
        self.username_button.setStyleSheet("background-color: #464EB8; color: white; border-radius: 20px")
        self.username_button.setGeometry(700, 150, 400, 40)
        # self.username_button.clicked.connect(self.connect)

        self.label2 = QLabel(self)
        self.label2.setGeometry(520, 750, 1400, 100)
        self.label2.setStyleSheet("background-color: lightblue; border-top: 2px solid black")
        
        # Type messages here
        self.message_textbox = QLineEdit(self)
        self.message_textbox.setFont(QFont('Times', 12))
        self.message_textbox.setStyleSheet("background-color: white; color: black; border-radius: 5px")
        self.message_textbox.setGeometry(580, 780, 1200, 40)
        self.message_textbox.returnPressed.connect(self.send_message)

        # Send Button
        send_icon = QIcon('images/send-icon.png')
        self.message_button = QPushButton("", self)
        self.message_button.setStyleSheet("border: none;")
        # self.message_button.setFont(QFont('Times', 12))
        # self.message_button.setStyleSheet("background-color: #464EB8; color: white; border-radius: 20px")
        self.message_button.setIcon(send_icon)
        self.message_button.setGeometry(1800, 775, 50, 50)
        size = QSize(50, 50)
        self.message_button.setIconSize(size)
        self.message_button.clicked.connect(self.send_message)

        # Messages displayed here
        self.message_box = QTextEdit(self)
        self.message_box.setFont(QFont('Times', 15))
        self.message_box.setStyleSheet("background-color: white; color: black")
        self.message_box.setGeometry(520, 200, 1400, 550)
        self.message_box.setReadOnly(True)
        # self.message_box.setVisible(True)
        
        self.message_box1 = QTextEdit(self)
        self.message_box1.setFont(QFont('Times', 15))
        self.message_box1.setStyleSheet("background-color: white; color: black")
        self.message_box1.setGeometry(520, 200, 1400, 550)
        self.message_box1.setReadOnly(True)
        self.message_box1.setVisible(False)
        
        self.message_box2 = QTextEdit(self)
        self.message_box2.setFont(QFont('Times', 15))
        self.message_box2.setStyleSheet("background-color: white; color: black")
        self.message_box2.setGeometry(520, 200, 1400, 550)
        self.message_box2.setReadOnly(True)
        self.message_box2.setVisible(False)

        self.footer = QLabel(self)
        self.footer.setGeometry(0, 900, 1920, 100)
        self.footer.setStyleSheet("QLabel{ background: black; position: fixed;} ")

        self.label6 = QPushButton(self.footer)
        self.label6.setGeometry(1750,0,150,100)
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
        
    def switchChat(self, chat_num):
        chat_boxes = [self.message_box, self.message_box1, self.message_box2]
        for i, box in enumerate(chat_boxes):
            if i == chat_num:
                box.setVisible(True)
            else:
                box.setVisible(False)
        
        self.active_chat = chat_num
        # self.username_button.setDisabled(False)
        
        
    def add_message(self, message):
        if self.active_chat == 0:
            message_box = self.message_box
        elif self.active_chat == 1:
            message_box = self.message_box1
        elif self.active_chat == 2:
            message_box = self.message_box2
        else:
            return
            
        message_box.moveCursor(QTextCursor.End)
        message_box.insertPlainText(message + '\n')
        message_box.moveCursor(QTextCursor.End)
    
    def connect(self):
        # try except block
        try:
            # Connect to the server
            self.client.connect((HOST, PORT))
            print("Successfully connected to server")
            # self.add_message("[SERVER] Successfully connected to the server")
        except:
            QMessageBox.critical(self, "Unable to connect to server", f"Unable to connect to server {HOST} {PORT}")
            return
        username = 'Arun Kulkarni'
        if username != '':
            self.client.sendall(username.encode())
        else:
            QMessageBox.critical(self, "Invalid username", "Username cannot be empty")
            return
        threading.Thread(target=self.listen_for_messages_from_server, args=(self.client, )).start()
        # self.username_textbox.setDisabled(True)
        # self.username_button.setDisabled(True)
        
    def send_message(self):
        message = self.message_textbox.text()
        if message != '':
            if self.active_chat == 0:
                self.client.sendall(message.encode())
            elif self.active_chat == 1:
                self.client.sendall(message.encode())
            elif self.active_chat == 2:
                self.client.sendall(message.encode())
            self.message_textbox.clear()
        else:
            QMessageBox.critical(self, "Empty message", "Message cannot be empty")

            
    def listen_for_messages_from_server(self, client):
        while 1:
            message = client.recv(2048).decode('utf-8')
            if message != '':
                username = message.split("~")[0]
                content = message.split('~')[1]
                self.add_message(f"  {content}")
            else:
                QMessageBox.critical(self, "Error", "Message received from client is empty")
                break


App = QApplication(sys.argv)
App.setStyleSheet("QMainWindow{background-color: #EBC7E6 }")
window = Announcements()
sys.exit(App.exec())
