from selenium import webdriver

def browserWindow():
    url = 'https://www.facebook.com/'
    driver = webdriver.Chrome(executable_path="/home/pemba/d1_SuperDismis/Dismis-HA_GUI/SystemService/Chrome_webdriver/chromedriver_linux64/chromedriver")
    driver.get(url)
    while True:
        entry = input('what do you want to do now: ')
        if 'maximize' == entry:
            driver.maximize_window()
        if 'minimize' == entry:
            driver.minimize_window()

browserWindow()

