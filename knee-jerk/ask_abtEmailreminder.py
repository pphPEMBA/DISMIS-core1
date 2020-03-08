#!/usr/bin/python3
#Say you want to schedule some code to run after a delay or at a specific time.
import time
import datetime, yaml, os, sys
import smtplib, socket
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText  

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
        tts_engine = 'pico2wave -w tts_wishMailer.wav '
        return os.system(tts_engine + ' "' + message + '"' + '&& aplay tts_wishMailer.wav && rm tts_wishMailer.wav')      
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


slave_sender = 'pembamoktan.t@gmail.com'
slave_passwd = 'D1i1s1m1i1s@'
receiver = 'pembatamang.m@gmail.com'
wish = 'Sir its time to ask about the gmail, if they are using new or the same gmail.'
while True:
    start_time = datetime.datetime(2020,3,8,13,00)
    if datetime.datetime.now() == start_time:
        try:
            msg = MIMEMultipart()
            msg['From'] = slave_sender
            msg['To'] = receiver
            msg['Subject'] = 'Update Emails!'
            body = wish
            msg.attach(MIMEText(body,'plain'))
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.starttls()
            server.ehlo()
            server.login(slave_sender, slave_passwd)
            server.sendmail(slave_sender, receiver, msg.as_string())
            server.quit()
            print('--- Ask email reminder send successful. ---')
        except socket.gaierror:
            pass
        break

#while True:
#    current_time = datetime.now().strftime("%H:%M:%S")
#    if current_time == "14:41:25":
#        print("alarm", "this is the message")
#        break
#    else:
#        pass
