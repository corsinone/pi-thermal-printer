import serial

port = '/dev/serial0'
baudrate = 9600

"""write to serial"""
ser = serial.Serial(port=port, baudrate=baudrate)

ser.write(bytes('Hello World!\n', 'utf-8'))
ser.flush()