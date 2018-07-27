from gtts import gTTS
import os


def talk(audio):

    try:
        print (audio)

        tts = gTTS( text=audio, lang='en')
        tts.save("audio.mp3")  #saving the audio responses into the specified file
        os.system("mpg123 audio.mp3")  #to run the saved audio in the specified mp3 file using mpg123
    except:
        print("Sorry, an error occured")
