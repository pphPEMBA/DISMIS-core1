#!/usr/bin/python3
#Say you want to schedule some code to run after a delay or at a specific time.
import time, datetime, yaml, os, socket

""" GLOBAL FUNCTION """
def Log_Time():
    import datetime
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

""" TTS """
def speak(message):
    """This function takes a message as an argument and converts it to speech depending on the OS.  """
    if sys.platform == 'darwin': 
        tts_engine = 'say'
        return os.system(tts_engine + ' ' + message)
    elif sys.platform == 'Linux' or sys.platform == 'linux' or sys.platform == 'Ubuntu':
        #espeak
        """tts_engine = 'espeak'
        print(tts_engine + ' "' + message + '"')
        return os.system(tts_engine + ' "' + message + '"')"""
        #pico2wave
        tts_engine = 'pico2wave -w ttsBestfriendBirthdayALERT.wav '
        return os.system(tts_engine + ' "' + message + '"' + '&& aplay ttsBestfriendBirthdayALERT.wav && rm ttsBestfriendBirthdayALERT.wav')      

""" Importing Profiles """
import yaml
profile = open("/home/d-slave1/d1_SuperDismis/Dismis_Home_Automation/SystemService/APIs/profile.yaml")
profile_data = yaml.safe_load(profile)
profile.close()
#Functioning Variables
slave_sender = profile_data['slave_sender']
slave_passwd = profile_data['slave_passwd']
receiver = profile_data['receiver']
conversationTTS_path = profile_data['conversationTTS_path']
conversationTTS = conversationTTS_path + '/SpeechDriver/tts/ServicesTTS/conversationTTS/'
#print(conversationTTS)

#BestfriendBirthday_path = profile_data['BestfriendBirthday_path']
#BestfriendBirthday_date = profile_data['BestfriendBirthday_date']

import smtplib
def Alert1(slave_sender, slave_passwd, receiver):
    try:
        From = slave_sender
        to = receiver
        subject = 'Dismis Alert: Anisha\'s Birthday Tomorrow '
        msg = 'Subject:{}\n\nPEMBA Tomorrow is Anisha\'s birthday, may you have already remebered it. I\'m here to assist you, Don\'t forget to wish her tonight.\n\nThis is a message from Alert1.\n\n\n And PEMBA don\'t forget to change the date as follows in the next year'.format(subject)
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.ehlo()
        server.login(slave_sender, slave_passwd)
        server.sendmail(From, to, msg)
        server.quit()
        print('--- Reminder Mail Sent ---')
    except socket.gaierror:
        pass
""" Tkinter """
#from tkinter import *
#def tk_window():
    #root = Tk()
    #root.geometry('1150x300+120+0')
    #root.title("Dismis's Birthday Reminder")
    #output = 'Boss, Anisha\'s birthday is tomorrow. Don\'t forget to wish her at 12 o\'clock'
    #speak('Boss, Anisha\'s birthday is tomorrow. Don\'t forget to wish her at 12 o\'clock')
    #Label(root, padx = 3000, pady = 3000, compound=CENTER, text=output, bg="#171717", fg = "white", font='times 15 bold').pack()
    #root.after(5000, lambda: root.destroy())
    #root.mainloop()
    
startTime = datetime.datetime(2020, 3, 2, 10, 00) #Years Months Days Hours Minutes
#२०७६ फागुन १९
#2020 March 2  
#2020, 3, 2, 11, 00
while datetime.datetime.now() < startTime:
    time.sleep(1)
print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
print(' ')
print(' ')
Log_Time()
print('Boss, Anisha\'s birthday is tomorrow. Don\'t forget to wish her at 12 o\'clock')
Alert1(slave_sender, slave_passwd, receiver)
print(' ')
print(' ')
print('\t\t\t\tFunction: BestfriendBirthdayALERT_ai')
print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
speak('Boss, Anisha\'s birthday is tomorrow. Don\'t forget to wish her at 12 o\'clock')
#tk_window()
time.sleep(1)


