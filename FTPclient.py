from socket import *
serverName = '222.20.104.175'
serverPort = 21
cmdSocket = socket(AF_INET,SOCK_STREAM)
cmdSocket.connect((serverName,serverPort))
fileSocket = socket(AF_INET,SOCK_STREAM)

newmessage = cmdSocket.recv(1024)
print(newmessage.decode('ascii'))
cmdSocket.send('USER anonymous\r\n'.encode('ascii'))

newmessage = cmdSocket.recv(1024)
print(newmessage.decode('ascii'))
cmdSocket.send('PASS \r\n'.encode('ascii'))

newmessage = cmdSocket.recv(1024)
print(newmessage.decode('ascii'))
cmdSocket.send('PASV \r\n'.encode('ascii'))

newmessage = cmdSocket.recv(1024)
print(newmessage.decode('ascii'))
cmdSocket.send('LIST \r\n'.encode('ascii'))

dataPort_str = newmessage.decode('ascii')[newmessage.find(','.encode('ascii'),39)+1:newmessage.find(')'.encode('ascii'))]
dataPort = 256*int(dataPort_str[0:dataPort_str.find(',')])+int(dataPort_str[dataPort_str.find(',')+1:])
fileSocket.connect((serverName,dataPort))
newmessage = fileSocket.recv(1024)
print(newmessage)

cmdSocket.close()
fileSocket.close()