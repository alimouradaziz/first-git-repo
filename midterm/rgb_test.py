from gpiozero import RGBLED
from time import sleep

COLORS = [(1, 0, 0), (0, 1, 0), (1, 1, 1)]
led = RGBLED(red=21, green=20, blue=16)

try:
	while True:
		for color in COLORS:
			led.color = color
			print(f"Color set to: {color}")
			sleep(1)

except KeyboardInterrupt:
	pass
