interval = ['1Y-sharpe', '3Y-sharpe', '5Y-sharpe', '10Y-sharpe']
r_interval = ['1Y-avg_r','3Y-avg_r','5Y-avg_r','10Y-avg_r']
std_interval = ['1Y-std','3Y-std','5Y-std','10Y-std']
conclu = pd.DataFrame(name, columns=['SET50'])
for j in range (len(interval)):
    if j == 0 :
        wo = 12
    elif j == 1:
        wo = 36
    elif j == 2:
        wo = 60
    else:
        wo = 120
    mean_list = []
    std_list = []
    for k in range (len(name)):
        mean = df_return[name[k]].iloc[-wo:].mean() * 12
        mean_list.append(mean)
        std = df_return[name[k]].iloc[-wo:].std() * sqrt(12)
        std_list.append(std)
    conclu['rrf'] = rf
    conclu[r_interval[j]] = np.array(mean_list)
    conclu[std_interval[j]] = np.array(std_list)
    conclu[interval[j]] = (conclu[r_interval[j]]-conclu['rrf'])/conclu[std_interval[j]]
