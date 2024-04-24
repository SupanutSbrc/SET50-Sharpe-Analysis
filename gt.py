for i in range(len(interval[i])):
    conclu['sname'] = conclu['SET50'].str[4:]
    plt.figure(figsize=(16,6))
    colors = ['red' if x <0 else 'green' for x in conclu['sharpe']]
    plt.bar(conclu['sname'], conclu['sharpe'],color = colors)
    plt.xlabel('Stocks')
    plt.ylabel('Sharpe Ratio')
    plt.title(interval[i])
    plt.xticks(rotation=90)
    plt.show()
