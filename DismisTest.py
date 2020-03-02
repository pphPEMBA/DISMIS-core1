
def incognitoMode():
    global chromedriverPath
    global driver

    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")

    driver = webdriver.Chrome(chromedriverPath, chrome_options=chrome_options)



    #Internet Commands
    elif "incognito" == command or "incognito mode" == command:
        incognitoMode()
    elif "click" in command:
        try:
            link = driver.find_element_by_link_text(command[5:].strip().upper())
            link.click()
        except Exception as e:
            print(e)

        try:
            link = driver.find_element_by_link_text(command[5:].strip().lower())
            link.click()
        except Exception as e:
            print(e)

        try:
            link = driver.find_element_by_link_text(command[5:].strip().capitalize())
            link.click()
        except Exception as e:
            print(e)

        try:
            clickHref(command[5:])
        except Exception as e:
            print(e)

    elif command == "go back":
        driver.back()
    elif command == "go forward":
        driver.forward()
    elif "refresh" in command:
        driver.refresh()
    elif command == "scroll down":
        try:
            driver.execute_script("window.scrollTo(0, " + scroll + ");")
        except Exception as e:
            print(e)
        scroll_num += 370
        scroll = str(scroll_num)
    elif command == "scroll up":
        if scroll_num > 370:
            scroll_num -= 370
            scroll = str(scroll_num)
        try:
            print("window.scrollTo(0, " + scroll + ");")
            driver.execute_script("window.scrollTo(0, " + scroll + ");")
        except Exception as e:
            print(e)

    elif command == "minimize window":
        try:
            driver.set_window_position(-10000, 0)
        except:
            pass
    elif command == "maximize window":
        try:
            driver.maximize_window()
        except:
            pass