
from datetime import datetime 
from SpeechDriver.SpeechDriver import speak

def date():
    now = datetime.now()
    print(now.strftime("%d %b %Y %A"))
    speak(now.strftime("%d %b %Y %A"))

def time():
    now = datetime.now()
    print(now.strftime("%I:%M:%S %A"))
    speak(now.strftime("%I:%M:%S %A"))

def countdown():
    while True:
        uin = input(">> ")
        try:
            when_to_stop = abs(int(uin))
        except:
            print('Not a number!')

        while when_to_stop > 0:
            m, s = divmod(when_to_stop, 60)
            h, m = divmod(m, 60)
            time_left = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
            print(time_left + "\r", end="")
        time.sleep(1)
            when_to_stop -= 1
 
def countdown2():
    # countdown.py - A simple countdown script.
    import time, subprocess
    timeLeft = 10
    while timeLeft > 0:

        print(timeLeft, end=' ')
    time.sleep(1)
        timeLeft = timeLeft - 1
    print('end')

