import requests
from bs4 import BeautifulSoup
import pandas as pd
url = 'https://www.thaiwarrant.com/dw/search'
head = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'

print('0')

html = requests.get(url, headers={'User-Agent': head}).content
df_list = pd.read_html(html)
df = df_list[2]
df = df.drop(df.columns[8],axis =1).drop(df.columns[7],axis =1).drop(df.columns[6],axis =1).drop(df.columns[5],axis =1).drop(df.columns[3],axis =1).drop(df.columns[0],axis =1)
df
