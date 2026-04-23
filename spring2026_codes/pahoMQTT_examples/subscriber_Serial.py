
import time

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
topic = "emqx/serial/read"

client = mqtt.Client()
client.connect(broker_address, broker_port)

# Read data from serial port and publish it to MQTT broker
for i in range(10):
    data = ser.readline().decode()
    client.publish(topic, data)
    print("Read data {data} from serial port and publish it to MQTT broker".format(data=data))
    time.sleep(1)


client.disconnect()

ser.close()
