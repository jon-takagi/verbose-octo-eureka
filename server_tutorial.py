# server.py
import socket
import time

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = ''

port = 42069

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

while True:
	clientsocket,addr = serversocket.accept()
	print(str(addr))
	tm = clientsocket.recv(1024)
	clientsocket.send("Hello, World!".encode('ascii'))
	print(tm.decode())
	clientsocket.close()
    # establish a connection
	# print("Got a connection from %s" % str(addr))
	# tm = s.recv(1024)
	# clientsocket.send("Hello, world!".encode('ascii'))
	# print(tm.decode())
	# clientsocket.close()
