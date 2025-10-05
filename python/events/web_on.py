import serial
import datetime
ser = serial.Serial(port='/dev/serial0', baudrate=9600)
now = datetime.datetime.now()
ser.write(bytes(f'{now.strftime("%d/%m/%y %H:%M:%S")} WEB aperto\n', 'utf-8'))
ser.flush()
