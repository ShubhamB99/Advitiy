from __future__ import division									# Else division doesn't give values after decimal
import wave
import struct
from math import sin, pi, asin, tan, atan, sqrt
import cv2


img = cv2.imread("image.jpg", cv2.IMREAD_COLOR)					# Our source image is image.jpg in the same folder

phase1 = 0.0													# Saves value of second last data point of sine wave
phase2 = 0.0													# Saves value of second last data point of sine wave
flag = 1
error = 0.0
A = 32767.0														# This corresponds to amplitude of 1 on actual scale
f = 1.0

sampleRate = 44100.0 											# This is the sampling rate of the wave,i.e., number of samples per second
wavef = wave.open('signal.wav','w')								# Our destination wave file is signal.wav in the same folder
wavef.setnchannels(1) 											# 1 is mono and 2 is stereo
wavef.setsampwidth(2) 
wavef.setframerate(sampleRate)

def genwave(frequency, duration):
	global phase1, phase2, flag, error, A, f
	
	sample = duration * sampleRate  * 1.0
	error += sample - int(sample)

	# Calculating error in samples and adding them to wave to prevent them from accumulating
	if (error < 1):												
		n = int(sample)
	else:
		n = int(sample) + 1
		error -= 1

	# Updating amplitude of next wave to match slope correctly
	if f == 1.0:
		A = 32767.0
	else:
		if (phase2 != 0) :
			A = phase2 / sin(atan((frequency/f)*tan(asin(phase2/A))))			# phase2 actually gives value between 0 and 1 not 0 and 32767
		else:
			A *= f/frequency

	if A > 32767.0 :								# Maximum amplitude of wave is limited
		A = 32767.0
			
	# Finding corresponding region of wave for phase calculation of next wave
	for i in range(n):
		if i == 0:
			if ((phase2 - phase1) >= 0 and phase1 >= 0):
				flag = 1
			elif ((phase2 - phase1) <= 0 and phase1 >= 0):
				flag = 2
				if phase2 <= 0:
					flag = 5
			elif ((phase2 - phase1) <= 0 and phase1 <= 0):
				flag = 3 
			elif ((phase2 - phase1) >= 0 and phase1 <= 0):
				flag = 4
				if phase2 >= 0:
					flag = 1
			
		# Finding value of the data points
		if flag == 1:
			value = int(A * sin((2 * frequency * pi *float(i)/float(sampleRate)) + atan((frequency/f)* tan(asin(phase2)))))
		elif flag == 2:
			value = int(A * sin((2 * frequency * pi *float(i)/float(sampleRate)) + pi - atan((frequency/f)* tan(asin(phase2)))))
		elif flag == 3:
			value = int(A * sin((2 * frequency * pi *float(i)/float(sampleRate)) + pi - atan((frequency/f)* tan(asin(phase2)))))
		elif flag == 4:
			value = int(A * sin((2 * frequency * pi *float(i)/float(sampleRate)) + atan((frequency/f)* tan(asin(phase2)))))
		elif flag == 5:
			value = int(A * sin((2 * frequency * pi *float(i)/float(sampleRate)) + pi ))
		elif flag == 6:
			value = int(A * sin((2 * frequency * pi *float(i)/float(sampleRate))))


		data = struct.pack('<h', value)									# Packing value of data in short int format - 2 bytes per data
		wavef.writeframesraw( data )									# Writing data in the file

		if i == n - 2:
			phase1 = value / 32767.0
			#for j in range(10):
			#	wavef.writeframesraw( data )

		elif i == n - 1:
			phase2 = value / 32767.0
			#for j in range(10):
			#	wavef.writeframesraw( data )

	f = frequency


genwave(1900, 0.3)				# VIS CODE
genwave(1200, 0.01)
genwave(1900, 0.3)
genwave(1200, 0.03)				

genwave(1100, 0.06)
genwave(1300, 0.09)
genwave(1100, 0.06)
genwave(1300, 0.03)
genwave(1200, 0.03)

#genwave(1200,0.009)				# START CODE

y1 = 320*[0.0000000]
y2 = 320*[0.0000000]
b = 320*[0.0000000]
r = 320*[0.0000000]
for y in range (128):
	print("Line % d" % y)
	for x in range(320):								# Color values are stored as BGR, i.e., 0 for B, 1 for G and 2 for R 
		
		y1[x] = round((16.0 + (0.003906 * ((65.738 * img[2*y, x][2]) + (129.057 * img[2*y, x][1]) + (25.064 * img[2*y, x][0])))) * 3.1272549, 2)
		y2[x] = round((16.0 + (0.003906 * ((65.738 * img[2*y+1, x][2]) + (129.057 * img[2*y+1, x][1]) + (25.064 * img[2*y+1, x][0])))) * 3.1372549, 2)  
		b[x] = round((128.0 + (0.003906 * ((-37.945 * (img[2*y, x][2] + img[2*y+1, x][2]) / 2) + (-74.494 * (img[2*y, x][1] + img[2*y+1, x][1]) / 2) + (112.439 * (img[2*y, x][0] + img[2*y+1, x][0]) / 2)))) * 3.1372549, 2)
		r[x] = round((128.0 + (0.003906 * ((112.439 * (img[2*y, x][2] + img[2*y+1, x][2]) / 2) + (-94.154 * (img[2*y, x][1] + img[2*y+1, x][1]) / 2) + (-18.285 * (img[2*y, x][0] + img[2*y+1, x][0]) / 2)))) * 3.1372549, 2)

	#genwave(1500,0.0015)								# SEPARATOR PULSE
	genwave(1200,0.020)									# SYNC PULSE
	genwave(1500,0.00208)								# SYNC PORCH
	
	for i in range(320):								# Y1 SCAN
		genwave((y1[i]+1500), 0.000532)
	
	#genwave(1500,0.0015)								# SEPARATOR PULSE
	
	for j in range(320):								# Y-B SCAN
		genwave((b[j]+1500), 0.000532)
	
	for k in range(320):								# Y-R SCAN
		genwave((r[k]+1500), 0.000532)	

	for l in range(320):								# Y2 SCAN
		genwave((y2[l]+1500), 0.000532)	


wavef.writeframes('')
wavef.close()

# VIS Code - 01100011 ( 99d)
# Y = 16.0 + (.003906 * ((65.738 * R) + (129.057 * G) + (25.064 * B)))
# RY = 128.0 + (.003906 * ((112.439 * R) + (-94.154 * G) + (-18.285 * B)))
# BY = 128.0 + (.003906 * ((-37.945 * R) + (-74.494 * G) + (112.439 * B)))