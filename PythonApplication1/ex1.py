# Rest API
import requests
from requests.models import parse_header_links

url = "https://api.upbit.com/v1/market/all"
resp = requests.get(url)
data = resp.json() #리스트 타입으로 저장

krw_ticker = []
for coin in data:
    ticker = coin["market"]

    if ticker.startswith("KRW"):
        krw_ticker.append(ticker)
print(krw_ticker)

