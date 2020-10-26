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


TIMER = int(3)
date_string = time.strftime("%Y-%m-%d-%H:%M")

i = 0
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
capture = cv2.VideoCapture(0)
result = True
while (result):
    ret, frame = capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
    net.setInput(blob)
    detections = net.forward()

    cv2.imshow('Capturing Photo', frame)
    #cv2.imwrite("pics/at_{}.jpg".format(current_time),frame)
    k = cv2.waitKey(100)
    if len(detections)>0:
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
            # Update and keep track of Countdown
            # if time elapsed is one second
            # than decrese the counter
            if cur-prev >= 1:
                prev = cur
                TIMER = TIMER-1
        else:
            ret, frame = capture.read()

            # Display the clicked frame for 2
            # sec.You can increase time in
            # waitKey also
            cv2.imshow('Capturing Photo', frame)

            # time for which image displayed
            cv2.waitKey(2000)

            Timer = int(3)



            # Save the frame
            image_cap = "Robot_image" + date_string + ".jpg".format(i)
            cv2.imwrite(image_cap, frame)
            i+=1

            msg = MIMEMultipart()
            msg['From'] = "restaurantrobot01@gmail.com"
            msg['To'] = "kk28296@gmail.com"
            msg['Subject'] = 'Python Mail'

            body  = 'Automated mail, image captured from the webcam'
            msg.attach(MIMEText(body, 'plain'))

            filename = "Robot_image" + date_string + ".jpg".format(i)
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

    elif k == 27:
        break

capture.release()
cv2.destroyAllWindows()

os.remove("Robot_image" + date_string + ".jpg".format(i))
