from socket import *
serverport = 12000
serverSocket = socket(AF_INET,SOCK_DGRAM)
serverSocket.bind(('',serverport))
while 1:
    message,adr = serverSocket.recvfrom(2048)
    print (message)
    newmessage = 'hello'
    serverSocket.sendto(newmessage.encode('utf-8'),adr)
