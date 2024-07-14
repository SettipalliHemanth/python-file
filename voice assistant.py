import pyttsx3
import speech_recognition as sr
import os
import webbrowser
import datetime
import wikipedia
import pyaudio
     
pyaudio.PyAudio()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voices',voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak('good morning')
    elif hour>=12 and hour<18:
        speak('good Afternoon')
    else:
        speak('good evening')

    speak('i am siri please tell me how can help you')
def takecommand():
    r = sr.Recognizer()
    with  sr.Microphone() as source:
        print("recognizing command ")
        r.adjust_for_ambient_noise(source) 
        audio = r.listen(source)

    try:
        print("Recognizing")
        query = r.recognize_google(audio,language='en-in')
       
        print(f"user said: {query}\n")
        return query
    except Exception as e:
        print("say repeatedly")
        return "None"
if __name__ == '__main__':
    wishMe()
    while True:
        query= takecommand().lower()
        if "wikipedia" in query:
            speak("wikipedia search")
            query= query.replace("wikipedia","")
            results = wikipedia.summary(query,sentences="24")
            speak("according to Wikipedia")
            print(results)
            speak(results)
        elif "open youtube" in query:
            webbrowser.open('http://www.youtube.com')
            speak('opening youtube sir')

        elif 'open google' in query:
            webbrowser.open('http://www.google.com')
        elif "search youtube" in query:
            query = query.replace("search youtube", "")
            webbrowser.open(f'https://www.youtube.com/results?search_query={query}')
        elif 'play music' in query:
            music_dir = webbrowser.open('http://spotify.com')
            print("songs")
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H-%M-%S")
            speak(f"sir this time {strTime}")
                  
