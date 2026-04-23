"""
==== Prof. Kartik V. Bulusu
==== CS and MAE Departments, SEAS GWU
==== Description
======== This program sends email from the Python script on a Raspberry Pi.
======== import yagmail
======== It has been written exclusively for CS4907 students in GWU.
======== It may not be used for any other purposes unless author's prior permission is acquired.
"""

# import yagmail
# yag = yagmail.SMTP('cs3907.edgelab@gmail.com', 'plll dqml iyid vbok')
# yag.send(contents = "Hello!")

import yagmail
   
yag_mail = yagmail.SMTP(user='cs3907.edgelab@gmail.com', password="plll dqml iyid vbok", host='smtp.gmail.com')
  
To= "kartik.bulusu@gmail.com" # Use temp-mail.org for testing this code
Subject = "Welcome to MAE 6291!!"
Body = """
        Opening the doors to IoT and Edge Compute.

        This exercise will teach you the following skills:
        1. How-to send emails from a Python script.
        2. How-to how to set up gmail service with a unique app-name and app-password outlined in the following sources:
        https://www.youtube.com/watch?v=zxFXnLEmnb4
        """
 
yag_mail.send(to=To, subject=Subject, contents=Body)
print("Email has been sent successfully to the receiver's address.")
