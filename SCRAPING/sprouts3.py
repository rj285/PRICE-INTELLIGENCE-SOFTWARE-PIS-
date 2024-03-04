import requests
import pandas as pd

cookie = "_gcl_au=1.1.521922636.1706679984; _fbp=fb.1.1706679988441.575132951; BVBRANDID=48829252-2d8f-4a5a-a583-e4783d338dcf; _pin_unauth=dWlkPU5qZ3pPVEEyWWpJdFpqWXpaUzAwTVRsa0xUaGtOakV0WXpJM1lqaGpPREF4TW1Zeg; ajs_anonymous_id=a97a839a-1b07-4021-a894-5e50b55564e6; _pin_unauth=dWlkPU5qZ3pPVEEyWWpJdFpqWXpaUzAwTVRsa0xUaGtOakV0WXpJM1lqaGpPREF4TW1Zeg; ajs_anonymous_id=a97a839a-1b07-4021-a894-5e50b55564e6; __stripe_mid=dd8bfc00-c656-4337-999c-dff73174b742cb83d4; loyaltyID=undefined; _gid=GA1.2.552717278.1707113988; BVBRANDSID=26334da0-c691-4e0e-af1a-f6e1ed46b80a; __cf_bm=llii48jpvLSgH1M6UmN.O3Ws5YYL7uDChvt7Nmyqb_M-1707114522-1-AcnwuxQK1a+ZbPzFQNIeE/1dqVlkBRkrQ4yBHoPXBg3hbFiqOGXvi21c+PieRPdceG/3Qno5WfJq+Yu8rVai3f4=; _gat_UA-47434162-1=1; dotcomSearchId=e33f95fa-4077-4c06-96b5-b03f5a3de153; __stripe_sid=028d58e3-ea7b-4de3-b533-78cf9ccdb590259959; session-sprouts=.eJwdjsFugjAAQP-lZ2MKEze4LcRoiS3KwCIXglChUKqhoJbFf1-zw7u8y3u_IL8OTDXAuxZCsQXI72zoC8nkCLxxmIxRTCl-k_l465gEHmA6aC7bkoc8QMmMLMIDd2mkVdonbZhLWzwuwr1nPlqjNugJjcR5Puo9TZyMJiPZbjTx4QrHAd_HGJK2dvB28zT-RTRSSJ7mLA2uBT3ysEWQzN-vME5M6MnPNBoL6vy3Ult0qL1PFX2pvW-mendi1HpUKeahjHRFE4V60VTmA8flk7TnjzDuHCzhMtdwx7vDbsYHmNWqV0jUSvw0fZTTNB7robkVlcKypV9gASbFhpxXwLNXn9ByHWf9_gOm3Wum.GKISFQ.ReS4D-eMm0TNlfs2KgdrXqbYdVo; _ga=GA1.2.853090590.1706679987; _uetsid=aee9e660c3ef11ee9dcb5594a497be15; _uetvid=14be1f60bffc11eea5691fbf32dcaa28; _ga_LPZ816BHL5=GS1.1.1707113988.6.1.1707114646.33.0.0; _dd_s=rum=1&id=b38a0299-e820-435e-825d-cc015233d2ec&created=1707114623230&expire=1707115547590"
HEADERS = {

    'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
    'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
    #user agent is a string of information that a web browser or other application sends to a web server as part of an HTTP request. 
    'Cookie': cookie    
}

URL = "https://shop.sprouts.com/api/v2/categories/store/2"
responses = requests.get(URL,headers=HEADERS)
data = responses.json()
print(data['items'][1]['name'])

