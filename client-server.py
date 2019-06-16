import socket
s = socket.socket()

hostname = "henrylaptop"
port = 8000

s.connect((hostname,port))

while True:
	x = raw_input("Enter message: ")
	s.send(x.encode())
	
