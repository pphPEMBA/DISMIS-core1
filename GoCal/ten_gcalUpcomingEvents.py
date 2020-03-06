import datetime
import os
import time
import pytz
import subprocess
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from SpeechDriver.tts.ttsdefault import speak

""" GLOBAL FUNCTION """
def Log_Time():
    import datetime
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))
""" IMPORING PROFILE """
from Core.profile import Ctoken_pickle,Ccredentials,gcal_upcoming,slave_sender,slave_passwd,receiver\
    ,temporaryfiles, accept_path
'--------------------------------------------------------------------------------------------------------------------------------------'
'--------------------------------------------------------------------------------------------------------------------------------------'

from pyfiglet import Figlet
def banner(gcal_upcoming):
    custom_fig = Figlet(font='graffiti')
    poster = custom_fig.renderText('Dismis')
    #print(custom_fig.renderText('Dismis'))
    d=open(gcal_upcoming,'a+')
    d.write("\n" + poster)
def extractTime(gcal_upcoming):
    import datetime
    now = str(datetime.datetime.now())
    d=open(gcal_upcoming, "a+")
    d.write("\n Extracted time is: " + now + "\n-----------------------------------------------------------------------------------------\n----------------------------------------------------------------------------------------- \n")

# If modifying these scopes, delete the file token.pickle.
SCOPES = ['https://www.googleapis.com/auth/calendar']
CREDENTIALS_FILE = Ccredentials
def get_calendar_service(Ctoken_pickle):
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(Ctoken_pickle):
        with open(Ctoken_pickle, 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                CREDENTIALS_FILE, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(Ctoken_pickle, 'wb') as token:
            pickle.dump(creds, token)
    service = build('calendar', 'v3', credentials=creds)
    return service

def get_events():
    service = get_calendar_service(Ctoken_pickle)
    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
    events_result = service.events().list(calendarId='primary', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])
    if not events:
        noEvent = 'No upcoming events found.'
        d=open(gcal_upcoming,'a+')
        d.write("\n\t\t-- GOOGLE CALENDAR!\n" + noEvent + "\n")
    else:
        numEvent = f'You have {len(events)} events first!!'
        d=open(gcal_upcoming,'a+')
        d.write ("\n\t\t-- GOOGLE CALENDAR!\n" + numEvent + "\n")
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            comming_events = event["summary"] + " at " + start
            d=open(gcal_upcoming,'a+')
            d.write(comming_events + "\n")

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
        filename = "gcal_upcoming.txt"    # open the file to be sent  
        attachment = open(gcal_upcoming, "rb") 
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
        tts = 'Google Calendar Upcomming_events mail sent boss.'
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

def get_upcomingEvents(accept_path):
    os.system('aplay ' + accept_path +' &')
    banner(gcal_upcoming)
    extractTime(gcal_upcoming)
    get_events()
    mailer(slave_sender, slave_passwd, receiver)
    os.system('rm ' + gcal_upcoming)
