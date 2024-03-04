import requests
import pandas as pd

cookie = "_gcl_au=1.1.521922636.1706679984; _fbp=fb.1.1706679988441.575132951; BVBRANDID=48829252-2d8f-4a5a-a583-e4783d338dcf; _pin_unauth=dWlkPU5qZ3pPVEEyWWpJdFpqWXpaUzAwTVRsa0xUaGtOakV0WXpJM1lqaGpPREF4TW1Zeg; ajs_anonymous_id=a97a839a-1b07-4021-a894-5e50b55564e6; _pin_unauth=dWlkPU5qZ3pPVEEyWWpJdFpqWXpaUzAwTVRsa0xUaGtOakV0WXpJM1lqaGpPREF4TW1Zeg; ajs_anonymous_id=a97a839a-1b07-4021-a894-5e50b55564e6; __stripe_mid=dd8bfc00-c656-4337-999c-dff73174b742cb83d4; loyaltyID=null; _gid=GA1.2.1724003856.1709013648; BVBRANDSID=174daf42-781e-4203-98ff-25d3c78b7df8; __cf_bm=LAkmuaSoyeDKy2QYdeiF9U5QE5jbPrClIJ8SyFOMneg-1709013649-1.0-AU2UPseTxuZBz7oDG91Rp8eDgGFFYGt7Csn6RCDIP8/+TS5EQj5NNQhLrRb0v9PdJYcGM19PtZHwMmC9N1+BX78=; _gat_UA-47434162-1=1; dotcomSearchId=55eb3ac9-c5ff-4688-a05b-62e12e9476e2; __stripe_sid=ea0d34fc-1db8-4f1f-9cab-f4903281d735dc71b8; session-sprouts=.eJwdjkFvgjAARv9Lz8YAigxuDt1WBu1GgIoXglBnoVRGQaXL_vuaHb7Ly5e89wOK80DlBXjnkku6AEVPh64UVIzAG4dJE0mlZFdRjNeWCuABOgeX02vFMAtgqqCJWOAuNTQrK5v1VGXx24m7_dGHG9hEM2qCFu14FyaplSfbEe2-Vtg31pHKWEhihlS0yvUPE9REPpRQZOp4CM4l-WS4gQZS2wdOUi26s5zEY0nsf9fB4i1s-qkmDxn6OqpzJ0rMW32IGBbxXJNUwo5fat0RJdUdNfkKJ60dCWMJ36aMk4_5vXJs1R_FPsXdY20-ZQwZz85esBeHEyc0v9UVLMAk6VCwGnjW2jFM17Y3v39xcWn_.GL8Mfg.DGOAtiw3vJDThtl3Y3Oehh8nB78; _ga=GA1.2.853090590.1706679987; _uetsid=8e1b2dc0d53511ee924c776b017f3394; _uetvid=14be1f60bffc11eea5691fbf32dcaa28; _ga_LPZ816BHL5=GS1.1.1709013647.30.1.1709013759.9.0.0; _dd_s=rum=0&expire=1709014660612"

HEADERS = {

    'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
    'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
    #user agent is a string of information that a web browser or other application sends to a web server as part of an HTTP request. 
    'Cookie': cookie    
}

df_romart = pd.read_excel("romart.xlsx",sheet_name="Sheet1")
for i in range(0,len(df_romart)):
    searchinput = df_romart.loc[i]['name']

    URL = f"https://shop.sprouts.com/api/v2/store_products?ads_enabled=true&ads_pagination_improvements=true&allow_autocorrect=true&limit=10&offset=0&search_provider=ic&search_term={searchinput}&secondary_results=true&sort=rank&unified_search_shadow_test_enabled=false"


    responses = requests.get(URL,headers=HEADERS)
    data = responses.json()


    items=data['items']
    df_items = pd.DataFrame(items)
    df_cleaned = df_items[['name','base_price','display_uom','average_weight']]

    df_cleaned.to_excel(f"scraped_items/{searchinput}.xlsx",index=False)
    #df_cleaned.to_excel(f"FOLDER NAME/{searchinput}.xlsx",index=False) all the data will 