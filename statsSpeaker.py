import os
from gtts import gTTS
import playsound


def speak():
    with open('speech.txt') as file:
        speech = file.read().replace('\n', '')
    tts = gTTS(text=speech)
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)
    os.remove(filename)


speak()
