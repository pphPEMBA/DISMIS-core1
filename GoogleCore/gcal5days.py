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

Ctoken_pickle = '/home/d-slave1/d1_SuperDismis/DISMIS-core/SystemService/middleware/Ctoken.pickle'
Ccredentials = '/home/d-slave1/d1_SuperDismis/DISMIS-core/SystemService/middleware/Ccredentials.json'
login_id_path = '/home/d-slave1/d1_SuperDismis/DISMIS-core/SystemService/middleware/login_Id.db'
greetingMail = '/home/d-slave1/d1_SuperDismis/DISMIS-core/SystemService/middleware/greetingMail.txt'

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


"""--- AUTHENTICATION ---"""
def authenticate_google(Ctoken_pickle, Ccredentials):
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
SERVICE = authenticate_google(Ctoken_pickle, Ccredentials)

""" FIRST DAY """
def get_events(day, service):
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
        noEvent = 'No events found in ' + str(datetime.date.today())
        d=open(greetingMail,'a+')
        d.write("\n\t\t-- GOOGLE CALENDAR! --\nTODAY:>\n" + noEvent + "\n-----------------------------------------------------------------------------------------")
    else:
        numEvent = f'You have {len(events)} events first!!'
        d=open(greetingMail,'a+')
        d.write ("\n\t\t-- GOOGLE CALENDAR! --\nTODAY:>\n" + numEvent + "\n")
        for event in events:
            start = event['start'].get('dateTime' , event['start'].get('date'))
            #print(start, event['summary'])
            start_time = str(start.split("T")[1].split("-")[0])
            #if int(start_time.split(":")[0]) < 12:
            #    start_time = start_time + " a m"
            #else:
            #    start_time = str(int(start_time.split(":")[0])-12) + start_time.split(":")[1]
            #    start_time = start_time + " p m"
            firstEvents = event["summary"] + " at " + start_time 
            d=open(greetingMail,'a+')
            d.write(firstEvents + "\n")
def get_date():
    first = datetime.date.today()
    return first
def firstCal():
    date = get_date()
    if date:
        get_events(date, SERVICE)


""" SECOND DAY """
def get_events2(day, service):
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
        noEvent2 = 'No events found in ' + str(datetime.date.today() + datetime.timedelta(days=1))
        d=open(greetingMail,'a+')
        d.write("\nTOMORROW:>\n" + noEvent2 + "\n-----------------------------------------------------------------------------------------")
    else:
        
        numEvent2 = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=1))
        d=open(greetingMail,'a+')
        d.write("\n\nTOMORROW:>\n" + numEvent2 + "\n")
        for event in events:
            start = event['start'].get('dateTime' , event['start'].get('date'))
            #print(start, event['summary'])
            start_time = str(start.split("T")[1].split("-")[0])
            #if int(start_time.split(":")[0]) < 12:
            #    start_time = start_time + " a m"
            #else:
            #    start_time = str(int(start_time.split(":")[0])-12) + start_time.split(":")[1]
            #    start_time = start_time + " p m"
            secondEvents2 = event["summary"] + " at " + start_time 
            d=open(greetingMail,'a+')
            d.write(secondEvents2 + "\n")
def get_date2():
    second = datetime.date.today() + datetime.timedelta(days=1)
    return second 

def secondCal():
    date = get_date2()
    if date:
        get_events2(date, SERVICE)

""" THIRD DAY """
def get_events3(day, service):
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
        noEvent = 'No events found in ' + str(datetime.date.today() + datetime.timedelta(days=2))
        d=open(greetingMail,'a+')
        d.write("\nDAY AFTER TOMORROW:>\n" + noEvent + "\n-----------------------------------------------------------------------------------------")
    else:
        numEvent = f'You have {len(events)} events in '+ str(datetime.date.today() + datetime.timedelta(days=2))
        d=open(greetingMail,'a+')
        d.write ("\nDAY AFTER TOMORROW:>\n" + numEvent + "\n")
        for event in events:
            start = event['start'].get('dateTime' , event['start'].get('date'))
            #print(start, event['summary'])
            start_time = str(start.split("T")[1].split("-")[0])
            #if int(start_time.split(":")[0]) < 12:
            #    start_time = start_time + " a m"
            #else:
            #    start_time = str(int(start_time.split(":")[0])-12) + start_time.split(":")[1]
            #    start_time = start_time + " p m"
            thirdEvents = event["summary"] + " at " + start_time 
            d=open(greetingMail,'a+')
            d.write(thirdEvents + "\n")
def get_date3():
    third = datetime.date.today() + datetime.timedelta(days=2)
    return third
def thirdCal():
    date = get_date3()
    if date:
        get_events3(date, SERVICE)

""" FOR forth """
def get_events4(day, service):
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
        noEvent2 = 'No events found in ' + str(datetime.date.today() + datetime.timedelta(days=3))
        d=open(greetingMail,'a+')
        d.write("\nFORTH DAY:>\n" + noEvent2 + "\n-----------------------------------------------------------------------------------------")
    else:
        numEvent2 = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=3))
        d=open(greetingMail,'a+')
        d.write("\n\nFORTH DAY:>\n" + numEvent2 + "\n")
        for event in events:
            start = event['start'].get('dateTime' , event['start'].get('date'))
            #print(start, event['summary'])
            start_time = str(start.split("T")[1].split("-")[0])
            #if int(start_time.split(":")[0]) < 12:
            #    start_time = start_time + " a m"
            #else:
            #    start_time = str(int(start_time.split(":")[0])-12) + start_time.split(":")[1]
            #    start_time = start_time + " p m"
            forthEvents2 = event["summary"] + " at " + start_time 
            d=open(greetingMail,'a+')
            d.write(forthEvents2 + "\n")
def get_date4():
    forth = datetime.date.today() + datetime.timedelta(days=3)
    return forth 
def forthCal():
    date = get_date4()
    if date:
        get_events4(date, SERVICE)

""" FIFTH DAY """
def get_events5(day, service):
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
        noEvent2 = 'No events found in ' + str(datetime.date.today() + datetime.timedelta(days=4))
        d=open(greetingMail,'a+')
        d.write("\nFIFTH DAY:>\n" + noEvent2 + "\n-----------------------------------------------------------------------------------------")
    else:
        numEvent2 = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=4))
        d=open(greetingMail,'a+')
        d.write("\n\nFIFTH DAY:>\n" + numEvent2 + "\n")
        for event in events:
            start = event['start'].get('dateTime' , event['start'].get('date'))
            #print(start, event['summary'])
            start_time = str(start.split("T")[1].split("-")[0])
            #if int(start_time.split(":")[0]) < 12:
            #    start_time = start_time + " a m"
            #else:
            #    start_time = str(int(start_time.split(":")[0])-12) + start_time.split(":")[1]
            #    start_time = start_time + " p m"
            fifthEvents2 = event["summary"] + " at " + start_time 
            d=open(greetingMail,'a+')
            d.write(fifthEvents2 + "\n")
def get_date5():
    fifth = datetime.date.today() + datetime.timedelta(days=4)
    return fifth 
def fifthCal():
    date = get_date5()
    if date:
        get_events5(date, SERVICE)
