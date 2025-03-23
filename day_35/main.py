import requests


url = "https://api.weatherapi.com/v1/current.json"
try:
    response = requests.get(url, params={
        "q": "Yangon",
        "aqi": "no",
        "key": "8b2f816cde2e468ba61151755230711"
    })
    if response.status_code:
        print(response.json())
except Exception as e:
    print(e)
