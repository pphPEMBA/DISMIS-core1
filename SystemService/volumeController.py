#!/usr/bin/python3
from os import system
import os
import time

#from tkinter import *

""" Importing Profiles """
import yaml
from Core.profile import temporaryfiles, profile_path
profile = open(profile_path)
profile_data = yaml.safe_load(profile)
profile.close()
#Functioning Variables
volumeControllerTTS_path = profile_data['volumeControllerTTS_path']
volumeControllerTTS = volumeControllerTTS_path + '/SpeechDriver/tts/ServicesTTS/volumeControllerTTS/'
#print(volumeControllerTTS)

""" GLOBAL FUNCTION """
def Log_Time():
    import datetime
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

def volume100__Linux(accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    #root = Tk()
    #root.geometry('1150x300+120+0')
    #root.title("Dismis's Volume")
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('Volume set to 100%')
    print(' ')
    print(' ')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    system("pactl -- set-sink-volume 0 100%")
    #result = "Volume set to 100%"
    #Label(root, padx = 3000, pady = 3000, compound=CENTER, text=result, bg="#171717", fg = "white", font='times 15 bold').pack()
    #root.after(2800, lambda: root.destroy())
    #volume100_txt = open(temporaryfiles + 'volume100.txt','w+')
    #volume100_txt.write(result)
    #os.system('gnome-terminal -- python3 ' + volumeControllerTTS + 'volume100__tts.py &')

def volume90__Linux(accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    #root = Tk()
    #root.geometry('1150x300+120+0')
    #root.title("Dismis's Volume")
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('Volume set to 90%')
    print(' ')
    print(' ')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    system("pactl -- set-sink-volume 0 90%")
    result = "Volume set to 90%"
    #Label(root, padx = 3000, pady = 3000, compound=CENTER, text=result, bg="#171717", fg = "white", font='times 15 bold').pack()
    #root.after(2800, lambda: root.destroy())
    #volume90_txt = open(temporaryfiles + 'volume90.txt','w+')
    #volume90_txt.write(result)
    #os.system('gnome-terminal -- python3 ' + volumeControllerTTS + 'volume90__tts.py &')

def volume80__Linux(accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    #root = Tk()
    #root.geometry('1150x300+120+0')
    #root.title("Dismis's Volume")
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('Volume set to 80%')
    print(' ')
    print(' ')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    system("pactl -- set-sink-volume 0 80%")
    result = "Volume set to 80%"
    #Label(root, padx = 3000, pady = 3000, compound=CENTER, text=result, bg="#171717", fg = "white", font='times 15 bold').pack()
    #root.after(2800, lambda: root.destroy())
    #volume80_txt = open(temporaryfiles + 'volume80.txt','w+')
    #volume80_txt.write(result)
    #os.system('gnome-terminal -- python3 ' + volumeControllerTTS + 'volume80__tts.py &')

def volume70__Linux(accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    root = Tk() 
    root.geometry('1150x300+120+0')
    root.title("Dismis's Volume")
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('Volume set to 70%')
    print(' ')
    print(' ')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    system("pactl -- set-sink-volume 0 70%")
    result = "Volume set to 70%"
    #Label(root, padx = 3000, pady = 3000, compound=CENTER, text=result, bg="#171717", fg = "white", font='times 15 bold').pack()
    #root.after(2800, lambda: root.destroy())
    #volume70_txt = open(temporaryfiles + 'volume70.txt','w+')
    #volume70_txt.write(result)
    #os.system('gnome-terminal -- python3 ' + volumeControllerTTS + 'volume70__tts.py &')

def volume60__Linux(accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    #root = Tk()
    #root.geometry('1150x300+120+0')
    #root.title("Dismis's Volume")
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('Volume set to 60%')
    print(' ')
    print(' ')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    system("pactl -- set-sink-volume 0 60%")
    result = "Volume set to 60%"
    #Label(root, padx = 3000, pady = 3000, compound=CENTER, text=result, bg="#171717", fg = "white", font='times 15 bold').pack()
    #root.after(2800, lambda: root.destroy())
    #volume60_txt = open(temporaryfiles + '.txt','w+')
    #volume60_txt.write(result)
    #os.system('gnome-terminal -- python3 ' + volumeControllerTTS + 'volume60__tts.py &')

def volume50__Linux(accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    #root = Tk()
    #root.geometry('1150x300+120+0')
    #root.title("Dismis's Volume")
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('Volume set to 50%')
    print(' ')
    print(' ')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    system("pactl -- set-sink-volume 0 50%")
    result = "Volume set to 50%"
    #Label(root, padx = 3000, pady = 3000, compound=CENTER, text=result, bg="#171717", fg = "white", font='times 15 bold').pack()
    #root.after(2800, lambda: root.destroy())
    #volume50_txt = open(temporaryfiles + 'volume50.txt','w+')
    #volume50_txt.write(result)
    #os.system('gnome-terminal -- python3 ' + volumeControllerTTS + 'volume50__tts.py &')

def volume40__Linux(accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    #root = Tk()
    #root.geometry('1150x300+120+0')
    #root.title("Dismis's Volume")
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('Volume set to 40%')
    print(' ')
    print(' ')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    system("pactl -- set-sink-volume 0 40%")
    result = "Volume set to 40%"
    #Label(root, padx = 3000, pady = 3000, compound=CENTER, text=result, bg="#171717", fg = "white", font='times 15 bold').pack()
    #root.after(2800, lambda: root.destroy())
    #volume40_txt = open(temporaryfiles + 'volume40.txt','w+')
    #volume40_txt.write(result)
    #os.system('gnome-terminal -- python3 ' + volumeControllerTTS + 'volume40__tts.py &')

def volume30__Linux(accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    #root = Tk()
    #root.geometry('1150x300+120+0')
    #root.title("Dismis's Volume")
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('Volume set to 30%')
    print(' ')
    print(' ')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    system("pactl -- set-sink-volume 0 30%")
    result = "Volume set to 30%"
    #Label(root, padx = 3000, pady = 3000, compound=CENTER, text=result, bg="#171717", fg = "white", font='times 15 bold').pack()
    #root.after(2800, lambda: root.destroy())
    #volume30_txt = open(temporaryfiles + 'volume30.txt','w+')
    #volume30_txt.write(result)
    #os.system('gnome-terminal -- python3 ' + volumeControllerTTS + 'volume30__tts.py &')

def volume20__Linux(accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    #root = Tk()
    #root.geometry('1150x300+120+0')
    #root.title("Dismis's Volume")
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('Volume set to 20%')
    print(' ')
    print(' ')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    system("pactl -- set-sink-volume 0 20%")
    result = "Volume set to 20%"
    #Label(root, padx = 3000, pady = 3000, compound=CENTER, text=result, bg="#171717", fg = "white", font='times 15 bold').pack()
    #root.after(2800, lambda: root.destroy())
    #volume20_txt = open(temporaryfiles + 'volume20.txt','w+')
    #volume20_txt.write(result)
    #os.system('gnome-terminal -- python3 ' + volumeControllerTTS + 'volume20__tts.py &')


def volume10__Linux(accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    #root = Tk()
    #root.geometry('1150x300+120+0')
    #root.title("Dismis's Volume")
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('Volume set to 10%')
    print(' ')
    print(' ')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    system("pactl -- set-sink-volume 0 10%")
    result = "Volume set to 10%"
    #Label(root, padx = 3000, pady = 3000, compound=CENTER, text=result, bg="#171717", fg = "white", font='times 15 bold').pack()
    #root.after(2800, lambda: root.destroy())
    #volume10_txt = open(temporaryfiles + 'volume10.txt','w+')
    #volume10_txt.write(result)
    #os.system('gnome-terminal -- python3 ' + volumeControllerTTS + 'volume10__tts.py &')

def volumeMute__Linux(accept_path):
    """Mute: Silence your speaker's sound."""
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    #root = Tk()
    #root.geometry('1150x300+120+0')
    #root.title("Dismis's Volume")
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('Volume set to 0%')
    print(' ')
    print(' ')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    #system("pactl -- set-sink-unmute 0 toggle") #Yo function use garo vaana manually volume increase garnu parcha. So instead
    system("pactl -- set-sink-volume 0 0%") #Yo use garney
    result = "Volume mute"
    #Label(root, padx = 3000, pady = 3000, compound=CENTER, text=result, bg="#171717", fg = "white", font='times 15 bold').pack()
    #root.after(2800, lambda: root.destroy())
    #volumeMute_txt = open(temporaryfiles + 'volumeMute.txt','w+')
    #volumeMute_txt.write(result)
    #os.system('gnome-terminal -- python3 ' + volumeControllerTTS + 'volumeMute__tts.py &')

def getCurrentVol__linux(accept_path): #not working
    """Get your current speaker's sound."""
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    #root = Tk()
    #root.geometry('1150x300+120+0')
    #root.title("Dismis's Volume")
    getVol = os.system("awk -F \"[][]\" '/dB/ { print $2 }' <(amixer sget Master)")
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print("Current volume is " + getVol)
    print(' ')
    print(' ')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    result = getVol
    #Label(root, padx = 3000, pady = 3000, compound=CENTER, text=result, bg="#171717", fg = "white", font='times 15 bold').pack()
    #root.after(2800, lambda: root.destroy())
    #getCurrentVol_txt = open(temporaryfiles + 'getCurrentVol.txt','w+')
    #getCurrentVol_txt.write(result)
    #os.system('gnome-terminal -- python3 ' + volumeControllerTTS + 'getCurrentVol__tts.py &')


""" Worked
from subprocess import call
valid = False

while not valid:
    volume = input('What volume? > ')

    try:
        volume = int(volume)

        if (volume <= 100) and (volume >= 0):
            call(["amixer", "-D", "pulse", "sset", "Master", str(volume)+"%"])
            valid = True

    except ValueError:
        pass    """