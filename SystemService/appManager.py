#!/usr/bin/python3
import os
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
appManagerTTS_path = profile_data['appManagerTTS_path']
appManagerTTS = appManagerTTS_path + '/SpeechDriver/tts/ServicesTTS/appManagerTTS/'
#print(appManagerTTS)

def chromeClose(accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    speak('now closing')
    app = "chrome"
    os.system("pkill "+app)
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('chromeClose')
    print(' ')
    print(' ')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    #_txt = open(temporaryfiles + '.txt','w+')
    #_txt.write(result)
    #os.system('gnome-terminal -- python3 ' + appManagerTTS + '__tts.py &')
    #print(' ')

    #_txt = open(temporaryfiles + '.txt','w+')
    #_txt.write(result)
    #os.system('gnome-terminal -- python3 ' + appManagerTTS + '__tts.py &')
    #print(' ')


def chromeOpen(accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    speak('now opening')
    app = "google-chrome"
    os.system(app)
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('chromeOpen')
    print(' ')
    print(' ')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    #_txt = open(temporaryfiles + '.txt','w+')
    #_txt.write(result)
    #os.system('gnome-terminal -- python3 ' + appManagerTTS + '__tts.py &')
    #print(' ')


def codeClose(accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    speak('now closing')
    app = "code"
    os.system("pkill "+app)
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('codeClose')
    print(' ')
    print(' ')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    #_txt = open(temporaryfiles + '.txt','w+')
    #_txt.write(result)
    #os.system('gnome-terminal -- python3 ' + appManagerTTS + '__tts.py &')
    #print(' ')


def codeOpen(accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    speak('now opening')
    app = "code"
    os.system(app)
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('codeOpen')
    print(' ')
    print(' ')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    #_txt = open(temporaryfiles + '.txt','w+')
    #_txt.write(result)
    #os.system('gnome-terminal -- python3 ' + appManagerTTS + '__tts.py &')
    #print(' ')


def filesClose(accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    speak('now closing')
    app = "nautilus"
    os.system("pkill "+app)
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('filesClose')
    print(' ')
    print(' ')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    #_txt = open(temporaryfiles + '.txt','w+')
    #_txt.write(result)
    #os.system('gnome-terminal -- python3 ' + appManagerTTS + '__tts.py &')
    #print(' ')


def filesOpen(accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    speak('now opening')
    app = "nautilus"
    os.system(app)
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('filesOpen')
    print(' ')
    print(' ')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    #_txt = open(temporaryfiles + '.txt','w+')
    #_txt.write(result)
    #os.system('gnome-terminal -- python3 ' + appManagerTTS + '__tts.py &')
    #print(' ')


def firefoxClose(accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    speak('now closing')
    app = "firefox"
    os.system("pkill "+app)
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('firefoxClose')
    print(' ')
    print(' ')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    #_txt = open(temporaryfiles + '.txt','w+')
    #_txt.write(result)
    #os.system('gnome-terminal -- python3 ' + appManagerTTS + '__tts.py &')
    #print(' ')


def firefoxOpen(accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    speak('now opening')
    app = "firefox"
    os.system(app)
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('firefoxOpen')
    print(' ')
    print(' ')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    #_txt = open(temporaryfiles + '.txt','w+')
    #_txt.write(result)
    #os.system('gnome-terminal -- python3 ' + appManagerTTS + '__tts.py &')
    #print(' ')


def terminalClose(accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    speak('now closing')
    app = "terminal"
    os.system("pkill "+app)
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('terminalClose')
    print(' ')
    print(' ')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    #_txt = open(temporaryfiles + '.txt','w+')
    #_txt.write(result)
    #os.system('gnome-terminal -- python3 ' + appManagerTTS + '__tts.py &')
    #print(' ')


def terminalOpen(accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    speak('now opening')
    app = "gnome-terminal"
    os.system(app)
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('terminalOpen')
    print(' ')
    print(' ')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    #_txt = open(temporaryfiles + '.txt','w+')
    #_txt.write(result)
    #os.system('gnome-terminal -- python3 ' + appManagerTTS + '__tts.py &')
    #print(' ')
