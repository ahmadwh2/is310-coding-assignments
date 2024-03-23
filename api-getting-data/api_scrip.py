import requests
import json
import apikey


apikey.save("api_key", "b0f7542d06260597ecb997cdc8a67dd9ee555c55")

api_key = apikey.load("api_key")
url = 'https://api.jcdecaux.com/vls/v1/stations?contract=bruxelles&apiKey='
response = requests.get(url + api_key)
with open('jdcecaux_developer.json', 'w') as f:
    json.dump(response.json(), f)