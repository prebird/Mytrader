import pyupbit
import pprint

f = open("C:\\Users\\jung\\Desktop\\pytext.txt")
lines = f.readlines()
access = lines[0].strip()
secret = lines[1].strip()
f.close()
# print(access,"\n",secret)

# 가진 모든 자산
upbit = pyupbit.Upbit(access, secret)
balances = upbit.get_balances()
# pprint.pprint(balances)

# xrp limit order 
xrp_price = pyupbit.get_current_price("KRW-XRP")
print(xrp_price)

