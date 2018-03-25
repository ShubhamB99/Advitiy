import serial
import time

uno = serial.Serial('com6', 9600)

var = 'a'

while var!='x':
	var = raw_input("Enter a character ")
	time.sleep(1)
	uno.write(var)
'''

var = raw_input("Enter a character ")
time.sleep(1)
uno.write(var)
'''