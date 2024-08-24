#TCP Client
from socket import *

clientSocket = socket(AF_INET, SOCK_STREAM) #set up a TCP socket
serverName = "localhost"
serverPort = 13001
clientSocket.connect((serverName, serverPort)) #set up connection to server
message = input("Enter lowercase sentence: ").encode() #read data, convert to bytes
clientSocket.send(message) #send message across connection
modMessage = clientSocket.recv(2048) #pull data from connection
print("New Message: ",modMessage.decode()) #print decoded string
clientSocket.close() #close socket

