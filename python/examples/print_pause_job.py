import datetime
import math
import serial
import time

port = '/dev/serial0'
baudrate = 9600
filename = '.logtime'

"""log pause time"""
t = math.trunc(time.clock_gettime(time.CLOCK_REALTIME))
with open(filename, 'a') as f:
    f.write(f'pause:{str(t)}\n')
    f.close()

"""write to serial"""
ser = serial.Serial(port=port, baudrate=baudrate)

now = datetime.datetime.now()
ser.write(bytes(f'{now.strftime("%d/%m/%Y | %H:%M:%S")} | Pausa\n', 'utf-8'))
ser.flush()