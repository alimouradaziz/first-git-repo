from gpiozero import Device, LED
from gpiozero.pins.pigpio import PiGPIOFactory
from time import sleep

Device.pin_factory = PiGPIOFactory()
led = LED(17)   # use the BCM pin you really wired

#led.on()
#sleep(2)
#led.off()
led.blink()
#led.off()