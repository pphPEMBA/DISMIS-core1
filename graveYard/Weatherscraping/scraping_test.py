from bs4 import BeautifulSoup
import requests
import pandas


page = requests.get('https://forecast.weather.gov/MapClick.php?lat=34.09979000000004&lon=-118.32721499999997#.XmCJyHUzbeQ')
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup)

week = soup.find(id="seven-day-forecast-body")
#print(week)

items = soup.find_all(class_="tombstone-container")
#print(item)
#print(items[0].find(class_="period-name").get_text())
#print(items[0].find(class_="short-desc").get_text())
#print(items[0].find(class_="temp").get_text())

#print(items[1].find(class_="period-name").get_text())
#print(items[1].find(class_="short-desc").get_text())
#print(items[1].find(class_="temp").get_text())

#print(items[2].find(class_="period-name").get_text())
#print(items[2].find(class_="short-desc").get_text())
#print(items[2].find(class_="temp").get_text())

#print(items[3].find(class_="period-name").get_text())
#print(items[3].find(class_="short-desc").get_text())
#print(items[3].find(class_="temp").get_text())

#print(items[4].find(class_="period-name").get_text())
#print(items[4].find(class_="short-desc").get_text())
#print(items[4].find(class_="temp").get_text())

#print(items[5].find(class_="period-name").get_text())
#print(items[5].find(class_="short-desc").get_text())
#print(items[5].find(class_="temp").get_text())

#print(items[6].find(class_="period-name").get_text())
#print(items[6].find(class_="short-desc").get_text())
#print(items[6].find(class_="temp").get_text())

#print(items[7].find(class_="period-name").get_text())
#print(items[7].find(class_="short-desc").get_text())
#print(items[7].find(class_="temp").get_text())

#print(items[8].find(class_="period-name").get_text())
#print(items[8].find(class_="short-desc").get_text())
#print(items[8].find(class_="temp").get_text())


period_name = [item.find(class_='period-name').get_text() for item in items]
description = [item.find(class_='short-desc').get_text() for item in items]
temperature = [item.find(class_='temp').get_text() for item in items]

#print(period_name)
#print(description)
#print(temperature)

weatherstuff = pandas.DataFrame(
    {'period': period_name,
    'short_description': description,
    'temperature': temperature,
    }
)
#print(weatherstuff)

weatherstuff.to_csv('weather.csv')