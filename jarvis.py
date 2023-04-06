# run in bash >>>>> $ python jarvis.py

import pyttsx3
import datetime



# Create the object engine to initialize the text-to-speech
engine = pyttsx3.init()



# Set properties for the voice
voice = engine.getProperty('voices')[0]                                                                                 # Get the voice object for TTS_MS_EN-US_DAVID_11.0
engine.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_DAVID_11.0')       # Set the voice for the engine to use
engine.setProperty('rate', 170)                                                                                         # Set the rate of speech (words per minute)
engine.setProperty('volume', 1.0)                                                                                       # Set the volume (between 0 and 1)
engine.setProperty('pitch', 80)                                                                                         # Set the pitch of the voice to a lower value (entoação/tom de voz)



# function text-to-speech
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    current_time = datetime.datetime.now().strftime("%I:%M:%S")
    speak(current_time)

time()