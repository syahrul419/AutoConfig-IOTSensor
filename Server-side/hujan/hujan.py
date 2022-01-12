import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(18,GPIO.IN)

while True:
    if not GPIO.input(18):
        print("hujan")
        time.sleep(1)
        continue
    else:
        print("tidak hujan")
        time.sleep(1)
        continue
