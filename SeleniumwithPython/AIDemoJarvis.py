import pyttsx3
import datetime
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[0].id)
engine.setProperty('voice', voices[0].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning Varun! How are you?")
    elif hour>=12 and hour<16:
        speak("Good Afternoon Varun!")
    else:
        speak("Good Evening!")
    speak("I am Your Personal Assistant. How may I help you?")

def takeCommand():
    '''

    It takes mic input from the user and returns string output

    '''
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
       # r.pause_threshold = 1 # seconds of non-speaking audio before a phrase is considered complete
      #  r.adjust_for_ambient_noise(source, duration=1)
        r.energy_threshold = 100
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, Language='en-uk')
        print("User said:" + query)
    except Exception as e:
        #print(e)
        print("Say that again please...Sorry I didn't understand")
        return "None"
    return query

if __name__ == '__main__':
    wishMe()
    takeCommand()
    #speak("Varun is a programmer and a good boy")