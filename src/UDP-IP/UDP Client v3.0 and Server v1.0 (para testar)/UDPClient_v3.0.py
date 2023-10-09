# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 15:32:46 2022

@author: Conrado
"""
#%%
'''
Version: 3.0

What it is: UDP Client

What it does: 
    1) Creates a Socket with certain parameters
    2) Reads XML File
    3) Encodes XML File
    4) Sends the Encoded XML Data to the Server (v2.0)
    3) Waits for the Server's Reply
'''

#%%
import socket
#-----------------------------------------------------------------------------
#Connection Parameters:
port = 8080
#serverAddressPort = ("192.168.137.2", port)
serverAddressPort = ("192.168.137.2", port)
bufferSize = 1024
#-----------------------------------------------------------------------------


# Create a UDP socket at client side
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


#-----------------------------------------------------------------------------
def sendMessage(XMLdata):

    bytesToSend = str.encode(XMLdata) #Encode Message to Bytes
    
    # Send to server using created UDP socket
    print("Sending message to Server...")
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



fileName = input(">Type the XML filename: > ")

if ((".xml" or ".XML") not in fileName):
    fileName = fileName + ".xml"

with open(fileName, encoding=("UTF-8")) as fid:
    FileData = fid.read()

input("> Press any key to send the message...")    
sendMessage(FileData)