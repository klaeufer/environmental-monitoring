Platform:
=========
1. Raspbian OS on Raspberry Pi
#. Phidget Interface Kit 8/8/8 (I/O board)
#. Python with version 2.7 or 3.2

Context:
========
There is a bug with Phidget's Python library. If you want to work with Phidget I/O board using this library on Raspberry Pi then there might be a problem in running your script. 
It may throw an **AttributError** exception all time. 

I had tried to run sample TemperatureSensor script provided by Phidget support and got the following errors:
	
	pi@raspberrypi ~/Python $ sudo python TemperatureSensor-simple.py
	Traceback (most recent call last):
	  File "TemperatureSensor-simple.py", line 71, in <module>
	    temperatureSensor.setOnAttachHandler(TemperatureSensorAttached)
	  File "/usr/local/lib/python2.7/dist-packages/Phidgets/Phidget.py", line 655, in setOnAttachHandler
	    self.__onAttach = self.__ATTACHHANDLER(self.__nativeAttachEvent)
	**AttributeError: TemperatureSensor instance has no attribute '_Phidget__ATTACHHANDLER'**


