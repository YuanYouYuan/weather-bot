#!/usr/bin/python
import speech_recognition as sr
import forecastio


api_key = "c7899699f9263f3140bb1b15c3fbba84"

lang = 'zh-TW'

r = sr.Recognizer(lang)
with sr.Microphone(device_index) as source:
    print("Say something!")
    audio = r.listen(source)

try:
    text = r.recognize_google(audio)
    print("Google Speech Recognition thinks you said " + text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

for t in text:
    if t == '北':
        lat = 25.105497
        lng = 121.597366
    elif t == '南':
        lat = 22.5935
        lng = 120.1213
    else:
        pass





