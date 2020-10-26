import cv2
import time
import numpy as np
import time
import smtplib
import os
import imghdr
import ssl
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import pygame
from pygame import mixer
# import RPi.GPIO as GPIO

def load_photo():
    mixer.init()
    cv2.namedWindow('QR_Code', cv2.WINDOW_NORMAL)
    cv2.setWindowProperty('QR_Code', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    path = ("/home/kai/Thermal_imaging/welcome.png")
    qr_code = cv2.imread(path)
    cv2.imshow("QR_Code", qr_code)

def ultrasonic():
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
        GPIO.cleanup()


def video():
    while 1:
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
        # print ("Distance:",distance,"cm")
        cv2.namedWindow('Capturing_Feedback', cv2.WINDOW_NORMAL)
        cv2.setWindowProperty('Capturing_Feedback', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        mixer.init()
        def change_res(cap, width, height):
            cap.set(3, width)
            cap.set(4, height)
        STD_DIMENSIONS =  {
            "480p": (640, 480),
            "720p": (1280, 720),
            "1080p": (1920, 1080),
            "4k": (3840, 2160),
        }
        def get_dims(cap, res='1080p'):
            width, height = STD_DIMENSIONS["480p"]
            if res in STD_DIMENSIONS:
                width,height = STD_DIMENSIONS[res]
            change_res(cap, width, height)
            return width, height
        VIDEO_TYPE = {
            'avi': cv2.VideoWriter_fourcc(*'XVID'),
            'mp4': cv2.VideoWriter_fourcc(*'XVID'),
        }
        def get_video_type(filename):
            filename, ext = os.path.splitext(filename)
            if ext in VIDEO_TYPE:
              return  VIDEO_TYPE[ext]
            return VIDEO_TYPE['avi']
        TIMER = int(10)
        i=0
        date_string = time.strftime("%Y-%m-%d-%H:%M")
        frames_per_second = 29.0
        res = '720p'
        filename = "/home/kai/Thermal_imaging/video.avi"
        capture = cv2.VideoCapture(0)
        out = cv2.VideoWriter(filename, get_video_type(filename), 25, get_dims(capture, res))

        result = True
        while (result):
            ret, frame = capture.read()
            out.write(frame)
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
            prev = time.time()
            distance = 14
            if distance < 50:
                time.sleep(4)
                if distance < 15:
                    while TIMER >= 0:
                        ret, frame = capture.read()
                        font = cv2.FONT_HERSHEY_SIMPLEX
                        cv2.putText(frame, str(TIMER),
                                    (200, 250), font,
                                    7, (0, 255, 255),
                                    4, cv2.LINE_AA)
                        out.write(frame)
                        cv2.imshow('Capturing_Feedback',frame)
                        cv2.waitKey(125)
                        cur = time.time()
                        if cur-prev >= 1:
                            prev = cur
                            TIMER = TIMER-1
                    else:
                        msg = MIMEMultipart()
                        msg['From'] = "restaurantrobot01@gmail.com"
                        msg['To'] = "billionhemanth22@gmail.com"
                        msg['Subject'] = 'Python Mail'
                        body  = 'Automated mail, image captured from the webcam'
                        msg.attach(MIMEText(body, 'plain'))
                        filename = "/home/kai/Thermal_imaging/video.avi"
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
                        out.release()
                        cv2.destroyWindow('Capturing_Feedback')
        break
    capture.release()
    out.release()
    cv2.destroyWindow('Capturing_Feedback')
    os.remove("/home/kai/Thermal_imaging/video.avi")


def image():
    while 1:
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
        # print ("Distance:",distance,"cm")
        distance = 14
        if distance < 15:
            mixer.music.load("/home/kai/Thermal_imaging/photo.mpeg")
            mixer.music.set_volume(0.7)
            mixer.music.play()
            cv2.namedWindow('Capturing Photo', cv2.WINDOW_NORMAL)
            cv2.setWindowProperty('Capturing Photo', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
            TIMER = int(3)
            date_string = time.strftime("%Y-%m-%d-%H:%M")
            mixer.init()
            i = 0
            capture = cv2.VideoCapture(0)
            ret, frame = capture.read()
            cv2.imshow('Capturing Photo', frame)
            cv2.waitKey(10)
            mixer.music.load("/home/kai/Thermal_imaging/cheese.mp3")
            mixer.music.set_volume(0.7)
            prev = time.time()
            while TIMER >= 0:
                ret, frame = capture.read()
                font = cv2.FONT_HERSHEY_SIMPLEX
                cv2.putText(frame, str(TIMER),
                            (200, 250), font,
                            7, (0, 255, 255),
                            4, cv2.LINE_AA)
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
                image_cap = "/home/kai/Thermal_imaging/Robot_image" + date_string + ".jpg".format(i)
                cv2.imwrite(image_cap, frame)
                i+=1
                msg = MIMEMultipart()
                msg['From'] = "restaurantrobot01@gmail.com"
                msg['To'] = "kk28296@gmail.com"
                msg['Subject'] = 'Python Mail'
                body  = 'Automated mail, image captured from the webcam'
                msg.attach(MIMEText(body, 'plain'))
                filename = "/home/kai/Thermal_imaging/Robot_image" + date_string + ".jpg".format(i)
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
                # capture.release()
                # cv2.destroyWindow('Capturing Photo')

        capture.release()
        cv2.destroyWindow('Capturing Photo')
        os.remove("/home/kai/Thermal_imaging/Robot_image" + date_string + ".jpg".format(i))
        break



if __name__ == '__main__':
    i = 0
    while i <= 10:
        load_photo()
        time.sleep(.1)
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
        # print ("Distance:",distance,"cm")
        distance = 49
        if distance<50:
            mixer.music.load("/home/kai/Thermal_imaging/welcome.mp3")
            mixer.music.set_volume(0.7)
            mixer.music.play()
            cv2.waitKey(300)
            cv2.destroyWindow("QR_Code")
            image()
            time.sleep(.1)
            import video
