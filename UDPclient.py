from socket import *
servername = '127.0.0.1'
serverhost = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
message = input('Input:')
while(message!='close'):
    clientSocket.sendto(message.encode('utf-8'),(servername,serverhost))
    newmessage,adr = clientSocket.recvfrom(2048)
    print (newmessage)
    message = input('Input:')
clientSocket.close()
