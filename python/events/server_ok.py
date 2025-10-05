import serial
import datetime
ser = serial.Serial(port='/dev/serial0', baudrate=9600)
now = datetime.datetime.now()
ser.write(bytes('\n', 'utf-8'))
ser.write(bytes('_________INIZIO LAVORO________\n', 'utf-8'))
ser.write(bytes(now.strftime("%d/%m/%y %H:%M:%S")+' OCTO ON\n', 'utf-8'))
ser.flush()