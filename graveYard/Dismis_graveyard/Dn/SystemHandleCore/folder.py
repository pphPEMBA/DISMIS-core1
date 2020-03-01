from os import system
import subprocess
from SpeechDriver.SpeechDriver import speak

def folder():
    try:
        system('/shCMD/./folder.sh')
        print ("Successfully created the directory %s " % path)
        speak("Successfully created the directory %s " % path)
    except:
        print ("Creation of the directory %s failed" % path)
        speak('sorry sir, I\'m to create directory')


def arrange():
    subprocess.call("/shCMD/./sortfolder.sh")
