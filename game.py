#!/usr/bin/env python

#importing modules
import time
import RPi.GPIO as GPIO
import random

#set modes
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False) # disable silly warnings
#set pins
GPIO.setup(12,GPIO.OUT) #Buzzer
GPIO.setup(16,GPIO.OUT) #LED
GPIO.setup(18,GPIO.IN)  #Button

#How long should this run for?
i = int(input("How many tries you want to have?"))
score = 0
#Turn LED on
while i > 0:
    time.sleep(random.randint(0,3))
    GPIO.output(16,True)
    time.sleep(0.5)
    GPIO.output(16,GPIO.LOW)
    if (GPIO.input(18) == False):
        GPIO.output(12,True)
        time.sleep(0.5)
        GPIO.output(12,GPIO.LOW)
        score += 1
    else:
        print("You missed the button")
    i -= 1

print("Your score was ", score,". Well done!")
# Unset all pins
GPIO.cleanup
