from tvDatafeed import TvDatafeed, Interval
import pandas as pd
import numpy as np
from math import sqrt

tv = TvDatafeed()

df = tv.get_hist(symbol='SET:SET50', exchange='SET', interval=Interval.in_daily, n_bars=4500)
from statsmodels.tsa.stattools import adfuller
result = adfuller(df['close'], autolag='BIC')
print(result[1])
returns = np.log(df['close']).diff().dropna() #1st difference

result = adfuller(returns, autolag='BIC')
print(result[4])
print(result[0])
print(result[1])
returns_train, returns_test= returns[:-120], returns[-120:]
from arch import arch_model
garch_model_fit = arch_model(returns_train,vol="Garch",p=1,q=1).fit(disp='off')
print(garch_model_fit.summary)
arch_model_fit = arch_model(returns_train,vol="ARCH").fit(disp='off')
print(arch_model_fit.summary)
egarch_model_fit = arch_model(returns_train,vol="EGARCH",p=1,q=1).fit(disp='off')
print(egarch_model_fit.summary)

realized_volatility = np.log(df['high']/df['low'])
realized_volatility = realized_volatility.iloc[1:]
realized_volatility = realized_volatility
realized_volatility_train, realized_volatility_test= realized_volatility[:-120], realized_volatility[-120:]