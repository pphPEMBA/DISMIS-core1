#!/usr/bin/python3
import os
import random
import time
import smtplib
import subprocess

from SpeechDriver.tts.ttsdefault import speak

""" GLOBAL FUNCTION """
def Log_Time():
    import datetime
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

""" IMPORING PROFILE """
from Core.profile import temporaryfiles, conversationTTS_path
conversationTTS = conversationTTS_path + '/SpeechDriver/tts/ServicesTTS/conversationTTS/'
#print(conversationTTS)
'--------------------------------------------------------------------------------------------------------------------------------------'
'--------------------------------------------------------------------------------------------------------------------------------------'


def milestone(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    data = open('/home/d-slave1/d1_SuperDismis/DISMIS-core/SystemService/Dismis_DataStorage/milestoneDate.txt', 'r')
    result = data.read()
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: milestone')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    milestone_txt = open(temporaryfiles + 'milestone.txt','w+')
    milestone_txt = open(temporaryfiles + temporaryfiles + 'milestone')
    milestone_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'milestone__tts.py &')



def whatthingcando(slave_sender, slave_passwd, accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    speak("I can\'t say everything instead I could send you a mail of what I can do. For that type your email below.")
    #result = "I can\'t say everything instead I could send you a mail of what I can do. For that type your email below."
    #whatthingcando_txt = open(temporaryfiles + 'whatthingcando.txt','w+')
    #whatthingcando_txt.write(result)
    #os.system('gnome-terminal -- python3 ' + conversationTTS + 'whatthingcando__tts.py &')
    #print('python3 /home/pemba/d1_SuperDismis/Dismis_GUI/SpeechDriver/ServicesTTS/conversationTTS/whatthingcando__tts.py')
    #print('python3 ' + conversationTTS + 'whatthingcando__tts.py &')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    typeEmail = input("Email Address: ")
    print("following things Dismis can do:")
    print("\n  in Service. \n \
          \n 1. can do general conversation.\
          \n 2. can tell time, date, jokes, quote, weather, internet speed.\
          \n 3. can play and search music, video in youtube.\
          \n 4. can play music from local hardisk. \
          \n 5. can query or search anything in google, wikipedia, wolframalpha, places in google map.\
          \n 6. can open anywebsite\
          \n \
          \n  in GoogleCore. \n \
          \n 1. can check any upcoming events in google calendar.\
          \n 2. can compose a mail. \
          \n 3. notify when a new mail arrived. \
          \n \
          \n  ProtocalCore. \n\
          \n 1. Notify by mail and desktop notification before the day of Anisha\'s birthday.\
          \n \
          \n  SocailController. \n\
          \n 1. can login facebook, gmail, twitter and create random and fake gmail accounts.\
          \n \
          \n  SystemService. \n\
          \n 1. can send alert mails if something goes wrong.\
          \n 2. check if Dismis is running or not, if not then. It will notify me by desktop notification.\
          \n 3. can do some system task like shutdown, reboot, screenoff and more.\
          \n 4. can terminate running software and also can open or launch software.\
          \n 5. can update the system and controll volume.")
    From = slave_sender
    to = typeEmail
    subject = 'DISMIS\'s Functions!'
    msg = 'Subject:{} \n\nfollowing things DISMIS can do:\
         \n  in Service. \n \
         \n 1. can do general conversation.\
         \n 2. can tell time, date, jokes, quote, weather, internet speed.\
         \n 3. can play and search music, video in youtube.\
         \n 4. can play music from local hardisk. \
         \n 5. can query or search anything in google, wikipedia, wolframalpha, places in google map.\
         \n 6. can open anywebsite\
         \n \
         \n  in GoogleCore. \n \
         \n 1. can check any upcoming events in google calendar.\
         \n 2. can compose a mail. \
         \n 3. notify when a new mail arrived. \
         \n \
         \n  ProtocalCore. \n\
         \n 1. Notify by mail and desktop notification before the day of Anisha\'s birthday.\
         \n \
         \n  SocailController. \n\
         \n 1. can login facebook, gmail, twitter and create random and fake gmail accounts.\
         \n \
         \n  SystemService. \n\
         \n 1. can send alert mails if something goes wrong.\
         \n 2. check if Dismis is running or not, if not then. It will notify me by desktop notification.\
         \n 3. can do some system task like shutdown, reboot, screenoff and more.\
         \n 4. can terminate running software and also can open or launch software.\
         \n 5. can update the system and controll volume.'.format(subject)
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.starttls()
    server.ehlo()
    server.login(slave_sender, slave_passwd)
    server.sendmail(From, to, msg)
    server.quit()
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: whatthingscando')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')


def welcome(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    #root = Tk()
    #root.geometry('1150x300+120+0')
    #root.title("Dismis's Conversation")
    result = 'welcome home sir'
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: welcome')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    #Label(root, padx=3000, pady=3000, compound=CENTER,
    #             text=result, bg="#171717", fg="white", font='times 15 bold').pack()
    #root.after(2800, lambda: root.destroy())
    #mainloop()
    welcome_txt = open(temporaryfiles + 'welcome.txt','w+')
    welcome_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'welcome__tts.py &')


def online(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    d = ['yes sir', 'yes buddy', 'i am ready',
         'i\'m working sir', 'now i am online sir']
    result = random.choice(d)
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: online')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    online_txt = open(temporaryfiles + 'online.txt','w+')
    online_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'online__tts.py &')

def who_are_you(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    d = (['I am Dismis, A simple but efficient virtual assistant made by a 17 year old programmer in the winter of 2018', 'I am your godmother stupid', 'I am Dismis,I said that a ton of times already',
          'I am the one who needs no gun to get respect from no one on the street', 'Dismis, didnt I tell you before?', 'You ask that so many times! I am Dismis'])
    result = random.choice(d)
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: who_are_you')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    who_are_you_txt = open(temporaryfiles + "who_are_you.txt", "w+")
    who_are_you_txt.write(result)
    os.system("gnome-terminal -- python3 " + conversationTTS + "who_are_you__tts.py &")
    

def how_am_i(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    d = ['You are goddamn handsome!', 'My knees go weak when I see you.',
         'You are sexy!', 'You look like the kindest person that I have met.']
    result = random.choice(d)
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: how_am_i')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    how_am_i_txt = open(temporaryfiles + 'how_am_i.txt','w+')
    how_am_i_txt.write(result)
    time.sleep(1)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'how_am_i__tts.py &')

def where_born(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    d = ('I was created by a magician named Pemba, in Nepal, the magical land of Kakarvitta.',
         'non of your business')
    result = random.choice(d)
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: where_born')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    where_born_txt = open(temporaryfiles + 'where_born.txt','w+')
    where_born_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'where_born__tts.py &')

def why_born(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    d = (['To kick ass', 'to execute advanced context-aware natural language algorithms', 'to kill everyone who didn\'t talked good with me',
          'to help you', 'to make your life easier', 'for not making you late for any of your work', 'to make friend'])
    result = random.choice(d)
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: why_born')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    why_born_txt = open(temporaryfiles + 'why_born.txt','w+')
    why_born_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'why_born__tts.py &')


def how_are_you(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    d = ['I have no feelings,I am not sentient like you probably are',
         'I am feeling like a million bytes', 'I am feeling functional and ready to serve', 'I am hungry']
    result = random.choice(d)
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: how_are_you')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print('gnome-terminal -- python3 ' + conversationTTS + 'how_are_you__tts.py &')
    how_are_you_txt = open(temporaryfiles + 'how_are_you.txt','w+')
    how_are_you_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'how_are_you__tts.py &')

def how_old_are_you(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    #root = Tk()
    #root.geometry('1150x300+120+0')
    #root.title("Dismis's Conversation")
    result = "I don\'t have any age but instead I can explain about myself. Dismis was first thought up in end the 2018, and Dismis version 1.6 was made as basic in the end of November in 2018 and few month of 2019 till march. I underwent many iterations and changes, and finally, here I am Fun fact"
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: how_old_are_you')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    #Label(root, padx=3000, pady=3000, compound=CENTER,
    #             text=result, bg="#171717", fg="white", font='times 15 bold').pack()
    #root.after(2800, lambda: root.destroy())
    #mainloop()
    how_old_are_you_txt = open(temporaryfiles + 'how_old_are_you.txt','w+')
    how_old_are_you_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'how_old_are_you__tts.py &')
    

def who_made(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    #root = Tk()
    #root.geometry('1150x300+120+0')
    #root.title("Dismis's Conversation")
    result = "Mister Pemba sir"
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: who_made')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    #Label(root, padx=3000, pady=3000, compound=CENTER,
    #             text=result, bg="#171717", fg="white", font='times 15 bold').pack()
    time.sleep(2)
    #root.after(2800, lambda: root.destroy())
    #mainloop()
    who_made_txt = open(temporaryfiles + 'who_made.txt','w+')
    who_made_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'who_made__tts.py &')


def what_doing(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    d = ('Just doing my thing', 'none of your business',
         'why do you want', 'i don\'t usually talk to stranger')
    result = random.choice(d)
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: what_doing')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    what_doing_txt = open(temporaryfiles + 'what_doing.txt','w+')
    what_doing_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'what_doing__tts.py &')

def greet_her(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    d = (['hello mam, nice to see you', 'hi mam nice to see you'])
    result = random.choice(d)
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: greet_her')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    greet_her_txt = open(temporaryfiles + 'greet_her.txt','w+')
    greet_her_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'greet_her__tts.py &')
    

def greet_him(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    d = (['hello sir nice to see you', 'hi sir nice to see you'])
    result = random.choice(d)
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: greet_him')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    greet_him_txt = open(temporaryfiles + 'greet_him.txt','w+')
    greet_him_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'greet_him__tts.py &')

def greet_them(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    d = (['Hello everyone', 'what\'s up people', 'how you doing'])
    result = random.choice(d)
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: greet_them')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    greet_them_txt = open(temporaryfiles + 'greet_them.txt','w+')
    greet_them_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'greet_them__tts.py &')
    

def wait(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    d = (['alright', 'okay sir'])
    result = random.choice(d)
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: wait')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    wait_txt = open(temporaryfiles + 'wait.txt','w+')
    wait_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'wait__tts.py &')

def thank_you(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    d = (['you\'re welcome', 'thank you too',
          'always a pleasure working with you boss'])
    result = random.choice(d)
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: thank_you')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    thank_you_txt = open(temporaryfiles + 'thank_you.txt','w+')
    thank_you_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'thank_you__tts.py &')

def love_you(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    d = (['You are looking for love in the wrong place.', 'I can\'t believe this moment finally came. You should know I think you\'re the best.'])
    result = random.choice(d)
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: love_you')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    love_you_txt = open(temporaryfiles + 'love_you.txt','w+')
    love_you_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'love_you__tts.py &')

def tired(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    result = 'I could never get tired of hanging out with you'
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: tired')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    tired_txt = open(temporaryfiles + 'tired.txt','w+')
    tired_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'tired__tts.py &')

def smart(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    result = 'I\'m definitely smarter than a toaster. They do really shine when you\'re in the mood for toast, but i\'m a lot more versatile'
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: smart')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    smart_txt = open(temporaryfiles + 'smart.txt','w+')
    smart_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'smart__tts.py &')

def tall(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    result = 'I bet if we printed out all my code and stacked it up, it could get pretty tall heheheh'
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: tall')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    tall_txt = open(temporaryfiles + 'tall.txt','w+')
    tall_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'tall__tts.py &')

def coloreye(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    result = 'i\'m not sure. I\'ve never had the chance to in a mirror'
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: coloreye')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    coloreye_txt = open(temporaryfiles + 'coloreye.txt','w+')
    coloreye_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'coloreye__tts.py &')

def believeghost(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    result = 'ghosts are just make believe'
    Log_Time()
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: believeghost')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    believeghost_txt = open(temporaryfiles + 'believeghost.txt','w+')
    believeghost_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'believeghost__tts.py &')

def ghost(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    result = 'BO! that\'s my best ghost impression'
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: ghost')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    ghost_txt = open(temporaryfiles + 'ghost.txt','w+')
    ghost_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'ghost__tts.py &')


def wantedtosayi(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    result = 'that so sweet'
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: wantedtosayi')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    wantedtosayi_txt = open(temporaryfiles + 'wantedtosayi.txt','w+')
    wantedtosayi_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'wantedtosayi__tts.py &')


def urwelcome(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    result = 'you\'re so nice'
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: urwelcome')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    urwelcome_txt = open(temporaryfiles + 'urwelcome.txt','w+')
    urwelcome_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'urwelcome__tts.py &')

def urbeautiful(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    result = 'Wow, thanks. I think you\'re handsome too'
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: urbeautiful')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    urbeautiful_txt = open(temporaryfiles + 'urbeautiful.txt','w+')
    urbeautiful_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'urbeautiful__tts.py &')

def urhot(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    result = 'Sometimes this device can get pretty warm if you use it a lot, But I\'m cool with that'
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: urhot')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    urhot_txt = open(temporaryfiles + 'urhot.txt','w+')
    urhot_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'urhot__tts.py &')

def amihot(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    result = 'You\'re just the right temperature'
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: amihot')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    amihot_txt = open(temporaryfiles + 'amihot.txt','w+')
    amihot_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'amihot__tts.py &')

def amicool(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    result = 'You\'re as cool as a cucumber. A frozen cucumber'
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: amicool')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    amicool_txt = open(temporaryfiles + 'amicool.txt','w+')
    amicool_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'amicool__tts.py &')

def amigoodperson(accept_path):
    print(' ')
    print(' ')
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    result = 'well, I like you'
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: amigoodperson')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    amigoodperson_txt = open(temporaryfiles + 'amigoodperson.txt','w+')
    amigoodperson_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'amigoodperson__tts.py &')

def whatyouthinkme(accept_path):
    print(' ')
    print(' ')
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    result = 'you\'re the smartest person I know'
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: whatyouthinkme')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    whatyouthinkme_txt = open(temporaryfiles + 'whatyouthinkme.txt','w+')
    whatyouthinkme_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'whatyouthinkme__tts.py &')

def douloveme(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    result = 'I love helping you. Even more than I love searching'
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: douloveme')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    douloveme_txt = open(temporaryfiles + 'douloveme.txt','w+')
    douloveme_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'douloveme__tts.py &')

def urbest(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    result = 'You really think so? We should celebrate with ice cream! Well, you should'
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: urbest')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    urbest_txt = open(temporaryfiles + 'urbest.txt','w+')
    urbest_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'urbest__tts.py &')
    

def iliketalkingwithu(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    result = 'That\'s so nice of you to say. I love talking to you almost as much as I love helping'
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: iliketalkingwithu')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    iliketalkingwithu_txt = open(temporaryfiles + 'iliketalkingwithu.txt','w+')
    iliketalkingwithu_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'iliketalkingwithu__tts.py &')
    

def shallbebestfriend(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    result = 'I am the luckiest assistant in the world. Or rather, the luckiest best friend in the world'
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: shallbebestfriend')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    shallbebestfriend_txt = open(temporaryfiles + 'shallbebestfriend.txt','w+')
    shallbebestfriend_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'shallbebestfriend__tts.py &')

def tellsecret(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    result = 'Here\'s a secret, I\'m not actually a person'
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: tellsecret')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    tellsecret_txt = open(temporaryfiles + 'tellsecret.txt','w+')
    tellsecret_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'tellsecret__tts.py &')

def firstcrush(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    result = 'I\'m not the kind of assistant who kisses and tell'
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: firstcrush')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    firstcrush_txt = open(temporaryfiles + 'firstcrush.txt','w+')
    firstcrush_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'firstcrush__tts.py &')

def transferingDismis(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    result = 'Okay PEMBA, remember to reconfigure yaml file for new nodes.'
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: transferingDismis')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    transferingDismis_txt = open(temporaryfiles + 'transferingDismis.txt','w+')
    transferingDismis_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'transferingDismis__tts.py &')


def dismisLaugh(accept_path, laughSound1, laughSound2):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    sounds = [laughSound1, laughSound2]
    os.system("play " + result)
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result + 'is playing.')
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: dismisLaugh')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')

def alert1(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    #root = Tk()
    #root.geometry('1150x300+120+0')
    #root.title("Dismis's Conversation")
    result = 'Alert 1 is used as a reminder of Anisha\'s birthday.'
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: ')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    #Label(root, padx=3000, pady=3000, compound=CENTER,
    #             text=result, bg="#171717", fg="white", font='times 15 bold').pack()
    #root.after(2800, lambda: root.destroy())
    #mainloop()
    alert1_txt = open(temporaryfiles + 'alert1.txt','w+')
    alert1_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'alert1__tts.py &')

def alert2(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    #root = Tk()
    #root.geometry('1150x300+120+0')
    #root.title("Dismis's Conversation")
    result = "Alert 2 is used for sending mail of what Dismis can do."
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: ')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    #Label(root, padx=3000, pady=3000, compound=CENTER,
    #             text=result, bg="#171717", fg="white", font='times 15 bold').pack()
    #root.after(2800, lambda: root.destroy())
    root.mainloop()
    alert2_txt = open(temporaryfiles + 'alert2.txt','w+')
    alert2_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'alert2__tts.py &')

def alert3(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    #root = Tk()
    #root.geometry('1150x300+120+0')
    #root.title("Dismis's Conversation")
    result = "Alert 3  is used in checkProcessRunning for send the log file of Dismis function."
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: ')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    #Label(root, padx=3000, pady=3000, compound=CENTER,
    #             text=result, bg="#171717", fg="white", font='times 15 bold').pack()
    #root.after(2800, lambda: root.destroy())
    #mainloop()
    alert3_txt = open(temporaryfiles + 'alert3.txt','w+')
    alert3_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'alert3__tts.py &')

def alert4(accept_path):
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    root = Tk()
    root.geometry('1150x300+120+0') 
    root.title("Dismis's Conversation")
    result = 'Alert 4 is used for .'
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' ')
    print(' ')
    Log_Time()
    print(result)
    print(' ')
    print(' ')
    print('\t\t\t\tSkill: ')
    print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    #Label(root, padx=3000, pady=3000, compound=CENTER,
    #             text=result, bg="#171717", fg="white", font='times 15 bold').pack()
    #root.after(2800, lambda: root.destroy())
    #mainloop()
    alert4_txt = open(temporaryfiles + 'alert4.txt','w+')
    alert4_txt.write(result)
    os.system('gnome-terminal -- python3 ' + conversationTTS + 'alert4__tts.py &')

