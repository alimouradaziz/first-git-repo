import RPi.GPIO as GPIO
import time

PIN = 4

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(PIN, GPIO.IN)

try:
	while True:
		if GPIO.input(PIN):
			print("Darkness detected")
		else:
			print("Light detected")
		time.sleep(0.5)
except KeyboardInterrupt:
	GPIO.cleanup()
