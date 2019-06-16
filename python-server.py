import socket
import time
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding

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

with open("private_key.pem", "rb") as key_file:
	private_key = serialization.load_pem_private_key(
		key_file.read(),
		password=None,
		backend=default_backend()
	)



while running:
	encrypted_message = clientsocket.recv(1024)#.decode()

	decrypted_message = private_key.decrypt(
	encrypted_message,
	padding.OAEP(
		mgf=padding.MGF1(algorithm=hashes.SHA1()),
		algorithm=hashes.SHA1(),
		label=None
	)
)
	print(encrypted_message)
	print(decrypted_message)
	
