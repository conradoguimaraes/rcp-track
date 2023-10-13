import os
import traceback
import cv2
import numpy as np
from matplotlib import pyplot as plt

class inputImage():
    def __init__(self, imageFilePath=None) -> None:
        #self.config = readConfig(moduleName="main")

        self.imageObj = cv2.imread(imageFilePath, cv2.IMREAD_UNCHANGED)

        #self.imageSubfolderOutput = self.config["imageSubfolderOutput"]
        #self.finalOutputImageName = self.config["finalOutputImageName"]
        self.imageSubfolderOutput = os.getcwd()
        self.finalOutputImageName = "output.png"
    #end-def

    def replaceColor2White(self, target_color, color_tolerance) -> None:
        #target_color = (160, 121, 63)  # Replace with your desired RGB color
        #image = replaceColor(image,target_color,158)

        # Create a mask for pixels with the target color within the specified tolerance
        mask = np.all(np.abs(self.imageObj - target_color) <= color_tolerance, axis=-1)
        
        # Replace pixels with the target color using a replacement color (e.g., white)
        replacement_color = (255, 255, 255)  # Replace with your desired replacement color
        
        self.imageObj[mask] = replacement_color
        return
    #end-def

    def convert2grayscale(self) -> None:
        # Convert image to grayscale
        self.imageObj = cv2.cvtColor(self.imageObj, cv2.COLOR_BGR2GRAY)
        return
    #end-def

    def denoiseImage(self, param_h = 30, param_windowSize=7, param_search_windowSize = 20) -> None:
        #Remove denoise (intensity {h}, template and window)
        self.imageObj = cv2.fastNlMeansDenoising(self.imageObj,
                                                 None, 
                                                 h = param_h, 
                                                 templateWindowSize = param_windowSize, 
                                                 searchWindowSize = param_search_windowSize)
        return
    #end-def

    def resizeImage(self, scale_factor = 1) -> None:
        minScaling = 0.1
        maxScaling = 5
        if (scale_factor == 1): return self.imageObj
        if (scale_factor < minScaling or scale_factor > maxScaling): raise Exception(f"scale_factor = {scale_factor} not within the value range [{minScaling}, {maxScaling}].")

        width = self.imageObj.shape[1]
        height = self.imageObj.shape[0]
        #scale_factor = 1
        # gray = gray.resize((width*scale_factor, height*scale_factor))
        
        self.imageObj = cv2.resize(self.imageObj, (round(width*scale_factor),round(height*scale_factor)), interpolation = cv2.INTER_AREA)
        return
    #end-def

    def thresholdAndMask(self, lowerBound = 245, upperBound = 255) -> None:
        if (lowerBound > 255 or lowerBound < 0): raise Exception(f"LowerBound = {lowerBound} not within the value range [0, 255].")
        if (upperBound > 255 or upperBound < 0): raise Exception(f"upperBound = {upperBound} not within the value range [0, 255].")

        _, mask = cv2.threshold(self.imageObj, 245, 255, cv2.THRESH_BINARY_INV)
        # _, mask = cv2.threshold(self.imageObj, 245, 255, cv2.THRESH_OTSU)

        # Invert the mask
        mask_inv = cv2.bitwise_not(mask)

        # Create a white background
        white_bg = np.ones_like(self.imageObj) * 255

        # Extract the text using the inverted mask
        self.imageObj = cv2.bitwise_and(white_bg, white_bg, mask=mask_inv)

        return
    #end-def

    def normalizeImage(self, lowerBound = 0, upperBound = 255) -> None:
        norm_img = np.zeros((self.imageObj.shape[0], self.imageObj.shape[1]))
        self.imageObj = cv2.normalize(self.imageObj, norm_img, lowerBound, upperBound, cv2.NORM_MINMAX)
        return
    #end-def

    def morphOperations(self, dilateFlag = False, erodeFlag = False, dilateIters = 5, erodeIters = 5) -> None:

        kernelErode = np.ones((1,1),np.uint8)
        kernelDilate = np.ones((1,1),np.uint8)

        if (dilateFlag): self.imageObj = cv2.dilate(self.imageObj, kernelDilate, iterations = dilateIters)
        if (erodeFlag): self.imageObj = cv2.erode(self.imageObj, kernelErode, iterations = erodeIters)

        #kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1,1))
        #result = cv2.morphologyEx(result, cv2.MORPH_OPEN, kernel, iterations=5)

        #result = cv2.bitwise_not(result)
        #result = cv2.erode(result, kernelErode, iterations = 15)

        return
    #end-def

    def sharpenImage(self, kernelParamValue=12) -> None:
        #Sharpen the image with some standard kernel configuration
        # Create a sharpening kernel
        k = kernelParamValue
        sharpening_kernel = np.array([[-1, -1, -1],
                                      [-1,  k, -1],
                                      [-1, -1, -1]])

        # Apply the sharpening kernel to the image
        self.imageObj = cv2.filter2D(self.imageObj, -1, sharpening_kernel)
        return
    #end-def


    def invertImage(self) -> None:
        self.imageObj = cv2.bitwise_not(self.imageObj)
        return
    #end-def
    
    def gray2rgb(self) -> None:
        self.imageObj = cv2.cvtColor(self.imageObj, cv2.COLOR_GRAY2RGB)
        return
    #end-def

    def saveOutputImage(self, prefix = "") -> int:
        rc = -1
        try:
            filepath = os.path.join(os.getcwd(),
                                    self.imageSubfolderOutput,
                                    prefix + self.finalOutputImageName)
            
            cv2.imwrite(filepath, self.imageObj)
            rc = 1
        except:
            print(traceback.format_exc())
            rc = -1
        return rc
    #end-def

    def showImage(self, windowName = "Result") -> None:
        interactive = True
        if (interactive):
            #https://stackoverflow.com/questions/50630825/matplotlib-imshow-distorting-colors
            plt.imshow(self.imageObj[...,::-1]) #BGR (opencv) to RGB (matplotlib)
            plt.xticks([]), plt.yticks([])
            plt.show()
        else:
            #cv2.namedWindow(windowName, cv2.WINDOW_NORMAL)
            cv2.namedWindow(windowName, cv2.WINDOW_AUTOSIZE)
            #cv2.resizeWindow(windowName, 1280, 720)
            cv2.imshow(windowName, self.imageObj)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        #end-if-else
        return
    #end-def

#end-class















    


