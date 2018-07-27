# -*- coding: utf-8 -*-
from weather import Weather,Unit
from Voice import talk
from MyCommand import myCommands
import requests
import json

def weather_report():

    weather = Weather()
    unit = Unit.CELSIUS

    talk("what is your city name?")
    city = myCommands()
    
    try:
        location = weather.lookup_by_location(city)
        condition = location.condition
        low_temp = location.print_obj['item']['forecast'][0]['low']
        high_temp = location.print_obj['item']['forecast'][0]['high']

        print('weather condition:',condition.text)
        print('current temperature:', condition.temp,'°C')
        print('today\'s temperature range:', low_temp,'°C to', high_temp,  '°C')
    except:
        print('Sorry, something went wrong!')
