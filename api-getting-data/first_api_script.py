import requests
import apikey


dpla_api_key = apikey.load("dpla_key")
url = 'https://api.dp.la/v2/items?q=kittens&api_key='
response = requests.get(url + dpla_api_key)
print(response.status_code)
import json

with open('dpla_kittens.json', 'w') as f:
    json.dump(response.json(), f)

dpla_data = response.json()
print(dpla_data.keys())
print('dataProvider', dpla_data['docs'][0]['dataProvider'])

print('isShownAt', dpla_data['docs'][0]['isShownAt'])

print('sourceResource', dpla_data['docs'][0]['sourceResource'])
print('object', dpla_data['docs'][0]['object'])
