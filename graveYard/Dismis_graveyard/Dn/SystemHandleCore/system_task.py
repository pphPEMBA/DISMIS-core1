from SpeechDriver.SpeechDriver import speak
import os
import sys
from os import system


def shutdown():
    os.system('shutdown -h')
    print('shutting down boss')
    speak('shutting down boss')

def cancel_shutdown():
    """Cancel an active shutdown"""
    os.system('sudo shutdown -c')
    speak('Shutdown cancelled.')


def hybridsleep():
    """
    Hybrid sleep.
    Will quickly wake up but also survive power cut.
    Performs both suspend AND hibernate.
    Will quickly wake up but also survive power cut.
    """
    os.system("sudo systemctl hybrid-sleep")

def suspend():
    """
    Suspend (to RAM) - also known as Stand By or Sleep mode. 

    Operate PC on a minimum to save power but quickly wake up.
    """
    os.system('sudo systemctl suspend')

def hibernate():
    """
    Hibernate - also known as "Suspend to Disk"

    Saves everything running to disk and performs shutdown.
    Next reboot computer will restore everything - including
    Programs and open files like the shutdown never happened.
    """
    os.system('sudo systemctl hibernate')


def restart():
    os.system('shutdown -r')
    print('rebooting sir')
    speak('rebooting sir')


def closesoftware(voice_text):
	data = voice_text.split(' ')
	process = data[1]
	os.system("killall "+process)
    #speak('closed sir')

def hotspot_start():
    """
    Jarvis will set up your own hotspot.
    """
    system("sudo ap-hotspot start")


def hotspot_stop():
    """
    Jarvis will stop your hotspot.
    """
    system("sudo ap-hotspot stop")

def clear_terminal():
    """Clears terminal"""
    os.system("clear")
    speak('terminal cleared boss')

def screen_off():
    """Turn of screen instantly"""
    os.system('xset dpms force off')

def batterystatus():
    subprocess.call("/shCMD/./batteryStatus.sh")


import os
import threading
from datetime import datetime


def take_screenshots():
    threading.Timer(30.0, take_screenshots).start()
    time = "{:%B-%d-%Y-%H-%M-%S}".format(datetime.now())
    os.system('screencapture screenshots/' + time + '.png')

def open_camera__LINUX():
    """Jarvis will open the camera for you."""
    speak("Opening cheese.......")
    os.system("cheese")


def check_ram():
    """
    checks your system's RAM stats.
    -- Examples:
        check ram
    """
    os.system("free -lm")
