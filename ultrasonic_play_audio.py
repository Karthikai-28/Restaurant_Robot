import RPi.GPIO as GPIO
import time
mixer.init()

def ultrasonic():
    while 1:
        GPIO.setmode(GPIO.BCM)
        TRIG = 5

        ECHO = 6
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

ultrasonic()
if (distance=>50):
    result = True
    while(result):
        while TIMER >= 0:
            if cur-prev >= 1:
                prev = cur
                TIMER = TIMER-1
                mixer.music.play()
                mixer.music.load("welcome.mp3")
                mixer.music.set_volume(0.7)
            break

break

if (distance=>10):
    mixer.music.play()
    mixer.music.load("pic.mp3")
    mixer.music.set_volume(0.7)
    import process

    mixer.music.play()
    mixer.music.load("feedback.mp3")
    mixer.music.set_volume(0.7)
    import Video

    mixer.music.play()
    mixer.music.load("thank_you.mp3")
    mixer.music.set_volume(0.7)

elif:
    mixer.music.play()
    mixer.music.load("feedback.mp3")
    mixer.music.set_volume(0.7)
    import Video

    mixer.music.play()
    mixer.music.load("thank_you.mp3")
    mixer.music.set_volume(0.7)
