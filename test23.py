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

#def authenticate_google(Ctoken_pickle, Ccredentials):
def authenticate_google():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    #if os.path.exists(Ctoken_pickle):
    if os.path.exists('/home/d-slave1/d1_SuperDismis/DISMIS-core/SystemService/middleware/Ctoken.pickle'):
        #with open(Ctoken_pickle, 'rb') as token:
        with open('/home/d-slave1/d1_SuperDismis/DISMIS-core/SystemService/middleware/Ctoken.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:            
            #flow = InstalledAppFlow.from_client_secrets_file(Ccredentials, SCOPES)
            flow = InstalledAppFlow.from_client_secrets_file('/home/d-slave1/d1_SuperDismis/DISMIS-core/SystemService/middleware/Ccredentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        #with open(Ctoken_pickle, 'wb') as token:
        with open('/home/d-slave1/d1_SuperDismis/DISMIS-core/SystemService/middleware/Ctoken.pickle', 'wb') as token:
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
            #if int(start_time.split(":")[0]) < 12:
            #    start_time = start_time + " a m"
            #else:
            #    start_time = str(int(start_time.split(":")[0])-12) + start_time.split(":")[1]
            #    start_time = start_time + " p m"
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
def get_date():
    today = datetime.date.today()
    return today

#SERVICE = authenticate_google(Ctoken_pickle, Ccredentials)
SERVICE = authenticate_google()
                                                                                                          
"--------------------------------------------------------------------------------------------------------"
def main():
    date = get_date()
    if date:
        get_events(date, SERVICE)
        time.sleep(2)

main()