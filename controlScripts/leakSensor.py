import time
from yap import yap
import json
import RPi.GPIO as GPIO

print("Starting Leak Sensor Node...")

leakPIN = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(leakPIN, GPIO.IN)

yapper = yap.Yapper()

print("Ready to Detect Leaks at 1hz")

counter = 0
while True:
    if(GPIO.input(leakPIN)):
        yapper.send('web',['leak',"1"])
        time.sleep(3)
    time.sleep(0.5)
