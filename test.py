import csv
import requests
url = 'https://api.burl=ikebros.co.jp/v1/bike//bike_model_detail.jsonp?bike_model_id=13521'
#url = 'https://api.zipaddress.net/?zipcode=5770056'
user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.131 Safari/537.36"
headers = {
    "Host": "api.bikebros.co.jp",
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:77.0) Gecko/20100101 Firefox/77.0",
"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
"Accept-Language": "ja,en-US,en;q=0.5",
"Accept-Encoding": "gzip, deflate, br",
"Referer": "https://www.google.com/",
"DNT": "1",
"Connection": "keep-alive",
"Upgrade-Insecure-Requests": "1"
}
res = requests.get(url, headers=headers)
print(res.json())
data = res.json()
print(data)