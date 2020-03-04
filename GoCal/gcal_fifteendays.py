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

#Ctoken_pickle = '/home/d-slave1/d1_SuperDismis/DISMIS-core/SystemService/middleware/Ctoken.pickle'
#Ccredentials = '/home/d-slave1/d1_SuperDismis/DISMIS-core/SystemService/middleware/Ccredentials.json'
#gcal15days = '/home/d-slave1/d1_SuperDismis/DISMIS-core/SystemService/DisArcade/gcal15days.txt'
#slave_sender = 'pembamoktan.t@gmail.com'
#slave_passwd = 'D1i1s1m1i1s@'
#receiver = 'pembatamang.m@gmail.com'
#accept_path = '/home/d-slave1/d1_SuperDismis/DISMIS-core/SystemService/DisArcade/Dismis_sounds/accept.wav'
#googleCalendarTTS
#temporaryfiles
""" GLOBAL FUNCTION """
def Log_Time():
    import datetime
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))


""" IMPORING PROFILE """
from Core.profile import Ctoken_pickle,Ccredentials,gcal15days,slave_sender,slave_passwd,receiver\
    ,temporaryfiles, accept_path, gcal15days
'--------------------------------------------------------------------------------------------------------------------------------------'
'--------------------------------------------------------------------------------------------------------------------------------------'

from pyfiglet import Figlet
def banner(gcal15days):
    custom_fig = Figlet(font='graffiti')
    poster = custom_fig.renderText('Dismis')
    #print(custom_fig.renderText('Dismis'))
    d=open(gcal15days,'a+')
    d.write("\n" + poster)
def extractTime(gcal15days):
    import datetime
    now = str(datetime.datetime.now())
    d=open(gcal15days, "a+")
    d.write("\n Extracted time is: " + now + "\n-----------------------------------------------------------------------------------------\n----------------------------------------------------------------------------------------- \n")

"""--- AUTHENTICATION ---"""
SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']
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
        d=open(gcal15days,'a+')
        d.write("\n\t\t-- GOOGLE CALENDAR! --\nTODAY::\n" + noEvent + "\n")
    else:
        numEvent = f'You have {len(events)} events first!!'
        d=open(gcal15days,'a+')
        d.write ("\n\t\t-- GOOGLE CALENDAR! --\nTODAY::\n" + numEvent + "\n")
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
            d=open(gcal15days,'a+')
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
        noEvent = 'No events found in ' + str(datetime.date.today() + datetime.timedelta(days=1))
        d=open(gcal15days,'a+')
        d.write("\nTOMORROW::\n" + noEvent + "\n")
    else:
        
        numEvent2 = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=1))
        d=open(gcal15days,'a+')
        d.write("\nTOMORROW::\n" + numEvent2 + "\n")
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
            d=open(gcal15days,'a+')
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
        d=open(gcal15days,'a+')
        d.write("\nDAY AFTER TOMORROW::\n" + noEvent + "\n")
    else:
        numEvent = f'You have {len(events)} events in '+ str(datetime.date.today() + datetime.timedelta(days=2))
        d=open(gcal15days,'a+')
        d.write ("\nDAY AFTER TOMORROW::\n" + numEvent + "\n")
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
            d=open(gcal15days,'a+')
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
        noEvent = 'No events found in ' + str(datetime.date.today() + datetime.timedelta(days=3))
        d=open(gcal15days,'a+')
        d.write("\nFORTH DAY::\n" + noEvent + "\n")
    else:
        numEvent2 = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=3))
        d=open(gcal15days,'a+')
        d.write("\nFORTH DAY::\n" + numEvent2 + "\n")
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
            d=open(gcal15days,'a+')
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
        noEvent = 'No events found in ' + str(datetime.date.today() + datetime.timedelta(days=4))
        d=open(gcal15days,'a+')
        d.write("\nFIFTH DAY::\n" + noEvent + "\n")
    else:
        numEvent2 = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=4))
        d=open(gcal15days,'a+')
        d.write("\nFIFTH DAY::\n" + numEvent2 + "\n")
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
            d=open(gcal15days,'a+')
            d.write(fifthEvents2 + "\n")
def get_date5():
    fifth = datetime.date.today() + datetime.timedelta(days=4)
    return fifth 
def fifthCal():
    date = get_date5()
    if date:
        get_events5(date, SERVICE)

""" SIXTH DAY"""
def get_events6(day, service):
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
        noEvent = 'No events found in ' + str(datetime.date.today() + datetime.timedelta(days=5))
        d=open(gcal15days,'a+')
        d.write("\nSIXTH DAY::\n" + noEvent + "\n")
    else:
        numEvent2 = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=5))
        d=open(gcal15days,'a+')
        d.write("\nSIXTH DAY::\n" + numEvent2 + "\n")
        for event in events:
            start = event['start'].get('dateTime' , event['start'].get('date'))
            #print(start, event['summary'])
            start_time = str(start.split("T")[1].split("-")[0])
            #if int(start_time.split(":")[0]) < 12:
            #    start_time = start_time + " a m"
            #else:
            #    start_time = str(int(start_time.split(":")[0])-12) + start_time.split(":")[1]
            #    start_time = start_time + " p m"
            sixthEvents2 = event["summary"] + " at " + start_time 
            d=open(gcal15days,'a+')
            d.write(sixthEvents2 + "\n")
def get_date6():
    sixth = datetime.date.today() + datetime.timedelta(days=5)
    return sixth 

def sixthCal():
    date = get_date6()
    if date:
        get_events6(date, SERVICE)



"*************************************************************************************************"
""" SEVENTH DAY """
def get_events7(day, service):
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
        noEvent = 'No events found in ' + str(datetime.date.today() + datetime.timedelta(days=6))
        d=open(gcal15days,'a+')
        d.write("\nSEVENTH DAY::\n" + noEvent + "\n")
    else:
        numEvent = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=6))
        d=open(gcal15days,'a+')
        d.write ("\nSEVENTH DAY::\n" + numEvent + "\n")
        for event in events:
            start = event['start'].get('dateTime' , event['start'].get('date'))
            #print(start, event['summary'])
            start_time = str(start.split("T")[1].split("-")[0])
            #if int(start_time.split(":")[0]) < 12:
            #    start_time = start_time + " a m"
            #else:
            #    start_time = str(int(start_time.split(":")[0])-12) + start_time.split(":")[1]
            #    start_time = start_time + " p m"
            seventhEvents = event["summary"] + " at " + start_time 
            d=open(gcal15days,'a+')
            d.write(seventhEvents + "\n")
def get_date7():
    seventh = datetime.date.today() + datetime.timedelta(days=6)
    return seventh
def seventhCal():
    date = get_date7()
    if date:
        get_events7(date, SERVICE)


""" EIGHTH DAY """
def get_events8(day, service):
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
        noEvent = 'No events found in ' + str(datetime.date.today() + datetime.timedelta(days=7))
        d=open(gcal15days,'a+')
        d.write("\nEIGHTH DAY::\n" + noEvent + "\n")
    else:
        numEvent2 = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=7))
        d=open(gcal15days,'a+')
        d.write("\nEIGHTH DAY::\n" + numEvent2 + "\n")
        for event in events:
            start = event['start'].get('dateTime' , event['start'].get('date'))
            #print(start, event['summary'])
            start_time = str(start.split("T")[1].split("-")[0])
            #if int(start_time.split(":")[0]) < 12:
            #    start_time = start_time + " a m"
            #else:
            #    start_time = str(int(start_time.split(":")[0])-12) + start_time.split(":")[1]
            #    start_time = start_time + " p m"
            eightEvents2 = event["summary"] + " at " + start_time 
            d=open(gcal15days,'a+')
            d.write(eightEvents2 + "\n")
def get_date8():
    eight = datetime.date.today() + datetime.timedelta(days=7)
    return eight 
def eightCal():
    date = get_date8()
    if date:
        get_events8(date, SERVICE)


"*************************************************************************************************"
""" NINETH DAY """
def get_events9(day, service):
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
        noEvent = 'No events found in ' + str(datetime.date.today() + datetime.timedelta(days=8))
        d=open(gcal15days,'a+')
        d.write("\nNINETH DAY::\n" + noEvent + "\n")
    else:
        numEvent = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=8))
        d=open(gcal15days,'a+')
        d.write ("\nNINETH DAY::\n" + numEvent + "\n")
        for event in events:
            start = event['start'].get('dateTime' , event['start'].get('date'))
            #print(start, event['summary'])
            start_time = str(start.split("T")[1].split("-")[0])
            #if int(start_time.split(":")[0]) < 12:
            #    start_time = start_time + " a m"
            #else:
            #    start_time = str(int(start_time.split(":")[0])-12) + start_time.split(":")[1]
            #    start_time = start_time + " p m"
            ninethEvents = event["summary"] + " at " + start_time 
            d=open(gcal15days,'a+')
            d.write(ninethEvents + "\n")
def get_date9():
    nineth = datetime.date.today() + datetime.timedelta(days=8)
    return nineth 

def ninethCal():
    date = get_date9()
    if date:
        get_events9(date, SERVICE)

""" TEN DAY """
def get_events10(day, service):
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
        noEvent = 'No events found in ' + str(datetime.date.today() + datetime.timedelta(days=9))
        d=open(gcal15days,'a+')
        d.write("\nTEN DAY::\n" + noEvent + "\n")
    else:
        numEvent = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=9))
        d=open(gcal15days,'a+')
        d.write ("\nTEN DAY::\n" + numEvent + "\n")
        for event in events:
            start = event['start'].get('dateTime' , event['start'].get('date'))
            #print(start, event['summary'])
            start_time = str(start.split("T")[1].split("-")[0])
            #if int(start_time.split(":")[0]) < 12:
            #    start_time = start_time + " a m"
            #else:
            #    start_time = str(int(start_time.split(":")[0])-12) + start_time.split(":")[1]
            #    start_time = start_time + " p m"
            tenEvents = event["summary"] + " at " + start_time 
            d=open(gcal15days,'a+')
            d.write("\n"+tenEvents + "\n")
def get_date10():
    ten = datetime.date.today() + datetime.timedelta(days=9)
    return ten

def tenCal():
    date = get_date10()
    if date:
        get_events10(date, SERVICE)

""" ELEVEN DAY """
def get_events11(day, service):
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
        noEvent = 'No events found in ' + str(datetime.date.today() + datetime.timedelta(days=10))
        d=open(gcal15days,'a+')
        d.write("\nELEVEN DAY::\n" + noEvent + "\n")
    else:
        numEvent = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=10))
        d=open(gcal15days,'a+')
        d.write ("\nELEVEN DAY::\n" + numEvent + "\n")
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
            d=open(gcal15days,'a+')
            d.write(firstEvents + "\n")
def get_date11():
    eleven = datetime.date.today() + datetime.timedelta(days=10)
    return eleven
def eleventeenCal():
    date = get_date11()
    if date:
        get_events11(date, SERVICE)


""" TWELVE DAY """
def get_events12(day, service):
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
        noEvent = 'No events found in ' + str(datetime.date.today() + datetime.timedelta(days=11))
        d=open(gcal15days,'a+')
        d.write("\nTWELVE DAY::\n" + noEvent + "\n")
    else:
        
        numEvent2 = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=11))
        d=open(gcal15days,'a+')
        d.write("\nTWELVE DAY::\n" + numEvent2 + "\n")
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
            d=open(gcal15days,'a+')
            d.write(secondEvents2 + "\n")
def get_date12():
    twelve = datetime.date.today() + datetime.timedelta(days=11)
    return twelve 

def twelveteenCal():
    date = get_date12()
    if date:
        get_events12(date, SERVICE)

""" THIRTEEN DAY """
def get_events13(day, service):
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
        noEvent = 'No events found in ' + str(datetime.date.today() + datetime.timedelta(days=12))
        d=open(gcal15days,'a+')
        d.write("\nTHIRTEEN DAY::\n" + noEvent + "\n")
    else:
        numEvent = f'You have {len(events)} events in '+ str(datetime.date.today() + datetime.timedelta(days=12))
        d=open(gcal15days,'a+')
        d.write ("\nTHIRTEEN DAY::\n" + numEvent + "\n")
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
            d=open(gcal15days,'a+')
            d.write(thirdEvents + "\n")
def get_date13():
    thirteen = datetime.date.today() + datetime.timedelta(days=12)
    return thirteen
def thirteenCal():
    date = get_date13()
    if date:
        get_events13(date, SERVICE)

""" FORTEEN DAY """
def get_events14(day, service):
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
        noEvent = 'No events found in ' + str(datetime.date.today() + datetime.timedelta(days=13))
        d=open(gcal15days,'a+')
        d.write("\nFORTEEN DAY::\n" + noEvent + "\n")
    else:
        numEvent2 = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=13))
        d=open(gcal15days,'a+')
        d.write("\nFORTEEN DAY::\n" + numEvent2 + "\n")
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
            d=open(gcal15days,'a+')
            d.write(forthEvents2 + "\n")
def get_date14():
    fourteen = datetime.date.today() + datetime.timedelta(days=13)
    return fourteen 
def fourteenCal():
    date = get_date14()
    if date:
        get_events14(date, SERVICE)

""" FIFTEEN DAY """
def get_events15(day, service):
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
        noEvent = 'No events found in ' + str(datetime.date.today() + datetime.timedelta(days=14))
        d=open(gcal15days,'a+')
        d.write("\nFIFTEEN DAY::\n" + noEvent + "\n")
    else:
        numEvent2 = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=14))
        d=open(gcal15days,'a+')
        d.write("\nFIFTEEN DAY::\n" + numEvent2 + "\n")
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
            d=open(gcal15days,'a+')
            d.write(fifthEvents2 + "\n")
def get_date15():
    fifteen = datetime.date.today() + datetime.timedelta(days=14)
    return fifteen
def fifteenCal():
    date = get_date15()
    if date:
        get_events15(date, SERVICE)

import socket
import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
def mailer(slave_sender, slave_passwd, receiver):
    try:
        fromaddr = slave_sender
        toaddr = receiver
        msg = MIMEMultipart() # instance of MIMEMultipart 
        msg['From'] = fromaddr    # storing the main_senders email address 
        msg['To'] = toaddr   # storing the receivers email address 
        msg['Subject'] = "GOOGLE CALENDAR 15DAYS!"# storing the subject  
        body = ''    # string to store the body of the mail
        msg.attach(MIMEText(body, 'plain'))     # attach the body with the msg instance 
        filename = "gcal15days.txt"    # open the file to be sent  
        attachment = open(gcal15days, "rb") 
        p = MIMEBase('application', 'octet-stream')     # instance of MIMEBase and named as p 
        p.set_payload((attachment).read())     # To change the payload into encoded form 
        encoders.encode_base64(p)     # encode into base64
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
        msg.attach(p)     # attach the instance 'p' to instance 'msg' 
        s = smtplib.SMTP('smtp.gmail.com', 587)     # creates SMTP session 
        s.starttls()     # start TLS for security 
        s.login(fromaddr, slave_passwd)     # Authentication 
        text = msg.as_string()     # Converts the Multipart msg into a string 
        s.sendmail(fromaddr, toaddr, text)     # sending the mail 
        s.quit()     # terminating the session 
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        print('Google Calendar 15 days mail sent')
        print(' ')
        print(' ')
        print('\t\t\t\tSkill: gcal_fifteendays')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        speak('Google Calendar 15 days mail sent boss.')
    except socket.gaierror:
        pass        

def fifteendays(accept_path):
    os.system('aplay ' + accept_path +' &')
    #try:
    banner(gcal15days)
    extractTime(gcal15days)
    firstCal()
    secondCal()
    thirdCal()
    forthCal()
    fifthCal()
    sixthCal()
    seventhCal()
    eightCal()
    ninethCal()
    tenCal()
    eleventeenCal()
    twelveteenCal()
    thirteenCal()
    fourteenCal()
    fifteenCal()
    mailer(slave_sender, slave_passwd, receiver)
    os.system('rm ' + gcal15days)
    #except:
    #    tts4 = 'I don\'t understand, please say again'
    #    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    #    print(' ')
    #    print(' ')
    #    Log_Time()
    #    print(tts4)
    #    print(' ')
    #    print(' ')
    #    print('\t\t\t\tFunction: googleCalender')
    #    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    #    #speak(tts4)
    #    googleCalender_txt = open(temporaryfiles + 'googleCalendar.txt', 'w+')
    #    googleCalender_txt.write(tts4)
    #    os.system('gnome-terminal -- python3 ' + googleCalendarTTS + 'googleDays_tts.py &')

