"""
==== flask app for random number plots toward IoT applications
==== Source code written by Prof. Kartik Bulusu
==== CS and MAE Department, SEAS GWU
==== Description:
======== flask API implementation for IoT demonstration in CS4907   
==== Description:
======== flask API implementation for IoT demonstration in CS3907   
======== This program incorporates the picamera2, cv2 and flask library
==== Requirements:
======== It has been written exclusively for MAE6291 students in GWU.
======== It may not be used for any other purposes unless author's prior permission is aquired.
==== Testing:
==== 1. Developed on 03/07/2023 using VSCode on Macbook Pro 
==== 2. Tested on 03/09/2023 on Python 3.5.3 on Raspberry Pi 3B+
==== 3. Modified on 03/10/2023 using VSCode on Macbook Pro  
==== 4. Revised and tested on 03/18/2025 on Raspberry Pi 4-->
==== Reference: https://towardsdatascience.com/web-visualization-with-plotly-and-flask-3660abf9c946
==== Reference: https://www.youtbe.com/watch?v=i9mJzdLYsVo
==== Reference: https://towardsdatascience.com/web-visualization-with-plotly-and-flask-3660abf9c946
==== Reference: https://towardsdatascience.com/creating-restful-apis-using-flask-and-python-655bad51b24
==== Reference: https://towardsdatascience.com/creating-restful-apis-using-flask-and-python-655bad51b24
"""

from flask import Flask, render_template, Response, stream_with_context, request
import numpy as np
import cv2
from picamera2 import Picamera2

# ======== Initialize flask app ===========


# Grab images as numpy arrays and leave everything else to OpenCV.

app = Flask(__name__)

# Grab images as numpy arrays and leave everything else to OpenCV.


def video_stream():
    face_detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
    assert not face_detector.empty()
    cv2.startWindowThread()
    
    picam2 = Picamera2()
    picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
    picam2.start()

#     while True:
#         ret, frame = video.read()
#         if not ret:
#             break;
#         else:
#             ret, buffer = cv2.imencode('.jpeg', frame)
#             frame = buffer.tobytes()

    while True:
        frame = picam2.capture_array()

        grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(grey, 1.1, 5)

        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0))

#         cv2.imshow("Camera", frame)
        ret, buffer = cv2.imencode('.jpeg', frame)
        frame = buffer.tobytes()
        
        yield(b'--frame\r\n'
              b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        
#         cv2.waitKey(1)

#     cv2.destroyAllWindows()
    
# ======== Create function to gather data and render to html-frontend ===========
@app.route('/')

def camera():
   return render_template('camera.html')

# ======== Create function to gather data and render to html-frontend ===========
@app.route('/video_feed')

def video_feed():
    return Response(video_stream(), mimetype='multipart/x-mixed-replace; boundary=frame')


   
if __name__ == '__main__':

    # If you have debug=True and receive the error "OSError: [Errno 8] Exec format error", then:
    # remove the execuition bit on this file from a Terminal, ie:
    # chmod -x flask_api_server.py
    #
    # Flask GitHub Issue: https://github.com/pallets/flask/issues/3189
    print()
    print('=======================================================')
    print('Welcome to My IoT camera device')
    print('=======================================================')
    print()
    
    app.run(host="0.0.0.0", debug=True)
    # Default port is 5000
    # To change use port = <integer>