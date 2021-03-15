# 시세 캔들 조회
import pyupbit

df = pyupbit.get_ohlcv("KRW-BTC", "minute1")
print(df)
