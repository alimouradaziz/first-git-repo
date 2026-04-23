"""
==== Modified still image capture with Raspberry Pi Camera 
==== Source code written by Prof. Kartik Bulusu and Gustavo Londono for CS1010-Fall2023
==== CS and MAE Department, SEAS GWU
==== Description:
======== Takes a simple still-image using the connected camera
======== and saves the image to the current directory.
======== Prints countdown before taking picture.
======== Displays the picture using OpenCV
==== Requirements:
============ The program requires Python 3.9.2 dependent libraries:
============ OpenCV 4.6.0, picamera2
======== It has been written exclusively for CS1010 and CS4907 students in GWU.
======== It may not be used for any other purposes unless author's prior permission is aquired.
==== Testing:
==== 1. Developed and tested on 11/03/2023 using Python 3.9.2 on Raspberry Pi 4B
"""

# modified by Prof. Kartik Bulusu and Gustavo Londono for CS1010-Fall2023

#takes a simple still-image using the connected camera and saves the image to the current directory. displays a countdown before taking picture.

#imports
from picamera2 import Picamera2, Preview
import cv2
import time
import numpy

#create an instance of the Picamera2
picam2 = Picamera2()
picam2.start_preview(Preview.QT)

#set and load the configuration to be used
capture_config = picam2.create_still_configuration(lores={"size": (320, 240)}, display="lores")

#start the camera and display a preview
# picam2.start(show_preview=True)
picam2.start()



#countdown for picture
countdown = 5
while countdown != 0:
    
    #print the number of seconds left in countdown
    print(countdown)
    
    #wait for one second to pass
    time.sleep(1)
    
    #decrement the countdown variable by 1
    countdown-=1

print("Say Cheese!")

#buffer time to allow for people to say cheese
time.sleep(0.5)

#Take the picture and save it as "image.jpg" to the current directory
picam2.switch_mode_and_capture_file(capture_config, "image.jpg")
array = picam2.capture_array("main")

picam2.stop_preview()

#Turn the camera and preview off
picam2.stop()

# display the image on screen and wait for a keypress

cv2.namedWindow('New Image',cv2.WINDOW_NORMAL) #Create a window to be used (NOT using the WINDOW_AUTOSIZE)
cv2.resizeWindow('New Image', 600,400) #Resize the window to the desired size
cv2.imshow('New Image', array) #Display the image in the window
cv2.waitKey(0)

#Exit the program and also close the preview window
exit()
