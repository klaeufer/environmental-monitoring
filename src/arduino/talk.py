import serial
import struct
from time import sleep

WAIT_TIME_IN_SECONDS = 5
port = serial.Serial('/dev/ttyACM0', 9600, xonxoff=True)
if (port.isOpen() == False):
    port.open()

port.flushInput()
port.flushOutput()

while True:
	numBytesInBuffer = port.inWaiting()
	while (numBytesInBuffer != 0):
		buf = port.read(2) #Read 2 bytes
		rawValue = struct.unpack('H', buf)[0] #Convert to 16 bit int
		degrees = (rawValue * 0.2222) - 61.111
		print(degrees)
		numBytesInBuffer = numBytesInBuffer - 2
	sleep(WAIT_TIME_IN_SECONDS)
