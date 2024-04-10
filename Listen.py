import speech_recognition as sr
from googletrans import Translator


def Listen():
    r = sr.Recognizer()

    try:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source, duration=0.2)
            print("Listening to your voice....")
            r.pause_threshold = 1
            audio = r.listen(source, 0, 6)
            print("Recognizing your command....")
            query = r.recognize_google(audio, language="en-in")
            query = str(query).lower()
            print(f"Your command was : {query}")
    except sr.UnknownValueError():
        return "Sorry! I didn't get that"



