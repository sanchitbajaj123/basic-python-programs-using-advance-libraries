import pywhatkit as kit


# Search on Google

import speech_recognition as sr
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize the recognizer
r = sr.Recognizer()

# Use the default microphone as the audio source
with sr.Microphone() as source:
    print("Say something!")
    # Listen for audio input from the user
    audio = r.listen(source)
    print("listining")

try:
    # Recognize speech using Google Speech Recognition
    print("strt")
    text = r.recognize_google(audio)
    print("You said:",text)
    engine.say(text)
    engine.runAndWait()
    kit.search(text)
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))


