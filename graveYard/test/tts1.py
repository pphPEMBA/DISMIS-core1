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

speak("The term planet is ancient, with ties to history, astrology, science, mythology, and religion. Five planets in the Solar System are visible to the naked eye. These were regarded by many early cultures as divine, or as emissaries of deities. As scientific knowledge advanced, human perception of the planets changed, incorporating a number of disparate objects. In 2006, the International Astronomical Union (IAU) officially adopted a resolution defining planets within the Solar System.")
#print("The term planet is ancient, with ties to history, astrology, science, mythology, and religion. Five planets in the Solar System are visible to the naked eye. These were regarded by many early cultures as divine, or as emissaries of deities. As scientific knowledge advanced, human perception of the planets changed, incorporating a number of disparate objects. In 2006, the International Astronomical Union (IAU) officially adopted a resolution defining planets within the Solar System.")
