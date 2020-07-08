from gtts import gTTS
import speech_recognition as sr
import time
import random
import playsound
import webbrowser
import os
import subprocess

r = sr.Recognizer()

def record_audio(ask= False):
    with sr.Microphone() as source:
        if ask:
            speak(ask)
        audio = r.listen(source)
        voice_data = ''
        try:
            voice_data = r.recognize_google(audio)

        except sr.RequestError:
            print('going offline')

        except sr.UnknownValueError:
            print('i did not get that')

        print(voice_data)

        return voice_data.lower()


def speak(audio_string):
    tts = gTTS(text=audio_string,lang='en')
    r = random.randint(1,200)
    audio_file = 'audio' + str(r) + '.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    os.remove(audio_file)

def there_exists(terms):
    for term in terms:
        if term in voice_data:
            return True

def if_there(terms):
    for term in terms:
        if term in authenticate:
            return True

def service(authenticate):
    if if_there(['hai','hello','whatsup']):
        greetings = ["Hey Deepak","Hello, welcome back","Welcome come back Deepak"]
        greet = greetings[random.randint(0,len(greetings)-1)]
        speak(greet) 
           



time.sleep(1)
while(1):
    voice_data = record_audio()
    if there_exists([""]):
        print("activated...")
        authenticate = record_audio()
        service(authenticate)

    