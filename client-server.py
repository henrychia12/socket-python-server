import socket
import os
from cryptography.fernet import Fernet

s = socket.socket()

path = os.path.join(os.path.expanduser("~"), ".ssh", "id_rsa.pub")
public_key_file = open(path, "rb")
public_key = public_key_file.read()

hostname = "henrylaptop"
port = 8000

s.connect((hostname,port))

while True:
	x = raw_input("Enter message: ")
	s.send(x.encode() + "\n")
	s.send(public_key.encode())
	
