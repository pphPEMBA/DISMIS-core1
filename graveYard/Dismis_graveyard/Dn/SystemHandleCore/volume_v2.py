from os import system


def increase_volume():
    """Increases your speaker's sound."""
    system("pactl -- set-sink-volume 0 +3%")

def decrease_volume():
    """Decreases your speaker's sound."""
    system("pactl -- set-sink-volume 0 -10%")

def mute():
    """Mute: Silence your speaker's sound."""
    system("pactl -- set-sink-mute 0 toggle")

