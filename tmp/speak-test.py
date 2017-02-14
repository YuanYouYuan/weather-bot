#from gtts import gTTS
import vlc

mp3_name = "hello.mp3"
#wav_name = "hello.wav"
#tts = gTTS(text='你好', lang='zh-TW')
#tts.save(mp3_name)

vlc.MediaPlayer("/home/circle/git-project/weather-bot/hello.mp3").play()



