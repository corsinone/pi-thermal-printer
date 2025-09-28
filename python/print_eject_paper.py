import serial

port = '/dev/serial0'
baudrate = 9600

ser = serial.Serial(port=port, baudrate=baudrate)

ser.write(bytes(f'{"-"*32}\n\n', 'utf-8'))
ser.flush()