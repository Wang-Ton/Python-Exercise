# %%
from urllib.request import urlopen
from bs4 import BeautifulSoup
r = urlopen('https://www.boc.cn/sourcedb/whpj/')
c = r.read()
bs_obj = BeautifulSoup(c)
t = bs_obj.find_all('table')[1]
alltr = t.find_all('tr')
alltr.pop(0)
for r in alltr:
    alltd = r.find_all('td')
    print(f'{alltd[0].text} 卖出价 {alltd[4].text}')
# %%
