import speech_recognition as sr
import os
#we use amazon poly services
from playsound import playsound
#this modeule help us to play the mp3 file
import webbrowser
import random
greeting_dict={'hello':'hello','hi':'hi'}
speech=sr.Recognizer;
def play_sound(mp3_list):
    mp3=random.choice(mp3_list)
    play_sound(mp3)

def read_voice():
    voice_text = ''
    print('listening msg')
    with sr.Microphone() as source:
        audio = speech.listen(source=source,timeout=10,phrase_time_limit=5)
    try:
        voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:
        print('pp error..')
        pass
    except sr.RequestError as e:
        print('network error..')
    except sr.WaitTimeoutError:
        pass
    print(voice_text)
    return voice_text

if __name__ == '__main__':
    playsound('mp3/greeting.mp3')
    while True:
        voice_note=read_voice()
        print('cmd : {}'.format(voice_note))
        if 'hello' in voice_note:
            continue
        elif 'name' in voice_note and 'your' in voice_note:
            continue
        elif 'open' in voice_note:
            continue
        elif 'by' in voice_note:
            pass