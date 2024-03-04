import pandas as pd
import requests
import json
from colorama import*

with open("competitor_list.json",'r') as file:
    competitor_list = json.load(file).get('competitor_list')
    
# serach_term = input("Enter the name to search:- ")
# serach_term = serach_term.lower()

for competitor in competitor_list:
    print(Style.BRIGHT+Fore.RED+competitor.get('name'))
    print("============================================")
    
    cookie = competitor.get('cookie')
    
        
    HEADERS = {

            'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
            'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
            #user agent is a string of information that a web browser or other application sends to a web server as part of an HTTP request. 
            'Cookie': cookie    
        }
    
    # URL = competitor.get('store_api')+serach_term
    URL = competitor.get('cat_url')
    
    responses = requests.get(URL,headers=HEADERS)
    # print(responses.status_code)
    data = responses.json()
    # print(data)
    items = data.get('items')
    # print(items[0]['name'])
    # for item in items:
    #     for category in item.get('categories'):
            # print(Style.BRIGHT+Fore.LIGHTCYAN_EX+category.get('name'))
    for category in items:
        print(Style.BRIGHT+Fore.LIGHTGREEN_EX+category.get('name'))

