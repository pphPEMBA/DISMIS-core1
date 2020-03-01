import RPi.GPIO as GPIO
import time
from SpeechDriver.SpeechDriver import speak
pin = 7

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.OUT)

def light_on():
    #set low
    print('GPIO=7 led on')
    GPIO.output(pin, GPIO.LOW)
    speak('activated')
    time.sleep(2)

def light_off():
    #set high
    print('GPIO=7 led off')
    GPIO.output(pin, GPIO.HIGH)
    speak('deactivated')
    time.sleep(2)
