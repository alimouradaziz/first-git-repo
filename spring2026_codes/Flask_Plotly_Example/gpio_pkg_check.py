"""
File: chapter01/gpio_pkg_check.py
Source: Practical Python Programming for IoT
Author: Gary Smart
Modified by Kartik Bulusu (CS Dept., GWU)

This Python script checks for the availability of various Python GPIO Library Packages for the Raspberry Pi.
It does this by attempting to import the Python package. If the package import is successful
we report the package as Available, and if the import (or import initialization) fails for any reason,
we report the package as Unavailable.

Dependencies:
  pip3 install gpiozero pigpio RPi.GPIO

==== 1. Built and tested with Python 3.7 on Raspberry Pi 4 Model B
==== 2. Tested with Python 3.5.3 on Raspberry Pi 3B+
==== 3. Modified on 02/22/2024 using Python 3.10.11 on Macbook Pro using Thonny IDE
"""
import importlib.metadata

try:
    import gpiozero
    print('GPIOZero   Available')
except:
    print('GPIOZero   Unavailable. Install with "pip install gpiozero"')
# sudo pigpiod  

try:
    import pigpio
    print('PiGPIO     Available')
except:
    print('PiGPIO     Unavailable. Install with "pip install pigpio"')

try:
    import RPi.GPIO
    print('RPi.GPIO     Available')
except:
    print('RPi.GPIO     Unavailable. Install with "pip install RPi.GPIO"')
    
try:
    import matplotlib
    print('matplotlib     Available', 'Version: ', matplotlib.__version__)
except:
    print('matplotlib     Unavailable. Install with "pip install matplotlib"')    
# sudo apt-get install libopenblas-dev  
        
try:
    import numpy
    print('numpy     Available', 'Version: ', numpy.__version__)
except:
    print('numpy     Unavailable. Install with "pip install numpy"')
    
try:
    import scipy
    print('scipy     Available', 'Version: ', scipy.__version__)
except:
    print('scipy     Unavailable. Install with "pip install scipy"')    

try:
    import cv2
    print('OpenCV     Available', 'Version: ', cv2.__version__)
except:
    print('OpenCV     Unavailable. Install with "pip install cv2"') 

try:
    import pandas
    print('pandas     Available', 'Version: ', pandas.__version__)
except:
    print('pandas     Unavailable. Install with "pip install numpy"')    

try:
    import yagmail
    print('yagmail     Available', 'Version: ', yagmail.__version__)
except:
    print('yagmail     Unavailable. Install with "pip install yagmail"')
# sudo apt-get install libxml2-dev libxslt-dev  

try:
    import requests
    print('requests     Available', 'Version: ', requests.__version__)
except:
    print('requests     Unavailable. Install with "pip install requests"')
    
try:
    import dweepy
    print('dweepy     Available', 'Version: ', 'Installed but doesn\'t have a .__version__ attribute')
except:
    print('dweepy     Unavailable. Install with "pip install dweepy"')
    
try:
    import flask
    version = importlib.metadata.version("flask")
    print('flask	Available.', 'Version: ', version)
except:
    print('flask     Unavailable. Install with "pip install flask"')

try:
    import dash
    print('dash	Available.', 'Version: ', dash.__version__)
except:
    print('dash     Unavailable. Install with "pip install flask"')


try:
    import plotly
    print('plotly	Available', 'Version: ', plotly.__version__)
except:
    print('plotly     Unavailable. Install with "pip install plotly"')
    
    
try:
    import ipywidgets
    print('ipywidgets     Available', 'Version: ', ipywidgets.__version__)
except:
    print('ipywidgets     Unavailable. Install with "pip install ipywidgets"')

try:
    import json
    print('json     Available', 'Version: ', json.__version__)
except:
    print('json     Unavailable. Install with "pip install json"')
    
try:
    import simplejson
    print('simplejson     Available', 'Version: ', simplejson.__version__)
except:
    print('simplejson     Unavailable. Install with "pip install simeplejson"')


try:
    import datetime
    print('datetime     Available', 'Version: ', 'Standard with Python installation')
except:
    print('datetime     Unavailable. Install with "pip install datetime"')
    
try:
    import time
    print('time     Available', 'Version: ', 'Standard with Python installation')
except:
    print('time     Unavailable. Install with "pip install time"')   