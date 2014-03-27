'''
Created on Mar 25, 2014

@author: asraf
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

# Event listener action
def sensorChanged(e):
    #print("Sensor %i: %i" % (e.index, e.value))
    global outfile
    global temperature
    global humidity
    
    if e.index == 0:
        raw_data = e.value
        temperature = (raw_data * 0.22222) - 61.11 
    elif e.index == 1:
        raw_data = e.value
        humidity = (raw_data * 0.1906) - 40.2                        
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
