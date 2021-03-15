from os import name
from pandas import DataFrame
from pandas.core.accessor import register_dataframe_accessor
import pyupbit
import time
import datetime
import pandas as pd

# https://www.youtube.com/watch?v=MW0WJHLHg6A&list=PLNPt2ycoheHrJBpCkpE2h4OBR8oxYyU3p&index=18


# 객체생성
f = open("C:\\Users\\GDC7\\Desktop\\pytext.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close
upbit = pyupbit.Upbit(access, secret)


# 변수설정
coin_name = []
coin_prices = []
coin_2nd_prices = []
fst_time =datetime.datetime(2020,3,14,hour=17, minute=21, second=10)
snd_time =datetime.datetime(2020,3,14,hour=17, minute=22, second=30)
tickers = pyupbit.get_tickers()

# 특정 두시간 사이의 가격을 가져오는 함수

def get_price_at_time():
    now = datetime.datetime.now()
    coin_name_list=[]
    coin_prices_list=[]
    # 첫번째 시간의 가격
      
    print(f"it's {now}")
    get_current_price = pyupbit.get_current_price(ticker = tickers)
    coin_name_list,coin_prices_list = list(get_current_price.keys()), list(get_current_price.values())
    

    return coin_name_list, coin_prices_list


# 프로그램
while(True):
    now = datetime.datetime.now()
    nextOn = False
    # 시간 출력
    print(now)
    time.sleep(1)

    coin_name, coin_prices = get_price_at_time()
    coin_name, coin_2nd_prices = get_price_at_time()
    if len(coin_2nd_prices) > 0 : 
        nextOn = True
        print(coin_name)
        print(coin_prices)
        print(coin_2nd_prices)
    if nextOn ==True: break
    # 두 시간 사이 가격차이를 구해서 minus열 추가
    # if nextOn == True:
    #     df = pd.DataFrame({'name':coin_name, 'price':coin_prices, 'price2':coin_2nd_prices})

    #     rise_rate = (df['price'] - df['price2'])/df['price']
    #     df = df.assign(rise_rate = rise_rate)

    #     # 상승률 내림차순 정렬
    #     df.sort_values(by='rise_rate', ascending=False, inplace=True)
        
    #     # 상승률 높은 4개 구하기
    #     top4 = df["name"].head(4).values
    #     print("top4 : ",top4)


        # # 가격 상승률 높은 TOP5 구매
        # if nextOn is True and len(top4)>0:
        #     krw_balance = upbit.get_balance("KRW")
        #     for coin in top4:
        #         upbit.buy_market_order(ticker=coin, price = krw_balance * 0.25)
        #         time.sleep(1)

        #     break



# test
# get_current_price = pyupbit.get_current_price(ticker = tickers)
# coin_name,coin_prices = list(get_current_price.keys()), list(get_current_price.values())
# for i in range(60):
#     time.sleep(1)
#     print(i)

# get_current_price = pyupbit.get_current_price(ticker = tickers)
# coin_9_prices = list(get_current_price.values())

# df = pd.DataFrame({'name':coin_name, 'price':coin_prices, 'price9':coin_9_prices})

# print(df)
# # 동작
# while True:
#     now =datetime.datetime.now()

#     # 09:00:00 목표가 갱신
#     # if now.hour == 9 and now.minute == 0 and 20 <=now.second <=30:
#     #     target = cal_target("KRW-BTC")
#     #     time.sleep(10) # 09:00:20 ~ 09:00:30
#     #     op_mode = True

#     # 현재가격 받아오기
#     price = pyupbit.get_current_price("KRW-BTC")
#     time.sleep(1)

#     # 조건을 계속 비교하다가 매수
#     if op_mode is True and price is not None and price >=target and hold is False:
#         # krw_balance = upbit.get_balance("KRW")
#         # upbit.buy_market_order("KRW-BTC", krw_balance * 0.1)
#         hold = True


#     # 매도기능 08:59:50 초에 전량 매도
#     if now.hour == 8 and now.minute == 59 and 50<=now.second<=59:
#         # if op_mode is True and hold is True:
#         #     btc_balance = upbit.get_balance("KRW-BTC")
#         #     upbit.sell_market_order("KRW-BTC, btc_balance")
#         #     hold = False

#         # 새로운 거래일에서 목표가 갱신될 때 까지 거래가 되지 않게
#         op_mode = False
#         time.sleep(10)

#     # 상태 출력
#     print(f"현재시간:{now} 목표가:{target} 현재가:{price} 보유상태:{hold} 동작상태:{op_mode}")
    
#     time.sleep(1)

