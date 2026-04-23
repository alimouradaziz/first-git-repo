"""
==== Video preview and record with Raspberry Pi Camera
==== Source code written by Prof. Kartik Bulusu and Gustavo Londono for CS1010-Fall2023
==== CS and MAE Department, SEAS GWU
==== Description:
======== Takes a short duration video using the connected camera
======== and saves the image to the current directory.
========
==== Requirements:
============ The program requires Python 3.9.2 dependent libraries:
============ picamera2
======== It has been written exclusively for CS1010 and CS4907 students in GWU.
======== It may not be used for any other purposes unless author's prior permission is aquired.
==== Testing:
==== 1. Developed and tested on 11/03/2023 using Python 3.9.2 on Raspberry Pi 4B
"""
# modified by Prof. Kartik Bulusu and Gustavo Londono for CS1010-Fall2023

from picamera2.encoders import H264Encoder
from picamera2 import Picamera2, Preview
import time

picam2 = Picamera2()
picam2.start_preview(Preview.QT)

video_config = picam2.create_video_configuration()
picam2.configure(video_config)

encoder = H264Encoder(bitrate=10000000)
output = "test.h264"

picam2.start_recording(encoder, output)
time.sleep(10)
picam2.stop_recording()
picam2.stop_preview()
