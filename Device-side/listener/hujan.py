import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN)
rain_state = False

def hujan():
    while True:
        if GPIO.input(18):
            rain_state = False
            time.sleep(1)
            return rain_state
            continue
        else:
            rain_state = True
            time.sleep(1)
            return rain_state
            break


#while True:
#    hujan()
