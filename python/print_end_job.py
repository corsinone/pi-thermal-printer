import datetime
import math
import serial
import time

port = '/dev/serial0'
baudrate = 9600
filename = '.logtime'

ser = serial.Serial(port=port, baudrate=baudrate)

"""log end time"""
t = math.trunc(time.clock_gettime(time.CLOCK_REALTIME))
with open(filename, 'a') as f:
    f.write(f'end:{str(t)}')
    f.close()

"""parse time log file to estimate job duration"""
with open(filename, 'r') as f:
    state = 0
    duration = 0
    for line in f:
        result = str.split(line, sep=":")
        if state == 0 and result[0] == 'start':
            duration -= int(result[1])
            state = 1
        elif state == 1 and (result[0] == 'pause' or result[0] == 'end'):
            duration += int(result[1])
            state = 2
        elif state == 2 and result[0] == 'resume':
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

now = datetime.datetime.now()
ser.write(bytes(f'{now.strftime("%d/%m/%Y | %H:%M:%S")} | Fine\n', 'utf-8'))
ser.write(bytes(f'{days}d {hours}h {mins}m {secs}s\n', 'utf-8'))
ser.flush()