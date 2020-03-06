import requests
import json
import feedparser
import random
import os
import time
import re

#from tkinter import *

from SpeechDriver.tts.ttsdefault import speak



""" GLOBAL FUNCTION """
def Log_Time():
    import datetime
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
""" IMPORING PROFILE """
from Core.profile import temporaryfiles, jokes_quoteTTS_path
jokes_quoteTTS = jokes_quoteTTS_path + '/SpeechDriver/tts/ServicesTTS/jokes_quoteTTS/'
#print(jokes_quoteTTS)
'--------------------------------------------------------------------------------------------------------------------------------------'
'--------------------------------------------------------------------------------------------------------------------------------------'


def Jokes():
    res = requests.get("https://icanhazdadjoke.com/", headers={"Accept": "application/json"})
    if res.status_code == requests.codes.ok:
        return str(res.json()["joke"])
"""
def chuck_norris(): ##Notusing because the jokes are longer than tkinter window.
    while (True):
        req = requests.get('http://api.icndb.com/jokes/random')
        json_joke = json.loads(req.text)['value']
        if json_joke[u'categories'] != u'explicit':
            return json_joke[u'joke']"""
def in_Dismis():
    jokes = [
        'What happens to a frogs car when it breaks down? It gets toad away.',
        'Why was six scared of seven? Because seven ate nine.',
        'Why are mountains so funny? Because they are hill areas.',
        'Have you ever tried to eat a clock?'
        'I hear it is very time consuming.',
        'What happened when the wheel was invented? A revolution.',
        'What do you call a fake noodle? An impasta!',
        'Did you hear about that new broom? It is sweeping the nation!',
        'What is heavy forward but not backward? Ton.',
        'No, I always forget the punch line.',
        'It’s hard to explain puns to kleptomaniacs because they always take things literally.',
        'A soldier survived mustard gas in battle, and then pepper spray by the police. He\'s now a seasoned veteran.'
        'What\'s the best thing about Switzerland? I don\'t know, but their flag is a huge plus.',
        'A Buddhist walks up to a hotdog stand and says, Make me one with everything.',
        'What\'s the difference between my ex and the titanic? The titanic only went down on 1,000 people.',
        'Two fish are sitting in a tank. One looks over at the other and says: Hey, do you know how to drive this thing?',
        'I told my doctor that I broke my arm in two places. He told me to stop going to those places.',
        'How do you keep an idiot in suspense?',
        'I hate Russian dolls...they\'re so full of themselves.',
        'My granddad has the heart of a lion and a lifetime ban from the San Diego Zoo.',
        'Rick Astley will let you borrow any movie from his Pixar collection, except one. He\'s never gonna give you up.',
        'There\'s no (I) in Denial.',
        'There are 10 types of people in the world: those who understand binary, and those who don\'t.',
        'What is red and smells like blue paint? Red Paint.',
        'What do you call bears with no ears? B',
        'I invented a new word! Plagiarism']

    return random.choice(jokes)
DismisJokeAPI = [Jokes, in_Dismis]

def tell_joke(accept_path):
    os.system('aplay ' + accept_path +' &')    
    print(' ')
    print(' ')
    time.sleep(1)
    #root= Tk()
    #root.geometry('1150x300+120+0')
    #root.title("Dismis's joke")
    #root.configure(background='#171717')
    try:
        dismis_jokes = random.choice(DismisJokeAPI)()
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        print(dismis_jokes)
        print(' ')
        print(' ')
        print('\t\t\t\tSkill: tell_joke')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        result = dismis_jokes
        #rootlabel = Label(root, padx = 3000, pady = 3000, compound=CENTER, text=result, bg="#171717", fg = "white", font='times 15 bold').pack()
        #root.after(10000, lambda: root.destroy())
        #root.mainloop()
        if os.uname()[1] == 'dslave':
            speak(result)
        else:
            tell_joke_txt = open(temporaryfiles + 'tell_joke.txt','w+')
            tell_joke_txt.write(result)
            os.system('gnome-terminal -- python3 ' + jokes_quoteTTS + 'tell_joke__tts.py')
    except:
        DisError = 'System Failure! Unable to perform tell joke skill sir'
        print('****************************************************************')
        print(' ')
        Log_Time()
        print('***' + DisError + '***')
        print(' ')
        print('****************************************************************')
        speak(DisError)

def quote(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(0.25)
    try:
        oftheday = feedparser.parse("https://www.brainyquote.com/link/quotebr.rss")     #QuoteOfTheDay
        Love = feedparser.parse("https://www.brainyquote.com/link/quotelo.rss")         #LoveQuoteOfTheDay
        Art = feedparser.parse("https://www.brainyquote.com/link/quotear.rss")          #ArtQuoteOfTheDay
        Funny = feedparser.parse("https://www.brainyquote.com/link/quotefu.rss")        #FunnyQuoteOfTheDay
        Natures = feedparser.parse("https://www.brainyquote.com/link/quotena.rss")      #NaturesQuoteOfTheDay
        quoteoftheday1 = oftheday['feed']['title']
        quoteoftheday2 = oftheday ["entries"][0]["description"]
        quoteoftheday2 = quoteoftheday2.replace('"', '')
        lovequote1 = Love['feed']['title']
        lovequote2 = Love["entries"][0]["description"]
        lovequote2 = lovequote2.replace('"', '')
        artquote1 = Art['feed']['title']
        artquote2 = Art["entries"][0]["description"]
        artquote2 = artquote2.replace('"', '')
        funnyquote1 = Funny['feed']['title']
        funnyquote2 = Funny["entries"][0]["description"]
        funnyquote2 = funnyquote2.replace('"', '')
        naturequote1 = Natures['feed']['title']
        naturequote2 =Natures["entries"][0]["description"]
        naturequote2 = naturequote2.replace('"', '')
        tts1=open(temporaryfiles + 'quote.txt','w+')
        tts1.write(quoteoftheday1)
        tts1.write("\n" + quoteoftheday2 )
        tts1.write("\n\n" + lovequote1)
        tts1.write("\n" + lovequote2)
        tts1.write("\n\n" + artquote1)
        tts1.write("\n" + artquote2)
        tts1.write("\n\n" + funnyquote1)
        tts1.write("\n" + funnyquote2)
        tts1.write("\n\n" + naturequote1)
        tts1.write("\n" + naturequote2)
        tts1.close()
        time.sleep(1)
        quote_txt = open(temporaryfiles + 'quote.txt','r')
        tts2 = quote_txt.read()
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        print(tts2)
        print(' ')
        print(' ')
        print('\t\t\t\t ::> Skill: quote')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        if os.uname()[1] == 'dslave':
            speak(tts2)
        else:
            os.system('gnome-terminal -- python3 ' + jokes_quoteTTS + 'quote__tts.py')
    except:
        DisError = 'System Failure! Unable to perform ( quote ) skill sir'
        print('****************************************************************')
        print(' ')
        Log_Time()
        print('***' + DisError + '***')
        print(' ')
        print('****************************************************************')
        speak(DisError)