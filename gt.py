import requests
from bs4 import BeautifulSoup
url = 'https://www.thaiwarrant.com/dw/search'
head = Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36

print('0')
response = requests.get(url, headers={Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36})
print('yes')
if response.status_code == 200:
    print('1')
    bs = BeautifulSoup(url,'html.parser')
    print('2')
    table = bs.find(lambda tag: tag.name=='table' and tag.has_attr('id') and tag['id']=="MainContent_gvDWSearch")
    print('3')
    rows = table.findAll(lambda tag: tag.name=='tr')
    print('4')
    rows
else:
    print("failed")
