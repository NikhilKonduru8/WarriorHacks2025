import os
import time
import playsound
import speech_recognition as sr
from gtts import gTTS
import google.generativeai as genai
#from elevenlabs import play
import random as rand
import pyaudio


def speak (text):
    tts = gTTS(text=text, lang="en")
    filename = "voice.mp3"
    tts.save(filename)
    playsound.playsound(filename)



print("-------------------------------")
print("What can I assist you with")
print("-------------------------------")
speak("What can I assist you with")

loop_options = ['Anything Else','Any other questions?','Need more help?','Anything else I can do?']




while True:


    r = sr.Recognizer()
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""

        try:
            said = r.recognize_google(audio)
        except Exception as e:
            print("Exception: " + str(e))


    genai.configure(api_key="AIzaSyBO5YGrnaTQ3YZjX46O1yJQ5ns4cam8swo")
    model = genai.GenerativeModel("gemini-1.5-flash")
    response = model.generate_content(said)

    response = response.text.replace("*"," ")

    time.sleep(2)
    print("----------------------------------")
    print("Prompt: "+ said)
    print("----------------------------------")

    print(response)
    speak(response)
    time.sleep(1.5)

    choice = rand.choice(loop_options)
    print("-------------------------------")
    print(choice)
    print("-------------------------------")
    speak(choice)
