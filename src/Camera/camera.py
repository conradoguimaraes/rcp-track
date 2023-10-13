# -*- coding: utf-8 -*-
"""
Created on Mon Mar 28 15:40:47 2022

@author: Conrado
"""
#%%
'''
Version: 1.0

'''
#%%

import numpy as np
import cv2
from datetime import datetime
#import cv2.aruco as aruco
#import math
#from datetime import datetime
#import RPi.GPIO as GPIO
#import time

import os

#pip install pygrabber
from pygrabber.dshow_graph import FilterGraph


def get_available_cameras() :
    #https://stackoverflow.com/questions/70886225/get-camera-device-name-and-port-for-opencv-videostream-python
    devices = FilterGraph().get_input_devices()

    available_cameras = {}

    for device_index, device_name in enumerate(devices):
        available_cameras[device_index] = device_name

    return available_cameras

cameras = get_available_cameras()
desiredCameraName = "GENERAL WEBCAM"
desiredCameraID = None

for cameraID in cameras:
    #print(cameraID, "->", cameras[cameraID])
    name = cameras[cameraID]
    if (name == desiredCameraName):
        desiredCameraID = cameraID
    
    
#end-for



# availableCameras = []
# for cameraID in range(5):
#     print("Creating Object...")
#     cap = cv2.VideoCapture(cameraID, cv2.CAP_DSHOW)
    
#     if not cap.isOpened():
#         print(f"Cannot open camera with ID {cameraID}")
#     else:
#         print(f"Success opening camera with ID {cameraID}")
#         availableCameras.append(cameraID)
#         #break
# #end-for

# #print(f"Camera ID: {cameraID}")

# print("\n > Available Cameras: ", availableCameras)

# cameraID = int(input("\n\nDesired camera ID: > "))
# cap = cv2.VideoCapture(cameraID, cv2.CAP_DSHOW)

cap = cv2.VideoCapture(desiredCameraID, cv2.CAP_DSHOW)


#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1366)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 768)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
#cap.set(cv2.CAP_PROP_CONVERT_RGB, float(-1))

print("CV_CAP_PROP_FRAME_WIDTH: '{}'".format(cap.get(cv2.CAP_PROP_FRAME_WIDTH))) 
print("CV_CAP_PROP_FRAME_HEIGHT : '{}'".format(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))) 
print("CAP_PROP_FPS : '{}'".format(cap.get(cv2.CAP_PROP_FPS))) 
print("CAP_PROP_POS_MSEC : '{}'".format(cap.get(cv2.CAP_PROP_POS_MSEC))) 
print("CAP_PROP_FRAME_COUNT  : '{}'".format(cap.get(cv2.CAP_PROP_FRAME_COUNT))) 
print("CAP_PROP_BRIGHTNESS : '{}'".format(cap.get(cv2.CAP_PROP_BRIGHTNESS))) 
print("CAP_PROP_CONTRAST : '{}'".format(cap.get(cv2.CAP_PROP_CONTRAST))) 
print("CAP_PROP_SATURATION : '{}'".format(cap.get(cv2.CAP_PROP_SATURATION))) 
print("CAP_PROP_HUE : '{}'".format(cap.get(cv2.CAP_PROP_HUE))) 
print("CAP_PROP_GAIN  : '{}'".format(cap.get(cv2.CAP_PROP_GAIN))) 
print("CAP_PROP_CONVERT_RGB : '{}'".format(cap.get(cv2.CAP_PROP_CONVERT_RGB))) 
print("CV_CAP_PROP_FRAME_WIDTH: '{}'".format(cap.get(cv2.CAP_PROP_FRAME_WIDTH))) 
print("CV_CAP_PROP_FRAME_HEIGHT : '{}'".format(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))) 
print("CAP_PROP_FPS : '{}'".format(cap.get(cv2.CAP_PROP_FPS))) 
print("CAP_PROP_POS_MSEC : '{}'".format(cap.get(cv2.CAP_PROP_POS_MSEC))) 
print("CAP_PROP_FRAME_COUNT  : '{}'".format(cap.get(cv2.CAP_PROP_FRAME_COUNT))) 
print("CAP_PROP_BRIGHTNESS : '{}'".format(cap.get(cv2.CAP_PROP_BRIGHTNESS))) 
print("CAP_PROP_CONTRAST : '{}'".format(cap.get(cv2.CAP_PROP_CONTRAST))) 
print("CAP_PROP_SATURATION : '{}'".format(cap.get(cv2.CAP_PROP_SATURATION))) 
print("CAP_PROP_HUE : '{}'".format(cap.get(cv2.CAP_PROP_HUE))) 
print("CAP_PROP_GAIN  : '{}'".format(cap.get(cv2.CAP_PROP_GAIN))) 
print("CAP_PROP_CONVERT_RGB : '{}'".format(cap.get(cv2.CAP_PROP_CONVERT_RGB))) 

input("\n . . . [ENTER] to start . . .")



counter = 0
printIters = 50
realTimePreProcessing = False

imageCounter = 0
while True:
    #frame = cv2.flip(frame, 0)
    #cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    # operations on the frame
    #if (counter % printIters == 0): print("Capturing image...")
    
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    if (counter % printIters == 0): print("Showing Image...")
    cv2.namedWindow("image", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)

    
    if (realTimePreProcessing):
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        frame = cv2.fastNlMeansDenoising(frame,
                                         None, 
                                         h = 10, 
                                         templateWindowSize = 7, 
                                         searchWindowSize = 20)
    else:
        pass
        #frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #end-if-else
        

    if (counter % printIters == 0):
        print("Image saved!")
        cv2.imwrite("sample.png", frame)
    #end-if-else
    
    cv2.imshow('image',frame)

    if cv2.waitKey(1) == ord('q'): break
    
    if cv2.waitKey(1) == ord('s'):
        filePath = os.path.join(os.getcwd(), "calibration_images", "image_"+str(imageCounter)+".png")
        try:
            os.mkdir(os.path.join(os.getcwd(), "calibration_images"))
        except:
            pass
        cv2.imwrite(filePath, frame)
        print("\07")
    #end-if

    counter += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
