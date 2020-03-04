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
        noEvent = 'No events found in ' + str(datetime.date.today() + datetime.timedelta(days=9))
        d=open(greetingMail,'a+')
        d.write("\nTWENTY DAY:>\n" + noEvent + "\n-----------------------------------------------------------------------------------------")
    else:
        numEvent = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=9))
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
    ten = datetime.date.today() + datetime.timedelta(days=9)
    return ten
def twentyCal():
    date = get_date20()
    if date:
        get_events20(date, SERVICE)

""" ELEVEN DAY """
def get_events21(day, service):
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
        d.write("\nTWENTY-ONE:>\n" + noEvent + "\n-----------------------------------------------------------------------------------------")
    else:
        numEvent = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=10))
        d=open(greetingMail,'a+')
        d.write ("\nTWENTY-ONE:>\n" + numEvent + "\n")
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
def get_date21():
    eleven = datetime.date.today() + datetime.timedelta(days=10)
    return eleven
def twentyoneCal():
    date = get_date21()
    if date:
        get_events21(date, SERVICE)


""" TWELVE DAY """
def get_events22(day, service):
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
        noEvent2 = 'No events found in ' + str(datetime.date.today() + datetime.timedelta(days=21))
        d=open(greetingMail,'a+')
        d.write("\nTWENTY-TWO DAY:>\n" + noEvent2 + "\n-----------------------------------------------------------------------------------------")
    else:
        
        numEvent2 = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=21))
        d=open(greetingMail,'a+')
        d.write("\n\nTWENTY-TWO DAY:>\n" + numEvent2 + "\n")
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
def get_date22():
    twelve = datetime.date.today() + datetime.timedelta(days=21)
    return twelve 

def twentytwoCal():
    date = get_date22()
    if date:
        get_events22(date, SERVICE)

""" THIRTEEN DAY """
def get_events23(day, service):
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
        noEvent = 'No events found in ' + str(datetime.date.today() + datetime.timedelta(days=22))
        d=open(greetingMail,'a+')
        d.write("\nTWENTY-THREE DAY:>\n" + noEvent + "\n-----------------------------------------------------------------------------------------")
    else:
        numEvent = f'You have {len(events)} events in '+ str(datetime.date.today() + datetime.timedelta(days=22))
        d=open(greetingMail,'a+')
        d.write ("\nTWENTY-THREE DAY:>\n" + numEvent + "\n")
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
def get_date23():
    thirteen = datetime.date.today() + datetime.timedelta(days=22)
    return thirteen
def twentythreeCal():
    date = get_date23()
    if date:
        get_events23(date, SERVICE)

""" FORTEEN DAY """
def get_events24(day, service):
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
        noEvent2 = 'No events found in ' + str(datetime.date.today() + datetime.timedelta(days=23))
        d=open(greetingMail,'a+')
        d.write("\nTWENTY-FOUR DAY:>\n" + noEvent2 + "\n-----------------------------------------------------------------------------------------")
    else:
        numEvent2 = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=23))
        d=open(greetingMail,'a+')
        d.write("\n\nTWENTY-FOUR DAY:>\n" + numEvent2 + "\n")
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
def get_date24():
    fourteen = datetime.date.today() + datetime.timedelta(days=23)
    return fourteen 
def twentyfourCal():
    date = get_date24()
    if date:
        get_events24(date, SERVICE)

""" FIFTEEN DAY """
def get_events25(day, service):
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
        noEvent2 = 'No events found in ' + str(datetime.date.today() + datetime.timedelta(days=24))
        d=open(greetingMail,'a+')
        d.write("\nTWENTY-FIVE DAY:>\n" + noEvent2 + "\n-----------------------------------------------------------------------------------------")
    else:
        numEvent2 = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=24))
        d=open(greetingMail,'a+')
        d.write("\n\nTWENTY-FIVE DAY:>\n" + numEvent2 + "\n")
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
def get_date25():
    fifteen = datetime.date.today() + datetime.timedelta(days=24)
    return fifteen
def twentyfiveCal():
    date = get_date25()
    if date:
        get_events25(date, SERVICE)

""" SIXTEEN DAY"""
def get_events26(day, service):
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
        noEvent2 = 'No events found in ' + str(datetime.date.today() + datetime.timedelta(days=25))
        d=open(greetingMail,'a+')
        d.write("\nTWENTY-SIX DAY:>\n" + noEvent2 + "\n-----------------------------------------------------------------------------------------")
    else:
        numEvent2 = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=25))
        d=open(greetingMail,'a+')
        d.write("\n\nTWENTY-SIX DAY:>\n" + numEvent2 + "\n")
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
def get_date26():
    sixteen = datetime.date.today() + datetime.timedelta(days=25)
    return sixteen

def twentysixCal():
    date = get_date26()
    if date:
        get_events26(date, SERVICE)



"*************************************************************************************************"
""" SEVENTEEN DAY """
def get_events27(day, service):
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
        noEvent = 'No events found in ' + str(datetime.date.today() + datetime.timedelta(days=26))
        d=open(greetingMail,'a+')
        d.write("\nTWENTY-SEVEN DAY:>\n" + noEvent + "\n-----------------------------------------------------------------------------------------")
    else:
        numEvent = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=26))
        d=open(greetingMail,'a+')
        d.write ("\nTWENTY-SEVEN DAY:>\n" + numEvent + "\n")
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
def get_date27():
    seventeen = datetime.date.today() + datetime.timedelta(days=26)
    return seventeen
def twentysevenCal():
    date = get_date27()
    if date:
        get_events27(date, SERVICE)


""" EIGHTEEN DAY """
def get_events28(day, service):
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
        noEvent2 = 'No events found in ' + str(datetime.date.today() + datetime.timedelta(days=27))
        d=open(greetingMail,'a+')
        d.write("\nTWENTY-EIGHT DAY:>\n" + noEvent2 + "\n-----------------------------------------------------------------------------------------")
    else:
        numEvent2 = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=27))
        d=open(greetingMail,'a+')
        d.write("\n\nTWENTY-EIGHT DAY:>\n" + numEvent2 + "\n")
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
def get_date28():
    eighteen = datetime.date.today() + datetime.timedelta(days=27)
    return eighteen
def twentyeightCal():
    date = get_date28()
    if date:
        get_events28(date, SERVICE)


"*************************************************************************************************"
""" NINETEEN DAY """
def get_events29(day, service):
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
        noEvent = 'No events found in ' + str(datetime.date.today() + datetime.timedelta(days=28))
        d=open(greetingMail,'a+')
        d.write("\nTWENTY-NINE DAY:>\n" + noEvent + "\n-----------------------------------------------------------------------------------------")
    else:
        numEvent = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=28))
        d=open(greetingMail,'a+')
        d.write ("\nTWENTY-NINE DAY:>\n" + numEvent + "\n")
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
def get_date29():
    nineteen = datetime.date.today() + datetime.timedelta(days=28)
    return nineteen
def twentynineCal():
    date = get_date29()
    if date:
        get_events29(date, SERVICE)


""" TWENTY DAY """
def get_events30(day, service):
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
        noEvent = 'No events found in ' + str(datetime.date.today() + datetime.timedelta(days=29))
        d=open(greetingMail,'a+')
        d.write("\nTHIRTY DAY:>\n" + noEvent + "\n-----------------------------------------------------------------------------------------")
    else:
        numEvent = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=29))
        d=open(greetingMail,'a+')
        d.write ("\nTHIRTY DAY:>\n" + numEvent + "\n")
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
def get_date30():
    thirty = datetime.date.today() + datetime.timedelta(days=29)
    return thirty
def thirtyCal():
    date = get_date30()
    if date:
        get_events30(date, SERVICE)

def main():
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
    sixteenCal()
    seventeenCal()
    eightteenCal()
    nineteenCal()

main()