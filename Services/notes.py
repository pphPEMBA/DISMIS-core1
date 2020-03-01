#!/usr/bin/python3
import sqlite3
from datetime import datetime
import os
import time

#from tkinter import *
from SpeechDriver.tts.ttsdefault import speak

# # # # # # # # # # # # #
# #NOT USING CURRENTLY# #
# #NOT USING CURRENTLY# #
# #NOT USING CURRENTLY# #
# #NOT USING CURRENTLY# #
# #NOT USING CURRENTLY# #
# #NOT USING CURRENTLY# #
# #NOT USING CURRENTLY# #
# #NOT USING CURRENTLY# #
# #NOT USING CURRENTLY# #
# #NOT USING CURRENTLY# #
# # # # # # # # # # # # #

""" GLOBAL FUNCTION """
def Log_Time():
    import datetime
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

""" Importing Profiles """
import yaml
from Core.profile import temporaryfiles, profile_path
profile = open(profile_path)
profile_data = yaml.safe_load(profile)
profile.close()
#Functioning Variables
notesTTS_path = profile_data['notesTTS_path']
notesTTS = notesTTS_path + '/SpeechDriver/tts/ServicesTTS/notesTTS/'
#print(notesTTS)


def note_something(voice_text, accept_path, memory_db):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    conn = sqlite3.connect(memory_db)
    words_of_message = voice_text.split()
    words_of_message.remove('note')
    cleaned_message = ' '.join(words_of_message)
    conn.execute("INSERT INTO notes (notes, notes_date) VALUES (?, ?)",
    (cleaned_message, datetime.strftime(datetime.now(), '%d-%m-%Y')))
    conn.commit()
    conn.close()
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('Your note has been saved')
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: note_something')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    result = 'Your note has been saved.'
    note_something_txt = open(temporaryfiles + 'note_something.txt','w+')
    note_something_txt.write(result)
    os.system('gnome-terminal -- python3 ' + notesTTS + 'note_something__tts.py &')
    print(' ')


def show_all_notes(accept_path, memory_db):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    conn = sqlite3.connect(memory_db)
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('Your notes are as follows:')
    result = 'Your notes are as follows:'
    cursor = conn.execute("SELECT notes FROM notes")
    for row in cursor:
        print(row[0])
        print(' ')
        print(' ')
        print('\t\t\t\tSkill: show_all_notes')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        #result(row[0])
    conn.close()
    show_all_notes_txt = open(temporaryfiles + 'show_all_notes.txt','w+')
    show_all_notes_txt.write(result)
    os.system('gnome-terminal -- python3 ' + notesTTS + 'show_all_notes__tts.py &')
    print(' ')

