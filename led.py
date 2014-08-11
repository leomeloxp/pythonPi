#!/usr/bin/env python

#importing modules
import time
import RPi.GPIO as GPIO

#set modes
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False) # disable silly warnings
#set pins
GPIO.setup(16,GPIO.OUT) #LED

i = 4
#Turn LED on
while (i > 0):
    GPIO.output(16,True)
    time.sleep(0.5)
    GPIO.output(16,GPIO.LOW)
    time.sleep(0.5)
    i-= 1

# Unset all pins
GPIO.cleanup
