import datetime
import serial

"""log ko time"""
t = math.trunc(time.clock_gettime(time.CLOCK_REALTIME))
with open(filename, 'a') as f:
    f.write(f'ko:{str(t)}\n')
    f.close()

"""write to serial"""
ser = serial.Serial(port='/dev/serial0', baudrate=9600)
now = datetime.datetime.now()
ser.write(bytes(f'{now.strftime("%d/%m/%y %H:%M:%S")} Stampa KO\n', 'utf-8'))
ser.flush()
