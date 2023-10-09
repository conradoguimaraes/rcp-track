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
import os
import traceback
import datetime
#-----------------------------------------------------------------------------
#Connection Parameters:
port = 54321
port = 8080


R = input(">>Ler IP de Ficheiro? (1-yes)(0-no) ")
R = int(R)
if (R==1):
    fid = open("ip.txt",'r',encoding = "utf-8")
    enderecoIP = fid.read()
    enderecoIP = enderecoIP.replace("\n",'')
else:
    R = input(">>IP LocalHost? (1-yes)(0-no) ")
    R = int(R)
    if (R==1):
        enderecoIP = "127.0.0.1"
    else:
        enderecoIP = input(">> IP: ")

print("IP: ", enderecoIP)
print("Port: ", port)
serverAddressPort = (enderecoIP, port)
bufferSize = 1024
#-----------------------------------------------------------------------------


# Create a UDP socket at client sidesample3
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


#-----------------------------------------------------------------------------
def sendMessage(XMLdata):

    bytesToSend = str.encode(XMLdata) #Encode Message to Bytes
    
    # Send to server using created UDP socket
    print("Sending message to Server...")
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    print("Message sent.\n")
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


def funclear():
    os.system('cls' if os.name == 'nt' else 'clear')
    return

def showIP(enderecoIP):
    print("\nIP: ", enderecoIP)
    return

def showPort(port):
    print("\nPort: ", port)
    return

counter = 0
useXML = False
while True:
    try:
        fileName = input("> Message > ")
        


        if (fileName.lower() == "clear"):
            funclear()
        elif (fileName.lower() == "showip"):
            showIP()
        elif (fileName.lower() == "showport"):
            showPort()
        elif (fileName.lower() == "stop" or fileName.lower() == "exit"):
            break



        else:
            if (useXML):
                if ((".xml" or ".XML") not in fileName):
                    fileName = fileName + ".xml"
                #end-if-else
                
                with open(fileName, encoding=("UTF-8")) as fid:
                    FileData = fid.read()
                    FileData = FileData.replace('”','"')
                    FileData = FileData.replace('”','"')
                #end-with
            else:
                FileData = "[" + str(datetime.datetime.now()) + "] " + fileName
            #end-if-else
            
            
            
            R = input("> Press any key to send the message...")
            if R.lower() == "stop":
                pass
            else:
                sendMessage(FileData)


    except:
        print(traceback.format_exc())