import subprocess
import os, time
from SpeechDriver.tts.ttsdefault import speak


""" GLOBAL FUNCTION """
def Log_Time():
    import datetime
    now = datetime.datetime.now()
    print(now.strftime("%Y-%m-%d %H:%M:%S"))

""" IMPORING PROFILE """
from Core.profile import temporaryfiles, noteManuallyTTS_path
noteManuallyTTS = noteManuallyTTS_path + '/SpeechDriver/tts/ServicesTTS/noteManuallyTTS/'
#print(noteManuallyTTS)
'--------------------------------------------------------------------------------------------------------------------------------------'
'--------------------------------------------------------------------------------------------------------------------------------------'


def note_manually(accept_path, noteManually_txt):
    ''' Opens 'noteManually.txt' using gedit to let users to set the appointments manually.
    Also displays the previous appointments. '''
    os.system('aplay ' + accept_path +' &')
    try:
        result = 'Opening gedit, PEMBA remember that you\'ve to save it manually'
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        print(' ')
        print(' ')
        Log_Time()
        print(result)
        print(' ')
        print(' ')
        print('\t\t\t\tSkill: note_manually')
        print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
        note_manually_txt = open(temporaryfiles + 'note_manually.txt','w+')
        note_manually_txt.write(result)
        note_manually_txt.close()
        os.system('gnome-terminal -- python3 ' + noteManuallyTTS + 'note_manually__tts.py &')
        time.sleep(3)
        proc = subprocess.Popen(['gedit', noteManually_txt])
        proc.wait()
    except:
        DisError = 'System Failure! Unable to perform ( note manually ) skill sir'
        print('****************************************************************')
        print(' ')
        Log_Time()
        print('***' + DisError + '***')
        print(' ')
        print('****************************************************************')
        speak(DisError)
    

def readNote_manually(accept_path, noteManually_txt):
    ''' Reads the appointments line by line from noteManually.txt '''
    os.system('aplay ' + accept_path +' &')
    time.sleep(1)
    try:
        if(os.stat(noteManually_txt).st_size == 0):
            tts1 = "You don't have any notes."
            print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            print(' ')
            print(' ')
            Log_Time()
            print(tts1)
            print(' ')
            print(' ')
            print('\t\t\t\tSkill: readNote_manually')
            print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            readNoteManually_txt = open(temporaryfiles + 'readNote_manually.txt','w+')
            readNoteManually_txt.write(tts1)
            os.system('gnome-terminal -- python3 ' + noteManuallyTTS + 'readNote_manually__tts.py &')
            print(noteManuallyTTS)
        else:
            with open(noteManually_txt) as f:
                no_of_tasks = sum(1 for _ in f)
                tts2 = "You have "+str(no_of_tasks) + " notes."
                print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
                print(' ')
                print(' ')
                Log_Time()
                print("You have "+str(no_of_tasks) + " notes.")
                readNoteManually_txt = open(temporaryfiles + 'readNote_manually.txt','w+')
                readNoteManually_txt.write(tts2)
                readNoteManually_txt.close()
                os.system('gnome-terminal -- python3 ' + noteManuallyTTS + 'readNote_manually__tts.py &')
                time.sleep(2)
            readNoteManually_txt = open(noteManually_txt, "r")
            result = readNoteManually_txt.read()
            print(result)
            print(' ')
            print(' ')
            print('\t\t\t\tSkill: readNote_manually')
            print('--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------')
            readNoteManually_txt = open(temporaryfiles + 'readNote_manually.txt','w+')
            readNoteManually_txt.write(result)
            os.system('gnome-terminal -- python3 ' + noteManuallyTTS + 'readNote_manually__tts.py &')
    except:
        DisError = 'System Failure! Unable to perform ( read note manually ) skill sir'
        print('****************************************************************')
        print(' ')
        Log_Time()
        print('***' + DisError + '***')
        print(' ')
        print('****************************************************************')
        speak(DisError)
