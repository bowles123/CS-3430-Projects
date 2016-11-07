# Brian Bowles, Assignment 7, March 3, 2015.
import socket

## 1. construct a client socket object.
client_socket = socket.socket()

## 2. specify the host name
host = socket.gethostname()
## 3. specify the port
port = 20005

## 4. connect to the host on the port
client_socket.connect((host, port))

## 5. print the server response.
##    1024 bytes
client_socket.send(str(30))
print client_socket.recv(1024)
