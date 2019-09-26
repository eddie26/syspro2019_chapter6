#!/usr/bin/env python

import cgi
import cgitb
import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(2, GPIO.OUT)
servo = GPIO.PWM(2, 50)
servo.start(0.0)

def setservo(deg):
    deg+=90.0
    sec = (0.5+1.9*(deg/180.0))/20.0*100.0
    servo.ChangeDutyCycle(sec)

print('Content-type: text/html; charset=UTF-8\r\n')
print('Web Servo')

print('<form action="" method="post">')
print('<input type="text" name="servo" size="3">')
print('<input type="submit" name="button" value="turn">')
print('</form>')

form = cgi.FieldStorage()
deg = float(form.getvalue('servo', '0'))
print(deg)
setservo(deg)
time.sleep(1.0)
