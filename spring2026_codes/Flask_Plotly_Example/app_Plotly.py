"""
Source code written by Kartik Bulusu
==== Description:
======== flask API implementation for IoT demonstration in CS4907   
==== Testing:
==== 1. Developed on 02/22/2024 using Python 3.10.11 on Macbook Pro using Thonny IDE
====
==== Reference: https://towardsdatascience.com/web-visualization-with-plotly-and-flask-3660abf9c946
"""

from flask import Flask, render_template, request
import pandas as pd
import json
import plotly
import plotly.express as px
import random
import numpy as np
import matplotlib.pyplot as plt
import time

# ======== Initialize Logging ===========
import thing_file

# # Global logging configuration
# logging.basicConfig(level=logging.WARNING)  
# 
# # Logger for this module
# logger = logging.getLogger('main')
# 
# # Debugging for this file.
# logger.setLevel(logging.INFO)

V = []
T = []

app = Flask(__name__)

@app.route('/'+thing_file.thing_name)

def notdash():
    data = {
        'time': [],
        'Voltage': [],
    }        
    # Create the graph with subplots
    fig = plotly.tools.make_subplots(rows=1, cols=1, vertical_spacing=0.2)
    fig['layout']['margin'] = {
        'l': 30, 'r': 10, 'b': 30, 't': 10
    }
    
    for i in range(20):
#         time = datetime.datetime.now() - datetime.timedelta(seconds=i*20)
        data['Voltage'].append(random.randint(0, 100))
        data['time'].append(i)
        
        fig.append_trace({
            'x': data['time'],
            'y': data['Voltage'],
            'name': 'Voltage',
            'mode': 'lines+markers',
            'type': 'scatter'
        }, 1, 1)
#         time.sleep(0.5)
    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return render_template('notdash.html', graphJSON=graphJSON)
    

if __name__ == '__main__':

    # If you have debug=True and receive the error "OSError: [Errno 8] Exec format error", then:
    # remove the execuition bit on this file from a Terminal, ie:
    # chmod -x flask_api_server.py
    #
    # Flask GitHub Issue: https://github.com/pallets/flask/issues/3189

    app.run(host="0.0.0.0", port=5000, debug=True) 