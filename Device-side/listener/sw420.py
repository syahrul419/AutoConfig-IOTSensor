#!/usr/bin/python
import RPi.GPIO as GPIO
import time

#GPIO SETUP
channel = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)
vibration_state = False

def callback(channel):
    global vibration_state
    if GPIO.input(channel):
        vibration_state = True
    else:
        #print ("masuk else")
        vibration_state = False

    time.sleep (1) 
    return vibration_state

GPIO.add_event_detect(channel, GPIO.FALLING, bouncetime=300)  
GPIO.add_event_callback(channel, callback)  

# infinite loop
#while True:
#callback(channel)
#time.sleep(1)
        #return a        
