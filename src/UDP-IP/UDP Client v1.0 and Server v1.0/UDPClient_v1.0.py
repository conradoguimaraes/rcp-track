# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 15:32:46 2022

@author: Conrado
"""
#%%
'''
Version: 1.0

What it is: UDP Client

What it does: 
    1) Creates a Socket with certain parameters
    2) Sends a Message inserted by the User at the Terminal
    3) Receives a Message (Server Reply) and prints it to the terminal
'''
#%%
import socket

#-----------------------------------------------------------------------------
#Connection Parameters:
port = 54321
serverAddressPort = ("127.0.0.1", port)
bufferSize = 1024
#-----------------------------------------------------------------------------
print("Type the message you want to send to the UDP Server: ")
msgFromClient = input("  > ")
bytesToSend = str.encode(msgFromClient) #Encode Message to Bytes
#-----------------------------------------------------------------------------


# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


#-----------------------------------------------------------------------------
# Send to server using created UDP socket
print("Sending message to Server...")
UDPClientSocket.sendto(bytesToSend, serverAddressPort)
print("Message sent.")

#-----------------------------------------------------------------------------
# Waits for Server's REPLY:
print("Waiting for Server's REPLY...")
msgFromServer = UDPClientSocket.recvfrom(bufferSize)

#-----------------------------------------------------------------------------
#Display Received Message:
msg = "Message from Server {}".format(msgFromServer[0])
print(msg)