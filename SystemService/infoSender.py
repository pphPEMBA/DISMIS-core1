#!/usr/bin/python3
import smtplib, socket
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import os
import time

from SpeechDriver.tts.ttsdefault import speak


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
host_ip= profile_data['host_ip']
infoSenderTTS_path = profile_data['infoSenderTTS_path']
infoSenderTTS = infoSenderTTS_path + '/SpeechDriver/tts/ServicesTTS/infoSenderTTS/'
#print(infoSenderTTS)

def backupGmailCodeInfo(main_sender, main_passwd, receiver, accept_path):
    try:
        os.system('aplay ' + accept_path +' &')
        print(' ')
        print(' ')
        time.sleep(1)
        fromaddr = main_sender
        toaddr = receiver
        msg = MIMEMultipart() # instance of MIMEMultipart 
        msg['From'] = fromaddr    # storing the main_senders email address 
        msg['To'] = toaddr   # storing the receivers email address 
        msg['Subject'] = "CONFIDENTIALS INFORMATION"# storing the subject  
        body = host_ip + '/login/backupCodePersonalMail'    # string to store the body of the mail
        msg.attach(MIMEText(body, 'plain'))     # attach the body with the msg instance 
        filename = "backupCodePersonalMailInfoSite.png"    # open the file to be sent  
        attachment = open("SystemService/PrimaryCredentials/credentialsSites/backupCodePersonalMailInfoSite.png", "rb") 
        p = MIMEBase('application', 'octet-stream')     # instance of MIMEBase and named as p 
        p.set_payload((attachment).read())     # To change the payload into encoded form 
        encoders.encode_base64(p)     # encode into base64
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
        msg.attach(p)     # attach the instance 'p' to instance 'msg' 
        s = smtplib.SMTP('smtp.gmail.com', 587)     # creates SMTP session 
        s.starttls()     # start TLS for security 
        s.login(fromaddr, main_passwd)     # Authentication 
        text = msg.as_string()     # Converts the Multipart msg into a string 
        s.sendmail(fromaddr, toaddr, text)     # sending the mail 
        s.quit()     # terminating the session 
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        print('backupGmailCode info sent')
        print(' ')
        print(' ')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        if os.uname()[1] == 'dslave':
            speak('Accomplish Pemba')
        else:
            #_txt = open(temporaryfiles + '.txt','w+')
            #_txt.write(result)
            #os.system('gnome-terminal -- python3 ' + infoSenderTTS + '__tts.py &')
            #print(' ')
    except socket.gaierror:
        pass

def citizenshipInfo(main_sender, main_passwd, receiver, accept_path):
    try:
        os.system('aplay ' + accept_path +' &')
        print(' ')
        print(' ')
        time.sleep(1)
        fromaddr = main_sender
        toaddr = receiver
        msg = MIMEMultipart() # instance of MIMEMultipart 
        msg['From'] = fromaddr    # storing the main_senders email address 
        msg['To'] = toaddr   # storing the receivers email address 
        msg['Subject'] = "CONFIDENTIALS INFORMATION"# storing the subject  
        body = host_ip + '/login/citizenshipInfo'   # string to store the body of the mail
        msg.attach(MIMEText(body, 'plain'))     # attach the body with the msg instance 
        filename = "citizenshipInfoSite.png"    # open the file to be sent  
        attachment = open("SystemService/PrimaryCredentials/credentialsSites/citizenshipInfoSite.png", "rb") 
        p = MIMEBase('application', 'octet-stream')     # instance of MIMEBase and named as p 
        p.set_payload((attachment).read())     # To change the payload into encoded form 
        encoders.encode_base64(p)     # encode into base64
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
        msg.attach(p)     # attach the instance 'p' to instance 'msg' 
        s = smtplib.SMTP('smtp.gmail.com', 587)     # creates SMTP session 
        s.starttls()     # start TLS for security 
        s.login(fromaddr, main_passwd)     # Authentication 
        text = msg.as_string()     # Converts the Multipart msg into a string 
        s.sendmail(fromaddr, toaddr, text)     # sending the mail 
        s.quit()     # terminating the session 
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        print('CitizenshipInfo Sent')
        print(' ')
        print(' ')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        if os.uname()[1] == 'dslave':
            speak('Accomplish Pemba')
        else:
            #_txt = open(temporaryfiles + '.txt','w+')
            #_txt.write(result)
            #os.system('gnome-terminal -- python3 ' + infoSenderTTS + '__tts.py &')
            #print(' ')
    except socket.gaierror:
        pass

def folderlockpassInfo(main_sender, main_passwd, receiver, accept_path):
    try:
        os.system('aplay ' + accept_path +' &')
        print(' ')
        print(' ')
        time.sleep(1)
        fromaddr = main_sender
        toaddr = receiver
        msg = MIMEMultipart() # instance of MIMEMultipart 
        msg['From'] = fromaddr    # storing the main_senders email address 
        msg['To'] = toaddr   # storing the receivers email address 
        msg['Subject'] = "CONFIDENTIALS INFORMATION"# storing the subject  
        body = host_ip + '/login/folderlockpassInfo'    # string to store the body of the mail
        msg.attach(MIMEText(body, 'plain'))     # attach the body with the msg instance 
        filename = "folderlockpassInfoSite.png"    # open the file to be sent  
        attachment = open("SystemService/PrimaryCredentials/credentialsSites/folderlockpassInfoSite.png", "rb") 
        p = MIMEBase('application', 'octet-stream')     # instance of MIMEBase and named as p 
        p.set_payload((attachment).read())     # To change the payload into encoded form 
        encoders.encode_base64(p)     # encode into base64
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
        msg.attach(p)     # attach the instance 'p' to instance 'msg' 
        s = smtplib.SMTP('smtp.gmail.com', 587)     # creates SMTP session 
        s.starttls()     # start TLS for security 
        s.login(fromaddr, main_passwd)     # Authentication 
        text = msg.as_string()     # Converts the Multipart msg into a string 
        s.sendmail(fromaddr, toaddr, text)     # sending the mail 
        s.quit()     # terminating the session 
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        print('folderlockpassInfo Sent')
        print(' ')
        print(' ')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        if os.uname()[1] == 'dslave':
            speak('Accomplish Pemba')
        else:
            #_txt = open(temporaryfiles + '.txt','w+')
            #_txt.write(result)
            #os.system('gnome-terminal -- python3 ' + infoSenderTTS + '__tts.py &')
            #print(' ')
    except socket.gaierror:
        pass

def internetAccInfo(main_sender, main_passwd, receiver, accept_path):
    try:
        os.system('aplay ' + accept_path +' &')
        print(' ')
        print(' ')
        time.sleep(1)
        fromaddr = main_sender
        toaddr = receiver
        msg = MIMEMultipart() # instance of MIMEMultipart 
        msg['From'] = fromaddr    # storing the main_senders email address 
        msg['To'] = toaddr   # storing the receivers email address 
        msg['Subject'] = "CONFIDENTIALS INFORMATION"# storing the subject  
        body = host_ip + '/login/internetAccInfo'    # string to store the body of the mail
        msg.attach(MIMEText(body, 'plain'))     # attach the body with the msg instance 
        filename = "internetAccInfoSite.png"    # open the file to be sent  
        attachment = open("SystemService/PrimaryCredentials/credentialsSites/internetAccInfoSite.png", "rb") 
        p = MIMEBase('application', 'octet-stream')     # instance of MIMEBase and named as p 
        p.set_payload((attachment).read())     # To change the payload into encoded form 
        encoders.encode_base64(p)     # encode into base64
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
        msg.attach(p)     # attach the instance 'p' to instance 'msg' 
        s = smtplib.SMTP('smtp.gmail.com', 587)     # creates SMTP session 
        s.starttls()     # start TLS for security 
        s.login(fromaddr, main_passwd)     # Authentication 
        text = msg.as_string()     # Converts the Multipart msg into a string 
        s.sendmail(fromaddr, toaddr, text)     # sending the mail 
        s.quit()     # terminating the session 
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        print('internetAccInfo Sent')
        print(' ')
        print(' ')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        if os.uname()[1] == 'dslave':
            speak('Accomplish Pemba')
        else:
            #_txt = open(temporaryfiles + '.txt','w+')
            #_txt.write(result)
            #os.system('gnome-terminal -- python3 ' + infoSenderTTS + '__tts.py &')
            #print(' ')
    except socket.gaierror:
        pass

def othersGmailInfo(main_sender, main_passwd, receiver, accept_path):
    try:
        os.system('aplay ' + accept_path +' &')
        print(' ')
        print(' ')
        time.sleep(1)
        fromaddr = main_sender
        toaddr = receiver
        msg = MIMEMultipart() # instance of MIMEMultipart 
        msg['From'] = fromaddr    # storing the main_senders email address 
        msg['To'] = toaddr   # storing the receivers email address 
        msg['Subject'] = "CONFIDENTIALS INFORMATION"# storing the subject  
        body = host_ip + '/login/otherGmailInfo'    # string to store the body of the mail
        msg.attach(MIMEText(body, 'plain'))     # attach the body with the msg instance 
        filename = "otherGmailInfoSite.png"    # open the file to be sent  
        attachment = open("SystemService/PrimaryCredentials/credentialsSites/otherGmailInfoSite.png", "rb") 
        p = MIMEBase('application', 'octet-stream')     # instance of MIMEBase and named as p 
        p.set_payload((attachment).read())     # To change the payload into encoded form 
        encoders.encode_base64(p)     # encode into base64
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
        msg.attach(p)     # attach the instance 'p' to instance 'msg' 
        s = smtplib.SMTP('smtp.gmail.com', 587)     # creates SMTP session 
        s.starttls()     # start TLS for security 
        s.login(fromaddr, main_passwd)     # Authentication 
        text = msg.as_string()     # Converts the Multipart msg into a string 
        s.sendmail(fromaddr, toaddr, text)     # sending the mail 
        s.quit()     # terminating the session 
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        print('othersGamilInfo Sent')
        print(' ')
        print(' ')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        if os.uname()[1] == 'dslave':
            speak('Accomplish Pemba')
        else:
            #_txt = open(temporaryfiles + '.txt','w+')
            #_txt.write(result)
            #os.system('gnome-terminal -- python3 ' + infoSenderTTS + '__tts.py &')
            #print(' ')
    except socket.gaierror:
        pass

def PasswordGmailInfo(main_sender, main_passwd, receiver, accept_path):
    try:
        os.system('aplay ' + accept_path +' &')
        print(' ')
        print(' ')
        time.sleep(1)
        fromaddr = main_sender
        toaddr = receiver
        msg = MIMEMultipart() # instance of MIMEMultipart 
        msg['From'] = fromaddr    # storing the main_senders email address 
        msg['To'] = toaddr   # storing the receivers email address 
        msg['Subject'] = "CONFIDENTIALS INFORMATION"# storing the subject  
        body = host_ip + '/login/passwd-GInfo'    # string to store the body of the mail
        msg.attach(MIMEText(body, 'plain'))     # attach the body with the msg instance 
        filename = "passwd-GInfoSite.png"    # open the file to be sent  
        attachment = open("SystemService/PrimaryCredentials/credentialsSites/passwd-GInfoSite.png", "rb") 
        p = MIMEBase('application', 'octet-stream')     # instance of MIMEBase and named as p 
        p.set_payload((attachment).read())     # To change the payload into encoded form 
        encoders.encode_base64(p)     # encode into base64
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
        msg.attach(p)     # attach the instance 'p' to instance 'msg' 
        s = smtplib.SMTP('smtp.gmail.com', 587)     # creates SMTP session 
        s.starttls()     # start TLS for security 
        s.login(fromaddr, main_passwd)     # Authentication 
        text = msg.as_string()     # Converts the Multipart msg into a string 
        s.sendmail(fromaddr, toaddr, text)     # sending the mail 
        s.quit()     # terminating the session 
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        print('PasswordGmailInfo Sent')
        print(' ')
        print(' ')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        if os.uname()[1] == 'dslave':
            speak('Accomplish Pemba')
        else:
            #_txt = open(temporaryfiles + '.txt','w+')
            #_txt.write(result)
            #os.system('gnome-terminal -- python3 ' + infoSenderTTS + '__tts.py &')
            #print(' ')
    except socket.gaierror:
        pass

def payeerInfo(main_sender, main_passwd, receiver, accept_path):
    try:
        os.system('aplay ' + accept_path +' &')
        print(' ')
        print(' ')
        time.sleep(1)
        fromaddr = main_sender
        toaddr = receiver
        msg = MIMEMultipart() # instance of MIMEMultipart 
        msg['From'] = fromaddr    # storing the main_senders email address 
        msg['To'] = toaddr   # storing the receivers email address 
        msg['Subject'] = "CONFIDENTIALS INFORMATION"# storing the subject  
        body = host_ip + '/login/payeerInfo'    # string to store the body of the mail
        msg.attach(MIMEText(body, 'plain'))     # attach the body with the msg instance 
        filename = "payeerInfoSite.png"    # open the file to be sent  
        attachment = open("SystemService/PrimaryCredentials/credentialsSites/payeerInfoSite.png", "rb") 
        p = MIMEBase('application', 'octet-stream')     # instance of MIMEBase and named as p 
        p.set_payload((attachment).read())     # To change the payload into encoded form 
        encoders.encode_base64(p)     # encode into base64
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
        msg.attach(p)     # attach the instance 'p' to instance 'msg' 
        s = smtplib.SMTP('smtp.gmail.com', 587)     # creates SMTP session 
        s.starttls()     # start TLS for security 
        s.login(fromaddr, main_passwd)     # Authentication 
        text = msg.as_string()     # Converts the Multipart msg into a string 
        s.sendmail(fromaddr, toaddr, text)     # sending the mail 
        s.quit()     # terminating the session 
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        print('payeerInfo Sent')
        print(' ')
        print(' ')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        if os.uname()[1] == 'dslave':
            speak('Accomplish Pemba')
        else:
            #_txt = open(temporaryfiles + '.txt','w+')
            #_txt.write(result)
            #os.system('gnome-terminal -- python3 ' + infoSenderTTS + '__tts.py &')
            #print(' ')
    except socket.gaierror:
        pass

def payoneerInfo(main_sender, main_passwd, receiver, accept_path):
    try:
        os.system('aplay ' + accept_path +' &')
        print(' ')
        print(' ')
        time.sleep(1)
        fromaddr = main_sender
        toaddr = receiver
        msg = MIMEMultipart() # instance of MIMEMultipart 
        msg['From'] = fromaddr    # storing the main_senders email address 
        msg['To'] = toaddr   # storing the receivers email address 
        msg['Subject'] = "CONFIDENTIALS INFORMATION"# storing the subject  
        body = host_ip + '/login/payoneerInfo'    # string to store the body of the mail
        msg.attach(MIMEText(body, 'plain'))     # attach the body with the msg instance 
        filename = "payoneerInfoSite.png"    # open the file to be sent  
        attachment = open("SystemService/PrimaryCredentials/credentialsSites/payoneerInfoSite.png", "rb") 
        p = MIMEBase('application', 'octet-stream')     # instance of MIMEBase and named as p 
        p.set_payload((attachment).read())     # To change the payload into encoded form 
        encoders.encode_base64(p)     # encode into base64
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
        msg.attach(p)     # attach the instance 'p' to instance 'msg' 
        s = smtplib.SMTP('smtp.gmail.com', 587)     # creates SMTP session 
        s.starttls()     # start TLS for security 
        s.login(fromaddr, main_passwd)     # Authentication 
        text = msg.as_string()     # Converts the Multipart msg into a string 
        s.sendmail(fromaddr, toaddr, text)     # sending the mail 
        s.quit()     # terminating the session 
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        print('payoneerInfo sent')
        print(' ')
        print(' ')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        if os.uname()[1] == 'dslave':
            speak('Accomplish Pemba')
        else:
            #_txt = open(temporaryfiles + '.txt','w+')
            #_txt.write(result)
            #os.system('gnome-terminal -- python3 ' + infoSenderTTS + '__tts.py &')
            #print(' ')
    except socket.gaierror:
        pass

def personalGmailInfo(main_sender, main_passwd, receiver, accept_path):
    try:
        os.system('aplay ' + accept_path +' &')
        print(' ')
        print(' ')
        time.sleep(1)
        fromaddr = main_sender
        toaddr = receiver
        msg = MIMEMultipart() # instance of MIMEMultipart 
        msg['From'] = fromaddr    # storing the main_senders email address 
        msg['To'] = toaddr   # storing the receivers email address 
        msg['Subject'] = "CONFIDENTIALS INFORMATION"# storing the subject  
        body = host_ip + '/login/personalGmailInfo'    # string to store the body of the mail
        msg.attach(MIMEText(body, 'plain'))     # attach the body with the msg instance 
        filename = "personalGmailInfoSite.png"    # open the file to be sent  
        attachment = open("SystemService/PrimaryCredentials/credentialsSites/personalGmailInfoSite.png", "rb") 
        p = MIMEBase('application', 'octet-stream')     # instance of MIMEBase and named as p 
        p.set_payload((attachment).read())     # To change the payload into encoded form 
        encoders.encode_base64(p)     # encode into base64
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
        msg.attach(p)     # attach the instance 'p' to instance 'msg' 
        s = smtplib.SMTP('smtp.gmail.com', 587)     # creates SMTP session 
        s.starttls()     # start TLS for security 
        s.login(fromaddr, main_passwd)     # Authentication 
        text = msg.as_string()     # Converts the Multipart msg into a string 
        s.sendmail(fromaddr, toaddr, text)     # sending the mail 
        s.quit()     # terminating the session 
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        print('personalGmailInfo sent')
        print(' ')
        print(' ')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        if os.uname()[1] == 'dslave':
            speak('Accomplish Pemba')
        else:
            #_txt = open(temporaryfiles + '.txt','w+')
            #_txt.write(result)
            #os.system('gnome-terminal -- python3 ' + infoSenderTTS + '__tts.py &')
            #print(' ')
    except socket.gaierror:
        pass

def twillioinfo(main_sender, main_passwd, receiver, accept_path):
    try:
        os.system('aplay ' + accept_path +' &')
        print(' ')
        print(' ')
        time.sleep(1)
        fromaddr = main_sender
        toaddr = receiver
        msg = MIMEMultipart() # instance of MIMEMultipart 
        msg['From'] = fromaddr    # storing the main_senders email address 
        msg['To'] = toaddr   # storing the receivers email address 
        msg['Subject'] = "CONFIDENTIALS INFORMATION"# storing the subject  
        body = host_ip + '/login/twillioInfo'    # string to store the body of the mail
        msg.attach(MIMEText(body, 'plain'))     # attach the body with the msg instance 
        filename = "twillioInfoSite.png"    # open the file to be sent  
        attachment = open("SystemService/PrimaryCredentials/credentialsSites/twillioInfoSite.png", "rb") 
        p = MIMEBase('application', 'octet-stream')     # instance of MIMEBase and named as p 
        p.set_payload((attachment).read())     # To change the payload into encoded form 
        encoders.encode_base64(p)     # encode into base64
        p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
        msg.attach(p)     # attach the instance 'p' to instance 'msg' 
        s = smtplib.SMTP('smtp.gmail.com', 587)     # creates SMTP session 
        s.starttls()     # start TLS for security 
        s.login(fromaddr, main_passwd)     # Authentication 
        text = msg.as_string()     # Converts the Multipart msg into a string 
        s.sendmail(fromaddr, toaddr, text)     # sending the mail 
        s.quit()     # terminating the session 
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        print('twillioinfo sent')
        print(' ')
        print(' ')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        if os.uname()[1] == 'dslave':
            speak('Accomplish Pemba')
        else:
            #_txt = open(temporaryfiles + '.txt','w+')
            #_txt.write(result)
            #os.system('gnome-terminal -- python3 ' + infoSenderTTS + '__tts.py &')
            #print(' ')
    except socket.gaierror:
        pass

def test(accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    print(' ')
    fromaddr = "dismis.homeautomation@gmail.com"
    toaddr = "pembatamang.m@gmail.com"
    msg = MIMEMultipart() # instance of MIMEMultipart 
    msg['From'] = fromaddr    # storing the main_senders email address 
    msg['To'] = toaddr   # storing the receivers email address 
    msg['Subject'] = "CONFIDENTIALS INFORMATION"# storing the subject  
    body = host_ip + ''    # string to store the body of the mail
    msg.attach(MIMEText(body, 'plain'))     # attach the body with the msg instance 
    filename = "paynoeerInfo.txt"    # open the file to be sent  
    attachment = open("SystemService/credentials/paynoeerInfo.txt", "rb") 
    p = MIMEBase('application', 'octet-stream')     # instance of MIMEBase and named as p 
    p.set_payload((attachment).read())     # To change the payload into encoded form 
    encoders.encode_base64(p)     # encode into base64
    p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
    msg.attach(p)     # attach the instance 'p' to instance 'msg' 
    s = smtplib.SMTP('smtp.gmail.com', 587)     # creates SMTP session 
    s.starttls()     # start TLS for security 
    s.login(fromaddr, "D1i1s1m1i1s@")     # Authentication 
    text = msg.as_string()     # Converts the Multipart msg into a string 
    s.sendmail(fromaddr, toaddr, text)     # sending the mail 
    s.quit()     # terminating the session 
    speak('Accomplish Pemba')