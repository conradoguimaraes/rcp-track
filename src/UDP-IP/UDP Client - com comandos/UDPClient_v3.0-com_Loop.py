# -*- coding: utf-8 -*-
"""
Created on Feb 26 14:25:46 2024

@author: Conrado
"""


#%%
import socket
import os
import traceback
import datetime
import keyboard
#pip install keyboard
#-----------------------------------------------------------------------------
#Connection Parameters:
port = 54321
port = 8080



#enderecoIP = input(">> IP: ")
enderecoIP = "192.168.137.161"
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


def on_key_event(event):
    try:
        #print(event.name)
        if event.name == 'up' or event.name == "seta acima":
            print("forward")
            sendMessage("mf")
            
        elif event.name == 'down' or event.name == "seta abaixo":
            print("backward")
            sendMessage("mb")
            
        elif event.name == 'left' or event.name == "seta à esquerda":
            print("left")
            sendMessage("mr")
            
        elif event.name == 'right' or event.name == "seta à direita":
            print("right")
            sendMessage("ml")
        
        elif event.name == 'a':
            print("a")
            sendMessage("+d")
        
        elif event.name == 'd':
            print("d")
            sendMessage("-d")
        
        
        elif event.name == 'esc':
            print("ESCAPE")
            sendMessage("rr")
        else:
            pass
    except:
        print(traceback.format_exc())
    return


counter = 0

keyboard.on_press(on_key_event)

try:
    keyboard.wait()
except KeyboardInterrupt:
    pass
finally:
    keyboard.unhook_all()

