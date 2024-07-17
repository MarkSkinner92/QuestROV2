import time
from yap import yap
import json
import math

yapper = yap.Yapper()

def sendJSON(topic,data):
    yapper.send('web',[topic, json.dumps(data)])
    print("sent IMU data")

counter = 0
while True:
    data = {
        "pitch" : 20*math.sin(counter/10),
        "roll" : 50*math.sin(counter/10),
        "heading" : 55
    }
    sendJSON("imu",data)
    counter += 1
    time.sleep(1/20)