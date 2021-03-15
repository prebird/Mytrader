import pyupbit
from pyupbit.exchange_api import Upbit

# 현재가 얻어오기
price = pyupbit.get_current_price("KRW-BTC")
print(price)

# 여러개의 데이터 받기
# ticker를 리스트 형태로 전달하기
tickers = ["KRW-BTC","KRW-CHZ"]
price = pyupbit.get_current_price(ticker=tickers)
# 딕터형태로반환
print(price)

# 원화시장에서 거래되는 모든 티커의 가격
tickers = pyupbit.get_tickers()
all_price = pyupbit.get_current_price(ticker=tickers)
print(all_price)

for k,v in all_price.items():
    print("{0} : {1}".format(k, v))