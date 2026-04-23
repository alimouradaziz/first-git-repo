import time
import paho.mqtt.client as mqtt
import requests
import random
from sense_hat import SenseHat
import time

# ===== ThingSpeak MQTT device credentials =====
MQTT_HOST = "mqtt3.thingspeak.com"
MQTT_PORT = 1883

CLIENT_ID = "EjISOjcGFy4FDBU6NycZIRE"
USERNAME = "EjISOjcGFy4FDBU6NycZIRE"
PASSWORD = "lQAMrj9zCXqYLnUmht6YJBzK"

# username = EjISOjcGFy4FDBU6NycZIRE
# clientId = EjISOjcGFy4FDBU6NycZIRE
# password = lQAMrj9zCXqYLnUmht6YJBzK

# ===== Your ThingSpeak channel details =====
CHANNEL_ID = "2921140"

# Publish to one field
TOPIC = f"channels/2921140/publish"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to ThingSpeak MQTT broker.")
    else:
        print(f"Connection failed with code {rc}")
                

client = mqtt.Client(client_id=CLIENT_ID, protocol=mqtt.MQTTv311)
client.username_pw_set(USERNAME, PASSWORD)
client.on_connect = on_connect

client.connect(MQTT_HOST, MQTT_PORT, 60)
client.loop_start()

time.sleep(2)

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
    
#     # Values for 3 fields
#     FIELD1_VALUE = 25.4
#     FIELD2_VALUE = 60
#     FIELD3_VALUE = 1012

    
    VALUE = (
        f"&field1={t}"
        f"&field2={p}"
        f"&field3={h}"
        )
#    VALUE = "25.4"
    result = client.publish(TOPIC, payload=VALUE, qos=0)

    if result.rc == 0:
        print(f"Published {VALUE} to {TOPIC}")
    else:
        print("Publish failed")

time.sleep(2)
client.loop_stop()
client.disconnect()