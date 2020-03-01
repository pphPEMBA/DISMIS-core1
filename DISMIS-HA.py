import socket

""" Importing Profiles """
import yaml
from Core.profile import profile_path
profile = open(profile_path)
profile_data = yaml.safe_load(profile)
profile.close()
#Functioning Variables
Dismis_HA_wholesystemlog = profile_data['Dismis_HA_wholesystemlog']
exit_Dismis_HA_log = profile_data['exit_Dismis_HA_log']
initialize_Dismis_HA_log = profile_data['initialize_Dismis_HA_log']
slave_sender = profile_data['slave_sender']
slave_passwd = profile_data['slave_passwd']
receiver = profile_data['receiver']

""" TimeStamp When Dimsis-Home Automation start """
def Initializinglog():
    import datetime
    d=open(initialize_Dismis_HA_log, 'a+')
    d.write(datetime.datetime.now().ctime())
    d.write (": Starting Dismis-Home Automation \n")
    print(datetime.datetime.now().ctime() + ": Starting Dismis-Home Automation")
    print(' ')
   
""" TimeStamp When Dimsis-Home Automation exit or stopped """
import smtplib
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders 
import os
import time
def Alert3(slave_sender, slave_passwd, receiver):
    try:
        fromaddr = slave_sender
        toaddr = receiver
        msg = MIMEMultipart() # instance of MIMEMultipart 
        msg['From'] = fromaddr    # storing the main_senders email address 
        msg['To'] = toaddr   # storing the receivers email address 
        msg['Subject'] = "Dismis-HA Log file"# storing the subject  
        #body = "Body_of_the_mail"    # string to store the body of the mail
        #msg.attach(MIMEText(body, 'plain'))     # attach the body with the msg instance 
        filename = "Dismis_HA_wholesystem.log"    # open the file to be sent  
        attachment = open(Dismis_HA_wholesystemlog, "rb") 
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
        print('--- Dismis-HomeAutomation Has Stopped Notify Sent')
        print(' ')
    except socket.gaierror:
        pass
    
import atexit
import datetime
def Exitlog():
    d=open(exit_Dismis_HA_log, 'a+')
    d.write(datetime.datetime.now().ctime())
    d.write (": Dismis-Home Automation Exit \n")
    Alert3(slave_sender, slave_passwd, receiver)
    print(datetime.datetime.now().ctime() + ": Dismis-Home Automation Ended")
    print(' ')
    print(' ') #hastage ko bitra dismis stop vanera lakhnu
    from pyfiglet import Figlet
    custom_fig = Figlet(font='larry3d')
    print(custom_fig.renderText('Dismis-HA Stopped'))
    

"#####################################################################################################"
"#####################################################################################################"
""" Running Dismis-Home Automation """
Initializinglog()
atexit.register(Exitlog)
from SpeechDriver.stt.googleDefault import read_voice_cmd
def Dismis_HomeAutomation():
    read_voice_cmd()

if __name__ == '__main__':
    while True:
        Dismis_HomeAutomation()

#python3 ~/.Dismis_Home_Automation/DISMIS-HA.py >> ~/.Dismis_Home_Automation/SystemService/Dismis_HA_log/Dismis_HA_wholesystem.log 2>&1 &