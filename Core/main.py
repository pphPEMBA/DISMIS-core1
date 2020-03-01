#!/usr/bin/python3
from pyfiglet import Figlet
import yaml, random
import sys
import os
import datetime
import time
from multiprocessing import Process, Queue

from SpeechDriver.tts.ttsdefault import speak
from Services import weather, jokes_quote
from Core import textAnimation
from Core.profile import *

"""
print("                                            ")
print("  ________  .__               .__           ")
print("  \______ \ |__| ______ _____ |__| ______   ")
print("   |    |  \|  |/  ___//     \|  |/  ___/   ")
print("   |    `   \  |\___ \|  Y Y  \  |\___ \    ")
print("  /_______  /__/____  >__|_|  /__/____  >   ")
print("          \/        \/      \/        \/    ")
print("                                            ")   """


""" Ping google.com """ #Current not using in main instead using in brain.
from urllib.request import urlopen
def internetExamine():
    while True:
        try:
            response = urlopen('https://www.google.com/', timeout=10)
            print('on')
            return True
        except: 
            print('false')
            return False


""" Greeting """
def greetMe():
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        speak('Good Morning!')
        print('Good Morning!')
    if currentH >= 12 and currentH < 18:
        speak('Good Afternoon!')
        print('Good Afternoon!')
    if currentH >= 18 and currentH != 0:
        speak('Good Evening!')
        print('Good Evening!')

""" MULTIPROCESSING """
def BestfriendBirthdayProtocal(BestfriendBirthdayProtocal_path):
    time.sleep(random.randint(1, 3))
    os.system("python3 " + BestfriendBirthdayProtocal_path + " &")
def PersonalGmailNotify(PersonalGmailNotify_path):
    time.sleep(random.randint(1, 3))
    os.system("python3 " + PersonalGmailNotify_path + " &")
def flask_credentials(flask_credentials_path):
    time.sleep(random.randint(1, 3))
    os.system("python3 " + flask_credentials_path + "&")
def schedule(schedule_path):
    time.sleep(random.randint(1, 3))
    os.system("python3 " + schedule_path + "&")

""" Desktop Notification """
"""
from gi.repository import Notify
# One time initialization of libnotify
Notify.init("Dismis-HA_slave1")
# Create the notification object
title = "Dismis-HA_slave1!"
body = "Meeting at 3PM!"
notification = Notify.Notification.new(
    title, body)
# Actually show on screen
notification.show() """
      

""" Booting """
def startup():
    """ Start Up """
    textAnimation.load_animation()
    time.sleep(0.30)
    print(' ')
    
    """ Dismis Banner """
    custom_fig = Figlet(font='graffiti')
    print(custom_fig.renderText('Dismis-HA'))
    
    """ Greeting """
    greetMe()
    #time.sleep(0.30)
    
    """ Weather of Default Location """
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        weather.weather_DefaultCity(default_CityLocation, openweatherAPI, accept_path)
        time.sleep(9)
    
    """ Jokes """
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        jokes_quote.tell_joke(accept_path)
        time.sleep(3)
    
    """ Quote of The Day """
    currentH = int(datetime.datetime.now().hour)
    if currentH >= 0 and currentH < 12:
        jokes_quote.quote(accept_path)
        



""" Running All Main Functions """
startup()
""" Running Parallel Processes """
#chkMail = Process(target = PersonalGmailNotify(PersonalGmailNotify_path))
#chkMail.start()
#bffbirthday = Process(target = BestfriendBirthdayProtocal(BestfriendBirthdayProtocal_path))
#bffbirthday.start()
#credentials = Process(target = flask_credentials(flask_credentials_path))
#credentials.start()
#routine = Process(target = schedule(schedule_path))
#routine.start()
#


