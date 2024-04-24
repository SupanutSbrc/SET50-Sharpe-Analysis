interval = ['1Y-sharpe', '3Y-sharpe', '5Y-sharpe', '10Y-sharpe']
r_interval = ['1Y-avg_r','3Y-avg_r','5Y-avg_r','10Y-avg_r']
std_interval = ['1Y-std','3Y-std','5Y-std','10Y-std']
conclu = pd.DataFrame(name, columns=['SET50'])
for i in range (len(interval)):
    if i == 0 :
        wo = 12
    elif i == 1:
        wo = 36
    elif i == 2:
        wo = 60
    else:
        wo = 120
    mean_list = []
    std_list = []
    for i in range (len(name)):
        mean = df_return[name[i]].iloc[-wo:].mean() * 12
        mean_list.append(mean)
        std = df_return[name[i]].iloc[-wo:].std() * sqrt(12)
        std_list.append(std)
    
    conclu[r_interval[i]] = np.array(mean_list)
    conclu[std_interval[i]] = np.array(std_list)
    conclu['rrf'] = rf
    conclu[interval[i]] = (conclu['avg_return']-conclu['rrf'])/conclu['std']
    conclu = conclu.sort_values(by=[interval[0]])