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
#import RPi.GPIO as GPIO
import pyaudio
import wave
import threading
import ffmpeg


cv2.namedWindow('Capturing_Feedback', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('Capturing_Feedback', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
mixer.init()

TIMER =20
i=0
date_string = time.strftime("%Y-%m-%d-%H:%M")
capture = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
out = cv2.VideoWriter('video.avi', fourcc, 10, (640, 480))
start_time = time.time()
result = True
while (result):
    ret, frame = capture.read()
    cv2.imshow('Capturing_Feedback',frame)
    cv2.waitKey(100)
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
    if distance < 50:
        time.sleep(4)
        if distance < 15:
            while (int(time.time() - start_time) < TIMER):
                import aud
                ret, frame = capture.read()
                out.write(frame)
                cv2.imshow('Capturing_Feedback',frame)
                cv2.waitKey(125)
                input_video = ffmpeg.input('/home/kai/Thermal_imaging/video.avi')
                input_audio = ffmpeg.input('/home/kai/Thermal_imaging/test1.wav')
                ffmpeg.concat(input_video, input_audio, v=1, a=1).output('/home/kai/Thermal_imaging/output.avi').run()

            else:
                msg = MIMEMultipart()
                msg['From'] = "restaurantrobot01@gmail.com"
                msg['To'] = "billionhemanth22@gmail.com"
                msg['Subject'] = 'Python Mail'
                body  = 'Automated mail, image captured from the webcam'
                msg.attach(MIMEText(body, 'plain'))
                filename = "output.avi"
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
                server.sendmail("restaurantrobot01@gmail.com", "kk28296@gmail.com", text)
                server.quit()
        break


capture.release()
out.release()
cv2.destroyWindow('Capturing_Feedback')
# os.remove("output.avi")
