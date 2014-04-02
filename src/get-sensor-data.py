'''
Created on Mar 25, 2014
@author: asraf

This script fetches raw data from Temperature and Humidity sensors attached with Phidgets 
and converts them into human readable format. Data are collected based on the 
event triggered by each individual sensor.

Temperature sensor --> Triggers an event when raw data changed by 1 point (default)
Humidity sensor    --> Triggers an event when raw data changed by 2 point (default)
'''

from Phidgets.PhidgetException import PhidgetErrorCodes, PhidgetException
from Phidgets.Devices.InterfaceKit import InterfaceKit

from time import time
import sys
import requests

# Define constants
WAIT_TIME = 10000
TEMPERATURE_TRIGGERING_POINT = 1    # Event triggered if raw-data changed by 1 point
HUMIDITY_TRIGGERING_POINT = 1       # Event triggered if raw-data changed by 1 point
URL = 'http://environmental-monitoring.herokuapp.com/'


temperature = 0
humidity = 0

outfile = open("sensor-data.csv", "w")
outfile.write("Time, Temperature(C), Humidity(%) \n")


# Formula for converting raw Temperature data to meaningful unit (C)
def temperatureFormula(raw_data):
    temp = (raw_data * 0.22222) - 61.11
    return '%.2f' % temp


# Formula for converting raw Humidity data to meaningful unit (%)
def humidityFormula(raw_data):
    humid = (raw_data * 0.1906) - 40.2
    return '%.2f' % humid


# Event/Change listener action
def sensorChanged(e):
    #print("Sensor %i: %i" % (e.index, e.value))
    global outfile
    global temperature
    global humidity
    
    dt = time()
    
    if e.index == 0:                                    # Port 0 = Temperature
        temperature = temperatureFormula(e.value) 
    elif e.index == 1:                                  # Port 1 = Humidity
        humidity = humidityFormula(e.value)                     
    
    outfile.write(str(dt) + ", " + str(temperature) + ", " + str(humidity) + "\n")
    
    # making json data format to dump on to server 
    payload = {'datetime': dt, 'temp': temperature, 'humid': humidity}
    
    
    sys.stdout.write(".")
    sys.stdout.flush()    
    return 0



# Create InterfaceKit
def createIK():
    try:
        device = InterfaceKit()
        print("InterfaceKit created..")
        return device
    except RuntimeError as e:
        print("Runtime error: %s" % e.message)



# Open InterfaceKit
def openIK(device):
    try:
        device.openPhidget()
        print("InterfaceKit opened..")
    except PhidgetException as e:    
        print("Phidget exception %i: %s" % (e.code, e.detail))




def start():
    # Create Interface Kit
    device = createIK()
    
    # Registering all sensors on change value event
    device.setOnSensorChangeHandler(sensorChanged)

    # Open it
    openIK(device)
    
    # Wait for device to be attached
    device.waitForAttach(WAIT_TIME)
    print("Device(%d) attached!" % (device.getSerialNum()))    
    
    # Set trigger point
    device.setSensorChangeTrigger(0, TEMPERATURE_TRIGGERING_POINT)      # Port 0 = Temperature
    device.setSensorChangeTrigger(1, HUMIDITY_TRIGGERING_POINT)         # Port 1 = Humidity

    # Exit
    print("Press Enter to end anytime...");
    character = str(raw_input())
    
    device.closePhidget()
    exit(0)

    
if __name__ == '__main__':
    start()

#print(device.getSensorValue(0))
#print(device.getSensorValue(1))
