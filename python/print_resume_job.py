import datetime
import math
import serial
import time

port = '/dev/serial0'
baudrate = 9600
filename = '.logtime'

ser = serial.Serial(port=port, baudrate=baudrate)

now = datetime.datetime.now()
ser.write(bytes(f'{now.strftime("%d/%m/%Y | %H:%M:%S")} | Riprendi\n', 'utf-8'))
ser.flush()

"""log resume time"""
t = math.trunc(time.clock_gettime(time.CLOCK_REALTIME))
with open(filename, 'a') as f:
    f.write(f'resume:{str(t)}\n')
    f.close()