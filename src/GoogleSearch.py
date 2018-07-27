from Get_search_url import get_url
import webbrowser
from Voice import talk
from MyCommand import myCommands 

def google_search(query):
    
    try:
        url = get_url(query)
        webbrowser.open(url)
    except:
        talk("Sorry, something went wrong!")
