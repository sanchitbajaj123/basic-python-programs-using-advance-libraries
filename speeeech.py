import speech_recognition as sr
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize the speech recognition engine
r = sr.Recognizer()

# Use the default microphone as the audio source
with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

try:
    # Use the speech recognition engine to transcribe the audio
    text = r.recognize_google(audio)
    print("You said:", text)

    # Use the text-to-speech engine to say the transcribed text
    engine.say(text)
    engine.runAndWait()

except sr.UnknownValueError:
    print("Could not understand audio")

except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))
