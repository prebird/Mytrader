import pyupbit
import pprint

f = open("C:\\Users\\jung\\Desktop\\pytext.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()

upbit = pyupbit.Upbit(access, secret)

## uuid에 접근해 캔슬함
#resp = upbit.cancel_order(uuid='')
#print(resp)

# 구매
# resp = upbit.buy_limit_order("KRW-XRP", 100, 100)
# uuid = resp['uuid']
# print(uuid)

 # 취소
uuid = '4f7a312a-481c-40cf-8556-c9c9b1bb12a6'
resp = upbit.cancel_order(uuid)
pprint.pprint(resp)
