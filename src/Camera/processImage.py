import os

import image_Class
import numpy as np
import cv2


if __name__ == '__main__':
    
    imageFilename = "sample.png"
    
    imageObj = image_Class.inputImage(imageFilePath=imageFilename)
    imageObj.convert2grayscale()
    
    print("Applying Morphological Operations...", end="\r")
    imageObj.morphOperations(dilateFlag=True, erodeFlag=True,
                            dilateIters=15, erodeIters=15)
    
    
    #imageObj.normalizeImage(lowerBound = 0, upperBound = 255)
    
    #Remove denoise (intensity {h}, template and window)
    print("Removing Image Noise...", end="\r")
    imageObj.denoiseImage(param_h=10,
                          param_windowSize=7,
                          param_search_windowSize=20)

    #Sharpen the image with some standard kernel configuration
    print("Sharpening Image with kernel...", end="\r")
    #imageObj.sharpenImage(kernelParamValue=5)

    
    imageObj.saveOutputImage(prefix="grayscale_")
    print("Grayscale image saved!")
    
    #imageObj.gray2rgb()
    
    #alpha = 1.5 # Contrast control (1.0-3.0)
    #beta = 0 # Brightness control (0-100)
    #adjusted = cv2.convertScaleAbs(imageObj, alpha=alpha, beta=beta)
    #contrast = 1.0
    
    #brightness = 0
    #brightness += int(round(255*(1-contrast)/2))
    #adjusted = cv2.addWeighted(imageObj, contrast, imageObj, 0, brightness)
    
    
    
    
    
    
    
    #------------------------------------------------------------
    #RGB
    #------------------------------------------------------------
    imageObj = image_Class.inputImage(imageFilePath=imageFilename)

    #imageObj.normalizeImage(lowerBound = 0, upperBound = 255)
    print("Removing Image Noise...", end="\r")
    imageObj.denoiseImage(param_h=10,
                          param_windowSize=7,
                          param_search_windowSize=20)

    
    imageObj.saveOutputImage(prefix="rgb_")
    print("RGB image saved!")

#end-if