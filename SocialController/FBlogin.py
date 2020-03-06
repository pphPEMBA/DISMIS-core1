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
FBloginTTS_path = profile_data['FBloginTTS_path']
FBloginTTS = FBloginTTS_path + '/SpeechDriver/tts/ServicesTTS/FBloginTTS/'
#print(FBloginTTS)


def login(accept_path, chromeDriver_linux):
    print(' ')
    print(' ')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print('loggin to facebook')
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: login')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    username = '9815028758'
    password = 'kakarvitta23'

    url = 'https://www.facebook.com/'

    driver = webdriver.Chrome(executable_path=chromeDriver_linux)

    driver.get(url)

    driver.find_element_by_id('email').send_keys(username)
    driver.find_element_by_id('pass').send_keys(password)

    time.sleep(2)

    driver.find_element_by_id('loginbutton').click()
    #FBlogin_txt = open(temporaryfiles + 'FBlogin.txt','w+')
    #FBlogin_txt.write(result)
    #os.system('gnome-terminal -- python3 ' + FBloginTTS + 'FBlogin__tts.py &')
    #print(' ')