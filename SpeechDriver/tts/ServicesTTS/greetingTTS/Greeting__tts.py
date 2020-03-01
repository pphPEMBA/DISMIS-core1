#!/usr/bin/python3
import os,yaml
import sys, time

temporaryfiles = '/home/d-slave1/d1_SuperDismis/DISMIS-core/.temporaryfiles/'


def speak(message): #ALSO USING IN || BestfriendBirthdayALERT_ai.py | schedule_ai.py | googleMailNotify ||
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
      tts_engine = 'pico2wave -w tts_pico2wave.wav '
      print(' ')
      return os.system(tts_engine + ' "' + message + '"' + '&& aplay tts_pico2wave.wav && rm tts_pico2wave.wav')

Greeting_txt = open(temporaryfiles + 'Greeting.txt','r')
tts = Greeting_txt.read()
speak(tts)
os.system('rm ' + temporaryfiles + 'Greeting.txt')
