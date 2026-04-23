# Source: https://www.emqx.com/en/blog/use-mqtt-with-raspberry-pi
# publisher.py
import paho.mqtt.client as mqtt
import time
import json

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")

    data = {"Hello World": 2025}
    # Send a message to the raspberry/topic every 1 second, 5 times in a row
    for i in range(10):
        # The four parameters are topic, sending content, QoS and whether retaining the message respectively
#         client.publish('raspberry/topic', json.dumps(data), payload=i, qos=0, retain=False)
        client.publish('raspberry/topic', json.dumps(data))
        print(f"send {i} to raspberry/topic")    

client = mqtt.Client()
client.on_connect = on_connect
client.connect("broker.emqx.io", 1883, 60)
# broker_address = "18.215.48.160"
# broker_address = "192.168.22.147"
# client.connect(broker_address, 1883, 60)


client.loop_forever()
