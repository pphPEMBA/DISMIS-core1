import subprocess

def volume_down():
    subprocess.call(['pactl', 'set-sink-volume', '0', '-15%'])

def volume_up():
    subprocess.call(['pactl', 'set-sink-volume', '0', '+15%'])
