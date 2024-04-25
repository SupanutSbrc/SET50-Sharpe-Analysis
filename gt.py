for loop in range(3,120):
    df_X = df_return.copy()
    df_X = df_X[['set50']]
    df_X['set50'] = df_X['set50'].rolling(window=loop).std()
    for i in range(len(name)):
        df_X[name[i]] = df_return[name[i]].rolling(window=loop).std()
    df_X_shifted = df_X.shift(120)
    df_X_shifted
    stacked_X_shifted = df_X_shifted.stack(dropna=False).reset_index(drop=True)
    stacked_X_shifted
    newdf = pd.concat([stacked_X_shifted,stacked_y],axis=1, keys=['X','Y'])
    newdf = newdf.dropna()
    Y = newdf['Y']
    X= newdf['X']
    X = sm.add_constant(X)
    model = sm.OLS(Y,X)
    result = model.fit()
    newdf['Yhat'] = result.predict(X)
    mae = mean_absolute_error(newdf['Y'],newdf['Yhat'])
    error.append(mae)
