import cv2
import os
import pygame
from pygame import mixer
import RPi.GPIO as GPIO


mixer.init()
cv2.namedWindow('QR_Code', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('QR_Code', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
path = ("welcome.png")
qr_code = cv2.imread(path)
#Resize if necessary
#resize_img = cv2.resize(path, (width, height))
cv2.imshow("QR_Code", qr_code)
cv2.waitKey(125)
TIMER = int(3)

date_string = time.strftime("%Y-%m-%d-%H:%M")

while True:
    # GPIO.setmode(GPIO.BCM)
    # TRIG = 23
    # ECHO = 24
    # GPIO.setup(TRIG,GPIO.OUT)
    # GPIO.setup(ECHO,GPIO.IN)
    # GPIO.output(TRIG, True)
    # time.sleep(0.00001)
    # GPIO.output(TRIG, False)
    # while GPIO.input(ECHO)==0:
    #   pulse_start = time.time()
    # while GPIO.input(ECHO)==1:
    #   pulse_end = time.time()
    # pulse_duration = pulse_end - pulse_start
    # distance = pulse_duration*17150
    # distance = round(distance, 2)
    # #print ("Distance:",distance,"cm")
    distance=49
    if (distance<50):
        prev = time.time()
        while TIMER >= 0:
            cur = time.time()
            if cur-prev >= 1:
                prev = cur
                TIMER = TIMER-1
        else:
            mixer.music.load("/home/kai/Thermal_imaging/welcome.mp3")
            mixer.music.set_volume(0.7)
            mixer.music.play()
            time.sleep(10)

            mixer.music.load("/home/kai/Thermal_imaging/photo.mpeg")
            mixer.music.set_volume(0.7)
            mixer.music.play()
            time.sleep(5)
            import process
    elif (distance >50):

        cv2.namedWindow('QR_Code', cv2.WINDOW_NORMAL)
        cv2.setWindowProperty('QR_Code', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        path = ("/home/kai/Thermal_imaging/welcome.png")
        qr_code = cv2.imread(path)
        #Resize if necessary
        #resize_img = cv2.resize(path, (width, height))
        cv2.imshow("QR_Code", qr_code)
        cv2.waitKey(125)
