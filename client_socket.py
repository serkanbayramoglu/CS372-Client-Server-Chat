# Author:       Serkan Bayramoglu  
# Email:        bayramos@oregonstate.edu
# Date:         4 Dec 2022
# Description:  This client program connects to the server to enable communication between the
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

# 1. The client creates a socket and connects to ‘localhost’ and port xxxx
clientSocket = socket(AF_INET, SOCK_STREAM)         
clientSocket.connect((serverName,serverPort))       

print("Connected to: ",serverName,"on port: ",serverPort)

running = True                                      # to control the loop

print("Please type /q to quit or write your message after prompt!")

while running == True:
    running_2 = True                                # used to read the received messages until chr(4) is read
    receivedData = ""

    # 2. When connected, the client prompts for a message to send
    inputText = input("> ")

    # 3. If the message is /q, the client quits
    if inputText == '/q':
        running = False
        print("Connection ended")
        running_2 = False
        
    inputText += chr(4)

    # 4. Otherwise, the client sends the message
    clientSocket.send(inputText.encode())           # sending the message in all case, if '/q' is sent, the server will close its connection

    # 5. The client calls recv to receive data
    while running_2 == True:
        receivedText = clientSocket.recv(10).decode()   # receiving the responses and collecting in a variable
        receivedData += receivedText
        if receivedText[-1] == chr(4):
            running_2 = False

    if receivedData[:-1] == '/q':
        running = False
        receivedData = ""
        print("Connection ended by the counterpart")
        break

    if len(receivedData) > 0:
        # 6. The client prints the data
        print (receivedData[:-1])                

    # 7. Back to step 2

# 8. Sockets are closed (can use with in python3)
clientSocket.close()                                  # connection closed