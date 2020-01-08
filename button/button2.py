#!/usr/bin/env python

import time
import sys, os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#warten fuer Reboot
time.sleep(5)


while True:
        i = GPIO.input(24)

        if i == False:
                print 'Button 2 gedrueckt'
                os.system("sh /opt/automation/cam/kill_camall.sh &")
                os.system("sh /opt/automation/web/kill_smarthome.sh &")
                time.sleep(1)
                print "Starte Uebertragung Uebersicht"
                os.system("sh /opt/automation/cam/play_camall.sh &")
                time.sleep(1)

        elif i == True:
                print 'Button 2 nicht gedrueckt'
                time.sleep(0.1)
