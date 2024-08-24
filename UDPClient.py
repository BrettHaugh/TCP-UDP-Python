# Code for UDP Client
from socket import *

clientSocket = socket(AF_INET, SOCK_DGRAM) # creates our UDP socket
serverName = "localhost" # indicates that the server is running on the same machine
serverPort = 12001 # choose a port number with no conflicts (same number that server chooses)

# message = bytes(input("Enter lowercase message: "), "utf-8")
message = input("Enter lowercase message: ").encode()
# read message from the user and convert it into bytes

clientSocket.sendto(message, (serverName, serverPort))
modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print("Modified Message: ",modifiedMessage.decode())
clientSocket.close() # shut down our socket