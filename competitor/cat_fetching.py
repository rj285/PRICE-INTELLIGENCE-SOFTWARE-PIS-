import pandas as pd
import numpy as np
import requests
import json
from colorama import*

init(autoreset=True)

with open("competitor_list.json",'r') as file:
    competitor_list = json.load(file).get('competitor_list')
    
row_data = {}

for competitor in competitor_list:
    row_data.update({competitor.get('name'): []})
#print(row_data)-> #{'sprouts': [], 'wegmans': [], 'tfm': []}
    
    
for competitor in competitor_list:
    print(Style.BRIGHT+Fore.GREEN+"Fetching data from "+competitor.get('name')+"......")
    
    URL = competitor.get('cat_url')
    
    cookie = competitor.get('cookie')
    
    HEADERS = {
        'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
        'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
        #user agent is a string of information that a web browser or other application sends to a web server as part of an HTTP request. 
        'Cookie': cookie
        }
        
    # try:
    #     responses = requests.get(URL,headers=HEADERS)
    #     if responses.status_code == 200:
    #         data = responses.json()
    #         item = data.get('items')
    #         for item in item:
    #             row_data[competitor.get('name')].append(item.get('name'))
    #             print(Style.BRIGHT+Fore.GREEN+"category data fetched\n")
    #     else:
    #         print("No data fetched")
    # except:
    #     print("Something went wrong")
    
    RESPONSES = requests.get(URL,headers=HEADERS)
    # print(RESPONSES.status_code)
    data = RESPONSES.json()
    items = data.get('items')
    
    for item in items:
        row_data[competitor.get('name')].append(item.get('name'))
        # print(Style.BRIGHT+Fore.YELLOW+"category data fetched \n")
        # print(item.get('name'))
        
# print(row_data)
maxlength = max(len(arr) for  arr in row_data.values())
# print(maxlength) #1186

# print(len(row_data['sprouts']))
# print(len(row_data['wegmans']))
# print(len(row_data['tfm']))
# print([np.nan]*10)
for key,value in row_data.items():
    print(f"name is:- {key} length:- {len(value)}")
    if len(value) < maxlength:
        row_data[key] = value + [np.nan]*(maxlength-len(value))
    # print(row_data)
        
df = pd.DataFrame(row_data)
# print(df)
df.to_excel("output/all_cats_fetched.xlsx",index=False)
