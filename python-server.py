import socket
import time

listensocket = socket.socket()
Port = 8000
maxConnections = 999
IP = socket.gethostname()

listensocket.bind(('', Port))

listensocket.listen(maxConnections)
print("Server started at " + IP + " on port " + str(Port))

(clientsocket, address) = listensocket.accept()
print("New connection made!")

running = True

while running:
	message = clientsocket.recv(1024).decode()
	print(message)
	
print("hello world")
