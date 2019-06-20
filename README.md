# Python Server with Socket
Socket programming allows two nodes on a network to communicate with one another. An encrypted message will be sent from the client server, and decrypted on the host server using the authroised public key.
## Installation
Use the package manager apt to install python-pip
```bash
apt install python-pip
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install cryptography
```bash
pip install cryptography
```
## Usage
```bash
python key_generator.py
```
Creating a private key.

```bash
python python-server.py
```
Start up host server.

```bash
python client-server.py
```
Start up client server. 
