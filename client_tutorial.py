# client.py
import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
# host = "104.236.213.174"
host = "localhost"
port = 42069

# connection to hostname on the port.
s.connect((host, port))
s.send("test".encode('ascii'))

# Receive no more than 1024 bytes
tm = s.recv(1024)

s.close()

print(tm.decode('ascii'))
