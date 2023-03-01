# Solution of Day 90 Exercise 10.

import requests
import json

secret_key = "8967df3b8d7642a39f687c109c6262f9"
query = input("What type of news are you interested in? ")
url = f"https://newsapi.org/v2/everything?q={query}&apiKey={secret_key}"
r = requests.get(url)
news = json.loads(r.text)
# print(news, type(news))
for article in news["articles"]:
    print(f"Title: {article['title']}")
    print(f"Description: {article['description']}")
    print("--------------------------------------")
