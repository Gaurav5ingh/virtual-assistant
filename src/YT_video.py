from pytube import YouTube
import webbrowser
from Get_search_url import get_url

def video_dwnld():

    query = input("Which do you want to download?")

    url = get_url(query + 'youtube') 
    
    yt = YouTube(url)

    stream = yt.streams.first()

    stream.download()


def video_stream():

    query = input("What do you want to play?")
    webbrowser.open(url)
