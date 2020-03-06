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
#gcal3days = '/home/d-slave1/d1_SuperDismis/DISMIS-core/SystemService/DisArcade/gcal3days.txt'
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
from Core.profile import Ctoken_pickle,Ccredentials,gcal3days,slave_sender,slave_passwd,receiver\
    ,temporaryfiles, accept_path
'--------------------------------------------------------------------------------------------------------------------------------------'
'--------------------------------------------------------------------------------------------------------------------------------------'

from pyfiglet import Figlet
def banner(gcal3days):
    custom_fig = Figlet(font='graffiti')
    poster = custom_fig.renderText('Dismis')
    #print(custom_fig.renderText('Dismis'))
    d=open(gcal3days,'a+')
    d.write("\n" + poster)
def extractTime(gcal3days):
    import datetime
    now = str(datetime.datetime.now())
    d=open(gcal3days, "a+")
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
        d=open(gcal3days,'a+')
        d.write("\n\t\t-- GOOGLE CALENDAR! --\nTODAY::\n" + noEvent + "\n")
    else:
        numEvent = f'You have {len(events)} events first!!'
        d=open(gcal3days,'a+')
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
            d=open(gcal3days,'a+')
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
        d=open(gcal3days,'a+')
        d.write("\nTOMORROW::\n" + noEvent + "\n")
    else:
        
        numEvent2 = f'You have {len(events)} events in ' + str(datetime.date.today() + datetime.timedelta(days=1))
        d=open(gcal3days,'a+')
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
            d=open(gcal3days,'a+')
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
        d=open(gcal3days,'a+')
        d.write("\nDAY AFTER TOMORROW::\n" + noEvent + "\n")
    else:
        numEvent = f'You have {len(events)} events in '+ str(datetime.date.today() + datetime.timedelta(days=2))
        d=open(gcal3days,'a+')
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
            d=open(gcal3days,'a+')
            d.write(thirdEvents + "\n")
def get_date3():
    third = datetime.date.today() + datetime.timedelta(days=2)
    return third
def thirdCal():
    date = get_date3()
    if date:
        get_events3(date, SERVICE)

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
        msg['Subject'] = "GOOGLE CALENDAR 3DAYS!"# storing the subject  
        body = ''    # string to store the body of the mail
        msg.attach(MIMEText(body, 'plain'))     # attach the body with the msg instance 
        filename = "gcal3days.txt"    # open the file to be sent  
        attachment = open(gcal3days, "rb") 
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
        tts = 'Google Calendar 3 days mail sent'
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        print(tts)
        print(' ')
        print(' ')
        print('\t\t\t\tSkill: gcal_threedays')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        if os.uname()[1] == 'dslave':
            speak(tts)
        else:
            speak('gnome-terminal is not working')
    except socket.gaierror:
        pass        

def threedays(accept_path):
    os.system('aplay ' + accept_path +' &')
    #try:
    banner(gcal3days)
    extractTime(gcal3days)
    firstCal()
    secondCal()
    thirdCal()
    mailer(slave_sender, slave_passwd, receiver)
    os.system('rm ' + gcal3days)
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

