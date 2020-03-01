#!/usr/bin/python3
import datetime
import time
import os

#from tkinter import *

from SpeechDriver.tts.ttsdefault import speak

""" GLOBAL FUNCTION """
def Log_Time():
    import datetime
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

""" IMPORING PROFILE """
from Core.profile import temporaryfiles, date_timeTTS_path
date_timeTTS = date_timeTTS_path + '/SpeechDriver/tts/ServicesTTS/date_timeTTS/'
currenttimeTTS = date_timeTTS_path + '/SpeechDriver/tts/ServicesTTS/date_timeTTS/'
#print(date_timeTTS)
'--------------------------------------------------------------------------------------------------------------------------------------'
'--------------------------------------------------------------------------------------------------------------------------------------'


def date(accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    try:
        #root = Tk()
        #root.geometry('1150x300+120+0')
        #root.title("Dismis's Date")
        currentdate = datetime.datetime.now()
        result = currentdate.strftime("%d %b %Y %A")
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        print(result)
        print(' ')
        print(' ')
        print('\t\t\t\tSkill: date')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        #Label(root, padx = 3000, pady = 3000, compound=CENTER, text=result, bg="#171717", fg = "white", font='times 15 bold').pack()
        #root.after(2800, lambda: root.destroy())
        #root.mainloop()
        #speak(result)
        date_txt = open(temporaryfiles + 'date.txt','w+')
        date_txt.write(result)
        os.system('gnome-terminal -- python3 ' + date_timeTTS + 'date__tts.py &')
        print(date_timeTTS)
    except:
        DisError = 'System Failure! Unable to perform date skill sir'
        print('****************************************************************')
        print(' ')
        Log_Time()
        print('***' + DisError + '***')
        print(' ')
        print('****************************************************************')
        speak(DisError)


def currenttime(accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    #root = Tk()
    #root.geometry('1150x300+120+0')
    #root.title("Dismis's Time")
    try:
        result = time.strftime("%I:%M:%S %A")
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        print(result)
        print(' ')
        print(' ')
        print('\t\t\t\tSkill: currenttime')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        #speak(result)
        #Label(root, padx = 3000, pady = 3000, compound=CENTER, text=result, bg="#171717", fg = "white", font='roots 15 bold').pack()
        #root.after(2800, lambda: root.destroy())
        #root.mainloop()
        currenttime_txt = open(temporaryfiles + 'currenttime.txt','w+')
        currenttime_txt.write(result)
        os.system('gnome-terminal -- python3 ' + date_timeTTS + 'currenttime__tts.py &')
    except:
        DisError = 'System Failure! Unable to perform currenttime skill sir'
        print('****************************************************************')
        print(' ')
        Log_Time()
        print('***' + DisError + '***')
        print(' ')
        print('****************************************************************')
        speak(DisError)
