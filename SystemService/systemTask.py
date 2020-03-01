#!/usr/bin/python3
import os
from platform import architecture, dist, release
from platform import system as sys
import platform
import time

from SpeechDriver.tts.ttsdefault import speak
 

""" GLOBAL FUNCTION """
def Log_Time():
    import datetime
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

""" Importing Profiles """
import yaml
from Core.profile import temporaryfiles, profile_path
profile = open(profile_path)
profile_data = yaml.safe_load(profile)
profile.close()
#Functioning Variables
systemTaskTTS_path = profile_data['systemTaskTTS_path']
systemTaskTTS = systemTaskTTS_path + '/SpeechDriver/tts/ServicesTTS/systemTaskTTS/'
#print(systemTaskTTS)

def screen_off__LINUX(accept_path):   #linux
    #Turn of screen instantly
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('Screen turning off')
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: screen_off__LINUX')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    os.system('xset dpms force off')
    #   _txt = open(temporaryfiles + '.txt','w+')
    #_txt.write(result)
    #os.system('gnome-terminal -- python3 ' + systemTaskTTS + '__tts.py &')
    #print(' ')

def Os__LINUX(accept_path): #linux&Window
    #Displays information about your operating system
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('[!] Operating System Information')
    print('[*] ' + sys())
    print('[*] ' + release())
    print('[*] ' + dist()[0])
    for _ in architecture():
        print('[*] ' + _)
    # machine
    print("[*] Machine: " + platform.machine())
    # node
    print("[*] Node: " + platform.node())
    # processor
    print("[*] Processors: ")
    with open("/proc/cpuinfo", "r")  as f:
        info = f.readlines()
    cpuinfo = [x.strip().split(":")[1] for x in info if "model name"  in x]
    for index, item in enumerate(cpuinfo):
        print("    " + str(index) + ": " + item)
    print("[*] Memory Info: ")
    with open("/proc/meminfo", "r") as f:
        lines = f.readlines()
    print("     " + lines[0].strip())
    print("     " + lines[1].strip())
    # Load
    with open("/proc/loadavg", "r") as f:
        print("[*] Average Load: " + f.read().strip())
    # uptime
    uptime = None
    with open("/proc/uptime", "r") as f:
        uptime = f.read().split(" ")[0].strip()
    uptime = int(float(uptime))
    uptime_hours = uptime // 3600
    uptime_minutes = (uptime % 3600) // 60
    print("[*] Uptime: " + str(uptime_hours) + ":" + str(uptime_minutes) + " hours")
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: os__LINUX')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    #   _txt = open(temporaryfiles + '.txt','w+')
    #_txt.write(result)
    #os.system('gnome-terminal -- python3 ' + systemTaskTTS + '__tts.py &')
    #print(' ')

def shutdown_LINUX(accept_path):
    """Shutdown the system"""
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    speak('Shuting down the system')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('Shuting down the system')
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: shutdown__LINUX')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    os.system('poweroff')
    #_txt = open(temporaryfiles + '.txt','w+')
    #_txt.write(result)
    #os.system('gnome-terminal -- python3 ' + systemTaskTTS + '__tts.py &')
    #print(' ')


def reboot_LINUX(accept_path):
    """ Reboot the system"""
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    speak('rebooting the system')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('Rebooting the system')
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: reboot__LINUX')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    os.system('reboot')
    #_txt = open(temporaryfiles + '.txt','w+')
    #_txt.write(result)
    #os.system('gnome-terminal -- python3 ' + systemTaskTTS + '__tts.py &')
    #print(' ')

def hibernate_LINUX(accept_path):
    """
    Hibernate - also known as "Suspend to Disk"

    Saves everything running to disk and performs shutdown.
    Next reboot computer will restore everything - including
    Programs and open files like the shutdown never happened.
    """
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('hibernating the system')
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: hibernate_LINUX')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    os.system('sudo systemctl hibernate')
    #_txt = open(temporaryfiles + '.txt','w+')
    #_txt.write(result)
    #os.system('gnome-terminal -- python3 ' + systemTaskTTS + '__tts.py &')
    #print(' ')


def hybridsleep_LINUX(accept_path):
    """
    Hybrid sleep.
    Will quickly wake up but also survive power cut.
    Performs both suspend AND hibernate.
    Will quickly wake up but also survive power cut.
    """
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('Hybridsleeping the system')
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: hybridsleep_LINUX')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    os.system("sudo systemctl hybrid-sleep")
    #hybrid_sleep_linux_txt = open(temporaryfiles + '.txt','w+')
    #hybrid_sleep_linux_txt.write(result)
    #os.system('gnome-terminal -- python3 ' + systemTaskTTS + 'hybrid_sleep_linux__tts.py &')
    #print(' ')

def suspend_LINUX(accept_path):
    """
    Suspend (to RAM) - also known as Stand By or Sleep mode.

    Operate PC on a minimum to save power but quickly wake up.
    """
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('Suspending the system')
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: suspend_LINUX')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    os.system('sudo systemctl suspend')
    #suspend_linux_txt = open(temporaryfiles + 'suspend_linux.txt','w+')
    #suspend_linux_txt.write(result)
    #os.system('gnome-terminal -- python3 ' + systemTaskTTS + 'suspend_linux__tts.py &')
    #print(' ')
