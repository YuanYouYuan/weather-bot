# This version is for windows, and there must be a mpv application in this work directory

import forecastio
from gtts import gTTS
import subprocess

api_key = 'Enter your api key'

# the following coordinate is Taipei/Taiwan
lat = 25.0391667
lng =  121.525
lang = 'zh-TW'
file_name = 'weather.mp3'
player = './mpv'

forecast = forecastio.load_forecast(api_key, lat, lng)

by_hour = forecast.hourly()

for data in by_hour.data:
    text = '在' + str(data.time) + '氣溫是' +  str(data.temperature) + '度西'
    print(text)
    tts = gTTS(text, lang)
    tts.save(file_name)
    subprocess.call([player, file_name])
    

