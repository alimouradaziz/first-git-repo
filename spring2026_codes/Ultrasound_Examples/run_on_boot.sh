#!/bin/bash
#File: LED_examples/run_on_boot.sh

# Absolute path to Virtual Environment python interpreter
PYTHON=/home/pi/Desktop/spring2026_codes/Ultrasound_Examples/venv/bin/python

# Absolute path to Python script
SCRIPT=/home/pi/Desktop/spring2026_codes/Ultrasound_Examples/UltrasonicLED_3.py

# Absolute path to output log file
LOG=/home/pi/Desktop/spring2026_codes/Ultrasound_Examples/UltrasonicLED_3.log

echo -e "\n####### STARTUP $(date) ######\n" >> $LOG

$PYTHON $SCRIPT >> $LOG 2>&1
