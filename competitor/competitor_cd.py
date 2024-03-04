import pandas as pd
import requests
import json
from colorama import*

with open('competitor_list.json','r') as file:
    competitor_list = json.load(file).get('competitor_list')
    
searchterm = input("Enter any item to search:- ")
searchterm = searchterm.lower()

for competitor in competitor_list:
    print(Style.BRIGHT+Fore.CYAN+competitor.get('name'))
    cookie = competitor.get('cookie')
    
    HEADERS = {

            'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
            'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
            #user agent is a string of information that a web browser or other application sends to a web server as part of an HTTP request. 
            'Cookie': cookie    
        }
    
    URL = competitor.get('store_api') + searchterm
    responses = requests.get(URL,headers=HEADERS)
    data = responses.json()

    items = data.get('items')
    
    # print(items[0]['name'])
    
    for item in items:
        if (searchterm in item.get('name').lower()):
            print(Style.BRIGHT+Fore.YELLOW+item.get('name'))
            for category in item.get('categories'):
                print(Style.BRIGHT+Fore.GREEN+category.get('name'))
            print("============================================================")
    
