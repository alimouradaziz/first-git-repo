from flask import Flask, request, jsonify
from gpiozero import Device, LED
from gpiozero.pins.pigpio import PiGPIOFactory

LED_GPIO_PIN = 17

Device.pin_factory = PiGPIOFactory()
led = LED(LED_GPIO_PIN)
last_state = None

app = Flask(__name__)

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

# @app.route("/led", methods=["POST"])
# def led_control():
#     data = request.get_json(silent=True) or {}
#     state = data.get("state")
#     new_state = set_led_state(state)
#     return jsonify({"state": new_state}), 200

# @app.route("/led", methods=["GET"])
# def led_status():
#     return jsonify({"state": last_state or "off"}), 200
# 
# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=5000)


@app.route("/led", methods=["GET"])
def led_control():
    #read state from query string, e.g. /led?state=on
    state = request.args.get("state")
    if state is None:
        # just report current state if no state given
        return jsonify({"state": last_state or "off"}), 200
    
    new_state = set_led_state(state)
    return jsonify({"state": new_state}), 200

if __name__ == "__main__":
    app.run(host="192.168.22.147", port=5000, debug=False)

