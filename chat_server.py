# import socket
# import threading

# # Change these values as per your requirements
# HOST = '192.168.0.106'
# PORTS = [9996, 9997, 9998]

# # List of all connected clients
# active_clients = []

# # Maximum number of clients that can connect to the server
# LISTENER_LIMIT = 5

# # Function to listen for incoming messages from a client
# def listen_for_messages(client, username):

#     while True:
#         try:
#             message = client.recv(2048).decode('utf-8')
#             if not message:
#                 break

#             final_msg = username + ': ' + message
#             send_messages_to_all(final_msg)
#         except:
#             break

#     print(f"Client {username} disconnected")
#     client.close()

# # Function to send a message to a single client
# def send_message_to_client(client, message):
#     client.sendall(message.encode())

# # Function to send a new message to all connected clients
# # Function to send a new message to all connected clients
# def send_messages_to_all(message):
#     for user in active_clients[:]:
#         try:
#             send_message_to_client(user[1], message)
#         except:
#             print(f"Client {user[0]} disconnected")
#             active_clients.remove(user)


# # Function to handle a client connection
# def client_handler(client):

#     # Prompt the client for their username
#     username = 'Arun Kulkarni'
#     # client.sendall("Enter your username: ".encode())
#     # username = client.recv(2048).decode('utf-8')

#     # Add the client to the list of active clients
#     active_clients.append((username, client))

#     # Notify other clients that a new user has joined the chat
#     prompt_message = "SERVER: " + f"{username} has joined the chat"
#     send_messages_to_all(prompt_message)

#     # Start a new thread to listen for incoming messages from the client
#     threading.Thread(target=listen_for_messages, args=(client, username, )).start()

# # Main function to start the server
# def main():

#     # Create a socket object for each port
#     sockets = []
#     for port in PORTS:
#         sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         try:
#             # Bind the socket to the host and port
#             sock.bind((HOST, port))
#             sockets.append(sock)
#             print(f"Socket bound to {HOST} on port {port}")
#         except socket.error as e:
#             print(f"Error binding socket to {HOST} on port {port}: {e}")
#             continue

#         # Start listening for incoming connections
#         sock.listen(LISTENER_LIMIT)

#     # Accept incoming connections and handle each one in a new thread
#     while True:
#         for sock in sockets:
#             conn, addr = sock.accept()
#             print(f"Connected by {addr} on port {sock.getsockname()[1]}")
#             threading.Thread(target=client_handler, args=(conn, )).start()

# if _name_ == '_main_':
#     main()




import socket

HOST = socket.gethostbyname(socket.gethostname()) # all available interfaces
PORT = 5555

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(2) # listen for up to 2 clients

print('Waiting for clients...')

# accept client connections
conn1, addr1 = s.accept()
print(f'Connected to {addr1}')

conn2, addr2 = s.accept()
print(f'Connected to {addr2}')

# start the chat loop
while True:
    # receive message from client 1
    data = conn1.recv(1024)
    if not data:
        break
    print(f'{addr1}: {data.decode()}')
    # send message to client 2
    conn2.sendall(data)

# close the connections
conn1.close()
conn2.close()