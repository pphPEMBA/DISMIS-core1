#!/usr/bin/python3
from selenium import webdriver
import time, os 


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
GloginTTS_path = profile_data['GloginTTS_path']
GloginTTS = GloginTTS_path + '/SpeechDriver/tts/ServicesTTS/GloginTTS/'
#print(GloginTTS)


def PersonalMail(accept_path, chromeDriver_linux):
    print(' ')
    print(' ')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('loggin to gmail')
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: PersonalMail')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

    # create a new Chrome session
    #driver = webdriver.Chrome()
    driver = webdriver.Chrome(executable_path=chromeDriver_linux)
    driver.implicitly_wait(30)
    driver.maximize_window()

    # navigate to the application home page
    driver.get("https://accounts.google.com/")

    #get the username textbox
    login_field = driver.find_element_by_name("identifier")
    login_field.clear()

    #enter username
    login_field.send_keys("pembatamang.m@gmail.com")
    login_field.send_keys(u'\ue007') #unicode for enter key
    time.sleep(2)

    #get the password textbox
    password_field = driver.find_element_by_name("password")
    password_field.clear()

    #enter password
    password_field.send_keys("dtgezqiqgzujbddf")
    password_field.send_keys(u'\ue007') #unicode for enter key
    #time.sleep(10)

    #navigate to gmail
    driver.get("https://mail.google.com/")
    Glogin1_txt = open(temporaryfiles + 'Glogin1.txt','w+')
    Glogin1_txt.write(result)
    os.system('gnome-terminal -- python3 ' + GloginTTS + 'Glogin1__tts.py &')
    print(' ')


#PersonalMail()

def YoutubeMail(accept_path, chromeDriver_linux):
    # create a new Chrome session
    #driver = webdriver.Chrome()
    driver = webdriver.Chrome(executable_path=chromeDriver_linux)
    driver.implicitly_wait(30)
    driver.maximize_window()

    # navigate to the application home page
    driver.get("https://accounts.google.com/")

    #get the username textbox
    login_field = driver.find_element_by_name("identifier")
    login_field.clear()

    #enter username
    login_field.send_keys("pembamoktan.t@gmail.com")
    login_field.send_keys(u'\ue007') #unicode for enter key
    time.sleep(2)

    #get the password textbox
    password_field = driver.find_element_by_name("password")
    password_field.clear()

    #enter password
    password_field.send_keys("hackerpemba")
    password_field.send_keys(u'\ue007') #unicode for enter key
    time.sleep(10)

    #navigate to gmail
    driver.get("https://mail.google.com/")


    #Glogin2_txt = open(temporaryfiles + 'Glogin2.txt','w+')
    #Glogin2_txt.write(result)
    #os.system('gnome-terminal -- python3 ' + GloginTTS + 'Glogin2__tts.py &')
    #print(' ')