import webbrowser
from TLD import get_tld
import re
import bs4
from bs4 import BeautifulSoup 
import requests


def get_url(query):
    
    tld = get_tld()
    base_url = "https://www.google"+tld+"/search?q=" + query
    check = requests.get(base_url)

    if  check.status_code == 200:
        url = "https://www.google"+tld+"/search?q=" + query
        
    else:
        url = "https://www.google"+".co"+tld+"/search?q=" + query
    
    page = requests.get(url)
       
    soup = BeautifulSoup(page.content,'lxml')

    for link in soup.find_all("a",href=re.compile("(?<=/url\?q=)(htt.*://.*)")):
        list_link = re.split(":(?=http)",link["href"].replace("/url?q=",""))
        break

    first_link = list_link[0]

 
    first_link = first_link.replace('%3F','?')
    first_link = first_link.replace('%3D','=')

    first_link = first_link.split('&')

    url = first_link[0]
    
    return url
    
    #print(url)

    #first_link = first_link.split('%3F')

    #url = first_link[0] + '?' + first_link[1]

    #webbrowser.open(url)



