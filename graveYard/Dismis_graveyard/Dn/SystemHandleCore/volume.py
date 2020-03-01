import alsaaudio
import sys

m = alsaaudio.Mixer()
vol = m.getvolume()

def getVolume():
	global vol
	return vol[0]


def increase(voice_text):
	global vol
	if (vol[0] + voice_text)>100:
		vol[0]= 100 - voice_text
	m.setvolume(vol[0] + voice_text)
	vol = m.getvolume()
	print("Volume increased to " + str(vol[0]) + " percent")

def decrease(voice_text):
	global vol
	if (vol[0] - voice_text)>100:
		vol[0]= 100 + voice_text
	m.setvolume(vol[0] - voice_text)
	vol = m.getvolume()
	print("Volume decreased to " + str(vol[0]) + " percent")

def setVolume(voice_text):
	global vol
	m.setvolume(voice_text)
	vol = m.getvolume()	
	print("Volume set to " + str(vol[0]) + " percent")

#if len(sys.argv) == 1 or sys.argv[1] == "g":
	#print("Current volume is " + str(getVolume()) + " percent")

