from selenium import webdriver


def YouTubeCommands():
    url = 'https://www.youtube.com/watch?v=3AyMjyHu1bA'
    driver = webdriver.Chrome(executable_path='/home/d-slave1/d1_SuperDismis/DISMIS-core/SystemService/DisArcade/Chrome_webdriver/chromedriver_linux64/chromedriver')
    driver.get(url)
    command = input('commds: ')
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