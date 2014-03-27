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

WAIT_TIME = 10000
TRIGGERING_POINT_TEMPERATURE = 1
TRIGGERING_POINT_HUMIDITY = 2


temperature = 0
humidity = 0

outfile = open("sensor-data.csv", "w")
outfile.write("Time, Temperature(C), Humidity(%) \n")


# Formula for converting raw Temperature data to human readable unit (C)
def temperatureFormula(raw_data):
    temp = (raw_data * 0.22222) - 61.11
    return '%.2f' % temp


# Formula for converting raw Humidity data to human readable unit (%)
def humidityFormula(raw_data):
    humid = (raw_data * 0.1906) - 40.2
    return '%.2f' % humid


# Event listener action
def sensorChanged(e):
    #print("Sensor %i: %i" % (e.index, e.value))
    global outfile
    global temperature
    global humidity
    
    if e.index == 0:        
        temperature = temperatureFormula(e.value) 
    elif e.index == 1:        
        humidity = humidityFormula(e.value)                     
    outfile.write(str(time()) + ", " + str(temperature) + ", " + str(humidity) + "\n")
    
    sys.stdout.write(".")
    sys.stdout.flush()    
    return 0


# Create InterfaceKit device
try:
    device = InterfaceKit()
    print("InterfaceKit created..")
except RuntimeError as e:
    print("Runtime error: %s" % e.message)


# Registering all sensors on change value event
device.setOnSensorChangeHandler(sensorChanged)


# Open it
try:
    device.openPhidget()
    print("InterfaceKit opened..")
except PhidgetException as e:    
    print("Phidget exception %i: %s" % (e.code, e.detail))


# Wait for device attachment
device.waitForAttach(WAIT_TIME)
print("Device(%d) attached!" % (device.getSerialNum()))

# Set trigger point
device.setSensorChangeTrigger(0, TRIGGERING_POINT_TEMPERATURE)
device.setSensorChangeTrigger(1, TRIGGERING_POINT_HUMIDITY)


print("Press Enter to end anytime...");
character = str(raw_input())

device.closePhidget()
exit(0)

#print(device.getSensorValue(0))
#print(device.getSensorValue(1))
