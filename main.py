#!/usr/bin/env python3

import speech_recognition as sr

# obtain path to "english.wav" in the same folder as this script
from os import path
AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), "english.wav")

# use the audio file as the audio source
r = sr.Recognizer()
# with sr.AudioFile(AUDIO_FILE) as source:
#     audio = r.record(source)  # read the entire audio file

with sr.Microphone() as source:
    print("Say something!")
    audio = r.listen(source)

# recognize speech using Sphinx
# try:
#     print("Sphinx thinks you said " + r.recognize_sphinx(audio))
# except sr.UnknownValueError:
#     print("Sphinx could not understand audio")
# except sr.RequestError as e:
#     print("Sphinx error; {0}".format(e))

# recognize speech using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("Maria Speech Recognition thinks you said " + r.recognize_google(audio, language='pt'))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))

# with open("microphone-results.wav", "wb") as f:
#     f.write(audio.get_wav_data())

import gtts
from playsound import playsound
tts = gtts.gTTS("Busca por "+ r.recognize_google(audio, language='pt'), lang="pt")
tts.save("hello.mp3")
playsound("hello.mp3")

# importing the search function from the pywhatkit library
from pywhatkit import search
# initializing a variable with the text that we want to search
query = r.recognize_google(audio, language='pt')
# Displaying the text that we want to search
print(f"Searching for the query : {query}")
# searching the text using teh search() function
search(query)