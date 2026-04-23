from flask import Flask, jsonify, render_template, request
import json
import os
import time

APP_DIR = os.path.dirname(os.path.abspath(__file__))

# neocoast.py writes here
STATE_PATH = "/home/pi/Desktop/midterm/state.json"

app = Flask(
    __name__,
    template_folder=os.path.join(APP_DIR, "templates"),
    static_folder=os.path.join(APP_DIR, "static"),
)

@app.route("/")
def index():
    # Your pretty dashboard HTML should be templates/index.html
    return render_template("index.html")

@app.route("/api/state", methods=["GET", "POST"])
def api_state():
    default = {
        "ts": time.time(),
        "daymode": True,
        "motion": "stopped",
        "speed": 0.0,
        "ax": 0.0, "ay": 0.0, "az": 0.0,
        "amag": 0.0,
    }

    if request.method == "POST":
        data = request.get_json(silent=True) or {}
        # fill missing keys
        for k, v in default.items():
            data.setdefault(k, v)

        # save so GET/dashboard can read it
        try:
            with open(STATE_PATH, "w") as f:
                json.dump(data, f)
        except Exception as e:
            return jsonify({"ok": False, "error": str(e)}), 500

        return jsonify({"ok": True})

    # GET behavior (your existing code)
    try:
        with open(STATE_PATH, "r") as f:
            data = json.load(f)
        for k, v in default.items():
            data.setdefault(k, v)
        return jsonify(data)
    except FileNotFoundError:
        return jsonify(default)
    except Exception as e:
        default["error"] = str(e)
        return jsonify(default), 200

    try:
        with open(STATE_PATH, "r") as f:
            data = json.load(f)

        # Ensure all keys exist (in case file is partially written)
        for k, v in default.items():
            data.setdefault(k, v)

        return jsonify(data)

    except FileNotFoundError:
        # neocoast.py hasn't written state.json yet
        return jsonify(default)

    except Exception as e:
        # Any other parse/read error
        default["error"] = str(e)
        return jsonify(default), 200

if __name__ == "__main__":
    # host=0.0.0.0 makes it reachable from your laptop/phone
    app.run(host="0.0.0.0", port=4000, debug=False)
