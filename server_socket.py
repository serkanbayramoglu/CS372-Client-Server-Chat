# Author:       Serkan Bayramoglu 
# Email:        bayramos@oregonstate.edu
# Date:         4 Dec 2022
# Description:  This server program connects to the client to enable communication between the
#               client and the server. When '/q' is typed by either party, the connection ends 
#               on both client and server. chr(4) is attached to the end of messages, which  
#               indicates end of transmission. There is no limit on the length of the messages.
# Sources:      Kurose and Ross, Computer Networking: A Top-Down Approach, 8th Edition, Pearson 
#               https://www.geeksforgeeks.org/socket-programming-python/
#               https://docs.python.org/3.4/howto/sockets.html 
#               https://realpython.com/python-sockets/


from socket import *

serverName = 'localhost'
serverPort = 12222

# 1. The server creates a socket and binds to ‘localhost’ and port xxxx
serverSocket = socket(AF_INET, SOCK_STREAM)         
serverSocket.bind((serverName,serverPort))         

# 2. The server then listens for a connection
serverSocket.listen(1)                              

print("Server listening on: ",serverName,"on port: ",serverPort)

running = True                                      # used to stop the loop when /q is typed

connectionSocket, connectionAddress = serverSocket.accept()

print("Connected by: ",connectionAddress)

print("Please type /q to quit or write your message after prompt!")

while running == True:
    running_2 = True                                # used to read the received messages until chr(4) is read
    receivedData = ""

    # 3. When connected, the server calls recv to receive data
    while running_2 == True:
        receivedText = connectionSocket.recv(10).decode()
        receivedData += receivedText
        if receivedText[-1] == chr(4):
            running_2 = False

    if receivedData[:-1] == '/q':
        running = False
        receivedData = ""
        print("Connection ended by the counterpart")
        break
        
    if len(receivedData) > 0:
        # 4. The server prints the data, then prompts for a reply
        print(receivedData[:-1])            
        
        inputText = input("> ")

        # 5. If the reply is /q, the server quits
        if inputText == '/q':
            running = False
            print("Connection ended")

        inputText += chr(4)
        
        # 6. Otherwise, the server sends the reply
        connectionSocket.send(inputText.encode())    # in all cases a reply is sent sending "/q" after a new line will be considered as end of communication
    # 7. Back to step 3

# 8. Sockets are closed (can use with in python3)
connectionSocket.close()
serverSocket.close()
