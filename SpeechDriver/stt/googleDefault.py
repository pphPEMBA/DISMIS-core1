#!/usr/bin/python3
import speech_recognition as sr
import datetime, socket
from os import system
import time

#from Core.main import *
from Core.profile import *
from Core.brainstem import cmd

""" GLOBAL FUNCTION """
def Log_Time():
    import datetime
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

speech = sr.Recognizer()

def read_voice_cmd():
    voice_text = ''
    print(datetime.datetime.now().ctime() + '  Listening...')
    try:
        with sr.Microphone() as source:
            speech.energy_threshold = 4000
            speech.adjust_for_ambient_noise(source)
            audio = speech.listen(source)
            #audio = speech.listen(source=source, timeout=10, phrase_time_limit=5)
        voice_text = speech.recognize_google(audio).lower().replace("'", "")
        print(' ')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print('**************************************************************************************************************************************************************************************')
        Log_Time()
        print("DISMIS thinks you said '" + voice_text + "'")
        print('**************************************************************************************************************************************************************************************')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        try:
            """ Notification of what Dismis had listen """
            from gi.repository import Notify
            # One time initialization of libnotify
            Notify.init("Dismis_slave1")
            # Create the notification object
            title = "Dismis_slave1"
            body = "DISMIS thinks you said '" + voice_text + "'"
            notification = Notify.Notification.new(title,body)
            # Actually show on screen
            notification.show()
        except:
            pass
        """ Write voice recognize log """
        d=open(voice_recognitionlog,'a+')
        d.write(datetime.datetime.now().ctime())
        d.write (" DISMIS thinks you said '" + voice_text + "'" + "\n")
    except sr.UnknownValueError:
        #pass
        listen = read_voice_cmd()
        return listen
        #voice_text = str(input('Command: '))
    except sr.WaitTimeoutError:
        pass
    except sr.RequestError:
        print('Network error')
    except ConnectionResetError:
        pass
    else:
        time.sleep(1)
        notification.close() # Close notification immediately
    cmd(voice_text,\
        name,default_CityLocation,openweatherAPI,temporaryfiles,\

        main_sender,main_passwd,slave_sender,slave_passwd,receiver,personalMail,personalPasswd,\

        accept_path,else_path,\

        Ctoken_pickle,Ccredentials,login_id_path,\

        Aneey_wishMailer_path,AneeyC_BirthdayAlert_path,Anisha_wishMailer_path,Anum_wishMailer_path,AnumBirthdayAlert_path,BestfriendBirthdayProtocal_path,PersonalGmailNotify_path,flask_credentials_path,schedule_path,StopEvent_ai_path,


        chromeDriver_linux,chromeDriver_win,chromeDriver_mac,\

        Dismis_sounds,NewYear,laughSound1,laughSound2,piano_tunes,memory_db,noteManually_txt,schedule_Gcalendar,greetingMail,routine_data1,routine_data2,routine_data3,routine_data4,routine_data5,routine_data6,routine_data7,routine_data8,routine_data9,routine_data10,\
        routine_time1,routine_time2,routine_time3,routine_time4,routine_time5,routine_time6,routine_time7,routine_time8,routine_time9,routine_time10,\
        gcal3days,gcal5days,gcal7days,gcal10days,gcal15days,gcal20days,gcal25days,gcal30days,gcal_upcoming,\
        Dismis_HA_wholesystemlog,exit_Dismis_HA_log,initialize_Dismis_HA_log,voice_recognitionlog,\

        BestfriendBirthday_date,host_ip,tts_pico2wave_wav,tts_main_wav,tts_BestfriendBirthdayALERT_wav,\

        googleCalendarTTS_path,conversationTTS_path,date_timeTTS_path,greetingTTS_path,internetTTS_path,jokes_quoteTTS_path,noteManuallyTTS_path,notesTTS_path,rhythmbox_client_ControllerTTS_path,weatherTTS_path,youtubeTTS_path,FBloginTTS_path,Gcreate_accountTTS_path,GloginTTS_path,twitterloginTTS_path,AI_TTS_path,PrimaryCredentialsTTS_path,appManagerTTS_path,infoSenderTTS_path,systemTaskTTS_path,updateSystemTTS_path,volumeControllerTTS_path
        
        )
