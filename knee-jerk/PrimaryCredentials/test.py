import os, subprocess


directory = os.path.dirname(os.path.realpath(__file__))
print(directory)
conversationTTS1 = directory + '/SpeechDriver/ServicesTTS/conversationTTS/'

print(conversationTTS1)

#os.system('python3 '+ conversationTTS + 'milestone__tts.py')
subprocess.run(['gnome-terminal', '-x', 'python3', conversationTTS1, ' milestone__tts.py'])