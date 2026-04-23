import RPi.GPIO as GPIO
import time
import math
from smbus import SMBus
import requests

# ------------------------
# GPIO Setup
# ------------------------
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

PIN_R = 21
PIN_G = 20
PIN_B = 16
PIN_LDR = 4

GPIO.setup(PIN_R, GPIO.OUT)
GPIO.setup(PIN_G, GPIO.OUT)
GPIO.setup(PIN_B, GPIO.OUT)
GPIO.setup(PIN_LDR, GPIO.IN)

# PWM for brightness control
pwm_r = GPIO.PWM(PIN_R, 500)
pwm_g = GPIO.PWM(PIN_G, 500)
pwm_b = GPIO.PWM(PIN_B, 500)

pwm_r.start(0)
pwm_g.start(0)
pwm_b.start(0)

# ------------------------
# MPU6050 Setup
# ------------------------
bus = SMBus(1)
MPU_ADDR = 0x68
PWR_MGMT_1 = 0x6B
ACCEL_XOUT_H = 0x3B
ACCEL_SCALE = 16384.0

bus.write_byte_data(MPU_ADDR, PWR_MGMT_1, 0)

def read_word(reg):
    high = bus.read_byte_data(MPU_ADDR, reg)
    low = bus.read_byte_data(MPU_ADDR, reg+1)
    val = (high << 8) + low
    if val >= 0x8000:
        val = -((65535 - val) + 1)
    return val

def read_accel_magnitude():
    ax = read_word(ACCEL_XOUT_H) / ACCEL_SCALE
    ay = read_word(ACCEL_XOUT_H+2) / ACCEL_SCALE
    az = read_word(ACCEL_XOUT_H+4) / ACCEL_SCALE
    return math.sqrt(ax*ax + ay*ay + az*az)

def led_off():
    pwm_r.ChangeDutyCycle(0)
    pwm_g.ChangeDutyCycle(0)
    pwm_b.ChangeDutyCycle(0)

def led_green():
    pwm_r.ChangeDutyCycle(0)
    pwm_g.ChangeDutyCycle(80)
    pwm_b.ChangeDutyCycle(0)

def led_red():
    pwm_r.ChangeDutyCycle(80)
    pwm_g.ChangeDutyCycle(0)
    pwm_b.ChangeDutyCycle(0)

print("Neocoast integration running... Ctrl+C to stop")

motion_history = []

try:
    while True:

        # ---- Read light ----
        dark = GPIO.input(PIN_LDR) == 1

        # ---- Read motion ----
        amag = read_accel_magnitude()
        motion_signal = abs(amag - 1.0)
        speed = motion_signal

        motion_history.append(motion_signal)
        if len(motion_history) > 5:
            motion_history.pop(0)

        moving = sum(motion_history)/len(motion_history) > 0.07

        # ---- Decision logic ----
        if not dark:
            led_off()
            state = "DAY"

        else:
            if moving:
                led_green()
                state = "NIGHT + MOVING"
            else:
                led_red()
                state = "NIGHT + STOPPED"

        #print(f"Light: {'DARK' if dark else 'BRIGHT'} | Motion: {motion_signal:.3f} | State: {state}")
        print (f"Light: {'Dark' if dark else 'BRIGHT'} | "
               f"Motion: {motion_signal:3f} | "
               f"State: {state}")

        payload = {
            "speed": float(speed),
            "amag": float(amag),
            "motion": "moving" if moving else "stopped",
            "daymode": not dark,
            "ts": time.time(),
        }
        try:
           requests.post("http://127.0.0.1:4000/api/state", json=payload, timeout=0.5)
        except Exception as e:
           # Flask might not be up yet on boot; don't crash
           print(f"POST failed (will retry): {e}")

        time.sleep(0.2)

except KeyboardInterrupt:
    led_off()
    GPIO.cleanup()
    bus.close()
