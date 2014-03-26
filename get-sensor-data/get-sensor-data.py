'''
Created on Mar 25, 2014

@author: asraf
'''

from Phidgets.PhidgetException import PhidgetErrorCodes, PhidgetException
from Phidgets.Devices.InterfaceKit import InterfaceKit


def sensorChanged(e):
    print("Sensor %i: %i" % (e.index, e.value))
    return 0


# Create InterfaceKit device
try:
    device = InterfaceKit()
    print("InterfaceKit created..")
except RuntimeError as e:
    print("Runtime error: %s" % e.message)


 
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

