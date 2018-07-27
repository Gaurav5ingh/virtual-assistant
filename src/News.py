import bs4
from bs4 import BeautifulSoup 
from urllib.request import urlopen

from Voice import talk
from MyCommand import myCommands  
from TLD import get_tld

def news_headlines():

    tld = get_tld()

    try:  
        news_url = "https://news.google"+tld+"/news/rss"
        reader = urlopen(news_url)
        page = reader.read()
        reader.close()
    except:
        news_url = "https://news.google"+".co"+tld+"/news/rss"
        reader = urlopen(news_url)
        page = reader.read()
        reader.close()
        
    soup = BeautifulSoup(page,"xml")
    news_list = soup.findAll("item")
    # Print news title and url
    for news in news_list:
        print(news.title.text)
        #print(news.link.text)
        print ("-"*60)

