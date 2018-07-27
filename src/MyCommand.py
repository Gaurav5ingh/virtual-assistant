import speech_recognition as sr
from Voice import talk


def myCommands():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("So ")
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source, duration = 1) 
        audio = r.listen(source, timeout=5)

    try:
        command = r.recognize_google(audio)
        print("You said: " + command)
        command = command.lower()
        return command

    except sr.UnknownValueError:
        talk("Could not understand what you said")
        
    except sr.RequestError as e:
        talk("Could not request results; {0}".format(e))#what does this mean?

