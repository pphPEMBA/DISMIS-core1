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
twitterloginTTS_path = profile_data['twitterloginTTS_path']
twitterloginTTS = twitterloginTTS_path + '/SpeechDriver/tts/ServicesTTS/twitterloginTTS/'
#print(twitterloginTTS)


def login(accept_path):
    print(' ')
    print(' ')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('loggin to twitter')
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: login')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

    # create a new Chrome session
    driver = webdriver.Chrome()
    driver.implicitly_wait(30)
    driver.maximize_window()

    # navigate to the application home page
    driver.get("https://twitter.com/login")


    # get the username textbox
    login_field = driver.find_element_by_class_name("js-username-field")
    login_field.clear()

    # enter username
    login_field.send_keys("ENTER USERNAME HERE")
    time.sleep(1)

    #get the password textbox
    password_field = driver.find_element_by_class_name("js-password-field")
    password_field.clear()

    #enter password
    password_field.send_keys("ENTER PASSWORD HERE")
    time.sleep(1)
    password_field.submit()
    twitterlogin_txt = open(temporaryfiles + 'twitterlogin.txt','w+')
    twitterlogin_txt.write(result)
    os.system('gnome-terminal -- python3 ' + twitterloginTTS + 'twitterlogin__tts.py &')
    print(' ')