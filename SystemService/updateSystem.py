#!/usr/bin/python3
import os
import subprocess
import time

#from tkinter import *

from SpeechDriver.tts.ttsdefault import speak


""" Importing Profiles """
import yaml
from Core.profile import temporaryfiles, profile_path
profile = open(profile_path)
profile_data = yaml.safe_load(profile)
profile.close()
#Functioning Variables
updateSystemTTS_path = profile_data['updateSystemTTS_path']
updateSystemTTS = updateSystemTTS_path + '/SpeechDriver/tts/ServicesTTS/updateSystemTTS/'
#print(updateSystemTTS)
 
""" GLOBAL FUNCTION """
def Log_Time():
    import datetime
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))


def update_system(accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    #root = Tk()
    #root.geometry('1150x300+120+0')
    #root.title("Dismis_slave1's System Update")
    user_distributor_id = subprocess.check_output('lsb_release -i', shell=True)
    user_distribution = user_distributor_id.decode("utf-8").split('\t')[1]
    result = "updating operating system, Please save your work or you may face some data loss after reboot, Enter the password"
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(user_distribution)
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: update_system')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    speak(result)
    #updateSystem_txt = open(temporaryfiles + 'updateSystem.txt','w+')
    #updateSystem_txt.write(result)
    #os.system('gnome-terminal -- python3 ' + updateSystemTTS + 'updateSystem__tts.py &')
    #label = Label(root, padx = 3000, pady = 3000, compound=CENTER, text=result, bg="#171717", fg = "white", font='times 15 bold').pack()
    #root.after(2800, lambda: root.destroy())
    #mainloop()
    if user_distribution == "Ubuntu\n" or user_distribution == "LinuxMint\n":
        os.system('sudo apt-get update && sudo apt-get upgrade -y &')

    elif user_distribution == "Fedora\n":
        os.system('dnf upgrade && dnf system-upgrade &')
        
    elif user_distribution == "Arch Linux\n":
        os.system('sudo pacman -Syu &')
        
    elif user_distribution == "openSUSE\n":
        os.system('sudo zypper update &')
