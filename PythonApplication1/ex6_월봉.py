import pyupbit
import pandas as pd

# 값이 너무 크거나 작으면 e 형태로표현되는거 방지
pd.options.display.float_format = '{:.1f}'.format
df = pyupbit.get_ohlcv(ticker="KRW-BTC", interval="month")
print(df)