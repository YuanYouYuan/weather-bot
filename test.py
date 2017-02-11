import time
from pygame import mixer # Load the required library

mixer.init()
mixer.music.load("/home/circle/git-project/weather-bot/hello.mp3")
mixer.music.play()

time.sleep(3)
