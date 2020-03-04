profile_path = '/home/d-slave1/d1_SuperDismis/DISMIS-core/SystemService/middleware/profile.yaml'

""" IMPORTING profile.py PATH """
import yaml
#from Core.profile import profile_path
profile = open(profile_path)
profile_data = yaml.safe_load(profile)
profile.close()
#Functioning Variables
name = profile_data['name']
default_CityLocation = profile_data['default_CityLocation']
openweatherAPI = profile_data['openweatherAPI']
temporaryfiles = profile_data['temporaryfiles']

main_sender = profile_data['main_sender']
main_passwd = profile_data['main_passwd']
slave_sender = profile_data['slave_sender']
slave_passwd = profile_data['slave_passwd']
receiver = profile_data['receiver']
personalMail = profile_data['personalMail']
personalPasswd = profile_data['personalPasswd']

accept_path = profile_data['accept_path']
else_path = profile_data['else_path']   #not using

Ctoken_pickle = profile_data['Ctoken_pickle'] 
Ccredentials = profile_data['Ccredentials'] 
login_id_path = profile_data['login_id_path']  #check where it is using

BestfriendBirthdayProtocal_path = profile_data['BestfriendBirthdayProtocal_path']
PersonalGmailNotify_path = profile_data['PersonalGmailNotify_path']
flask_credentials_path = profile_data['flask_credentials_path']
schedule_path = profile_data['schedule_path']
StopEvent_ai_path = profile_data['StopEvent_ai_path']

Dismis_HA_wholesystemlog = profile_data['Dismis_HA_wholesystemlog'] # using in DISMIS-HA
exit_Dismis_HA_log = profile_data['exit_Dismis_HA_log'] # using in DISMIS-HA
initialize_Dismis_HA_log = profile_data['initialize_Dismis_HA_log'] # using in DISMIS-HA
voice_recognitionlog = profile_data['voice_recognitionlog'] # using in googleDefault

chromeDriver_linux = profile_data['chromeDriver_linux']
chromeDriver_win = profile_data['chromeDriver_win']
chromeDriver_mac = profile_data['chromeDriver_mac']

Dismis_sounds = profile_data['Dismis_sounds']
NewYear = profile_data['NewYear']
laughSound1 = profile_data['laughSound1']
laughSound2 = profile_data['laughSound2']
piano_tunes = profile_data['piano_tunes']
memory_db = profile_data['memory_db']
noteManually_txt = profile_data['noteManually_txt'] 
schedule_Gcalendar = profile_data['schedule_Gcalendar']
greetingMail = profile_data['greetingMail']
routine_data1  = profile_data['routine_data1']
routine_data2 = profile_data['routine_data2']
routine_data3 = profile_data['routine_data3']
routine_data4 = profile_data['routine_data4']
routine_data5 = profile_data['routine_data5']
routine_data6 = profile_data['routine_data6']
routine_data7 = profile_data['routine_data7']
routine_data8 = profile_data['routine_data8']
routine_data9 = profile_data['routine_data9']
routine_data10 = profile_data['routine_data10']
routine_time1 = profile_data['routine_time1']
routine_time2 = profile_data['routine_time2']
routine_time3 = profile_data['routine_time3']
routine_time4 = profile_data['routine_time4']
routine_time5 = profile_data['routine_time5']
routine_time6 = profile_data['routine_time6']
routine_time7 = profile_data['routine_time7']
routine_time8 = profile_data['routine_time8']
routine_time9 = profile_data['routine_time9']
routine_time10 = profile_data['routine_time10']
gcal3days = profile_data['gcal3days']
gcal5days = profile_data['gcal5days']
gcal7days = profile_data['gcal7days']
gcal10days = profile_data['gcal10days']
gcal15days = profile_data['gcal15days']
gcal20days = profile_data['gcal20days']
gcal25days = profile_data['gcal25days']
gcal30days = profile_data['gcal30days']

BestfriendBirthday_date = profile_data['BestfriendBirthday_date'] 
host_ip= profile_data['host_ip'] # using in PrimaryCredentials.flaskServer & in infosender
tts_pico2wave_wav = profile_data['tts_pico2wave_wav']
tts_main_wav = profile_data['tts_main_wav']
tts_BestfriendBirthdayALERT_wav = profile_data['tts_BestfriendBirthdayALERT_wav']


googleCalendarTTS_path = profile_data['googleCalendarTTS_path']
conversationTTS_path = profile_data['conversationTTS_path']
date_timeTTS_path = profile_data['date_timeTTS_path']
greetingTTS_path = profile_data['greetingTTS_path']
internetTTS_path = profile_data['internetTTS_path']
jokes_quoteTTS_path = profile_data['jokes_quoteTTS_path']
noteManuallyTTS_path = profile_data['noteManuallyTTS_path']
notesTTS_path = profile_data['notesTTS_path']
rhythmbox_client_ControllerTTS_path  = profile_data['rhythmbox_client_ControllerTTS_path']
weatherTTS_path = profile_data['weatherTTS_path']
youtubeTTS_path = profile_data['youtubeTTS_path']
FBloginTTS_path = profile_data['FBloginTTS_path']
Gcreate_accountTTS_path = profile_data['Gcreate_accountTTS_path']
GloginTTS_path = profile_data['GloginTTS_path']
twitterloginTTS_path = profile_data['twitterloginTTS_path']
AI_TTS_path = profile_data['AI_TTS_path']
PrimaryCredentialsTTS_path = profile_data['PrimaryCredentialsTTS_path']
appManagerTTS_path = profile_data['appManagerTTS_path']
infoSenderTTS_path = profile_data['infoSenderTTS_path']
systemTaskTTS_path = profile_data['systemTaskTTS_path']
updateSystemTTS_path = profile_data['updateSystemTTS_path']
volumeControllerTTS_path = profile_data['volumeControllerTTS_path']
