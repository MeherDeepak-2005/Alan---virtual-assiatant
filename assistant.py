from gtts import gTTS
import speech_recognition as sr
import time
import random
import playsound
import webbrowser
import os
import subprocess
import datetime

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




def shutdown():
    subprocess.call(['osascript', '-e',
'tell app "System Events" to shut down'])


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
    if if_there(['netflix','movie']):
        search_term = record_audio("what do yuo want to search")
        url = f"https://www.netflix.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak('enjoy watching')
        exit()

    if if_there(['youtube']):
        search_term = record_audio("what do yuo want to watch")
        url = f"https://www.youtube.com/results?search_query={search_term}"
        webbrowser.get().open(url)
        speak('enjoy watching')
        exit()

    if if_there(['search','google','what is ']):
        search_term = record_audio('what to search')
        url = f"https://www.google.com/search?q={search_term}"
        webbrowser.get().open(url)
        speak(f"i found this on the web about {search_term}")

    if if_there(['set alarm','alarm']):
        set_hour = int(record_audio('what hour should i wake you up'))
        set_minute = int(record_audio('what minute should i wake you up'))
        ste_am = record_audio('am or pm')
        if (ste_am == 'pm'):
            set_hour = set_hour+ 12
        while True:
            if(set_hour == datetime.datetime.now().hour and
            set_minute == datetime.datetime.now().minute):
                set_timer = speak('wake up')
                print(set_timer)
                if if_there(['kill alarm','set alarm']):
                    speak('killing alarm')
                    break


    if if_there(['shutdown']):
        speak('logging out')
        shutdown()




    if if_there(['goodbye','bye']):
        bye = [f"going offline",f"bye","it was nice to meet you",f"have a nice day"]
        breakpoint_2 = bye[random.randint(0,len(bye)-1)]
        speak(breakpoint_2)
        exit()


time.sleep(1)
while(1):
    voice_data = record_audio()
    if there_exists(["wake up"]):
        speak("activated...")
        authenticate = record_audio()
        service(authenticate)

    


    
