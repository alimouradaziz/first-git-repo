"""
==== Read and display with OpenCV
==== Source code written by Prof. Kartik Bulusu and Josephina Libbon for CS1010-Fall2022
==== CS and MAE Department, SEAS GWU
==== Description:
======== Reads an image saved in a folder,
======== displays the original image 
======== and displays the filtered image with OpenCV.
========
==== Requirements:
============ The program requires Python 3.9.2 dependent libraries:
============ OpenCV 4.6.0
======== It has been written exclusively for CS1010 and CS4907 students in GWU.
======== It may not be used for any other purposes unless author's prior permission is aquired.
==== Testing:
==== 1. Developed by Prof. Kartik Bulusu and Josephina Libbon on Raspberry Pi 3B+ for Fall2022
==== 2. Modified and tested on 11/03/2023 by Gustavo Londono for CS1010-Fall2023 using Python 3.9.2 on Raspberry Pi 4B
==== 3. Modified and tested on 03/01/2024 using Python 3.9.2 on Raspberry Pi 4B
==== Reference: https://pyimagesearch.com/2015/03/30/accessing-the-raspberry-pi-camera-with-opencv-and-python/
"""
# modified by Prof. Kartik Bulusu and Josephina Libbon for CS1010-Fall2022

import cv2
import numpy as np

#IMAGE COLOR FILTERING

img  = cv2.imread('./HW5_mod.png')
# img  = cv2.imread('./image.jpg')


retval, threshold = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)

grayscaled = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

retval2, threshold2 = cv2.threshold(grayscaled, 12, 255, cv2.THRESH_BINARY)

gaus = cv2.adaptiveThreshold(grayscaled, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)

retval2, otsu = cv2.threshold(grayscaled, 125, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.namedWindow('original',cv2.WINDOW_NORMAL) #Create a window to be used (NOT using the WINDOW_AUTOSIZE)
cv2.resizeWindow('original', 600,400) #Resize the window to the desired size
cv2.imshow('original', img) #Display the image in the window

# cv2.namedWindow('threshold',cv2.WINDOW_NORMAL) #Create a window to be used (NOT using the WINDOW_AUTOSIZE)
# cv2.resizeWindow('threshold', 600,400) #Resize the window to the desired size
# cv2.imshow('threshold', threshold) #Display the image in the window
# 
# cv2.namedWindow('threshold2',cv2.WINDOW_NORMAL) #Create a window to be used (NOT using the WINDOW_AUTOSIZE)
# cv2.resizeWindow('threshold2', 600,400) #Resize the window to the desired size
# cv2.imshow('threshold2', threshold2) #Display the image in the window

cv2.namedWindow('Gaus',cv2.WINDOW_NORMAL) #Create a window to be used (NOT using the WINDOW_AUTOSIZE)
cv2.resizeWindow('Gaus', 600,400) #Resize the window to the desired size
cv2.imshow('Gaus', gaus) #Display the image in the window

cv2.namedWindow('otsu',cv2.WINDOW_NORMAL) #Create a window to be used (NOT using the WINDOW_AUTOSIZE)
cv2.resizeWindow('otsu', 600,400) #Resize the window to the desired size
cv2.imshow('otsu', otsu) #Display the image in the window

#destroy all windows when the '0' key is pressed
cv2.waitKey(0)
cv2.destroyAllWindows()
