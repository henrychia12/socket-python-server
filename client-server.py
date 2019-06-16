import socket
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import padding

s = socket.socket()

with open("private_key.pem", "rb") as key_file:
	private_key = serialization.load_pem_private_key(
		key_file.read(),
		password=None,
		backend=default_backend()
	)
	
public_key = private_key.public_key()

hostname = "henrylaptop"
port = 8000

s.connect((hostname,port))

while True:
	message = raw_input("Enter message: ")
	
	ciphertext = public_key.encrypt(
	message,
	padding.OAEP(
		mgf = padding.MGF1(algorithm=hashes.SHA1()),
		algorithm = hashes.SHA1(),
		label = None
	)
)
	s.send(ciphertext)

