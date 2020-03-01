#!/usr/bin/python3
import requests
import time
import feedparser
from bs4 import BeautifulSoup
import os

#from tkinter import *

#from SpeechDriver.tts.ttsdefault import speak


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
newsTTS_path = profile_data['newsTTS_path']
newsTTS = newsTTS_path + '/SpeechDriver/tts/ServicesTTS/newsTTS/'
#print(newsTTS)


def top_google_news(accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    news = Tk()
    news.geometry('550x250')
    news.configure(background = 'black')
    news.title("Dismis'\s News")
    url = 'http://news.google.com/news?pz=1&cf=all&ned=in&hl=en&output=rss'
    feed = feedparser.parse(url)
    print("Here is the headline news")
    #output = "Here is the headline news"
    #newslabel1 =  Label(news, padx = 3000, pady = 3000, compound=CENTER, text=output, bg="#171717", fg = "white", font='times 15 bold').pack()
    for post in feed.entries:
        d = post.title
        print(d)
        output2 = d
        newslabel2 = Label(news, padx = 3000, pady = 3000, compound=CENTER, text=output2, bg="#171717", fg = "white", font='times 15 bold').pack()
        news.after(10000, lambda: news.destroy())
        news.mainloop()

top_google_news()
def news(accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    print('Getting news...!')
    # BBC news api 
    main_url = " https://newsapi.org/v1/articles?source=bbc-news&sortBy=top&apiKey=4dbc17e007ab436fb66416009dfb59a8"
  
    # fetching data in json format 
    open_bbc_page = requests.get(main_url).json() 
  
    # getting all articles in a string article 
    article = open_bbc_page["articles"] 
  
    # empty list which will  
    # contain all trending news 
    results = [] 
      
    for ar in article: 
        results.append(ar["title"]) 
          
    for i in range(len(results)): 
          
        # printing all trending news 
        print(i + 1, results[i])                  
  

def us_headlines(accept_path):
    print(' ')
    print(' ')
    url = "http://news.google.com/news?pz=1&cf=all&ned=us&hl=en&output=rss"
    rootfeed = feedparser.parse(url)
    print("Today's top headlines")
    
    titles = []
    for entry in rootfeed["entries"]:
        titles.append(entry.title)
        print (entry.title)
        print(entry.title)
    return titles
    print("That's all of today's top headlines")

