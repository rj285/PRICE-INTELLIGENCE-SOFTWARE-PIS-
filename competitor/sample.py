import pandas as pd
import requests
import numpy as np
import json
from colorama import *
init(autoreset=True)

with open('competitor_list.json', 'r') as file:
    competitor_list=json.load(file).get('competitor_list')    

row_data={}
for competitor in competitor_list:    
    row_data.update({competitor.get('name'): []})

for competitor in competitor_list:
    print(Fore.GREEN + "Fetching data from "+competitor.get('name')+"...")
    URL=competitor.get('cat_url')    
    cookie=competitor.get('cookie')
    HEADERS = {
            'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
            'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
            'Cookie': cookie
        }

    response = requests.get(URL, headers=HEADERS)

    data=response.json()
    items=data.get('items')
    for item in items:            
        row_data[competitor.get('name')].append(item.get('name'))


        # print(Style.BRIGHT + Fore.GREEN + "category data fetched\n")
# print(row_data)
# df=pd.DataFrame(row_data)
# print(df)
maxlength=max(len(arr) for arr in row_data.values())
print(maxlength)

# print(len(row_data['tfm']))

# for key,value in row_data.items():
#     print(f"name is :{key} category{value}")