from datetime import datetime
from socket import *

# Server details
serverName='localhost'
serverPort = 12000

# Create the UDP client socket
clientS = socket(AF_INET, SOCK_DGRAM)

# Set maximum ping coount
maxPingCount = 10
ping = 1

print 'Beginning the connection..' , maxPingCount , 'pings'
print '-----------------------------------------------------------'

while ping<=maxPingCount:
    message = 'Ping   ' + str(ping)   
    ping +=1
    # Packet sent time
    sentTime = datetime.now()
    # Send the UDP packet with the message
    clientS.sendto(message,(serverName,serverPort))
    # Set the request timeout
    clientS.settimeout(1)
    
    print 'Sent Message : ' + message + '   ' + str(sentTime)
    try:
        # Listen for server to respond
        modifiedMessage,serverAddress = clientS.recvfrom(1024)
        # Packet received time
        receivedTime = datetime.now()
        # Calculate the round trip time 
        rtt = sentTime-receivedTime
        # Print the response from the server
        print 'Received Message : '+ modifiedMessage + '   ' + str(receivedTime)
        print 'Round Trip Time : ' ,rtt.microseconds
    except timeout:
        print 'Last Request timed out!'
    print '-----------------------------------------------------------'

clientS.close()
print 'Number of pings exhausted!!'
