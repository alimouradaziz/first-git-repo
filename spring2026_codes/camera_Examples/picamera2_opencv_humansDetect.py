# https://github.com/freedomwebtech/rpicam-detect-human/blob/main/picam.py

# from picamera.array import PiRGBArray
from picamera2 import Picamera2
import time
import numpy as np
import cv2

# allow the camera to warmup
time.sleep(0.1)
hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())
cv2.startWindowThread()

# initialize the camera and grab a reference to the raw camera capture
picam2 = Picamera2()
picam2.resolution = (640, 480)
# picam2.framerate = 32
# picam2.rotation = 180
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": picam2.resolution}))
picam2.start()




# # # capture frames from the camera
# for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
#     image = frame.array

while True:
    frame = picam2.capture_array()
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    (boxes, weights) = hog.detectMultiScale(gray, winStride=(8,8))
    boxes = np.array([[x, y, x + w, y + h] for (x, y, w, h) in boxes])
    for (xA, yA, xB, yB) in boxes:
        # display the detected boxes in the colour picture
        cv2.rectangle(frame, (xA, yA), (xB, yB),(0, 255, 0), 2)
    cv2.imshow("Frame", frame);
    
    key = cv2.waitKey(1) & 0xFF
#     frame.truncate(0)
    if key == ord("q"):
       break
    
cv2.destroyAllWindows()