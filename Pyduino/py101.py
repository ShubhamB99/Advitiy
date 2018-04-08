import serial
import cv2
import time

uno = serial.Serial('com3', 9600)

def send (x, y):
	img = cv2.imread("image.jpg", cv2.IMREAD_COLOR)
	b = img[x, y, 0]
	g = img[x, y, 1]
	r = img[x, y, 2]
	time.sleep(0.5)
	uno.write(b)
	time.sleep(0.5)
	uno.write(g)
	time.sleep(0.5)
	uno.write(r)

var = 'a'

while var != 'q' :
	var = raw_input("Enter the command ")
	#time.sleep(1)
	uno.write(var)
	if var == 'r' :
		#time.sleep(1)
		#uno.write('x')
		while uno.in_waiting == 0:
			continue
			#r = uno.read(100)
		x = uno.read()
		y = uno.read()
		print x
		print "Now y "
		print y
		#send(int(x), int(y))
		
	
'''
When press 'r', arduino starts transmitting. On pressing 'x', sends x coordinate. On pressing 'y', sends y coordinate.
After that arduino is set on receiving mode.
'q' is to quit the program.
'''
