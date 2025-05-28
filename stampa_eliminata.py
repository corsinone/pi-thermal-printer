import serial
import datetime
ser = serial.Serial(port='/dev/serial0', baudrate=9600)
now = datetime.datetime.now()
ser.write(bytes(now.strftime("%d/%m/%Y %H:%M:%S")+' Eliminata\n', 'utf-8'))
