# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 15:40:47 2022

@author: Conrado
"""
#%%
'''
Version: 1.0

What it is: UDP Server

What it does: 
    1) Creates a Socket with certain parameters
    2) Keeps waiting for a Message sent by a Client
    3) Prints, to the terminal, the Client Messange and IP/Port
'''
#%%
import socket

#-----------------------------------------------------------------------------
#Connection Parameters:
localIP = "127.0.0.1"
#localIP = "10.227.144.2"
port = 54321
bufferSize = 1024
#-----------------------------------------------------------------------------


msgFromServer = "Hello UDP Client" #Standard REPLY Message
bytesToSend = str.encode(msgFromServer) #Encode String to Bytes


#-----------------------------------------------------------------------------
# Create a Socket
UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to Address and IP
UDPServerSocket.bind((localIP, port))
#-----------------------------------------------------------------------------
 

print("UDP Server READY!\n")

# Listen for incoming messages
while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]
    address = bytesAddressPair[1] #tuple (address, port)
    
    #-------------------------------------------------------------------------        
    #clientMsg = "\t> Message Received from Client:{}".format(message)
    clientMsg = "\t> Message Received from Client: " + message.decode("utf-8")
    clientIP  = "\t> Client IP Address:{}".format(address)
    
    print(clientMsg)
    print(clientIP)
    print("\n")
    #-------------------------------------------------------------------------
   
    # Sending a REPLY to client
    UDPServerSocket.sendto(bytesToSend, address)