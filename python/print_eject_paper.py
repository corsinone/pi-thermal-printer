import serial
ser = serial.Serial(port='/dev/serial0', baudrate=9600)
hb = '-'*32
ser.write(bytes(hb+'\n\n', 'utf-8'))

