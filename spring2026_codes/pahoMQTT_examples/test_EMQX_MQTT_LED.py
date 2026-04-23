import paho.mqtt.client as mqtt
from paho.mqtt.client import CallbackAPIVersion
# from flask import Flask, request, jsonify
from gpiozero import Device, LED
from gpiozero.pins.pigpio import PiGPIOFactory

LED_GPIO_PIN = 17

Device.pin_factory = PiGPIOFactory()
led = LED(LED_GPIO_PIN)
last_state = None

def set_led_state(state: str):
    global last_state
    s = (state or "").strip().lower()
    if s == last_state:
        return s

    if s == "on":
        led.on()
    elif s == "blink":
        led.blink()
    else:
        s = "off"
        led.off()

    last_state = s
    return s


MQTT_BROKER = "broker.emqx.io"   # example public broker
MQTT_PORT = 1883
MQTT_TOPIC = "my/device/led"     # choose your own topic
client_id = 'python-mqtt-test'

def on_connect(client, userdata, flags, rc, properties):
    print("Connected with result code", rc)
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    payload = msg.payload.decode("utf-8")
    # Expect payload like "on", "off", "blink"
    set_led_state(payload)
    print(f"{msg.topic}: {msg.payload.decode()}")

# mqtt_client = mqtt.Client()
mqtt_client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2, client_id)

mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message
mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
mqtt_client.loop_forever()

# # Example using mosquitto_pub
# mosquitto_pub -h broker.emqx.io -t my/device/led -m "on"
# mosquitto_pub -h broker.emqx.io -t my/device/led -m "off"
# mosquitto_pub -h broker.emqx.io -t my/device/led -m "blink"

