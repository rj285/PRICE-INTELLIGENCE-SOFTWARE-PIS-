import pandas as pd
import requests
import json
from colorama import*

with open('competitor.json','r') as file :
    competitor_list = json.load(file).get('competitor')
    
searchterm = input("Enter the item to search:- ")
searchterm=searchterm.lower()

for cmpt in competitor_list:
    print(Style.BRIGHT+Fore.YELLOW+cmpt.get('name'))
    cookie = cmpt.get('cookie')
    
    HEADERS = {

            'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
            'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
            #user agent is a string of information that a web browser or other application sends to a web server as part of an HTTP request. 
            'Cookie': cookie    
        }

    url = cmpt.get('store_api')+searchterm
    
    responses = requests.get(url,headers=HEADERS)
    data = responses.json()
    print(data)