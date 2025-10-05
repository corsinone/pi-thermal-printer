import datetime
import math
import os
import serial
import time

filename = f'{os.environ["HOME"]}/.ptp.logtime'

"""log pause time"""
t = math.trunc(time.clock_gettime(time.CLOCK_REALTIME))
with open(filename, 'a') as f:
    f.write(f'pausa:{str(t)}\n')
    f.close()

"""write to serial"""
ser = serial.Serial(port='/dev/serial0', baudrate=9600)
now = datetime.datetime.now()
ser.write(bytes(f'{now.strftime("%d/%m/%y %H:%M:%S")} In pausa\n', 'utf-8'))
ser.flush()
