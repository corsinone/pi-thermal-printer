import serial
ser = serial.Serial(port='/dev/serial0', baudrate=9600)
ser.write(bytes('Hello World!\n', 'utf-8'))

