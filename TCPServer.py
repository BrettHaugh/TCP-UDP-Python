#TCP Server
from socket import *

welcomeSocket = socket(AF_INET, SOCK_STREAM) #for all clients to connect
serverPort = 13001 #use same port number as defined in the client
welcomeSocket.bind(("", serverPort)) #connect to the port on localhost
welcomeSocket.listen(1) #how many connections we can have at our welcome socket
print("Server Ready")

while True: #keeps server running at all times
    connectionSocket, address = welcomeSocket.accept() #create connection to the client
    #create connection to client
    message = connectionSocket.recv(2048)
    print("Old Message: ",message)
    modMessage = message.upper() #convert message to uppercase
    print("New Message: ",modMessage)
    connectionSocket.send(modMessage) #send back to client
    connectionSocket.close()