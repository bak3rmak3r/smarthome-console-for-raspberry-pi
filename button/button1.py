#!/usr/bin/env python

import time
import sys, os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(26, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#warten fuer Reboot
time.sleep(5)


while True:
        i = GPIO.input(26)
        print i
        if i == False:
                print 'Button 1 gedrueckt'
                os.system("sh /opt/automation/cam/kill_camall.sh &")
                os.system("sh /opt/automation/web/kill_smarthome.sh &")
                time.sleep(1)
                print "Starte SmartHome"
                os.system("sh /opt/automation/web/start_smarthome.sh &")
                time.sleep(1)

        elif i == True:
                print 'Button 1 nicht gedrueckt'
                time.sleep(0.1)