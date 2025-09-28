import serial
import datetime

port = '/dev/serial0'
baudrate = 9600

ser = serial.Serial(port=port, baudrate=baudrate)

now = datetime.datetime.now()
ser.write(bytes(f'{now.strftime("%d/%m/%Y | %H:%M:%S")} | Pausa\n', 'utf-8'))
ser.flush()

