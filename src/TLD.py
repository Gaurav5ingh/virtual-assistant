import requests
import json

def get_tld():

    url = 'http://ipinfo.io/json'
    response = requests.get(url)
    data = json.loads(response.content.decode('utf-8'))

    tld = data['country']

    return "." + tld.lower()
