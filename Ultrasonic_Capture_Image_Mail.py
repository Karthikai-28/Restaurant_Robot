import cv2
import time
import numpy as np
import time
import smtplib
import os
import imghdr
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import pygame
from pygame import mixer
# import RPi.GPIO as GPIO
#from threading import Thread, Event

cv2.namedWindow('Capturing Photo', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('Capturing Photo', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
TIMER = int(3)
date_string = time.strftime("%Y-%m-%d-%H:%M")
mixer.init()
i = 0
capture = cv2.VideoCapture(0)


while True:
    ret, frame = capture.read()
    cv2.imshow('Capturing Photo', frame)
    cv2.waitKey(100)
    # prev = time.time()
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
    #print ("Distance:",distance,"cm")
    distance = 14


    if (distance < 50):
        time.sleep(4)
        if (distance < 15):
            mixer.music.load("/home/kai/Thermal_imaging/cheese.mp3")
            mixer.music.set_volume(0.7)
            mixer.music.play()
            prev = time.time()
            time.sleep(3)
            while TIMER >= 0:
                ret, frame = capture.read()
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, str(TIMER),
                            (200, 250), font,
                            7, (0, 255, 255),
                            4, cv2.LINE_AA)
                cv2.destroyWindow("QR_Code")

                cv2.imshow('Capturing Photo', frame)
                cv2.waitKey(125)
                cur = time.time()
                if cur-prev >= 1:
                    prev = cur
                    TIMER = TIMER-1
            else:
                ret, frame = capture.read()
                cv2.imshow('Capturing Photo', frame)
                cv2.waitKey(2000)
                image_cap = "/home/kai/Thermal_imaging/Robot_image_" + date_string + ".jpg".format(i)
                cv2.imwrite(image_cap, frame)
                i+=1
                msg = MIMEMultipart()
                msg['From'] = "restaurantrobot01@gmail.com"
                msg['To'] = "billionhemanth22@gmail.com"
                msg['Subject'] = 'Python Mail'
                body  = 'Automated mail, image captured from the webcam'
                msg.attach(MIMEText(body, 'plain'))
                filename = "/home/kai/Thermal_imaging/Robot_image_" + date_string + ".jpg".format(i)
                attachment = open(filename, 'rb')
                part = MIMEBase('application', 'octet-stream')
                part.set_payload((attachment).read())
                encoders.encode_base64(part)
                part.add_header('Content-Disposition', "attachment; filename=" +filename)
                msg.attach(part)
                text = msg.as_string()
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.starttls()
                server.login("restaurantrobot01@gmail.com", "Stumbleupon01")
                server.sendmail("restaurantrobot01@gmail.com", "billionhemanth22@gmail.com", text)
                server.quit()
                capture.release()
                cv2.destroyWindow('Capturing Photo')
                os.remove("/home/kai/Thermal_imaging/Robot_image_" + date_string + ".jpg".format(i))

                import video

    else:
        import open

capture.release()
cv2.destroyWindow('Capturing Photo')
