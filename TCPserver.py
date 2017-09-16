from socket import *
serverPort = 12000
serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('',serverPort))
serverSocket.listen(1)
while 1:
	newSocket,adr = serverSocket.accept()
	message = newSocket.recv(1024)
	while(message):
		print(message)
