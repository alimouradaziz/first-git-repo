import RPi.GPIO as GPIO
import time

SOUND_PIN = 18 # GPIO18

GPIO.setmode(GPIO.BCM)
GPIO.setup(SOUND_PIN, GPIO.IN)

print("Sound sensor test started...")

try:
    while True:
        if GPIO.input(SOUND_PIN) == 1:
            print("Sound detected!")
        else:
            print("No sound")
        time.sleep(0.2)

except KeyboardInterrupt:
    print("Exiting...")
    GPIO.cleanup()