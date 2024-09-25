# -*- coding: utf-8 -*-
"""
Created on Wed May  3 03:19:03 2023

@author: Conrado
"""


import os
import cv2
import numpy as np



def detectObject(mapImage = None, objectTemplateImage = None, threshold = 0.95, outputFileName = None):
            
    # read game image
    img = cv2.imread(mapImage)
    
    # read image template
    template = cv2.imread(objectTemplateImage, cv2.IMREAD_UNCHANGED)
    hh, ww = template.shape[:2]
    
    # extract bananas base image and alpha channel and make alpha 3 channels
    base = template[:,:,0:3]
    alpha = template[:,:,3]
    alpha = cv2.merge([alpha,alpha,alpha])
    
    # do masked template matching and save correlation image
    correlation = cv2.matchTemplate(img, base, cv2.TM_CCORR_NORMED, mask=alpha)
    
    # set threshold and get all matches
    #threshold = 0.96
    loc = np.where(correlation >= threshold)
    
    # draw matches
    result = img.copy()
    
    matchesCounter = 0
    hasMatch = False
    matchesList = []
    for pt in zip(*loc[::-1]):
        cv2.rectangle(result, pt, (pt[0]+ww, pt[1]+hh), (0,255,0), 1)
        #print(pt)
        matchesCounter += 1
        hasMatch = True
        matchesList.append(pt)
    #end-for
    
    saveResult = True
    if (saveResult is True and outputFileName is not None):
        
        
        filename = "0-result_" + outputFileName
        outFilePath = os.path.join(os.getcwd(), ".outputs", filename)
        cv2.imwrite(outFilePath, result)
        #print("\07")
    #end-if
    
    
    return hasMatch, matchesList

#end-def

"""
templateImagePath = os.path.join(os.getcwd(), "stash", "20-beer", "20-beer.png")

flag, lista = detectObject(mapImage = "map.png", 
                           objectTemplateImage = templateImagePath, 
                           templateSubfolder = "stashTransparent",
                           threshold = 0.94)
"""