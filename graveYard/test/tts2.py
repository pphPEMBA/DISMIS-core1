#!/usr/bin/python3
import os,yaml
import sys, time


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

#speak("Earth is the third planet from the Sun and the only astronomical object known to harbor life. According to radiometric dating and other evidence, Earth formed over 4.5 billion years ago. Earth's gravity interacts with other objects in space, especially the Sun and the Moon, which is Earth's only natural satellite. Earth orbits around the Sun in 365.256 days, a period known as an Earth sidereal year. During this time, Earth rotates about its axis about 366.256 times.")
print("Earth is the third planet from the Sun and the only astronomical object known to harbor life. According to radiometric dating and other evidence, Earth formed over 4.5 billion years ago. Earth's gravity interacts with other objects in space, especially the Sun and the Moon, which is Earth's only natural satellite. Earth orbits around the Sun in 365.256 days, a period known as an Earth sidereal year. During this time, Earth rotates about its axis about 366.256 times.")