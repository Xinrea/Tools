from socket import *
import threading

def sendmessage():
    while 1:
        message = input('me:')
        socketClient.sendto(message.encode('utf-8'),(serverName,serverPort))

def recmessage():
    while 1:
        newmessage,adr = socketServer.recvfrom(2048)
        print('he:'+newmessage.decode('utf-8'))

threads = []
t1 = threading.Thread(target = sendmessage,)
threads.append(t1)
t2 = threading.Thread(target = recmessage,)
threads.append(t2)

if __name__ == '__main__':
    serverName = input('Input IP:')
    serverPort = int(input('Input Port:'))
    port = int(input('port:'))
    socketClient = socket(AF_INET,SOCK_DGRAM)
    socketServer = socket(AF_INET,SOCK_DGRAM)
    socketServer.bind(('',port))
    t1.setDaemon(True)
    t1.start()
    t2.setDaemon(True)
    t2.start()
    t2.join()
    
