"""
Realtime video capture and filtering toward IoT applications
Adapted to run as a Flask MJPEG streaming server.
"""

from picamera2 import Picamera2
import time
import cv2
import numpy as np
from flask import Flask, Response, render_template_string

# ---------------- CAMERA SETUP ----------------

picam2 = Picamera2()
resolution = (320, 240)

picam2.configure(
    picam2.create_preview_configuration(
        main={"format": "XRGB8888", "size": resolution}
    )
)
picam2.start()
time.sleep(0.1)  # camera warmup

# ---------------- FLASK APP ----------------

app = Flask(__name__)

INDEX_HTML = """
<!doctype html>
<html>
<head>
    <title>PiNoIR Filters - Flask</title>
    <style>
        body { font-family: Arial, sans-serif; background:#111; color:#eee; text-align:center; }
        img { border: 2px solid #555; margin:10px; }
    </style>
</head>
<body>
    <h1>Pi NoIR Realtime Filters (Flask)</h1>
    <p>Original + Laplacian + Sobel X + Sobel Y + Canny edges.</p>
    <img src="{{ url_for('video_feed') }}" width="800">
</body>
</html>
"""


@app.route("/")
def index():
    return render_template_string(INDEX_HTML)


def gen_frames():
    """
    Generator that grabs frames from Picamera2, applies filters with OpenCV,
    stitches them into a single image, encodes as JPEG, and yields as MJPEG.
    Pattern follows standard Flask MJPEG examples.[web:59][web:83][web:86]
    """
    while True:
        # Capture frame as NumPy array (RGB)
        frame = picam2.capture_array()

        # Convert to BGR for OpenCV
        frame_bgr = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

        gray = cv2.cvtColor(frame_bgr, cv2.COLOR_BGR2GRAY)

        laplacian = cv2.Laplacian(gray, cv2.CV_64F)
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
        edges = cv2.Canny(gray, 100, 200)

        # Encode as JPEG
        ret, jpeg = cv2.imencode(".jpg", frame)
        if not ret:
            continue
        frame_bytes = jpeg.tobytes()

        # Yield MJPEG frame
        yield (b"--frame\r\n"
               b"Content-Type: image/jpeg\r\n\r\n" + frame_bytes + b"\r\n")


@app.route("/video_feed")
def video_feed():
    return Response(
        gen_frames(),
        mimetype="multipart/x-mixed-replace; boundary=frame",
    )


if __name__ == "__main__":
    try:
        app.run(host="0.0.0.0", port=5000, debug=False, threaded=True)
    finally:
        picam2.stop()
