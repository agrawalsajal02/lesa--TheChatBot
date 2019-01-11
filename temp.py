import speech_recognition as sr
import pyttsx3
import  os
speech =sr.Recognizer()
engine= pyttsx3.init()
def speak_text_cmd(cmd):
    engine.say(cmd)
    engine.runAndWait()
def read_voice_cmd():
    voice_text = ''
    print('listening msg')
    with sr.Microphone() as source:
        audio = speech.listen(source)
    voice_text=speech.recognize_google(audio)
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
            speak_text_cmd('My name is sexy !')
            speak_text_cmd('next command')
            continue
        elif 'know' in voice_note and 'about me' in voice_note:
            speak_text_cmd('your are the world best coder !!!!keep champ pushing it. your day will came.')
            speak_text_cmd('next command')
            continue
        elif 'my' in voice_note and 'girlfriend' in voice_note:
            speak_text_cmd('why are you asking me !!!!!!. you know it')
            speak_text_cmd('next command')
            continue
        elif 'open' in voice_note:
            os.system('explorer C:\\ ()'.format(voice_note.replace('open','')))
            speak_text_cmd('next command')
            continue
        elif 'by' in voice_note:
            speak_text_cmd("by Mr. sajal agrawal")
            exit()
        else:
            continue;










