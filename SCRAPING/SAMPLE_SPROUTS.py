import requests
import pandas as pd

cookie = "_gcl_au=1.1.521922636.1706679984; _gid=GA1.2.1964669730.1706679987; loyaltyID=null; _fbp=fb.1.1706679988441.575132951; BVBRANDID=48829252-2d8f-4a5a-a583-e4783d338dcf; _pin_unauth=dWlkPU5qZ3pPVEEyWWpJdFpqWXpaUzAwTVRsa0xUaGtOakV0WXpJM1lqaGpPREF4TW1Zeg; ajs_anonymous_id=a97a839a-1b07-4021-a894-5e50b55564e6; _pin_unauth=dWlkPU5qZ3pPVEEyWWpJdFpqWXpaUzAwTVRsa0xUaGtOakV0WXpJM1lqaGpPREF4TW1Zeg; ajs_anonymous_id=a97a839a-1b07-4021-a894-5e50b55564e6; __stripe_mid=dd8bfc00-c656-4337-999c-dff73174b742cb83d4; BVBRANDSID=01ba9332-6714-4d0a-be7d-d9e9d9b30fb7; __cf_bm=m.O3hsjKFc9KFg1RN_iNoqctlPTGFxq82psHxXgpjkA-1706772314-1-ARnmt28nAf9g/tk3cb1BJKfXEut9wSM4y4Fba25cNQ16eiwm5cbLCZZ2a/uYdlLhZbDxjB/1wFjQtq8KIEL3ZGA=; _gat_UA-47434162-1=1; dotcomSearchId=0642693a-928e-4306-b3e7-1491fb109c9b; __stripe_sid=a2f5ee9e-54cf-4dc7-995f-79cde9edb42c086300; session-sprouts=.eJwdjkFvgjAARv9Lz2YBJm5w29xmyqQoASpcCNICbaEaCipd9t_X7PBdXvLlvR9QNiNVHfCbqld0BcorHYdKUjkBfxpnQxRVil1kOV0ElcAHdAm6865mEQtgqqGNWOA9GWjXTraY6drpb-feuxZbuIH8vQs1EuEQiz2GDkrghD6OumDWusCp3ic9zzkRiLc611-9-SgoM12cgqbCRxZxaCH99oiS1IjuLMfxVGH333VyegH5dSb4ofZbEzV4M8X2jZxCFsl4IThVcOg7YjrCpL4jnj9HiXBDaT211v2bnlEQULGUVfta3JqdnNtZxl128FLyebQOUdbBg7MGKzArOpaMAN9Zv1i257qb3z9ChGuB.GJzaBQ.1dCr-u_FmIOQI08P9Dmg3QuEReA; _ga=GA1.2.853090590.1706679987; _uetsid=14bcaab0bffc11ee90adf963202ac90f; _uetvid=14be1f60bffc11eea5691fbf32dcaa28; _ga_LPZ816BHL5=GS1.1.1706772312.3.1.1706772615.36.0.0; _dd_s=rum=0&expire=1706773515735"

HEADERS = {

    'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
    'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
    #user agent is a string of information that a web browser or other application sends to a web server as part of an HTTP request. 
    'Cookie': cookie    
}

# user_input = str(input("Enter the name to search:- "))
# user_input_2 = int(input("Enter the limit:- "))

df_rohit = pd.read_excel("rohit.xlsx",sheet_name="Sheet1")
searchitem = df_rohit.loc[0]['name']

# for i in range(0,len(df_rohit)):
#     searchinput = df_rohit.loc[i]['name']

URL = f"https://shop.sprouts.com/api/v2/store_products?ads_enabled=true&ads_pagination_improvements=true&allow_autocorrect=true&limit=5&offset=0&search_provider=ic&search_term={searchitem}&secondary_results=true&sort=rank&unified_search_shadow_test_enabled=false"
# URL = "https://shop.sprouts.com/api/v2/store_products?ads_enabled=true&ads_pagination_improvements=true&allow_autocorrect=true&limit=5&offset=0&search_is_autocomplete=true&search_provider=ic&search_term=apples&secondary_results=true&sort=rank&unified_search_shadow_test_enabled=false"



responses = requests.get(URL,headers=HEADERS)
data = responses.json()
# sts_cd = responses.status_code #to check the status code


# for i in range(0,len(data['items'])):
#     print(f"{data['items'][i]['name']}")

items=data['items']

# DATA FRAME
df_items = pd.DataFrame(items)
df_cleaned = df_items[['name','base_price','display_uom','average_weight']]

df_cleaned.to_excel("apple.xlsx",index=False)

#to fetch the zero th index data
# zero = df_items.loc[0]
# zero.to_csv("items.csv",index=False) #converting the above data into csv

# df_cleaned.to_csv("items.csv",index=False)#converting to csv

# df_cleaned.to_json("items.json",index=False)#converting to json

# df_cleaned.to_html("items.html",index=False)#converting to html

# df_cleaned.to_excel("items.xlsx",index=False)#converting to excel

# df_cleaned.to_excel("sprouts_items.xlsx",index=False)

# df_rohit = pd.read_excel("rohit.xlsx",sheet_name="Sheet1") #code to read a file useing panda 
# searchitem = df_rohit.loc[0] #display the zero th raw data
