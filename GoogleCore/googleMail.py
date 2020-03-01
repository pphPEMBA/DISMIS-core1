#!/usr/bin/python3

import smtplib
import os
from SpeechDriver.tts.ttsdefault import speak


""" GLOBAL FUNCTION """
def Log_Time():
    import datetime
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))


def gmail(personalMail, personalPasswd, accept_path):
    os.system('aplay ' + accept_path +' &')
    print(' ')
    speak('Creating Google Mail Environment sir')
    TO = input('To whom sir, write there email: ')
    SUBJECT = input('Subject: ')
    TEXT = input('Message sir: ')

    # Gmail Sign In
    gmail_sender = personalMail
    gmail_passwd = personalPasswd

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_sender, gmail_passwd)

    BODY = '\r\n'.join(['To: %s' % TO,
                        'From: %s' % gmail_sender,
                        'Subject: %s' % SUBJECT,
                        '', TEXT])

    try:
        server.sendmail(gmail_sender, [TO], BODY)
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        print('email sent')
        print(' ')
        print(' ')
        print('\t\t\t\tFunction: googleMail')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        speak('mail sent sir')
    except smtplib.SMTPServerDisconnected:
        speak('Failed to connect to the server. Wrong user/password?')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        print('Failed to connect to the server. Wrong user/password?')
        print(' ')
        print(' ')
        print('\t\t\t\tFunction: googleMail')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    except smtplib.SMTPException as e:
        speak('SMTP error occurred: ' + str(e))
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        print('SMTP error occurred: ' + str(e))
        print(' ')
        print(' ')
        print('\t\t\t\tFunction: googleMail')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    server.quit()

