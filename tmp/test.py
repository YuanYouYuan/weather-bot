#!/usr/bin/python
import speech_recognition as sr

# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone(sample_rate=44100) as source:
    print("Say something!")
    audio = r.listen(source)
text = r.recognize_google(audio)
print(text)
