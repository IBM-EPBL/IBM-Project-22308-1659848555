"""
 LED BLINKING
 ASSIGNMENT 3
"""

import RPi.GPIO as GPIO 
import time

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(8, GPIO.OUT, initial=GPIO.LOW) 

while True:
 GPIO.output(8, GPIO.HIGH)
time.sleep(100)
 GPIO.output(8, GPIO.LOW)
 time.sleep(100)