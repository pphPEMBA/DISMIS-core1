import RPi.GPIO as GPIO
import time
from SpeechDriver.SpeechDriver import speak
pin = 17


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.OUT)

def light_on():
    #set low
    print('GPIO=17 led on')
    GPIO.output(pin, GPIO.LOW)
    speak('Activated')
    time.sleep(2)

def light_off():
    #set high
    print('GPIO=17 led off')
    GPIO.output(pin, GPIO.HIGH)
    speak('Deactivated')
    time.sleep(2)


