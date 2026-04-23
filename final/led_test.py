import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt
import time
import threading
import yagmail

# ----------------------------
# Email settings
# ----------------------------
EMAIL_USER = "mayaj.lerma@gmail.com"
EMAIL_APP_PASSWORD = "hzzs tgew kztq lhwn"
EMAIL_TO = "alimourad@gwu.edu"

yag_mail = yagmail.SMTP(
    user=EMAIL_USER,
    password=EMAIL_APP_PASSWORD,
    host="smtp.gmail.com"
)

last_email_event = None

def send_email(event):
    global last_email_event

    # Only send for important events
    if event not in ("KNOCK", "ALERT"):
        return

    if event == last_email_event:
        return

    try:
        if event == "KNOCK":
            subject = "Nur el Donya: Knock Detected"
            body = "Nur el Donya alert: Knock detected. LED changed to yellow."
        elif event == "ALERT":
            subject = "Nur el Donya: High Alert"
            body = "Nur el Donya alert: High-priority sound detected. LED changed to red."

        yag_mail.send(
            to=EMAIL_TO,
            subject=subject,
            contents=body
        )

        print("Email sent!")
        last_email_event = event

    except Exception as e:
        print("Email failed:", e)

# ----------------------------
# GPIO / MQTT settings
# ----------------------------
GPIO.setwarnings(False)

BROKER = "localhost"
TOPIC = "nureldonya/event"

RED = 17
GREEN = 27
BLUE = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(RED, GPIO.OUT)
GPIO.setup(GREEN, GPIO.OUT)
GPIO.setup(BLUE, GPIO.OUT)

stop_effect = False

def all_off():
    GPIO.output(RED, 0)
    GPIO.output(GREEN, 0)
    GPIO.output(BLUE, 0)

def set_color(red, green, blue):
    GPIO.output(RED, red)
    GPIO.output(GREEN, green)
    GPIO.output(BLUE, blue)

def idle_blue():
    all_off()
    set_color(0, 0, 1)

def knock_yellow_pulse():
    global stop_effect
    for _ in range(3):
        if stop_effect:
            idle_blue()
            return
        set_color(1, 1, 0)
        time.sleep(0.3)
        all_off()
        time.sleep(0.2)
    idle_blue()

def alert_red_flash():
    global stop_effect
    for _ in range(6):
        if stop_effect:
            idle_blue()
            return
        set_color(1, 0, 0)
        time.sleep(0.2)
        all_off()
        time.sleep(0.2)
    idle_blue()

def run_effect(event):
    global stop_effect

    if event == "IDLE":
        return

    stop_effect = True
    time.sleep(0.05)
    stop_effect = False

    if event == "KNOCK":
        t = threading.Thread(target=knock_yellow_pulse, daemon=True)
        t.start()
    elif event == "ALERT":
        t = threading.Thread(target=alert_red_flash, daemon=True)
        t.start()

def on_connect(client, userdata, flags, rc):
    print("Connected with result code", rc)
    client.subscribe(TOPIC)

def on_message(client, userdata, msg):
    global last_email_event
    event = msg.payload.decode().strip()
    print("Received event:", event)

    if event == "IDLE":
        last_email_event = None

    run_effect(event)
    send_email(event)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

try:
    idle_blue()
    client.connect(BROKER, 1883, 60)
    client.loop_forever()

except KeyboardInterrupt:
    print("Exiting...")

finally:
    all_off()
    GPIO.cleanup()