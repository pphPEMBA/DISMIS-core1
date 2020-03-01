
    #volume

from os import system

from plugin import LINUX, MACOS, plugin, require


@require(platform=LINUX, native="pactl")
@plugin('increase volume')
def increase_volume__LINUX(jarvis, s):
    """Increases your speaker's sound."""
    system("pactl -- set-sink-volume 0 +3%")


@require(platform=MACOS, native="osascript")
@plugin('increase volume')
def increase_volume__MAC(jarvis, s):
    """Increases your speaker's sound."""
    system(
        'osascript -e "set volume output volume '
        '(output volume of (get volume settings) + 10) --100%"'
    )


@require(platform=LINUX, native="pactl")
@plugin('decrease volume')
def decrease_volume__LINUX(jarvis, s):
    """Decreases your speaker's sound."""
    system("pactl -- set-sink-volume 0 -10%")


@require(platform=MACOS, native="osascript")
@plugin('decrease volume')
def decrease_volume__MAC(jarvis, s):
    """Decreases your speaker's sound."""
    system(
        'osascript -e "set volume output volume '
        '(output volume of (get volume settings) - 10) --100%"'
    )


@require(platform=LINUX, native="pactl")
@plugin('mute')
def mute(jarvis, s):
    """Mute: Silence your speaker's sound."""
    system("pactl -- set-sink-mute 0 toggle")








import alsaaudio
import sys

m = alsaaudio.Mixer()
vol = m.getvolume()

def getVolume():
	global vol
	return vol[0]

def increase(n):
	global vol
	if (vol[0] + n)>100:
		vol[0]= 100 - n
	m.setvolume(vol[0] + n)
	vol = m.getvolume()
	print "Volume increased to " + str(vol[0]) + " percent"

def decrease(n):
	global vol
	if (vol[0] - n)>100:
		vol[0]= 100 + n
	m.setvolume(vol[0] - n)
	vol = m.getvolume()
	print "Volume decreased to " + str(vol[0]) + " percent"

def setVolume(n):
	global vol
	m.setvolume(n)
	vol = m.getvolume()	
	print "Volume set to " + str(vol[0]) + " percent"

if len(sys.argv) == 1 or sys.argv[1] == "g":
	print "Current volume is " + str(getVolume()) + " percent"

if len(sys.argv)>=3:
	if sys.argv[1] == "i":
		try:
			i = int(sys.argv[2])
			increase(i)
		except ValueError:
			print "Please specify a number after saying increase volume by"

	elif sys.argv[1] == "d":
		try:
			d = int(sys.argv[2])
			decrease(d)
		except:
			print "Please specify a number after saying decrease volume by"

	elif sys.argv[1] == "s":
		try:
			s = int(sys.argv[2])
			setVolume(s)
		except:
			print "Please specify a number after saying set volume to"
