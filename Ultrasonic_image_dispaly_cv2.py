import cv2
import RPi.GPIO as GPIO
import time
from datetime import datetime

GPIO.setmode(GPIO.BOARD)

GPIO.setwarnings(False)

GPIO.setup(40,GPIO.IN) # IR INPUT
GPIO.setup(38,GPIO.OUT) # IR POSITIVE ,NEGATIVE AT GPIO 39

try:

    GPIO.output(38, 1)

    while True:
        state=GPIO.input(40)
        if state==False:
            time.sleep(1)

        else:

            print("Object Detected")

            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print( current_time)

            vid_capture = cv2.VideoCapture(0)

            ret,frame = vid_capture.read()

            if ret==True:
                cv2.imwrite("pics/at_{}.jpg".format(current_time),frame)


            vid_capture.release()
            cv2.destroyAllWindows()


            vid_capture = cv2.VideoCapture(0) # webcam
            vid_cod = cv2.VideoWriter_fourcc(*'XVID')
            output = cv2.VideoWriter("videos/at_{}.mp4".format(current_time), vid_cod, 20.0, (640,480))

            while(int(time.time() - start_time) < 10): # 10 is 10 seconds of video

                ret,frame = vid_capture.read()
                if ret==True:
                    cv2.imshow("My cam video", frame)
                    output.write(frame)
                else:
                    break

            vid_capture.release()
            output.release()
            cv2.destroyAllWindows()

            img = cv2.imread('qr.png')
            cv2.imshow('sample image',img)
            check=True
            while check:
                state=GPIO.input(40)
                if state==False:
                    time.sleep(1)
                else:
                    check=False


            cv2.destroyAllWindows()

except KeyboardInterrupt:          # trap a CTRL+C keyboard interrupt
    GPIO.cleanup()
except Exception as e:
    print("An exception occurred")
    print("Oops!", e.__class__, "occurred.")
    print(e)
