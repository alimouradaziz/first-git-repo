# Source: https://www.emqx.com/en/blog/use-mqtt-with-raspberry-pi
# publisher_Serial.py
import paho.mqtt.client as mqtt
import serial


# Establishing the connection with the serial port
ser = serial.Serial(
    # Serial Port to read the data from
    port='/dev/ttyAMA0', # Use `dmesg | grep tty` to find the port
    baudrate=9600,
    parity=serial.PARITY_NONE,
    stopbits=serial.STOPBITS_ONE,
    bytesize=serial.EIGHTBITS,
    timeout=1
)

broker_address = "broker.emqx.io"
broker_port = 1883
topic = "emqx/serial/write"


def on_connect(client, userdata, flags, rc):
    print("Connected to MQTT broker")
    client.subscribe(topic)


def on_message(client, userdata, msg):
    payload = msg.payload.decode()
    print("Received message: {payload} on topic {topic}".format(payload=payload, topic=msg.topic))
    # Write data to serial port
    ser.write(payload.encode())


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker_address, broker_port)
client.loop_forever()
