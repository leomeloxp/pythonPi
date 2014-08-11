#!/usr/bin/env python

#importing modules
import time
import RPi.GPIO as GPIO

#set modes
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False) # disable silly warnings
#set pins
GPIO.setup(12,GPIO.OUT) #Buzzer
GPIO.setup(16,GPIO.OUT) #LED
GPIO.setup(18,GPIO.IN)  #Button

#How long will it run for? (in seconds)
i = 15
#Read button pres
while i > 0:
    print("Please press and hold the button")
    time.sleep(1)
    if (GPIO.input(18) == False):
        print("Button pressed")
    else:
        print("You didn't press it")
    i -= 1
# Unset all pins
GPIO.cleanup
