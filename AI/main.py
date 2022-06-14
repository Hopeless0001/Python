from typing_extensions import Self
import speech_recognition as sr
import pyttsx3
import webbrowser
from datetime import date, timedelta, datetime
import serial
import pyowm
import operator
import random  
import os

# Speech Recognition Constants
recognizer = sr.Recognizer()
microphone = sr.Microphone()

# Python Text-to-Speech (pyttsx3) Constants
engine = pyttsx3.init()
engine.setProperty('volume', 1.0)

WAKE = "shane"

# Used to store user commands for analysis
CONVERSATION_LOG = "Conversation Log.txt"

# Initial analysis of words that would typically require a Google search
SEARCH_WORDS = {"who": "who", "what": "what", "when": "when", "where": "where", "why": "why", "how": "how"}

# Establish serial connection for arduino board
try:
    ser = serial.Serial('com3', 9600)
    LED = True
except serial.SerialException:
    print("LEDs are not connected. There will be no lighting support.")
    # If the LEDs aren't connected this will allow the program to skip the LED commands.
    LED = False
    pass

##################################################################
#                       Command and stuff                        #
##################################################################

class Shane:

    s = Self

    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    # Used to hear the commands after the wake word has been said
    def hear(self, recognizer, microphone, response):
        try:
            with microphone as source:
                print("Waiting for command.")
                recognizer.adjust_for_ambient_noise(source)
                recognizer.dynamic_energy_threshold = 3000
                audio = recognizer.listen(source, timeout=5.0)
                command = recognizer.recognize_google(audio)
                s.remember(command)
                return command.lower()
        except sr.WaitTimeoutError:
            pass
        except sr.UnknownValueError:
            pass
        except sr.RequestError:
            print("Network error.")

    # Used to speak to the user
    def speak(self, text):
        engine.say(text)
        engine.runAndWait()
