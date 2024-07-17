import serial
import socketio, time
import json
import signal
import threading
import sys
from yap import yap
# Ensures the program gets shut down and doesn't hang on waiting for serial data
signal.signal(signal.SIGINT, signal.SIG_DFL)

# Get config settings
configSettings = {}
with open("configuration/config.json", "r") as configData:
    # Load the JSON data
    configSettings = json.load(configData)

yapper = yap.Yapper()

# Serial port configuration
try:
    ser = serial.Serial(configSettings.get('serialPort', '/dev/ttyAMA1'), 9600) #/dev/ttyAMA1 is the default, if config doesn't have it
    print("Checking Port Open:",ser.isOpen())
    time.sleep(0.5)
    ser.write("$$screen=3=Serial Connected\r\n".encode())

except Exception as e:
    print("Failed to connect to serial port. Exiting...", e)
    ser.close()
    sys.exit()

def read_from_port(ser):
    while True:
        if ser.in_waiting > 0:
            try:
                line = ser.readline().decode('utf-8')
                # line = ser.readline()
                print("Received:", line)
                yapper.send("serial/out",line)
            except:
                print("error parsing")

thread = threading.Thread(target=read_from_port, args=(ser,))
thread.daemon = True
thread.start()

# Receive and process messages
while True:
    messages = yapper.waitForMessages("serial")
    for message in messages:
        print("sending out the serial port:",message)
        ser.write(message.encode())