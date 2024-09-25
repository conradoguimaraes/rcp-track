import numpy as np
import cv2


# read the image
image = cv2.imread("img1.jpg")
# convert from BGR to HSV color space
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# lower and upper limits for the white color
#lower_limit = np.array([150, 100, 180])
#upper_limit = np.array([150, 255, 255])



#For HSV, hue range is [0,179], saturation range is [0,255], and value range is [0,255]
"""
Hue is responsible for modeling the color type, 
saturation we could understand as the strength with which the color is displayed and finally 
value is the brightness or intensity of the color
"""


#BLUE:
blue_lower_limit = np.array([100, 100, 140])
blue_upper_limit = np.array([150, 255, 255])

#RED:
red_lower_limit = np.array([176, 90, 140])
red_upper_limit = np.array([179, 255, 255])

#PINK:
pink_lower_limit = np.array([150, 80, 150])
pink_upper_limit = np.array([170, 200, 255])





# lower_limit = np.array([75, 0, 99])
# upper_limit = np.array([179, 62, 255])
#mask = cv2.inRange(hsv_image, lower_limit, upper_limit)


# create a mask for the specified color range
maskBlue = cv2.inRange(hsv_image, blue_lower_limit, blue_upper_limit)
maskRed  = cv2.inRange(hsv_image, red_lower_limit, red_upper_limit)
maskPink = cv2.inRange(hsv_image, pink_lower_limit, pink_upper_limit)




mask1 = cv2.bitwise_or(maskBlue, maskRed)
mask = cv2.bitwise_or(mask1, maskPink)






# Taking a matrix of size 5 as the kernel 
kernel = np.ones((2, 2), np.uint8) 
mask = cv2.erode(mask, kernel, iterations=1) 






# Bitwise-AND mask and original image
res = cv2.bitwise_and(image, image, mask= mask)
 
# get the bounding box from the mask image
# bbox = cv2.boundingRect(mask)

# if we get a bounding box, use it to draw a rectangle on the image
# if bbox is not None:
#     print("Object detected")
#     x, y, w, h = bbox
#     cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 5)
# else:
#     print("Object not detected")
#end-if-else

image = cv2.resize(image, (960, 540))
#hsvImage = cv2.resize(hsv_image, (960, 540))
mask = cv2.resize(mask, (960, 540))
res = cv2.resize(res, (960, 540))

cv2.imshow('frame',image)
#cv2.imshow('hsvImage',hsvImage)
cv2.imshow('mask',mask)
cv2.imshow('res',res)
 
#image2Show = cv2.resize(mask, (960, 540))
#cv2.imshow('image', image2Show)
cv2.waitKey(0)
#cv2.imwrite("new.jpg", image)

