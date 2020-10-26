import os
import time
import pygame
from pygame import mixer
import RPi.GPIO as GPIO
import cv2

path = 'path of the image'
qr_code = cv2.imread(path)
cv2.imshow("welcome", qr_code)

TIMER = int(5)

time.sleep(2)
while 1:
    GPIO.setmode(GPIO.BCM)
    TRIG = 23

    ECHO = 24
    GPIO.setup(TRIG,GPIO.OUT)

    GPIO.setup(ECHO,GPIO.IN)
    GPIO.output(TRIG, True)

    time.sleep(0.00001)

    GPIO.output(TRIG, False)

    while GPIO.input(ECHO)==0:

      pulse_start = time.time()

    while GPIO.input(ECHO)==1:

      pulse_end = time.time()

    pulse_duration = pulse_end - pulse_start

    distance = pulse_duration*17150

    distance = round(distance, 2)

    print ("Distance:",distance,"cm")

if(distance>0):
    result = True

    while(result):
        while TIMER >= 0:
            if cur-prev >= 1:
                prev = cur
                TIMER = TIMER-1
                import yes_or_no


    GPIO.cleanup()
