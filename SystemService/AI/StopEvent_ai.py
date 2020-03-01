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

import smtplib
def Alert5(slave_sender, slave_passwd, receiver):
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
        print('--- StopEvent Mail Sent ---')
    except socket.gaierror:
        pass

startTime = datetime.datetime(2020, 4, 18, 10, 00) #Years Months Days Hours Minutes
#2020, 4, 18, 10, 00 [Baishak 6 2077]
while datetime.datetime.now() < startTime:
    time.sleep(1)
output = 'Boss, it\'s time to change schedule\'s time and routines in schedule_ai.py, schedule.txt'
print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
print(' ')
print(' ')
Log_Time()
print(output')
Alert5(slave_sender, slave_passwd, receiver)
print(' ')
print(' ')
print('\t\t\t\tFunction: StopEvent_ai')
print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
speak(output')



