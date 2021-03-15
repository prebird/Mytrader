import pyupbit
import time
import datetime

# https://www.youtube.com/watch?v=MW0WJHLHg6A&list=PLNPt2ycoheHrJBpCkpE2h4OBR8oxYyU3p&index=18

def cal_target(ticker):
    df = pyupbit.get_ohlcv(ticker, "day")
    yesterday = df.iloc[-2]
    today = df.iloc[-1]
    yesterday_range = yesterday['high'] - yesterday['low']
    target = today['open'] + yesterday_range*0.5
    return target


# 객체생성
f = open("C:\\Users\\jung\\Desktop\\pytext.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close
upbit = pyupbit.Upbit(access, secret)

# 변수설정
hold = False # 코인을 보유하고 있냐 없냐
op_mode = False #작동
target = cal_target("KRW-BTC")

while True:
    now =datetime.datetime.now()

    # 09:00:00 목표가 갱신
    if now.hour == 9 and now.minute == 0 and 20 <=now.second <=30:
        target = cal_target("KRW-BTC")
        time.sleep(10) # 09:00:20 ~ 09:00:30
        op_mode = True

    # 현재가격 받아오기
    price = pyupbit.get_current_price("KRW-BTC")
    time.sleep(1)

    # 조건을 계속 비교하다가 매수
    if op_mode is True and price is not None and price >=target and hold is False:
        # krw_balance = upbit.get_balance("KRW")
        # upbit.buy_market_order("KRW-BTC", krw_balance * 0.1)
        hold = True


    # 매도기능 08:59:50 초에 전량 매도
    if now.hour == 8 and now.minute == 59 and 50<=now.second<=59:
        if op_mode is True and hold is True:
            btc_balance = upbit.get_balance("KRW-BTC")
            upbit.sell_market_order("KRW-BTC, btc_balance")
            hold = False

        # 새로운 거래일에서 목표가 갱신될 때 까지 거래가 되지 않게
        op_mode = False
        time.sleep(10)

    # 상태 출력
    print(f"현재시간:{now} 목표가:{target} 현재가:{price} 보유상태:{hold} 동작상태:{op_mode}")
    
    time.sleep(1)

