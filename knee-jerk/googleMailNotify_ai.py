#!/usr/bin/python3
import imaplib
import email, yaml, time
import time, os, sys


""" GLOBAL FUNCTION """
def Log_Time():
    import datetime
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

""" Importing Profiles """
profile = open(
    "/home/d-slave1/d1_SuperDismis/Dismis_Home_Automation/SystemService/APIs/profile.yaml")
profile_data = yaml.safe_load(profile)
profile.close()
# Functioning Variables
#schedule_path = profile_data['schedule_path']
main_sender = profile_data['main_sender']
main_passwd = profile_data['main_passwd']

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
      print(' ')
      tts_engine = 'pico2wave -w tts_GmailNotify.wav '
      print(' ')
      return os.system(tts_engine + ' "' + message + '"' + '&& aplay tts_GmailNotify.wav && rm tts_GmailNotify.wav')

mail=imaplib.IMAP4_SSL('imap.gmail.com',993)
mail.login(main_sender, main_passwd)
msg =''
while 1:
	typ, messages = mail.select('INBOX')
	if(str(messages)!=msg):
			print(' ')
			print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
			print(' ')
			print(' ')
			Log_Time()
			print('new message arrived !')
			print(' ')
			print(' ')
			print("\t\t\t\tFunction: googleMailNotify")
			print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
			msg=str(messages)
			speak('PEMBA You have mail')
			print(' ')