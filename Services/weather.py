#!/usr/bin/python3
import requests
import os
import time

#from tkinter import *

from SpeechDriver.tts.ttsdefault import speak

""" GLOBAL FUNCTION """
def Log_Time():
    import datetime
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
""" IMPORING PROFILE """
import yaml
from Core.profile import temporaryfiles, weatherTTS_path
weatherTTS = weatherTTS_path + '/SpeechDriver/tts/ServicesTTS/weatherTTS/'
#print(weatherTTS)
'--------------------------------------------------------------------------------------------------------------------------------------'
'--------------------------------------------------------------------------------------------------------------------------------------'


def weather_DefaultCity(default_CityLocation, openweatherAPI, accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    #city_name= "kakarbhitta"
    speak('Extracting weather')
    #weather1 = Tk()
    #weather1.geometry('1150x300+120+0')
    #weather1.title("Dismis's Weather")
    api_key = openweatherAPI
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + default_CityLocation 
    json_data=requests.get(complete_url).json()
    try:
        temp=json_data['main']
        temp=str(int(int(temp['temp'])-273.15))
        temp1=json_data['weather'][0]['description']
        wind_speed =json_data['wind']['speed']
        tts1 = "Current temperature in "+default_CityLocation+" is "+temp+" degree celsius with "+temp1+ ". And " + 'wind speed is {} metre per seconds.'.format(wind_speed)
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        print("city you said is",default_CityLocation)
        print(tts1)
        print(' ')
        print(' ')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        #Label(weather1 , padx = 3000, pady = 3000, compound=CENTER, text=result, bg="#171717", fg = "white", font='times 15 bold').pack()
        #speak(d)
        #weather1.after(5000, lambda: weather1.destroy())
        #weather1.mainloop()
        weather_txt = open(temporaryfiles + 'weather_DefaultCity.txt','w+')
        weather_txt.write(tts1)
        os.system('gnome-terminal -- python3 ' + weatherTTS + 'weather_DefaultCity__tts.py')
    except:
        result = "Key invalid or city not found. Try again sir."
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        print(result)
        print(' ')
        print(' ')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        weather_txt = open(temporaryfiles + 'weather_DefaultCity.txt','w+')
        weather_txt.write(result)
        os.system('gnome-terminal -- python3 ' + weatherTTS + 'weather_DefaultCity__tts.py &')
        

def weather(openweatherAPI, accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    time.sleep(1)
    city_name=input("enter city name to confirm:  ")
    speak('Extracting weather')
    #weather2 = Tk()
    #weather2.geometry('1150x300+120+0')
    #weather2.title("Dismis's Weather")
    ##speak("city you said is",city_name) #print ra speak lakda chaldana
    api_key = openweatherAPI
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "appid=" + api_key + "&q=" + city_name 
    json_data=requests.get(complete_url).json()
    try:
        temp=json_data['main']
        temp=str(int(int(temp['temp'])-273.15))
        temp1=json_data['weather'][0]['description']
        wind_speed =json_data['wind']['speed']
        tts2 = "Current temperature in "+city_name+" is "+temp+" degree celsius with "+temp1+ ". And " + 'wind speed is {} metre per seconds.'.format(wind_speed)
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        print("city you said is",city_name)
        print(tts2)
        print(' ')
        print(' ')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        #Label(weather2 , padx = 3000, pady = 3000, compound=CENTER, text=result, bg="#171717", fg = "white", font='times 15 bold').pack()
        #speak(d)
        #weather2.after(5000, lambda: weather2.destroy())
        #weather2.mainloop()
        weather2_txt = open(temporaryfiles + 'weather.txt','w+')
        weather2_txt.write(tts2)
        os.system('gnome-terminal -- python3 ' + weatherTTS + 'weather__tts.py &')
        print(' ')
    except:
        result = "Key invalid or city not found. Try again sir." 
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        print(result)
        print(' ')
        print(' ')
        print('\t\t\t\tSkill: weather')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        #Label(weather2 , padx = 3000, pady = 3000, compound=CENTER, text=result, bg="#171717", fg = "white", font='times 15 bold').pack()
        #speak("key invalid or city not found")
        #weather2.after(5000, lambda: weather2.destroy())
        #weather2.mainloop()
        weather2_txt = open(temporaryfiles + 'weather.txt','w+')
        weather2_txt.write(result)
        os.system('gnome-terminal -- python3 ' + weatherTTS + 'weather__tts.py &')

#cca979ed5fb2c8d3a9c99594191482f9
