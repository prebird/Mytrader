import pyupbit
import pprint

f = open("C:\\Users\\jung\\Desktop\\pytext.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()

upbit = pyupbit.Upbit(access, secret)
# resp = upbit.buy_market_order("KRW-CHZ", 10)
#pprint.pprint(resp)