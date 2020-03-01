#!/usr/bin/python3
import smtplib
import socket

""" GLOBAL FUNCTION """
def Log_Time():
    import datetime
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))


""" Alert2 is used in bestfriendBirthdayProtocal Function as a reminder of bestfriend's birthday tomorrow. """
#def Alert1(slave_sender, slave_passwd, receiver):

""" Alert2 is used in conversation of what can you do function """
#def Alert2(slave_sender, slave_passwd, receiver):
    
""" Alert3 is used in DISMIS-HA.py for send the whole system log file of Dismis-Home Automation """
#def Alert3(slave_sender, slave_passwd, receiver):

""" Alert4 is used in greeting.py for send greeting module data in the formate of text file to primary mail """
#def Alert4(slave_sender, slave_passwd, receiver):

def Alert5(slave_sender, slave_passwd, receiver):
    try:
        From = slave_sender
        to = receiver
        subject = 'Dismis Alert: Anisha\'s Birthday Tomorrow '
        msg = 'Subject:{}\n\nPEMBA Tomorrow is Anisha\'s birthday, may you have already remebered it. I\'m here to assist you, Don\'t forget to wish her tonight.\n\nThis is a message from Alert1.\n\n\n And PEMBA don\'t forget to change the date as follows in the next year'.format(subject)
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.ehlo()
        server.login(slave_sender, slave_passwd)
        server.sendmail(From, to, msg)
        server.quit()
        print('--- Reminder Sent ---')
    except socket.gaierror:
        pass

def Alert6(slave_sender, slave_passwd, receiver):
    try:
        From = slave_sender
        to = receiver
        subject = 'Dismis Alert: Anisha\'s Birthday Tomorrow '
        msg = 'Subject:{}\n\nPEMBA Tomorrow is Anisha\'s birthday, may you have already remebered it. I\'m here to assist you, Don\'t forget to wish her tonight.\n\nThis is a message from Alert1.\n\n\n And PEMBA don\'t forget to change the date as follows in the next year'.format(subject)
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.ehlo()
        server.login(slave_sender, slave_passwd)
        server.sendmail(From, to, msg)
        server.quit()
        print('--- Reminder Sent ---')
    except socket.gaierror:
        pass

def Alert7(slave_sender, slave_passwd, receiver):
    try:
        From = slave_sender
        to = receiver
        subject = 'Dismis Alert: Anisha\'s Birthday Tomorrow '
        msg = 'Subject:{}\n\nPEMBA Tomorrow is Anisha\'s birthday, may you have already remebered it. I\'m here to assist you, Don\'t forget to wish her tonight.\n\nThis is a message from Alert1.\n\n\n And PEMBA don\'t forget to change the date as follows in the next year'.format(subject)
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.starttls()
        server.ehlo()
        server.login(slave_sender, slave_passwd)
        server.sendmail(From, to, msg)
        server.quit()
        print('--- Reminder Sent ---')
    except socket.gaierror:
        pass

    