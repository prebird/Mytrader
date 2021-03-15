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

# 지정가 주문을 통해서 매매 금액보다 낮게 주문을 넣기
# 홈페이지 보고 최소수량 이상으로 주문해야함
# resp = upbit.buylimit_order("KRW-XRP", 525, 2)
# pprint.pprint(resp)


# 주문을 하면 부여되는 고유 아이디(uuid)로 주문취소할수잇음
# 지정가 매도
# xrp_balance = upbit.get_balance("KRW-XRP")
# resp = upbit.sell_limit_order("KRW-XRP", 265, xrp_balance)
# pprint.pprint(resp)
