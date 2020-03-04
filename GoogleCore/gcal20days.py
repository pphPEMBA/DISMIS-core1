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
        noEvent2 = 'No events found in ' + str(datetime.date.today() + datetime.timedelta(days=5))
        d=open(greetingMail,'a+')
        d.write("\nSIXTH DAY:>\n" + noEvent2 + "\n-----------------------------------------------------------------------------------------")
    else:
        numEvent2 = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=5))
        d=open(greetingMail,'a+')
        d.write("\n\nSIXTH DAY:>\n" + numEvent2 + "\n")
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
            d=open(greetingMail,'a+')
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
        d=open(greetingMail,'a+')
        d.write("\nSEVENTH DAY:>\n" + noEvent + "\n-----------------------------------------------------------------------------------------")
    else:
        numEvent = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=6))
        d=open(greetingMail,'a+')
        d.write ("\nSEVENTH DAY:>\n" + numEvent + "\n")
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
            d=open(greetingMail,'a+')
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
        noEvent2 = 'No events found in ' + str(datetime.date.today() + datetime.timedelta(days=7))
        d=open(greetingMail,'a+')
        d.write("\nEIGHTH DAY:>\n" + noEvent2 + "\n-----------------------------------------------------------------------------------------")
    else:
        numEvent2 = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=7))
        d=open(greetingMail,'a+')
        d.write("\n\nEIGHTH DAY:>\n" + numEvent2 + "\n")
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
            d=open(greetingMail,'a+')
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
        d=open(greetingMail,'a+')
        d.write("\nNINETH DAY:>\n" + noEvent + "\n-----------------------------------------------------------------------------------------")
    else:
        numEvent = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=8))
        d=open(greetingMail,'a+')
        d.write ("\nNINETH DAY:>\n" + numEvent + "\n")
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
            d=open(greetingMail,'a+')
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
        d=open(greetingMail,'a+')
        d.write("\nTEN DAY:>\n" + noEvent + "\n-----------------------------------------------------------------------------------------")
    else:
        numEvent = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=9))
        d=open(greetingMail,'a+')
        d.write ("\nTEN DAY:>\n" + numEvent + "\n")
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
            d=open(greetingMail,'a+')
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
        d=open(greetingMail,'a+')
        d.write("\nELEVEN DAY:>\n" + noEvent + "\n-----------------------------------------------------------------------------------------")
    else:
        numEvent = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=10))
        d=open(greetingMail,'a+')
        d.write ("\nELEVEN DAY:>\n" + numEvent + "\n")
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
        noEvent2 = 'No events found in ' + str(datetime.date.today() + datetime.timedelta(days=11))
        d=open(greetingMail,'a+')
        d.write("\nTWELVE DAY:>\n" + noEvent2 + "\n-----------------------------------------------------------------------------------------")
    else:
        
        numEvent2 = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=11))
        d=open(greetingMail,'a+')
        d.write("\n\nTWELVE DAY:>\n" + numEvent2 + "\n")
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
        d=open(greetingMail,'a+')
        d.write("\nTHIRTEEN DAY:>\n" + noEvent + "\n-----------------------------------------------------------------------------------------")
    else:
        numEvent = f'You have {len(events)} events in '+ str(datetime.date.today() + datetime.timedelta(days=12))
        d=open(greetingMail,'a+')
        d.write ("\nTHIRTEEN DAY:>\n" + numEvent + "\n")
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
        noEvent2 = 'No events found in ' + str(datetime.date.today() + datetime.timedelta(days=13))
        d=open(greetingMail,'a+')
        d.write("\nFORTEEN DAY:>\n" + noEvent2 + "\n-----------------------------------------------------------------------------------------")
    else:
        numEvent2 = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=13))
        d=open(greetingMail,'a+')
        d.write("\n\nFORTEEN DAY:>\n" + numEvent2 + "\n")
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
        noEvent2 = 'No events found in ' + str(datetime.date.today() + datetime.timedelta(days=14))
        d=open(greetingMail,'a+')
        d.write("\nFIFTEEN DAY:>\n" + noEvent2 + "\n-----------------------------------------------------------------------------------------")
    else:
        numEvent2 = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=14))
        d=open(greetingMail,'a+')
        d.write("\n\nFIFTEEN DAY:>\n" + numEvent2 + "\n")
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
def get_date15():
    fifteen = datetime.date.today() + datetime.timedelta(days=14)
    return fifteen
def fifteenCal():
    date = get_date15()
    if date:
        get_events15(date, SERVICE)

""" SIXTEEN DAY"""
def get_events16(day, service):
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
        noEvent2 = 'No events found in ' + str(datetime.date.today() + datetime.timedelta(days=15))
        d=open(greetingMail,'a+')
        d.write("\nSIXTEEN DAY:>\n" + noEvent2 + "\n-----------------------------------------------------------------------------------------")
    else:
        numEvent2 = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=15))
        d=open(greetingMail,'a+')
        d.write("\n\nSIXTEEN DAY:>\n" + numEvent2 + "\n")
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
            d=open(greetingMail,'a+')
            d.write(sixthEvents2 + "\n")
def get_date16():
    sixteen = datetime.date.today() + datetime.timedelta(days=15)
    return sixteen

def sixteenCal():
    date = get_date16()
    if date:
        get_events16(date, SERVICE)

""" SEVENTEEN DAY """
def get_events17(day, service):
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
        noEvent = 'No events found in ' + str(datetime.date.today() + datetime.timedelta(days=16))
        d=open(greetingMail,'a+')
        d.write("\nSEVENTEEN DAY:>\n" + noEvent + "\n-----------------------------------------------------------------------------------------")
    else:
        numEvent = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=16))
        d=open(greetingMail,'a+')
        d.write ("\nSEVENTEEN DAY:>\n" + numEvent + "\n")
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
            d=open(greetingMail,'a+')
            d.write(seventhEvents + "\n")
def get_date17():
    seventeen = datetime.date.today() + datetime.timedelta(days=16)
    return seventeen
def seventeenCal():
    date = get_date17()
    if date:
        get_events17(date, SERVICE)

""" EIGHTEEN DAY """
def get_events18(day, service):
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
        noEvent2 = 'No events found in ' + str(datetime.date.today() + datetime.timedelta(days=17))
        d=open(greetingMail,'a+')
        d.write("\nEIGHTEEN DAY:>\n" + noEvent2 + "\n-----------------------------------------------------------------------------------------")
    else:
        numEvent2 = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=17))
        d=open(greetingMail,'a+')
        d.write("\n\nEIGHTEEN DAY:>\n" + numEvent2 + "\n")
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
            d=open(greetingMail,'a+')
            d.write(eightEvents2 + "\n")
def get_date18():
    eighteen = datetime.date.today() + datetime.timedelta(days=17)
    return eighteen
def eightteenCal():
    date = get_date18()
    if date:
        get_events18(date, SERVICE)

""" NINETEEN DAY """
def get_events19(day, service):
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
        noEvent = 'No events found in ' + str(datetime.date.today() + datetime.timedelta(days=18))
        d=open(greetingMail,'a+')
        d.write("\nNINETEEN DAY:>\n" + noEvent + "\n-----------------------------------------------------------------------------------------")
    else:
        numEvent = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=18))
        d=open(greetingMail,'a+')
        d.write ("\nNINETEEN DAY:>\n" + numEvent + "\n")
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
            d=open(greetingMail,'a+')
            d.write("\n"+ninethEvents + "\n")
def get_date19():
    nineteen = datetime.date.today() + datetime.timedelta(days=18)
    return nineteen
def nineteenCal():
    date = get_date19()
    if date:
        get_events19(date, SERVICE)

""" TWENTY DAY """
def get_events20(day, service):
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
        noEvent = 'No events found in ' + str(datetime.date.today() + datetime.timedelta(days=19))
        d=open(greetingMail,'a+')
        d.write("\nTWENTY DAY:>\n" + noEvent + "\n-----------------------------------------------------------------------------------------")
    else:
        numEvent = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=19))
        d=open(greetingMail,'a+')
        d.write ("\nTWENTY DAY:>\n" + numEvent + "\n")
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
            d=open(greetingMail,'a+')
            d.write("\n"+tenEvents + "\n")
def get_date20():
    ten = datetime.date.today() + datetime.timedelta(days=19)
    return ten
def twentyCal():
    date = get_date20()
    if date:
        get_events20(date, SERVICE)
