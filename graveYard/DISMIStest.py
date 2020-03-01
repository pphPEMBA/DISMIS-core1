import requests
import os 

def open_camera__LINUX():
    """Jarvis will open the camera for you."""
    print("Opening cheese.......")
    os.system("cheese")

#open_camera__LINUX()






# -*- coding: utf-8 -*-
import json
import requests
from colorama import Fore


def main(city=0):
    send_url = (
        "http://api.openweathermap.org/data/2.5/forecast/daily?q={0}&cnt=1"
        "&APPID=ab6ec687d641ced80cc0c935f9dd8ac9&units=metric".format(city)
    )
    r = requests.get(send_url)
    j = json.loads(r.text)
    rain = j['list'][0]['weather'][0]['id']
    if rain >= 300 and rain <= 500:  # In case of drizzle or light rain
        print(
            Fore.CYAN
            + "It appears that you might need an umbrella today."
            + Fore.RESET)
    elif rain > 700:
        print(
            Fore.CYAN
            + "Good news! You can leave your umbrella at home for today!"
            + Fore.RESET)
    else:
        print(
            Fore.CYAN
            + "Uhh, bad luck! If you go outside, take your umbrella with you."
            + Fore.RESET)



# -*- coding: utf-8 -*-
import json
import webbrowser
import requests
from colorama import Fore

location = 0


def get_location():
    global location
    if not location:
        print("Getting Location ... ")
        send_url = 'http://api.ipstack.com/check?access_key=8f7b2ef26a8f5e88eb25ae02606284c2&output=json&legacy=1'
        r = requests.get(send_url)
        location = json.loads(r.text)
    return location


def directions(to_city, from_city=0):
    if not from_city:
        from_city = get_location()['city']
    url = "https://www.google.com/maps/dir/{0}/{1}".format(from_city, to_city)
    webbrowser.open(url)


def locate_me():
    hcity = get_location()['city']
    print(Fore.BLUE + "You are at " + hcity + Fore.RESET)


def weather(city=None):
    if not city:
        city = get_location()['city']

    # Checks country
    country = get_location()['country_name']

    # If country is US, shows weather in Fahrenheit
    if country == 'United States':
        send_url = (
            "http://api.openweathermap.org/data/2.5/weather?q={0}"
            "&APPID=ab6ec687d641ced80cc0c935f9dd8ac9&units=imperial".format(
                city)
        )
        unit = ' ºF in '

    # If country is not US, shows weather in Celsius
    else:
        send_url = (
            "http://api.openweathermap.org/data/2.5/weather?q={0}"
            "&APPID=ab6ec687d641ced80cc0c935f9dd8ac9&units=metric".format(
                city)
        )
        unit = ' ºC in '
    r = requests.get(send_url)
    j = json.loads(r.text)

    # check if the city entered is not found
    if 'message' in j and j['message'] == 'city not found':
        print(Fore.BLUE + "City Not Found" + Fore.RESET)
        return False

    else:
        temperature = j['main']['temp']
        description = j['weather'][0]['main']
        print("{COLOR}It's {TEMP}{UNIT}{CITY} ({DESCR}){COLOR_RESET}"
              .format(COLOR=Fore.BLUE, COLOR_RESET=Fore.RESET,
                      TEMP=temperature, UNIT=unit, CITY=city,
                      DESCR=description))

    return True


def search_near(things, city=0):
    if city:
        print("{COLOR}Hold on! I'll show {THINGS} near {CITY}{COLOR_RESET}"
              .format(COLOR=Fore.GREEN, COLOR_RESET=Fore.RESET,
                      THINGS=things, CITY=city))
    else:
        print("{COLOR}Hold on!, I'll show {THINGS} near you{COLOR_RESET}"
              .format(COLOR=Fore.GREEN, COLOR_RESET=Fore.RESET, THINGS=things))
        url = "https://www.google.com/maps/search/{0}/@{1},{2}".format(
            things, get_location()['latitude'], get_location()['longitude'])
    webbrowser.open(url)



from utilities.GeneralUtilities import wordIndex
import CmdInterpreter
from . import mapps


def main(data):
    word_list = data.split()
    try:
        things = " ".join(word_list[0:wordIndex(data, "|")])
    except ValueError:
        cmd = CmdInterpreter.CmdInterpreter("", "")
        cmd.help_near()
        return

    if " me" in data:
        city = 0
    else:
        word_list = data.split()
        city = " ".join(word_list[wordIndex(data, "|") + 1:])
        print(city)
    mapps.search_near(things, city)


