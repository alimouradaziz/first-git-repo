"""
==== Video preview with Raspberry Pi Camera
==== Source code written by Prof. Kartik Bulusu and Gustavo Londono for CS1010-Fall2023
==== CS and MAE Department, SEAS GWU
==== Description:
======== Face detection using OpenCV pretrained model
======== https://github.com/opencv/opencv/tree/4.x/data/haarcascades
========
==== Requirements:
============ The program requires Python 3.9.2 dependent libraries:
============ OpenCV 4.6.0, picamera2
======== It has been written exclusively for CS4907 students in GWU.
======== It may not be used for any other purposes unless author's prior permission is aquired.
==== Testing:
==== 1. Developed and tested on 11/03/2023 using Python 3.9.2 on Raspberry Pi 4B
"""
# modified by Prof. Kartik Bulusu and Gustavo Londono for CS1010-Fall2023

#turns on camera and displays a preview

import time
from picamera2.picamera2 import Picamera2, Preview

#create an instance of Picamera2
picam2 = Picamera2()

#begin the preview
picam2.start_preview(Preview.QT)

#turn on the camera
picam2.start()

#wait 10 seconds
time.sleep(10)

#turn off the camera and preview
picam2.stop()


#exit the program
exit()