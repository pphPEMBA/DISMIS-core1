# Python3 program for reverse geocoding. 
  
# importing necessary libraries 
import reverse_geocoder as rg 
import pprint 
from SpeechDriver.SpeechDriver import speak

def reverseGeocode(): 
    latitude = input("enter latitude: ")
    logitute = input("enter logitute: ")
    coordinates =(latitude, logitute)
    result = rg.search(coordinates) 
    speak('latitude and logitute is set boss')
    # result is a list containing ordered dictionary. 
    pprint.pprint(result)
    speak(result)
  
