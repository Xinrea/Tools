from socket import *
serverName = '222.20.104.175'
serverPort = 21
cmdSocket = socket(AF_INET,SOCK_STREAM)
cmdSocket.connect((serverName,serverPort))
fileSocket = socket(AF_INET,SOCK_STREAM)
fileSocket.bind(('',12000))
newmessage = cmdSocket.recv(1024)
print(newmessage.decode('ascii'))
cmdSocket.send('USER anonymous\r\n'.encode('ascii'))

newmessage = cmdSocket.recv(1024)
print(newmessage.decode('ascii'))
cmdSocket.send('PASS \r\n'.encode('ascii'))

newmessage = cmdSocket.recv(1024)
print(newmessage.decode('ascii'))
cmdSocket.send('PORT 222,20,104,175,46,224 \r\n'.encode('ascii'))

fileSocket.listen(1)
newmessage = cmdSocket.recv(1024)
print(newmessage.decode('ascii'))
cmdSocket.send('LIST \r\n'.encode('ascii'))

newSocket,adr = fileSocket.accept()
newmessage = newSocket.recv(1024)
print(newmessage)


cmdSocket.close()
fileSocket.close()