#!/usr/bin/python3
"""
#techwithtem

ugage > 
    What do I have on January Third
    What's my schedule like on Friday
    Do I have anything next Monday
    What does my day look like on the 5th  

"""
from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import os
import time
import pytz
import subprocess

from Core.main import *

from SpeechDriver.tts.ttsdefault import speak


""" GLOBAL FUNCTION """
def Log_Time():
    import datetime
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

""" IMPORING PROFILE """
from Core.profile import temporaryfiles, googleCalendarTTS_path
googleCalendarTTS = googleCalendarTTS_path + '/SpeechDriver/tts/GoogleCoreTTS/'
'--------------------------------------------------------------------------------------------------------------------------------------'
'--------------------------------------------------------------------------------------------------------------------------------------'


SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
MONTHS = ["january", "february", "march", "april", "may", "june","july", "august", "september","october","november", "december"]
DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
DAY_EXTENTIONS = ["rd", "th", "st", "nd"]

def authenticate_google(Ctoken_pickle, Ccredentials):
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    if os.path.exists(Ctoken_pickle):
        with open(Ctoken_pickle, 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:            
            flow = InstalledAppFlow.from_client_secrets_file(Ccredentials, SCOPES)
            creds = flow.run_local_server(port=0)

        with open(Ctoken_pickle, 'wb') as token:
            pickle.dump(creds, token)

    service = build('calendar', 'v3', credentials=creds)

    return service


def get_events(day, service):
    # Call the Calendar API
    date = datetime.datetime.combine(day, datetime.datetime.min.time())
    end_date = datetime.datetime.combine(day, datetime.datetime.max.time())
    utc = pytz.UTC
    date = date.astimezone(utc)
    end_date = end_date.astimezone(utc)

    events_result = service.events().list(calendarId='primary', timeMin=date.isoformat(), timeMax=end_date.isoformat(),
                                        singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        tts = 'No upcoming events found.'
        #speak(tts)
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        print(tts)
        print(' ')
        print(' ')
        print('\t\t\t\tFunction: googleCalender')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        googleCalender_txt = open(temporaryfiles + 'googleCalendar.txt', 'w+')
        googleCalender_txt.write(tts)
        os.system('gnome-terminal -- python3 ' + googleCalendarTTS + 'googleCalender_tts.py &')
    else:
        """ External gnome-terminal is not working """
        tts2 = f'You have {len(events)} events on this day.'
        speak(tts2)
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        #googleCalender_txt = open(temporaryfiles + 'googleCalendar.txt', 'w+')
        #googleCalender_txt.write(tts2)
        #os.system('gnome-terminal -- python3 /home/d-slave1/d1_SuperDismis/DISMIS-core/SpeechDriver/tts/GoogleCoreTTS/googleCalender_tts.py')
        for event in events:
            start = event['start'].get('dateTime' , event['start'].get('date'))
            #print(start, event['summary'])
            start_time = str(start.split("T")[1].split("-")[0])
            if int(start_time.split(":")[0]) < 12:
                start_time = start_time + " a m"
            else:
                start_time = str(int(start_time.split(":")[0])-12) + start_time.split(":")[1]
                start_time = start_time + " p m"
            tts3 = event["summary"] + " at " + start_time 
            print(tts3) 
            print(' ')
            print(' ')
            print('\t\t\t\tFunction: googleCalender')
            print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            #speak(tts3)
            googleCalender_txt = open(temporaryfiles + 'googleCalendar.txt', 'w+')
            googleCalender_txt.write(tts3)
            os.system('gnome-terminal -- python3 ' + googleCalendarTTS + 'googleCalender_tts.py &')
            print(googleCalendarTTS)
def get_date(voice_text):
    text = voice_text.lower()
    today = datetime.date.today()

    if text.count("today") > 0:
        return today
    day = -1
    day_of_week = -1
    month = -1
    year = today.year
    for word in text.split():
        if word in MONTHS:
            month = MONTHS.index(word) + 1
        elif word in DAYS:
            day_of_week = DAYS.index(word)
        elif word.isdigit():
            day = int(word)
        else:
            for ext in DAY_EXTENTIONS:
                found = word.find(ext)
                if found > 0:
                    try:
                        day = int(word[:found])
                    except:
                        pass

    # THE NEW PART STARTS HERE
    if month < today.month and month != -1:  # if the month mentioned is before the current month set the year to the next
        year = year+1

    # This is slighlty different from the video but the correct version
    if month == -1 and day != -1:  # if we didn't find a month, but we have a day
        if day < today.day:
            month = today.month + 1
        else:
            month = today.month

    # if we only found a dta of the week
    if month == -1 and day == -1 and day_of_week != -1:
        current_day_of_week = today.weekday()
        dif = day_of_week - current_day_of_week

        if dif < 0:
            dif += 7
            if text.count("next") >= 1:
                dif += 7

        return today + datetime.timedelta(dif)

    if day != -1:  # FIXED FROM VIDEO
        return datetime.date(month=month, day=day, year=year)

    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    if text.count("tomorrow") > 0:
        return tomorrow 

    day_after_tomorrow = datetime.date.today() + datetime.timedelta(days=2)
    if text.count("overmorrow") > 0:
        return day_after_tomorrow 

SERVICE = authenticate_google(Ctoken_pickle, Ccredentials)

def main(voice_text, accept_path):
    os.system('aplay ' + accept_path +' &')
    date = get_date(voice_text)
    if date:
        get_events(date, SERVICE)
    else:
        tts4 = 'I don\'t understand, please say again'
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        print(tts4)
        print(' ')
        print(' ')
        print('\t\t\t\tFunction: googleCalender')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        #speak(tts4)
        googleCalender_txt = open(temporaryfiles + 'googleCalendar.txt', 'w+')
        googleCalender_txt.write(tts4)
        os.system('gnome-terminal -- python3 ' + googleCalendarTTS + 'googleCalender_tts.py &')
