#!/usr/bin/env python
#ir scan to check person presence and switch on display through relais

import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(12, GPIO.IN)
GPIO.setup(8, GPIO.OUT)

while True:
	i = GPIO.input(12)

	if i == True:
        	GPIO.output(8, GPIO.HIGH)
        	print 'TFT an'
		x = 0

		#adjust seconds for switch off delay
		while x < 10:
			i = GPIO.input(12)
            		if i == 1:
                		x = 0
                		print 'jemand da'
                		time.sleep(1)
            		elif i == 0:
                		x = x + 1
                		print 'niemand da'
                		time.sleep(1)

	elif i == False:
		GPIO.output(8, GPIO.LOW)
        	print 'TFT aus'
        	time.sleep(1)
