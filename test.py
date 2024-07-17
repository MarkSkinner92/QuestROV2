import yap
import time
import random

yapper = yap.Yapper()

while True:
    try:
        print("sending a random value")
        yapper.send("serial",{"topic":"cool","data":random.random()})
        time.sleep(1)

    except KeyboardInterrupt:
        break

print("stopping")
yapper.shutup()