'''
Created on Mar 25, 2014

@author: asraf
'''

from Phidgets.PhidgetException import PhidgetErrorCodes, PhidgetException
from Phidgets.Devices.InterfaceKit import InterfaceKit

from time import time
import sys


temperature = 0
humidity = 0

outfile = open("sensor-data.csv", "w")
outfile.write("Time, Temperature, Humidity \n")

# Event listener action
def sensorChanged(e):
    #print("Sensor %i: %i" % (e.index, e.value))
    global outfile
    global temperature
    global humidity
    
    if e.index == 0:
        temperature = e.value                
    elif e.index == 1:
        humidity = e.value                        
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
device.waitForAttach(10000)
print("Device(%d) attached!" % (device.getSerialNum()))

# Set trigger point
device.setSensorChangeTrigger(0, 1)
device.setSensorChangeTrigger(1, 2)


print("Press Enter to end anytime...");
character = str(raw_input())

device.closePhidget()
exit(0)

#print(device.getSensorValue(0))
#print(device.getSensorValue(1))
