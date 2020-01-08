#!/usr/bin/env python

import time
import sys, os
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_UP)


#warten fuer Reboot
time.sleep(5)

x = 1
while True:
        i = GPIO.input(3)
        print i
        if i == False:
                print 'Button 3 gedrueckt'

                os.system("sh /opt/automation/cam/kill_camall.sh &")
                os.system("sh /opt/automation/web/kill_smarthome.sh &")
                time.sleep(1)

                if x == 1:
                        print "Starte Uebertragung Kamera 1"
                        os.system("sh /opt/automation/cam/play_cam1full.sh &")
                        time.sleep(1)
                        x = 2

                elif x == 2:
                        print "Starte Uebertragung Kamera 2"
                        os.system("sh /opt/automation/cam/play_cam2full.sh &")
                        time.sleep(1)
                        x = 3

                elif x == 3:
                        print "Starte Uebertragung Kamera 3"
                        os.system("sh /opt/automation/cam/play_cam3full.sh &")
                        time.sleep(1)
                        x = 1

        elif i == True:
                print 'Button 3 nicht gedrueckt'
                time.sleep(0.1)