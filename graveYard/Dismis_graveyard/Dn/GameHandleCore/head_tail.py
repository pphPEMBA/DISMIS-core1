import random
import time

def coin_flip(voice_text):
    speak('what do you like to choose')
    time.sleep(1)
    coin=["tails","heads"]
    print("its "+random.choice(coin))
    