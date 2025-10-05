import datetime
import serial

"""write to serial"""
ser = serial.Serial(port='/dev/serial0', baudrate=9600)
now = datetime.datetime.now()
ser.write(bytes('\n', 'utf-8'))
ser.write(bytes('_________INIZIO LAVORO________\n', 'utf-8'))
ser.write(bytes(f'{now.strftime("%d/%m/%y %H:%M:%S")} OCTO ON\n', 'utf-8'))
ser.flush()