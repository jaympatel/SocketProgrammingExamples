'''
@author: Jay(jmp840-N10541249)
'''


import socket
from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('',1234))
serverSocket.listen(5)
print('Server started...')

while True:
    print 'Ready To Serve...'
    connectionSocket, addr = serverSocket.accept()
    try:
        message = connectionSocket.recv(1024)
        if message:
            filename=message.split()[1]
            print'Requested resource:'+filename
            f=open(filename[1:])
            outputdata=f.read()
            connectionSocket.send('\HTTP/1.1 200 OK\n\n')
            for i in range(0,len(outputdata)):
                connectionSocket.send(outputdata[i])
        connectionSocket.close()
    except IOError:
        print'404 Requested Resource Not Found !!'
        connectionSocket.send('\HTTP/1.1 404 Not Found\n\n')
        connectionSocket.send('404 Requested Resource Not Found !!')
        connectionSocket.close()
        pass
