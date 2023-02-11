import pickle
import socket
import struct

import cv2

HOST = '192.168.237.156'
PORT = 9999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print('Socket created')

s.bind((HOST, PORT))
print('Socket bind complete')
s.listen(10)
print('Socket now listening')

conn, addr = s.accept()

data = b'' ### CHANGED
payload_size = struct.calcsize("L") ### CHANGED

while True:

    # Retrieve message size
    while len(data) < payload_size:
        data += conn.recv(20480)

    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack("L", packed_msg_size)[0] ### CHANGED

    # Retrieve all data based on message size
    while len(data) < msg_size:
        data += conn.recv(20480)

    frame_data = data[:msg_size]
    data = data[msg_size:]

    # Extract frame
    frame = pickle.loads(frame_data)

    # Display
    cv2.imshow('videomeet', frame)
    cv2.waitKey(1)

#from tqdm import tqdm
#import requests

#url = "http://download.thinkbroadband.com/10MB.zip"
#response = requests.get(url, stream=True)

#with open("10MB", "wb") as handle:
 #   for data in tqdm(response.iter_content()):
  #      handle.write(data)
