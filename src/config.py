'''
Created on Apr 04, 2014
@author: asraf
Global file to set up various fixed values
'''

URL = 'http://environmental-monitoring.herokuapp.com/'      # Server

WAIT_TIME = 10000                   # Wait time to attach the Phidget
OUT_FILE = 'sensor-data.csv'
CSV_HEADER = 'Time, Temperature(C), Humidity(%) \n'

TEMPERATURE_TRIGGERING_POINT = 1    # Event triggered if raw-data changed by 1 point
HUMIDITY_TRIGGERING_POINT = 1       # Event triggered if raw-data changed by 1 point
