#!/bin/bash
PY="/usr/bin/python3"
BASE="/home/pi/Desktop/midterm"

NEO="$BASE/neocoast.py"
APP="$BASE/dashboard/app.py"

LOG1="$BASE/neocoast.log"
LOG2="$BASE/dashboard.log"

# Prevent duplicates (use patterns that match the running commands)
pkill -f "python3.*neocoast.py" || true
pkill -f "python3.*/dashboard/app.py" || true

echo "####### STARTUP $(date) #######" >> "$LOG1"
echo "####### STARTUP $(date) #######" >> "$LOG2"

# Give boot/network a moment
sleep 10

# Start Neocoast logic
nohup "$PY" "$NEO" >> "$LOG1" 2>&1 &

# Wait until Flask is accepting connections on 4000 (max ~30s)
for i in $(seq 1 30); do
  if curl -s http://127.0.0.1:4000/api/state >/dev/null 2>&1; then
    echo "Flask is up on port 4000" >> "$LOG2"
    break
  fi
  sleep 1
done

# Start Dashboard (Flask)
nohup "$PY" "$APP" >> "$LOG2" 2>&1 &

# Wait for Flask to be up (optional but nice)
for i in $(seq 1 40); do
  if curl -s http://127.0.0.1:4000/api/state >/dev/null 2>&1; then
    echo "Flask is up" >> "$LOG2"
    break
  fi
  sleep 1
done

# Start Neocoast (auto-restart)
nohup bash -lc "while true; do $PY $NEO >> $LOG1 2>&1; echo 'neocoast exited, restarting in 2s' >> $LOG1; sleep 2; done" >> $LOG1 2>&1 &
