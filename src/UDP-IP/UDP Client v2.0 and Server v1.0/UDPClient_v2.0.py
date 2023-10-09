# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 15:32:46 2022

@author: Conrado
"""
#%%
'''
Version: 2.0

What it is: UDP Client

What it does: 
    1) Creates a Socket with certain parameters
    2) Sends a Message to the Server (v1.0)
    3) Waits for the Server's Reply
    4)  repeat n.º 2
    
    OBS: The cycle ends after the Message #100
'''
#%%
import socket
import time
delay = 5
count = 0

#-----------------------------------------------------------------------------
#Connection Parameters:
port = 54321
serverAddressPort = ("127.0.0.1", port)
bufferSize = 1024
#-----------------------------------------------------------------------------


# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


#-----------------------------------------------------------------------------
def sendMessage(count):
    msgFromClient = "This is the Message #" + str(count)
    bytesToSend = str.encode(msgFromClient) #Encode Message to Bytes
    
    # Send to server using created UDP socket
    #print("Sending message to Server...")
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    print("Message sent.")
    return

#-----------------------------------------------------------------------------
# Waits for Server's REPLY:
def receiveReply():
    print("Waiting for Server's REPLY...")
    msgFromServer = UDPClientSocket.recvfrom(bufferSize)
    
    
    #Display Received Message:
    msg = "Message from Server {}".format(msgFromServer[0])
    print(msg)
    return
#-----------------------------------------------------------------------------

while (count <= 100):
    sendMessage(count)
    count += 1
    receiveReply()
    time.sleep(delay)
    