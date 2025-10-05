import argparse
import datetime
import math
import os
import serial
import time

"""parse input arguments"""
parser = argparse.ArgumentParser(prog='Stampa Start')
parser.add_argument('-f', help='filename', default='')
args = parser.parse_args()

filename = f'{os.environ["HOME"]}/.ptp.logtime'

"""log start time"""
t = math.trunc(time.clock_gettime(time.CLOCK_REALTIME))
with open(filename, 'w') as f:
    f.write(f'inizio:{str(t)}\n')
    f.close()

"""write to serial"""
ser = serial.Serial(port='/dev/serial0', baudrate=9600)
now = datetime.datetime.now()
ser.write(bytes(f'{now.strftime("%d/%m/%y %H:%M:%S")} Inizio stampa\n',
            'utf-8'))
if args.f != '':
    ser.write(bytes(f'file: {args.f}\n', 'utf-8'))
ser.flush()