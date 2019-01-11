import speech_recognition as sr
import pyttsx3
import  os

speech =sr.Recognizer()

try:
    engine= pyttsx3.init()
except ImportError:
    print('Requested driver is not found')
except RuntimeError:
    print('Driver  Fail to Initialize ')


voices = engine.getProperty('voices')
# return the list of installed voices

for voice in voices:
    print(voice.id)


engine.setProperty('voice','HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0')
rate= engine.getProperty('rate')
engine.setProperty('rate',rate)


#engine.say('hello sir . this is Friday ...')
engine.runAndWait()

def speak_text_cmd(cmd):
    engine.say(cmd)
    engine.runAndWait()


def read_voice_cmd():
    voice_text = ''
    print('listening msg')
    with sr.Microphone() as source:
        audio = speech.listen(source)
    try:
        voice_text=speech.recognize_google(audio)
    except sr.UnknownValueError:
        print('pp error..')
        pass
    except sr.RequestError as e:
        print('network error..')
    print(voice_text)
    return voice_text


if __name__ == '__main__':
    speak_text_cmd('Hello Mr. sajal agrawal . this is friday as your artificial intelligent .  ')

    while True:

        voice_note=read_voice_cmd()
        print('cmd : {}'.format(voice_note))
        if 'hello' in voice_note:
            speak_text_cmd('hello dear , How may i help you')
            continue
        elif 'name' in voice_note and 'your' in voice_note:
            speak_text_cmd('My name is sexy ')
            speak_text_cmd('next command')
            continue
        elif 'open' in voice_note:
            os.system('explorer C:\\ ()'.format(voice_note.replace('open','')))
            speak_text_cmd('next command')
            continue
        elif 'by' in voice_note:
            speak_text_cmd("by Mr. sajal agrawal")
            exit()










