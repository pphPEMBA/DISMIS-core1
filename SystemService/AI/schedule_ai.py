# Schedule Library imported
import yaml
import schedule
import time
import os
import sys
import smtplib

""" GLOBAL FUNCTION """
def Log_Time():
    import datetime
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))


""" SPECIFIC FUNCTION only for schedule.py """
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
      tts_engine = 'pico2wave -w ttsSchedule_ai.wav '
      return os.system(tts_engine + ' "' + message + '"' + '&& aplay ttsSchedule_ai.wav && rm ttsSchedule_ai.wav')
    
    
""" Importing Profiles """
profile = open(
    "/home/d-slave1/d1_SuperDismis/Dismis_Home_Automation/SystemService/APIs/profile.yaml")
profile_data = yaml.safe_load(profile)
profile.close()
# Functioning Variables
#schedule_path = profile_data['schedule_path']
slave_sender = profile_data['slave_sender']
slave_passwd = profile_data['slave_passwd']
receiver = profile_data['receiver']
conversationTTS_path = profile_data['conversationTTS_path']
conversationTTS = conversationTTS_path + '/SpeechDriver/tts/ServicesTTS/conversationTTS/'
#print(conversationTTS)


""" Routines """
def routine1(slave_sender, slave_passwd, receiver):
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('Its time to work on Dismis Home Automation. You got 1 hours 5 minutes.')
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: routine1')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    speak('Its time to work on Dismis Home Automation. You got 1 hours 5 minutes')
    From = slave_sender
    to = receiver
    subject = 'Dismis Alert: SCHEDULE '
    msg = 'Subject:{}\n\nPEMBA Its time to work on Dismis Home Automation. You got 1 hours 5 minutes'.format(subject)
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.ehlo()
    server.login(slave_sender, slave_passwd)
    server.sendmail(From, to, msg)
    server.quit()

def routine2(slave_sender, slave_passwd, receiver):
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('Lets have some study PEMBA.')
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: routine2')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    speak('Lets have some study PEMBA.')
    From = slave_sender
    to = receiver
    subject = 'Dismis Alert: SCHEDULE '
    msg = 'Subject:{}\n\nPEMBA Lets have some study'.format(subject)
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.ehlo()
    server.login(slave_sender, slave_passwd)
    server.sendmail(From, to, msg)
    server.quit()

def routine3(slave_sender, slave_passwd, receiver):
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('Now stop all your running works and get ready for tuition class PEMBA.')
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: routine3')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    speak('Now stop all your running works and get ready for tuition class PEMBA')
    From = slave_sender
    to = receiver
    subject = 'Dismis Alert: SCHEDULE '
    msg = 'Subject:{}\n\nPEMBA Now stop all your running works and get ready for tuition class'.format(subject)
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.ehlo()
    server.login(slave_sender, slave_passwd)
    server.sendmail(From, to, msg)
    server.quit()

def routine4(slave_sender, slave_passwd, receiver):
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('Its time to get fit. Get ready for some exercise.')
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: routine4')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    speak('Its time to get fit. Get ready for some exercise')
    From = slave_sender
    to = receiver
    subject = 'Dismis Alert: SCHEDULE '
    msg = 'Subject:{}\n\nPEMBA Its time to get fit. Get ready for some exercise'.format(subject)
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.ehlo()
    server.login(slave_sender, slave_passwd)
    server.sendmail(From, to, msg)
    server.quit()
    
def routine5(slave_sender, slave_passwd, receiver):
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('Again lets study PEMBA.')
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: routine5')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    speak('Again lets study PEMBA.')
    From = slave_sender
    to = receiver
    subject = 'Dismis Alert: SCHEDULE '
    msg = 'Subject:{}\n\nAgain lets study PEMBA.'.format(subject)
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.ehlo()
    server.login(slave_sender, slave_passwd)
    server.sendmail(From, to, msg)
    server.quit()

def routine6(slave_sender, slave_passwd, receiver):
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('Study hard PEMBA.')
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: routine6')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    speak('Study hard PEMBA.')
    From = slave_sender
    to = receiver
    subject = 'Dismis Alert: SCHEDULE '
    msg = 'Subject:{}\n\nPEMBA Study hard'.format(subject)
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.ehlo()
    server.login(slave_sender, slave_passwd)
    server.sendmail(From, to, msg)
    server.quit()

""" TASK SCHEDULEING """
""" After every 10mins geeks() is called. """
# schedule.every(2).minutes.do(routine1)
""" After every hour geeks() is called. """
# schedule.every().hour.do(routine1)
""" After every 5 to 10mins in between run work() """
# schedule.every(5).to(10).minutes.do(work)
""" Every monday good_luck() is called """
# schedule.every().monday.do(good_luck)
""" Every tuesday at 18:00 sudo_placement() is called """
# schedule.every().tuesday.at("18:00").do(sudo_placement)

""" Every day at 12am or 00:00 time bedtime() is called. """
schedule.every().day.at("10:00").do(routine1, slave_sender, slave_passwd, receiver)
schedule.every().day.at("13:00").do(routine2, slave_sender, slave_passwd, receiver)
schedule.every().day.at("14:30").do(routine3, slave_sender, slave_passwd, receiver)
schedule.every().day.at("17:00").do(routine4, slave_sender, slave_passwd, receiver)
schedule.every().day.at("19:00").do(routine5, slave_sender, slave_passwd, receiver)
schedule.every().day.at("11:05").do(routine6, slave_sender, slave_passwd, receiver)

# Loop so that the scheduling task
# keeps on running all time.
while True:
        # Checks whether a scheduled task
        # is pending to run or not
    schedule.run_pending()
    
