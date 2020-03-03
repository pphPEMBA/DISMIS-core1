import urllib.request
import urllib.parse  # for Youtube
from urllib import request
from urllib.parse import quote, urlencode, parse_qsl, unquote
from urllib.request import urlop
from pytube import YouTube  # for downloading YouTube videos
import os
import re
from selenium import webdriver

# Setting up the Chrome Selenium Webdriver and getting PATHs setup for easy access later with "global"
currentDirectory = os.path.dirname(__file__)
print(currentDirectory)
soundDirectory = currentDirectory + r"/trash//"
chromedriverPath = "/home/d-slave1/d1_SuperDismis/DISMIS-core/SystemService/DisArcade/Chrome_webdriver/chromedriver_linux64/chromedriver"

# -------------------------------------YouTube and its commands-------------------------------
def youtube(command):
    youtube_open = True

    # If it's youtube instead of play
    vid = command
    if "youtube" == command[0:7]:
        vid = vid[7:]
    try:
        vid_search = vid

        query_string = urllib.parse.urlencode({"search_query": vid_search})
        html_content = urllib.request.urlopen(
            "http://www.youtube.com/results?" + query_string)
        search_results = re.findall(
            r'href=\"\/watch\?v=(.{11})', html_content.read().decode())

        top_result = "http://www.youtube.com/watch?v=" + search_results[0]
        youtube_tab = top_result
        driver = webdriver.Chrome(chromedriverPath)
        driver.get(youtube_tab)

        youtubeLinkFile = currentDirectory + "\scripts"

        with open(os.path.join(youtubeLinkFile, "youtube_link.txt"), "w") as write_tab:
            write_tab.write(youtube_tab)

    except Exception as e:
        print(e)
        # os.startfile("error.mp3")


def YouTubeToMp3():
    musicdownloader_path = currentDirectory + "\scripts\musicdownloader.py"
    os.system("python " + musicdownloader_path)


def downloadYouTube(url):
    try:
        desktop_path = str(os.path.join(os.environ['HOMEPATH'], 'Desktop'))
        # print(desktop_path)
        yt = YouTube(url.strip())
        print("SECOND STEP")
        yt.streams.first().download("C:" + desktop_path)

    except:
        print("Download failed. Check the link or try another link.")


def YouTubeCommands():
    global driver

    commmand = input('commds: ')
    print("IN YOUTUBE COMMANDS")
    if command == "full screen":
        try:
            classname = 'button.ytp-fullscreen-button'
            button = driver.find_element_by_css_selector(classname).click()
        except Exception as e:
            print(e)
    elif command == "play" or command == "pause":
        try:
            classname = 'button.ytp-play-button'
            button = driver.find_element_by_css_selector(classname).click()
        except Exception as e:
            print(e)
    elif command == "skip" or command == "skip video":
        try:
            element = driver.find_element_by_css_selector("a.ytp-next-button")
            element.click()
        except Exception as f:
            print(f)
    elif "search youtube" == command[14:] or "youtube search" == command[14:]:
        try:
            element = driver.find_element_by_id("search")
            element.send_keys(command[14:])
            element.send_keys(u'\ue007')
        except Exception as f0:
            print(f0)

YouTubeCommands()