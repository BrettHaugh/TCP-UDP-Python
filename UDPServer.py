# Code for UDP Server
from socket import *

serverSocket = socket(AF_INET, SOCK_DGRAM) # builds ther server
serverPort = 12001 # port number
serverSocket.bind(("", serverPort)) # open socket for others to access

while True:  #sets up an infinite loop to always keep the server open
    print("Server Ready")
    message, clientAddress = serverSocket.recvfrom(2048) #get data from socket
    print("Old Message: ",message)
    modMessage = message.upper() #convert message to uppercase
    print("New Message: ",modMessage)
    serverSocket.send(modMessage) #send back to client
    