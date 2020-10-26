import cv2
import time



cv2.namedWindow('Capturing_Feedback', cv2.WINDOW_NORMAL)
cv2.setWindowProperty('Capturing_Feedback', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
mixer.init()

cam = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
rec = cv2.VideoWriter('video.avi', fourcc, 29, (640, 480))

while True:
    ret, frame = cam.read()
    cv2.imshow('Video', frame)
    rec.write(frame)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('q'):
        rec.release()
        break
cam.release()
cv2.destroyAllWindows()
