#!/usr/bin/python3
import os
import sys
import random
import time

from SpeechDriver.tts.ttsdefault import speak



""" GLOBAL FUNCTION """
def Log_Time():
    import datetime
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))


def mp3gen(music_path):
    """
    This function finds all the MP3 files in a folder and its subfolders and
    returns a list:
    """
    music_list = []
    for root, dirs, files in os.walk(music_path):
        for filename in files:
            if os.path.splitext(filename)[1] == ".mp3":
                music_list.append(os.path.join(root, filename.lower()))
    return music_list


def music_player(file_name):
    """
    This function takes the name of a music file as an argument and plays it
    depending on the OS.
    """
    if sys.platform == 'darwin':
        player = "afplay '" + file_name + "'"
        return os.system(player)
    elif sys.platform == 'linux2' or sys.platform == 'linux':
        player = "play '" + file_name + "'"
        return os.system(player)


def play_random(music_path, accept_path):
    """
    Random music played.

    :param music_path:
    :return:
    """
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    try:
        music_listing = mp3gen(music_path)
        music_playing = random.choice(music_listing)
        speak("Now playing: " + music_playing)
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        print('Now playing: ' + music_playing + ' > Function: play_Random')
        print(' ')
        print(' ')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        music_player(music_playing)
    except IndexError as e:
        speak('No music files found.')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        print("No music files found: {0}"+ ' > Function: play_Random '.format(e))
        print(' ')
        print(' ')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        

def play_specific_music(voice_text, music_path, accept_path):
    """
    User selected music played.

    :param voice_text:
    :param music_path:
    :return:
    """
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    words_of_message = voice_text.split()
    words_of_message.remove('play')
    cleaned_message = ' '.join(words_of_message)
    music_listing = mp3gen(music_path)
    for i in range(0, len(music_listing)):
        if cleaned_message in music_listing[i]:
            music_player(music_listing[i])
            print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            print(' ')
            print(' ')
            Log_Time()
            print(music_player(music_listing[i]) + ' > Function: play_specific_music')
            print(' ')
            print(' ')
            print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

def play_shuffle(music_path, accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    try:
        music_listing = mp3gen(music_path)
        random.shuffle(music_listing)
        for i in range(0, len(music_listing)):
            music_player(music_listing[i])
            print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            print(' ')
            print(' ')
            Log_Time()
            print(music_player(music_listing[i]) + ' > Function: play_shuffle')
            print(' ')
            print(' ')
            print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    except IndexError as e:
        speak('No music files found.')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        print("No music files found: {0}"+ ' > Function: play_Random '.format(e))
        print(' ')
        print(' ')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        

    #brainstem
    """
    elif check_message(['music', 'on']) or check_message(['lets','party']):
        music.play_random(music_path, accept_path)
    elif check_message(['hey', 'play']):
        music.play_specific_music(voice_text, music_path, accept_path)
    elif check_message(['dj', 'on']):
        music.play_shuffle(music_path, accept_path)"""

    #main
    """
        from Core.profile import profile_path
        profile = open(profile_path)
        profile_data = yaml.safe_load(profile)
        profile.close()
        #Functioning Variables
        music_path = profile_data['music_path']
        music.mp3gen(music_path)"""