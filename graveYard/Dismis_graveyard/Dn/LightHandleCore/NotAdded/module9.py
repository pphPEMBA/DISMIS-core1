import RPi.GPIO as GPIO
import time

pin = [18]
 

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.OUT)

def light_on():
    #set low
    print('GPIO=18 led on')
    GPIO.output(pin, GPIO.LOW)
    time.sleep(2)

def light_off():
    #set high
    print('GPIO=18 led off')
    GPIO.output(pin, GPIO.HIGH)
    time.sleep(2)
