import ctypes
from google import google
import boto3
import speech_recognition as sr
import os
from playsound import playsound
import webbrowser
import random
import pyttsx3
import time

speech = sr.Recognizer()

online_dict = {'auntie': 'anutie', 'aunty': 'aunty', 'ugly': 'ugly', 'online': 'online', 'baby': 'baby', 'start on': 'start on', 'buddy': 'buddy', 'honey': 'honey', 'love': 'love'}
greeting_dict = {'hi': 'hi', 'yo': 'yo', 'oye': 'oye'}
open_launch_dict = {'open': 'open', 'launch': 'launch'}
google_searches_dict = {'what': 'what', 'why': 'why', 'who': 'who', 'which': 'which', 'when': 'when'}
social_media_dict = {'facebook': 'https://www.facebook.com', 'twitter': 'https://www.twitter.com', 'instagram': 'https://www.instagram.com', 'gmail': 'https://www.gmail.com', '500': 'https://www.500px.com', 'page': 'https://www.facebook.com/pembashoot/', 'telegram': 'https://web.telegram.org', 'youtube': 'http://www.youtube.com'}
social_post = {'post': 'post'}

mp3_thankyou_list = ['DISMIS mp3/thankyou_1.mp3', 'DISMIS mp3/thankyou_2.mp3']
mp3_listening_problem_list = ['DISMIS mp3/listening_problem_1.mp3', 'DISMIS mp3/listening_problem_2.mp3']
mp3_struggling_list = ['DISMIS mp3/struggling_1.mp3']
mp3_google_search = ['DISMIS mp3/google_search_1.mp3', 'DISMIS mp3/google_search_2.mp3']
mp3_greeting_list = ['DISMIS mp3/greeting_accept.mp3', 'DISMIS mp3/greeting_accept_2.mp3']
mp3_open_launch_list = ['DISMIS mp3/open_1.mp3', 'DISMIS mp3/open_2.mp3', 'DISMIS mp3/open_3.mp3']


error_occurrence = 0

def greet(self):
    """ Greet the user """
print(r" _  _      ________   _      _    ________    _      _    _______   ____  ")
print(r"|      \      |      | \    / |      |       | \    / |      |     /      ")
print(r"|       |     |      |  \  /  |      |       |  \  /  |      |     \      ")
print(r"|       |     |      |   \/   |      |       |   \/   |      |      '---; ")
print(r"|______/      |      |        |      |       |        |      |      ___/  ")
print(r"           -------                --------                -------         ")

try:
    engine = pyttsx3.init()
except ImportError:
    print('Requested driver is not foun')
except RuntimeError:
    print('Driver fail to initialize')

voices = engine.getProperty('voices')

engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
rate = engine.getProperty('rate')
engine.setProperty('rate',rate)

def is_valid_google_search(phrase):
    if (google_searches_dict.get(phrase.split(' ')[0]) == phrase.split(' ')[0]):
        return True

def play_sound(mp3_list):
    mp3 = random.choice(mp3_list)
    playsound(mp3)

def speak_text_cmd(cmd):
    engine.say(cmd)
    engine.runAndWait()

def read_voice_cmd():
    voice_text = ''
    print('Listening...')

    global error_occurrence


    try:
        with sr.Microphone() as source:
            audio = speech.listen(source=source, timeout=10, phrase_time_limit=5)
        voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:

        if error_occurrence == 0:
            play_sound(mp3_listening_problem_list)
            error_occurrence += 1
        elif error_occurrence == 1:
            play_sound(mp3_struggling_list)
            error_occurrence += 1

    except sr.RequestError as e:
        print('Network error')
    except sr.WaitTimeoutError:
        if error_occurrence == 0:
            play_sound(mp3_listening_problem_list)
            error_occurrence += 1
        elif error_occurrence == 1:
            play_sound(mp3_struggling_list)
            error_occurrence += 1

    return voice_text

def relaxingmusic():
    speak_text_cmd('sure thing')
    speak_text_cmd('playing relaxing music')
    speak_text_cmd('what do you want me to play for you')
    k = read_voice_cmd()
    speak_text_cmd('ok sir playing' + k + 'for you')
    os.startfile('C:\Users\Mr P.H PEMBA\OneDrive\Music/' + k + '.mp3')


def countdown():
    seconds = int(input("How many second to wait?"))
    for i in range(seconds):
        print(str(seconds - i) + " seconds remin")
        speak_text_cmd(str(seconds - i) + " seconds remin")
    time.sleep(1)

def online():
    d = random.choice(['yes sir', 'yes buddy', 'i am ready', 'i\'m working sir', 'now i am online sir'])
    speak_text_cmd(d)

def is_valid_note(greet_dict, voice_note):
    for key, value in greet_dict.iteritems():
        # 'hello Dismiss'
        try:
           if value == voice_note.split(' ')[0]:
               return True
               break
           elif key == voice_note.split(' ')[1]:
               return True
               break
        except IndexError:
           pass

    return False


if __name__ == '__main__':

    playsound('DISMIS mp3/greeting.mp3')

    while True:

        voice_note = read_voice_cmd().lower()
        print('cmd : {}'.format(voice_note))

        if is_valid_note(greeting_dict, voice_note):
            print('In greeting....')
            play_sound(mp3_greeting_list)
            continue
        elif 'hello' in voice_note:
            speak_text_cmd('To whom shall I greet sir?')
            a = raw_input('To whom shall I greet sir?')
            speak_text_cmd('hello ' + a + ' have a good day')
            continue
        elif is_valid_note(open_launch_dict, voice_note):
            print('In open....')
            play_sound(mp3_open_launch_list)
            if(is_valid_note(social_media_dict,voice_note)):
                # Launch Facebook
                key = voice_note.split(' ')[1]
                webbrowser.open(social_media_dict.get(key))
            else:
                os.system('explorer C:\\ {}"'.format(voice_note.replace('open ', '').replace('launch', '')))   #For Windows
            continue
        elif is_valid_google_search(voice_note):
            print('in google search...')
            play_sound(mp3_google_search)
            webbrowser.open('https://www.google.com/search?q={}'.format(voice_note))
            continue
        elif 'play some relaxing music' in voice_note:
            relaxingmusic()
            continue
        elif 'time' in voice_note:
            speak_text_cmd(time.strftime("%I:%M:%S %A"))
        elif 'date' in voice_note:
            speak_text_cmd(time.strftime("%d %b %Y %A"))
        elif 'day' in voice_note:
            speak_text_cmd(time.strftime("%A"))
            continue
        elif 'countdown' in voice_note:
            countdown()
            playsound('Dismis sound/slanesh__bip.mp3')
            continue
        elif is_valid_note(online_dict, voice_note):
            online()
            continue
        elif 'thank you' in voice_note:
            play_sound(mp3_thankyou_list)
            continue
        elif 'applause' in voice_note:  #not working
            play_sound('DISMIS applause/Applause2.mp3')
            continue
        elif 'lock' in voice_note:  #for windows
            for value in ['pc','window','system']:
                ctypes.windll.user32.LockWorkStation()
                speak_text_cmd('System locked')
                continue
        elif 'restart' in voice_note:  #for windows
            os.system('shutdown -r')
        elif 'shutdown' in voice_note: #for windows
            for value in ['pc','window','system']:
                username = raw_input("Username:")
                password = raw_input("Password:")
            if password == "yesDISMIS" and username == "DISMIS":
                speak_text_cmd('Shuting down')
                os.system('shutdown -s')
            else:
                speak_text_cmd("wait 5minutes, you're logging.")
                continue
        elif 'get out' in voice_note:
            playsound('DISMIS mp3/bye.mp3')
            exit()