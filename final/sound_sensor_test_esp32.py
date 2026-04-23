print("STARTING...")

from machine import ADC, Pin
import time

sound = ADC(Pin(34))
sound.atten(ADC.ATTN_11DB)
sound.width(ADC.WIDTH_12BIT)

print("ADC SETUP DONE")

while True:
        print("LOOP RUNNING")
        val = sound.read()
        print(val)
        time.sleep(1)

def read_avg(samples=20):
    total=0
    for _ in range(samples):
        total += sound.read()
        time.sleep_ms(2)
        return total // samples
    baseline = read_avg(50)
    while True:
        raw = sound.read()
        avg = read_avg(10)
        level = avg - baseline
        if level < 0:
            level = 0
            print("raw:", raw, "avg:", avg, "level:", level)
            time.sleep(0.1)
            
               
