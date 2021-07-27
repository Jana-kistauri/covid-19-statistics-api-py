import requests
import json

url = "https://covid-19-coronavirus-statistics.p.rapidapi.com/v1/total"

country = input("შეიტანეთ ქვეყანა: ")

querystring = {"country":country}

headers = {
    'x-rapidapi-key': "1f77456fcamsh4ff879ab310009bp13f2e9jsna2ba84228f3c",
    'x-rapidapi-host': "covid-19-coronavirus-statistics.p.rapidapi.com"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

data = json.loads(response.text)

print("Country:",data['data']['location'])
print("Last report:", data['data']['lastReported'])
print("Confirmed:",data['data']['confirmed'])
print("Recovered:",data['data']['recovered'])
print("Deaths:",data['data']['deaths'])


