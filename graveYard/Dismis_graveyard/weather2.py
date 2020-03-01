import json
import time
import urllib.request

def get_weather():
    api = "Gcb772BLcKh5mNcBv40hifgHekwSVlg9"
    location_id = 244306
    url = 'http://dataservice.accuweather.com/currentconditions/v1/%s?apikey=%s&details=true' % (location_id, api)
    print(url)
    with urllib.request.urlopen(url) as url:
        data = json.loads(url.read().decode())
    print(data)
    return (data[0]['Temperature']['Imperial']['Value'],
            data[0]['RelativeHumidity'],
            data[0]['Wind']['Direction']['Degrees'],
            data[0]['Wind']['Speed']['Imperial']['Value'],
            data[0]['UVIndex'],
            data[0]['CloudCover'],
            data[0]['Pressure']['Metric']['Value'],
            data[0]['Precip1hr']['Metric']['Value'],
            data)


timestamp = time.time()

temperature, humidity, wind_bearing, wind_speed, uv_index, cloud_cover, pressure, precipitation, raw \
    = get_weather()

