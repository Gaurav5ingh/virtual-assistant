import webbrowser
from Get_search_url import get_url
#from selenium.webdriver import Firefox
#from selenium.webdriver.firefox.options import Options

def play_music():
    song = input("What do you want to listen:")
    query = 'play ' + song + ' from gaana.com'
    url = get_url(query)
    print('playing...')
    webbrowser.open(url)

#for start playing song without opening any window/tab  
'''
opts = Options()
opts.set_headless()
browser = Firefox(options=opts)
browser.get(url)
try :
    browser.find_element_by_class('play').click()  
    browse.find_element_by_class('pause').click()
except AttributeError:
    print("playing...")
'''
