for i in range (len(name)):
    df = tv.get_hist(symbol=name[i], exchange='HKEX', interval=Interval.in_daily, n_bars=961)
    df = df[['close']]
    print(len(df))
    hk50 = pd.merge(hk50, df, left_index=True, right_index=True, how='outer')
    hk50.rename(columns = {'close':name[i]}, inplace=True)
