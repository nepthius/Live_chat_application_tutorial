import socket

HOST = '172.16.42.78'
PORT = 9090

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST,PORT))

message = input("Enter your message: ")

socket.send(message.encode('utf-8'))
print(socket.recv(1024).decode('utf-8'))