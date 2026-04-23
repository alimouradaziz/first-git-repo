import requests
import time
import random
from sense_hat import SenseHat
import time

sense = SenseHat()

while True:
    print('Sending data to ThingSpeak')
    
    t = sense.get_temperature()
    p = sense.get_pressure()
    h = sense.get_humidity()
        
    t = round(t,1)
    p = round(p,1)
    h = round(h,1)
        
    msg = "Temp = %s C, Pressure = %s mbar, Humidity =%s" % (t, p, h)
        
    sense.show_message(msg, scroll_speed=0.05)
    
    # attempt to publish this data to the topic.
    try:    
#     data = random.randint(0, 200)
        URL = 'https://api.thingspeak.com/update?api_key=PDMSVQEHEWRAAD5K&field1='+str(t)+'&field2='+str(p)+'&field3='+str(h)    
        r = requests.get(URL)
        print(r)
        print(t, p, h)
        time.sleep(5)
    except keyboardInterrupt:
        break
    except Exception as e:
        print(e)
        
    sense.clear()