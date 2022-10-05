"""
TRAFFIC LIGHT CONTROL
ASSIGNMENT 3
"""

import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(9, GPIO.OUT) #GREEN
GPIO.setup(10, GPIO.OUT) #RED
GPIO.setup(11, GPIO.OUT) #ORANGE


GPIO.output(9, False)
GPIO.output(10, False)
GPIO.output(11, False)
GPIO.cleanup()

while True: 
    
    GPIO.output(9, True) 
    time.sleep(300)  
     
    GPIO.output(10, True) 
    time.sleep(100)  

    GPIO.output(9, False) 
    GPIO.output(10, False) 
    GPIO.output(11, True) 
    time.sleep(500)  

    GPIO.output(11, False) 
    GPIO.output(10, True) 
    time.sleep(200)  

    GPIO.output(10, False)