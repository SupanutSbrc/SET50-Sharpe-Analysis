from tvDatafeed import TvDatafeed, Interval
import pandas as pd
import numpy as np
from scipy.stats import gmean
from math import sqrt
import matplotlib.pyplot as plt

tv = TvDatafeed()
print('')
month = int(input('Analysis of the last ______ months:'))
month += 1
df = tv.get_hist(symbol='SET:SET50', exchange='SET', interval=Interval.in_monthly, n_bars=month)
set50 = df[['close']]
set50.rename(columns = {'close':'set50'}, inplace=True)

name = ['SET:ADVANC', 'SET:AOT', 'SET:AWC', 'SET:BANPU', 'SET:BBL', 'SET:BDMS', 'SET:BEM', 'SET:BGRIM', 'SET:BH', 'SET:BTS', 'SET:CBG', 'SET:CENTEL', 'SET:COM7', 'SET:CPALL', 'SET:CPF', 'SET:CPN', 'SET:CRC', 'SET:DELTA', 'SET:EA', 'SET:EGCO', 'SET:GLOBAL', 'SET:GPSC', 'SET:GULF', 'SET:HMPRO', 'SET:INTUCH', 'SET:IVL', 'SET:KBANK', 'SET:KCE', 'SET:KTB', 'SET:KTC', 'SET:LH', 'SET:MINT', 'SET:MTC', 'SET:OR', 'SET:OSP', 'SET:PTT', 'SET:PTTEP', 'SET:PTTGC', 'SET:RATCH', 'SET:SAWAD', 'SET:SCB', 'SET:SCC', 'SET:SCGP', 'SET:TISCO', 'SET:TOP', 'SET:TRUE', 'SET:TTB', 'SET:TU', 'SET:WHA', 'SET:TLI']

#load all set50 data
for i in range (len(name)):
    df = tv.get_hist(symbol=name[i], exchange='SET', interval=Interval.in_monthly, n_bars=month)
    df = df[['close']]
    set50 = pd.merge(set50, df, left_index=True, right_index=True, how='outer')
    set50.rename(columns = {'close':name[i]}, inplace=True)
#print(set50)

df_return = set50.pct_change() * 100
#drop nan based on stocks with the least histirical data
df_return = df_return.dropna()
#print(df_return)

#data of the current month assumes price closes at current price
mean_list = []
std_list = []

for i in range (len(name)):
    mean = df_return[name[i]].mean() * 12
    mean_list.append(mean)
    std = df_return[name[i]].std() * sqrt(12)
    std_list.append(std)

rf = 2.269432

#currently there is a problem with real-time data on tradingview, when the problem is fixed, use the code below instead of typing risk-free rate manually

############rfr = tv.get_hist(symbol='TVC:TH01Y', exchange='TVC', interval=Interval.in_monthly, n_bars=1)
############rf = rfr['close'][0]

print(rf)
conclu = pd.DataFrame(name, columns=['SET50'])
conclu['avg_return'] = np.array(mean_list)
conclu['std'] = np.array(std_list)
conclu['rrf'] = rf
conclu['sharpe'] = (conclu['avg_return']-conclu['rrf'])/conclu['std']
conclu = conclu.sort_values(by=['sharpe'])

neg = conclu[conclu['sharpe'] < 0]
print("Stocks that underperform the risk-free rate:")
print(neg[['SET50','sharpe']])

# Print stocks with positive Sharpe ratio
pos = conclu[conclu['sharpe'] >= 0]
print("\nStocks that outperformed risk-free rate:")
print(pos[['SET50','sharpe']])

good = conclu[conclu['sharpe'] >= 1]
print("\nStocks with acceptable performance:")
print(good[['SET50','sharpe']])