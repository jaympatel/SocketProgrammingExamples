"""

Jay Patel
jmp840
N10541249

SMTP Client Code

"""

from socket import *
import ssl
import base64


msg = "\r\nI love computer networks !!"
endmsg = "\r\n.\r\n"

# Mail server details
mailServer = "smtp.gmail.com"
mailServerPort = 587


# Create a SMTP connection with the mail server
clientSocket = socket(AF_INET, SOCK_STREAM)                         
clientSocket.connect((mailServer,mailServerPort))
recv=clientSocket.recv(1024)
print recv
if recv[:3]!="220":
	print "Error! 220 reply not received from server."


# Send HELO command and print server response.
heloCommand="HELO localhost\r\n"
clientSocket.send(heloCommand)
recv1=clientSocket.recv(1024)
print recv1
if recv1[:3]!="250":
	print "Error! 250 reply not received from server."

# Send STARTTLS command to start SSL connection with Gmail SMTP server.
clientSocket.send("STARTTLS\r\n")
recv2 = clientSocket.recv(1024)
print recv2
if recv2[:3] != "220":
	print "Error! 220 reply not received from server."

# Wrap simple clientSocket to SSL.
clientSocketSSL = ssl.wrap_socket(clientSocket)


# Send HELO command again after SSL handshake.
clientSocketSSL.send(heloCommand)
recv1=clientSocketSSL.recv(1024)
print recv1
if recv1[:3] != "250":
	print "Error! 250 reply not received from server."


# Send AUTH command to authenticate with the Gmail server and print sesrver response.

userName="jmp840@nyu.edu"                     # To test the program in these two lines replace your username
password="password_goes_here"                 # and password

clientSocketSSL.send("AUTH LOGIN "+base64.b64encode(userName)+"\r\n")
recv1=clientSocketSSL.recv(1024)
print recv1
if recv1[:3] != "334":
	print "Error! 334 reply not received from server."


# Send respective Gmail password for the account and print server response.
clientSocketSSL.send(base64.b64encode(password)+"\r\n")
recv1=clientSocketSSL.recv(1024)
print recv1
if recv1[:3] != "235":
	print "Authentication Error! 235 reply not received from server."


# Send MAIL FROM command and print server response.
clientSocketSSL.send("MAIL FROM: <"+userName+">\r\n")
recv1 = clientSocketSSL.recv(1024)
print recv1
if recv1[:3] != "250":
	print "Error! 250 reply not received from server."


# Send RCPT TO command and print server response.
mailToAddress="jaympatel567@gmail.com"
clientSocketSSL.send("RCPT TO:<"+mailToAddress+">\r\n")
recv1 = clientSocketSSL.recv(1024)
print recv1
if recv1[:3] != "250":
	print "Error! 250 reply not received from server."


# Send DATA command and print server response.
clientSocketSSL.send("DATA\r\n")
recv1 = clientSocketSSL.recv(1024)
print recv1
if recv1[:3] != "354":
	print "Error! 250 reply not received from server."


# Send message data.
clientSocketSSL.send(msg)


# Message ends with a single period. Send that and print server response
clientSocketSSL.send(endmsg)
recv1 = clientSocketSSL.recv(1024)
print recv1
if recv1[:3] != "250":
        print "Error! 250 reply not received from server."

# Send QUIT command and get server response.
clientSocketSSL.send("QUIT\r\n")
clientSocketSSL.close()
