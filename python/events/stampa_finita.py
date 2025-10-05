import datetime
import math
import os
import serial
import time

filename = f'{os.environ["HOME"]}/.ptp.logtime'

"""log end time"""
t = math.trunc(time.clock_gettime(time.CLOCK_REALTIME))
with open(filename, 'a') as f:
    f.write(f'fine:{str(t)}')
    f.close()

"""parse time log file to estimate job duration"""
with open(filename, 'r') as f:
    state = 0
    duration = 0
    for line in f:
        result = str.split(line, sep=":")
        if state==0 and result[0]=='inizio':
            duration -= int(result[1])
            state = 1
        elif state==1 and \
                (result[0]=='pausa' or result[0]=='ko' or result[0]=='fine'):
            duration += int(result[1])
            state = 2
        elif state==2 and result[0]=='ripresa':
            duration -= int(result[1])
            state = 1
        else:
            print('time log file is inconsistent', file=sys.stderr)
            exit()

    """compute duration as days, hours, mins, secs"""
    result = math.modf(duration/60)
    secs = math.ceil(result[0]*60)
    result = math.modf(int(result[1])/60)
    mins = math.ceil(result[0])*60
    result = math.modf(int(result[1])/24)
    hours = math.ceil(result[0]*24)
    days = int(result[1])
    f.close()

"""write to serial"""
ser = serial.Serial(port='/dev/serial0', baudrate=9600)
now = datetime.datetime.now()
ser.write(bytes(f'{now.strftime("%d/%m/%y %H:%M:%S")} Fine stampa\n', 'utf-8'))
ser.write(bytes(f'{now.strftime("%d/%m/%y %H:%M:%S")} OCTO FINE\n', 'utf-8'))
ser.write(bytes(f'Durata: {days:2d}d {hours:2d}h {mins:2d}m {secs:2d}s\n',
            'utf-8'))
ser.write(bytes('__________FINE LAVORO_________\n', 'utf-8'))
ser.write(bytes('\n\n\n','utf-8'))
ser.flush()