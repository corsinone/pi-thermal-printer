import argparse
import serial
import datetime

parser = argparse.ArgumentParser(prog='Stampa Start')
parser.add_argument('-f', help='filename', default='')
args = parser.parse_args()

ser = serial.Serial(port='/dev/serial0', baudrate=9600)
now = datetime.datetime.now()
ser.write(bytes(f'{now.strftime("%d/%m/%y %H:%M:%S")} Inizio stampa\n',
            'utf-8'))
if args.f != '':
    ser.write(bytes(f'file: {args.f}\n', 'utf-8'))
ser.flush()