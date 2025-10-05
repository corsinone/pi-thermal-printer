import datetime
import serial

ser = serial.Serial(port='/dev/serial0', baudrate=9600)
now = datetime.datetime.now()
ser.write(bytes(f'{now.strftime("%d/%m/%y %H:%M:%S")} Ripresa\n', 'utf-8'))
ser.flush()
