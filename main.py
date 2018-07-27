import speech_recognition as sr
from gtts import gTTS
import os

from Voice import talk
from MyCommand import myCommands  
from News import news_headlines
from Weather_rep import weather_report
from Translator import translate
from GoogleSearch import google_search
from Music import play_music
from YT_video import video_dwnld
from YT_video import video_stream
from WikiSearch import wiki_search

def assistant(command):
    if 'hey' in command:
        talk("hello")
    

    elif ('news' in command) or ('headlines' in command):
        try:
            news_headlines()
        except:
            talk("Sorry, something went wrong")
            

    elif 'weather' in command:
        try:
            weather_report()
        except:
            talk("Sorry, something went wrong")


    elif 'translate' in command:
        try:
            translate()
        except:
            talk("Sorry, something went wrong")


    elif 'wikipedia' in command:
        try:
            wiki_search()
        except:
            talk("Sorry, something went wrong")
        

    elif ('song' in command) or ('music' in command):
        try:
            play_music()
        except:
            talk("Sorry, something went wrong")


    elif ('download' in command) and ('video' in command):
        try:
            video_dwnld()
        except:
            talk("Sorry, something went wrong")

    
    elif ('stream' in command) and ('video' in command):
        try:
            video_stream()
        except:
            talk("Sorry, something went wrong")
        

    else:
        try:
            talk("Opening search result from google")
            google_search(command)
        except:
            talk("Sorry, something went wrong")
        

talk("Welcome!")
while True:

    talk("How may I help you?")
    try:
        command = myCommands()
    
        if (command == 'bye'):
            talk("Good bye! have a nice day!")
            break

        assistant(command)
    
    except:
        talk("Could you please repeat that?")
        
    


    
