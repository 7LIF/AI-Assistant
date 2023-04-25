# run in bash >>>>> $ python jarvis.py

import pyttsx3
import datetime


# Create the object engine to initialize the text-to-speech
engine = pyttsx3.init()


# Set properties for the voice
voice = engine.getProperty('voices')[0]                                                                                 # Get the voice object for TTS_MS_EN-US_DAVID_11.0
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')       # Set the voice for the engine to use
engine.setProperty('rate', 175)                                                                                         # Set the rate of speech (words per minute)
engine.setProperty('volume', 1.0)                                                                                       # Set the volume (between 0 and 1)
engine.setProperty('pitch', 0.20)                                                                                       # Set the pitch of the voice to a lower value (entoação/tom de voz)


# function text-to-speech 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# function to get current time
def time():
    current_time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(current_time)


# function to get current date
def date(): 
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak(day)
    speak(month)
    speak(year)


# function greeting
def greeting():  
    hour = datetime.datetime.now().hour
    if hour>=6 and hour<12:
        speak("Good morning!")
    elif hour>=12 and hour<18:
        speak("Good afternoon!")
    elif hour>=18 and hour<24:
        speak("Good evening!")
    else:
        speak("Good night!")
    
    speak("Welcome back!")
    speak("The current time is")
    time()
    speak("The current date is")
    date()
    speak("Jarvis at your service. Please tell me how can i help you?")


greeting()