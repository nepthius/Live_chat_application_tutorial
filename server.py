import socket

HOST = '172.16.42.78'
PORT = 9090

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))

server.listen(5)

while True:
    communication_socket, address = server.accept()
    print(f"Connected to {address}")
    message = communication_socket.recv(1024).decode('utf-8')
    print(f"Message from the clinet is {message}")
    communication_socket.send(f"Message has been succesfully recieved!".encode('utf-8'))
    communication_socket.close()
    print(f"Communication with {address} has been terminated")