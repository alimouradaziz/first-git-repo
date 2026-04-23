# =================Import libraries=================================
import smtplib
from email.message import EmailMessage
import ssl

import time
from time import asctime

# ================= Emailing the English, Spanish and Spanish_audio messages ========

email_sender = "cs3907.edgelab@gmail.com"
email_password = "plll dqml iyid vbok"
email_receiver = ["kartik.bulusu@gmail.com"]

now = str(asctime())

msg = EmailMessage()
msg['From'] = email_sender
msg['To'] = email_receiver
msg['Subject'] = "Message from Prof. Kartik Bulusu, MAE 6291 Spring 2026"

header = "Prof. Bulusu send you a message on " + now + '\n'
text = """
Dear Edge-Lab: \n
If you are seeing this email you are getting an automated message from my Raspberry Pi. \n
We are opening yet another door to IoT and Edge Compute in MAE 6291 Spring 2025. \n

The in-class exrecise will teach you the following skills:
1. How-to send emails from a Python script using gmail.
2. How-to set up gmail service with a unique app-name and app-password outlined in the following source:
https://www.youtube.com/watch?v=zxFXnLEmnb4

Best wishes
Professor Bulusu

Associate Research Professor
Department of Mechanical and Aerospace Engineering
The George Washington University
"""

body = header + text
msg.set_content(body)


# with open('FRIES_Bulusu_Msg4.mp3', 'rb') as f: # r for read and b for binary
#     file_data = f.read()
#     file_name = f.name
    
# msg.add_attachment(file_data, maintype='audio', subtype='mp3', filename=file_name)

context = ssl.create_default_context()

with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, msg.as_string())

