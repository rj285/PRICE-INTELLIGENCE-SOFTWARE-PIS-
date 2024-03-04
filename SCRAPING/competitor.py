import requests
import pandas as pd

competitor_list = [
    {
        'url':"https://shop.thefreshmarket.com/api/v2/store_products?ads_enabled=true&ads_pagination_improvements=true&limit=60&offset=0&page=1&prophetScorer=frequency&sort=rank&allow_autocorrect=true&search_is_autocomplete=false&search_provider=ic&search_term=apple&secondary_results=true&unified_search_shadow_test_enabled=false",
        'cookie':"osano_consentmanager_uuid=cea5c46c-578e-47c7-9ac7-abdf696baaf5; osano_consentmanager=qCSkykYbFeqysfZuugMjaPUZoy2XiAYbVqLnGy_zgqAH-_FXKOmrbqJWx3KzuYS8gFkE1WwOPlqVjwSnLi_Y5VYkff0VfK-oTFnHOu58xl9kCVdPsShWMVkIgeHAczupkeXVmZH-QCh9EsCFJAj4Nqmcv5SN1fdMocraHmrstTxLvZwPvbOffs_as4L97wlGZ2MsMfwqRmcsrj_GNdY2RSK7r4dVuDaovm50bHc5hf3wMEl1VN4rjShOAgW0epFjeDrii72d3W9SUvuhjAMHA0KUZFiiTAzsjDUnuQ==; _gcl_au=1.1.333545714.1707113976; fw_se={%22value%22:%22fws2.80a9daae-858f-43f6-a5ac-29b794e2079f.1.1707113977886%22%2C%22createTime%22:%222024-02-05T06:19:37.886Z%22}; _gid=GA1.2.2004274543.1707113979; _uetsid=8ade2a40c3ee11eea9afb992ad3910d0; _uetvid=8adfa1c0c3ee11ee8b36658e007879a6; fw_chid={%22value%22:%22N7A4N3b%22%2C%22createTime%22:%222024-02-05T06:19:40.523Z%22}; _fbp=fb.1.1707114020517.923646554; _pin_unauth=dWlkPU5qZ3pPVEEyWWpJdFpqWXpaUzAwTVRsa0xUaGtOakV0WXpJM1lqaGpPREF4TW1Zeg; _ga_EMDXDP2N4W=GS1.2.1707114021.1.0.1707114027.54.0.0; __cf_bm=r_X1HQvtB9o3pP6lVisImvy_xbM4g2ytjrx1gqJAL.w-1707114029-1-ATAcvnE7lwrvVUyUORTJXLSIr4GEOm9+fPZcWYxBymYEWfYhWucoVvlUB6A4NdmqLndlBFTitw5E8E8kS7Z9zrs=; ajs_anonymous_id=0ab0eebf-e936-4536-abc3-b9921847e441; __stripe_mid=df67225e-0227-4f43-87cd-d97213c3a616c39ca6; __stripe_sid=3374354e-894e-4e71-b394-a00d9c832c5db78f56; fw_utm={%22value%22:%22{}%22%2C%22createTime%22:%222024-02-05T06:24:00.703Z%22}; fw_uid={%22value%22:%224f9d5ffe-2f8b-4292-adef-2e29d099597c%22%2C%22createTime%22:%222024-02-05T06:24:00.748Z%22}; session-prd-tfm=.eJxNybFygjAAgOF3yWw9goIHW0-RBiVUC1JZOIJBkhKwCYik13evY4d_-f4fkFeSqhq4VdEoOgP5jUpRtLTtgdvL4SmKKsW6Nu-7L9oCF9ApqIlfsogFKNEIYhY48yfC0jxNz3RpNnfSOLdsjWzETzxLk8eZn419fH2EftjjzdXEa8iwSKZ93AisszrkxxrH4YgnpFB70tlnUBXpgUU8maL4POKNZ-zXQZ358Eb-f2FB4o8Kie1ATMsiqQPLCdmXtwBmHyMr0q2BePfA-nURxp4RbkKjOsyj451UuxdPNyup6wT3shDDovu-8q2QtvduFatdWgUEJSWYgUFRmbMLcC3TsY0lXP7-AcxBaZE.GKIQgA.Q_1oLgWJVY06YP9EgCR-xZvnwOc; _gat_UA-000000000-1=1; _ga=GA1.1.294049640.1707113979; _ga_2NZ40CS25B=GS1.1.1707113978.1.1.1707114242.55.0.0; _dd_s=rum=0&expire=1707115141406"
        },
    {
        'url':"https://shop.wegmans.com/api/v2/store_products?ads_enabled=true&ads_pagination_improvements=true&limit=60&offset=0&page=1&prophetScorer=frecency&sort=rank&allow_autocorrect=true&search_is_autocomplete=true&search_provider=ic&search_term=apples&secondary_results=true&unified_search_shadow_test_enabled=false",
        'cookie':"AMCVS_68B620B35350F1650A490D45%40AdobeOrg=1; _fbp=fb.1.1706764786410.643157239; _pin_unauth=dWlkPU5qZ3pPVEEyWWpJdFpqWXpaUzAwTVRsa0xUaGtOakV0WXpJM1lqaGpPREF4TW1Zeg; _gcl_au=1.1.46368221.1706764787; wfm.tracking.sessionStart=1706764786734; at_check=true; ajs_anonymous_id=027c35d5-fb2a-442c-8663-1e2505626047; wegmans.chatbot.closed=1; wfm.tracking.s10=1; wfm.tracking.x2p=1; sa-user-id=s%253A0-cbe65070-4924-44f6-6cad-673bf9842009.JCt6Wyu74ha%252BRqY4wyLNSMW8lpiPQW%252BZUA1zrvfVolM; sa-user-id-v2=s%253Ay-ZQcEkkRPZsrWc7-YQgCTEvxsY.fYF7xykLXlmRoMKzyHfHRDBALsG%252Ba4nWFlP19bqjr%252Fg; sa-user-id-v3=s%253AAQAKINb91By4xSA9vuViO6slNSwbixtQbRT8Yiv57nVp5ua7ENQHGAIgnLTaqwY6BE5BDgxCBFO8ijI.S%252FZYTyHIEv8ew3kVXVcBfuaQr5bVTmiu22kVA30CEDQ; _pin_unauth=dWlkPU5qZ3pPVEEyWWpJdFpqWXpaUzAwTVRsa0xUaGtOakV0WXpJM1lqaGpPREF4TW1Zeg; at_check=true; __stripe_mid=f8fb3be8-2a34-4398-af6c-107927a609f30b3a0d; ajs_anonymous_id=027c35d5-fb2a-442c-8663-1e2505626047; AMCV_68B620B35350F1650A490D45%40AdobeOrg=179643557%7CMCIDTS%7C19759%7CMCMID%7C16508299969545549350492265713510682574%7CMCAAMLH-1707718785%7C12%7CMCAAMB-1707718785%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1707121185s%7CNONE%7CMCSYNCSOP%7C411-19762%7CMCCIDH%7C0%7CvVersion%7C5.5.0; kndctr_68B620B35350F1650A490D45_AdobeOrg_identity=CiYxNjUwODI5OTk2OTU0NTU0OTM1MDQ5MjI2NTcxMzUxMDY4MjU3NFIRCLqx75jWMRgBKgRJTkQxMAPwAdLosL_XMQ==; kndctr_68B620B35350F1650A490D45_AdobeOrg_cluster=ind1; __cf_bm=EAStGkE8DvKS_xVE_R2QtT09lE7nYRe8nxlTC3Fs5GM-1707113986-1-ASoQmO3HWS88Q5RKW4K1F6ptEpV2Xm4Ky3Q21nYSAh13sJ8SWtRyqER0IUmZoNrJ1wu08xBWtsX8RGErNG/Z1K4=; wfmStoreId=16; inRedirectGoldPanAudience=1; dotcomSearchId=a1e18b73-b8bf-4a30-afc0-0ef59468eb62; lux_uid=170711449487789986; s_gpv=Search%20Results:%20apples%20|%20Wegmans; __stripe_sid=3b8fa9a4-71f3-471a-900a-659528482b3d50845c; session-prd-weg=.eJwdjstygjAARf8la-vw0g7sBLQTasJoAwE2DIYgQUBLQAqd_ntpF3dzFvecb5AWHZclsIqslnwF0gfvmqzlbQ-svhsWIrmU4t6m_f3GW2ABPnnl5Y0JX3gwmKGKhWeuF6gyLZyWzUyrn5fafCQO3MIG15jEY0KQdiS7GZGgx-5Jj4UqMLHLI9mryGUTIrGOm6TEH1DCNpyTyCsyehJ-dVJ8EmvYZQpyRhHTc5_Rzb8r0uobrB5DTr_k0VmiGnPgVH3mERJ-e55yGkjY1GW-dCDCRlyxvx8D68r6YLuhO2Z2UQa2_oKvTnR1uvmsbdrPZq8e3vkurExjopgwsAKD5F0qcmAZhrndGq-G8vML1TlopA.GKIRow.t1ZhErs_eJAUofKKbiD5DqwAEr8; _uetsid=913484f0c3ee11ee9fe0c5bd0e7645cb; _uetvid=83f4a710c0c111ee991425330603c45d; _dd_s=rum=0&expire=1707115432910; mbox=session#70b2e93ae955439d8ca6a835dcb38ff2#1707116396|PC#70b2e93ae955439d8ca6a835dcb38ff2.41_0#1770359301"
        },
    {
        'url':"https://shop.sprouts.com/api/v2/store_products?ads_enabled=true&ads_pagination_improvements=true&allow_autocorrect=true&limit=60&offset=0&search_provider=ic&search_term=apple&secondary_results=true&sort=rank&unified_search_shadow_test_enabled=false",
        'cookie':"_gcl_au=1.1.521922636.1706679984; _fbp=fb.1.1706679988441.575132951; BVBRANDID=48829252-2d8f-4a5a-a583-e4783d338dcf; _pin_unauth=dWlkPU5qZ3pPVEEyWWpJdFpqWXpaUzAwTVRsa0xUaGtOakV0WXpJM1lqaGpPREF4TW1Zeg; ajs_anonymous_id=a97a839a-1b07-4021-a894-5e50b55564e6; _pin_unauth=dWlkPU5qZ3pPVEEyWWpJdFpqWXpaUzAwTVRsa0xUaGtOakV0WXpJM1lqaGpPREF4TW1Zeg; ajs_anonymous_id=a97a839a-1b07-4021-a894-5e50b55564e6; __stripe_mid=dd8bfc00-c656-4337-999c-dff73174b742cb83d4; loyaltyID=undefined; _gid=GA1.2.552717278.1707113988; BVBRANDSID=26334da0-c691-4e0e-af1a-f6e1ed46b80a; __cf_bm=llii48jpvLSgH1M6UmN.O3Ws5YYL7uDChvt7Nmyqb_M-1707114522-1-AcnwuxQK1a+ZbPzFQNIeE/1dqVlkBRkrQ4yBHoPXBg3hbFiqOGXvi21c+PieRPdceG/3Qno5WfJq+Yu8rVai3f4=; _gat_UA-47434162-1=1; dotcomSearchId=e33f95fa-4077-4c06-96b5-b03f5a3de153; __stripe_sid=028d58e3-ea7b-4de3-b533-78cf9ccdb590259959; session-sprouts=.eJwdjsFugjAAQP-lZ2MKEze4LcRoiS3KwCIXglChUKqhoJbFf1-zw7u8y3u_IL8OTDXAuxZCsQXI72zoC8nkCLxxmIxRTCl-k_l465gEHmA6aC7bkoc8QMmMLMIDd2mkVdonbZhLWzwuwr1nPlqjNugJjcR5Puo9TZyMJiPZbjTx4QrHAd_HGJK2dvB28zT-RTRSSJ7mLA2uBT3ysEWQzN-vME5M6MnPNBoL6vy3Ult0qL1PFX2pvW-mendi1HpUKeahjHRFE4V60VTmA8flk7TnjzDuHCzhMtdwx7vDbsYHmNWqV0jUSvw0fZTTNB7robkVlcKypV9gASbFhpxXwLNXn9ByHWf9_gOm3Wum.GKISFQ.ReS4D-eMm0TNlfs2KgdrXqbYdVo; _ga=GA1.2.853090590.1706679987; _uetsid=aee9e660c3ef11ee9dcb5594a497be15; _uetvid=14be1f60bffc11eea5691fbf32dcaa28; _ga_LPZ816BHL5=GS1.1.1707113988.6.1.1707114646.33.0.0; _dd_s=rum=1&id=b38a0299-e820-435e-825d-cc015233d2ec&created=1707114623230&expire=1707115547590"
        },

    ]

searchterm = 'Apple'


cookie = competitor_list[2]['cookie']


HEADERS = {

    'Accept-Language': "en-US,en;q=0.9,hi;q=0.8",
    'User-Agent' : "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36(KHTML, like Gecko) Chrome/103.0.5060.53 Safari/537.36",
    #user agent is a string of information that a web browser or other application sends to a web server as part of an HTTP request. 
    'Cookie': cookie    
}

URL = competitor_list[2]['url']+"apple"

responses = requests.get(URL,headers=HEADERS)
data = responses.json()

items = data.get('items')

for item in items:         
    print(item.get('name'))
    
print("==========================================================")   
# this will print all value that named {searchterm = 'Apple}


for item in items:
    for category in item.get('categories'):
        # print(category.get('name'))
        # if(category.get('name')=='Fresh Fruits' or 'Fruits'):
        if(category.get('name')=='Fresh Fruits' or 'Fruits'):
            if(searchterm in item.get('name')):
                print(item.get('name'))
    # if (searchterm in item.get('name')):
        # print(item.get('name'))

