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
#import cv2.aruco as aruco
#import math
#from datetime import datetime
#import RPi.GPIO as GPIO
#import time



#pip install pygrabber
from pygrabber.dshow_graph import FilterGraph


def get_available_cameras() :
    #https://stackoverflow.com/questions/70886225/get-camera-device-name-and-port-for-opencv-videostream-python
    devices = FilterGraph().get_input_devices()

    available_cameras = {}

    for device_index, device_name in enumerate(devices):
        available_cameras[device_index] = device_name

    return available_cameras


print(get_available_cameras())



availableCameras = []
for cameraID in range(5):
    print("Creating Object...")
    cap = cv2.VideoCapture(cameraID, cv2.CAP_DSHOW)
    
    if not cap.isOpened():
        print(f"Cannot open camera with ID {cameraID}")
    else:
        print(f"Success opening camera with ID {cameraID}")
        availableCameras.append(cameraID)
        #break
#end-for

#print(f"Camera ID: {cameraID}")

print("\n > Available Cameras: ", availableCameras)

cameraID = int(input("\n\nDesired camera ID: > "))
cap = cv2.VideoCapture(cameraID, cv2.CAP_DSHOW)


#cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
#cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1366)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 768)


counter = 0
printIters = 500
while True:
    #frame = cv2.flip(frame, 0)
    #cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)
    # operations on the frame
    if (counter % printIters == 0): print("Capturing image...")
    ret, frame = cap.read()

    if not ret:
        print("Can't receive frame (stream end?). Exiting ...")
        break
    
    if (counter % printIters == 0): print("Showing Image...")
    cv2.namedWindow("image", cv2.WND_PROP_FULLSCREEN)
    cv2.setWindowProperty("image", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_NORMAL)

    cv2.imshow('frame',frame)

    if cv2.waitKey(1) == ord('q'): break

    counter += 1

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
