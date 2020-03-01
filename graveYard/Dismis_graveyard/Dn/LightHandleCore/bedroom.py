import RPi.GPIO as GPIO
import time
from SpeechDriver.SpeechDriver import speak
pin = 3

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.OUT)

def light_on():
    #set low
    print('GPIO=3 led on')
    GPIO.output(pin, GPIO.LOW)
    speak('Boss\'s room light Activated')
    time.sleep(2)

def light_off():
    #set high
    print('GPIO=3 led off')
    GPIO.output(pin, GPIO.HIGH)
    speak('Boss\'s room light deactivated')
    time.sleep(2)