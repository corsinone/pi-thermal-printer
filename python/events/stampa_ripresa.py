import datetime
import math
import serial
import time

"""log resume time"""
t = math.trunc(time.clock_gettime(time.CLOCK_REALTIME))
with open(filename, 'a') as f:
    f.write(f'ripresa:{str(t)}\n')
    f.close()

"""write to serial"""
ser = serial.Serial(port='/dev/serial0', baudrate=9600)
now = datetime.datetime.now()
ser.write(bytes(f'{now.strftime("%d/%m/%y %H:%M:%S")} Ripresa\n', 'utf-8'))
ser.flush()
