from urllib.parse import quote_from_bytes
import speech_recognition as sr
import pyttsx3
import pyaudio
import os
import datetime
import smtplib
import wikipedia
import webbrowser
import pywhatkit
import pyjokes
import pywhatkit as kit
from threading import Thread

operator = pyttsx3.init('sapi5')  # micorsoft's sapi5 prdefined voice
voices = operator.getProperty('voices')
operator.setProperty('voice', voices[1].id) #Setting voice for ALICIA [0]= male voice [1]= female voice


def speak(audio):                           #Default voice for the assistant
    operator.say(audio)
    operator.runAndWait()                   #It is just like getch() in C used to hold output


def demo():                                 #Assistant speaks this when it start's
    print("Hi I am Alicia what can I do for you")
    speak("Hi I am Alicia what can I do for you")


def wishMe():               #Function to wish the user that's it
    hr = int(datetime.datetime.now().hour)
    if hr >= 0 and hr < 12:
        speak("Good Morning")
    elif hr >= 12 and hr < 18:
        speak("Good Afternoon")
    else:
        speak("Good Evening")


def listenCommand():      #Alicia Understands the user command and evaluates it as a speech
    t = sr.Recognizer()
    with sr.Microphone() as source :
        print('listening....')
        t.pause_threshold = 1   #thread issue
        audio = t.listen(source)

    try:
        print("I am Recognizing......")
        query = t.recognize_google(audio, language='en-in')  #Uses google API to understand and accept our command
        print(f"User Said: {query}\n")

    except Exception as e :
        print("Say that Again please.....")
        speak('Say that Again please.....')
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    demo()
    while True :
        query = listenCommand().lower()
        #print(query)
        if 'youtube' in query:
            speak("Opening Youtube ")
            webbrowser.open("https://www.youtube.com/")

        elif 'netflix' in query:
            speak("opening netflix")
            webbrowser.open("https://www.netflix.com/browse")

        elif 'open amazon prime video' in query:
            speak("opening Amazon Prime video ")
            webbrowser.open("https://www.primevideo.com/")

        elif 'open google' in query:
            speak("opening google ")
            webbrowser.open("https://www.google.com/")

        elif 'vs code' in query :
            speak('opening vs code')
            Path = "C:/Program Files/Microsoft VS Code/Code.exe"
            os.startfile(Path)

        elif 'open stackoverflow' in query:
            speak("opening stackoverflow ") #File path is wrong
            webbrowser.open("https://stackoverflow.com/")

        elif 'sahu technology' in query:
            speak("opening sahu technology website")
            webbrowser.open("https://www.sahutechnologies.com/")
        
        elif 'discord' in query:
            speak("Opening Discord")
            Path = "C:/Users/vipin/AppData/Local/Discord/Update.exe --processStart Discord.exe"   
            os.startfile(Path)

        elif 'time' in query:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print('Current time is : '+time)
            speak('current time is'+time)
        
        elif 'play' in query:                   
            song = query.replace('play','')
            speak('playing'+song)
            pywhatkit.playonyt(song)


        elif 'wikipedia' in query:
            data = query.replace('wikipedia','')
            info = wikipedia.summary(data,1)
            print(info)
            speak(info)

        elif 'what is' in query:
            data = query.replace('wikipedia','')
            info = wikipedia.summary(data,2)
            print(info)
            speak(info)

        elif 'joke' in query:
            speak(pyjokes.get_joke())

         


        elif 'stop' in query: #To terminate the Alicia
            speak("Glad to help you")
            exit()