# Exercise 10 NewsApi.

import requests
import pprint

secret_key = "8967df3b8d7642a39f687c109c6262f9"

url = "https://newsapi.org/v2/everything?"

parameters = {"q": "cricket", "pageSize": 20, "apiKey": secret_key}
response = requests.get(url, params=parameters)
responseJson = response.json()
pprint.pprint(responseJson)

for i in responseJson['articles']:
    print(i['title'])
