import cv2
import numpy as np
import socket
import sys
import pickle
import struct

cap=cv2.VideoCapture(0)
clientsocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
clientsocket.connect(('192.168.237.156',9999))

data = b''
payload_size = struct.calcsize("L") ### CHANGED


while True:

    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    ret,frame=cap.read()
    
    # Serialize frame
    data = pickle.dumps(frame)

    # Send message length first
    message_size = struct.pack("L", len(data)) ### CHANGED
    # frame_data = data[:message_size]
    # data = data[message_size:]


    # Then data
    clientsocket.sendall(message_size + data)
    
    cv2.imshow('frame', frame)
    cv2.waitKey(1)