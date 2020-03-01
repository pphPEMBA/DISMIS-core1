import random  # random is a python built-in module
from SpeechDriver.SpeechDriver import speak

def roll_dice():
    dice_side = random.randrange(1, 7)
    speak(dice_side)
    print(dice_side)

