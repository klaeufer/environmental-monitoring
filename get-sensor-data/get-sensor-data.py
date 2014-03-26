'''
Created on Mar 25, 2014

@author: asraf
'''

from Phidgets.PhidgetException import PhidgetErrorCodes, PhidgetException
from Phidgets.Devices.InterfaceKit import InterfaceKit


# Create InterfaceKit device
try:
    device = InterfaceKit()
    print("InterfaceKit created..")
except RuntimeError as e:
    print("Runtime error: %s" % e.message)
    

# Open it
try:
    device.openPhidget()
    print("InterfaceKit opened..")
except PhidgetException as e:    
    print("Phidget exception %i: %s" % (e.code, e.detail))


# Wait for device attachment
device.waitForAttach(10000)
print("Device(%d) attached!" % (device.getSerialNum()))


print(device.getSensorValue(0))
print(device.getSensorValue(1))
