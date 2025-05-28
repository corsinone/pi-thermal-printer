import serial
import datetime
ser = serial.Serial(port='/dev/serial0', baudrate=9600)
now = datetime.datetime.now()
ser.write(bytes(now.strftime("%d/%m/%Y %H:%M:%S")+' Fine stampa\n', 'utf-8'))
ser.write(bytes(now.strftime("%d/%m/%Y %H:%M:%S")+' OCTO FINE\n', 'utf-8'))
ser.write(bytes('__________FINE LAVORO_________\n', 'utf-8'))
ser.write(bytes('\n\n\n','utf-8'))
