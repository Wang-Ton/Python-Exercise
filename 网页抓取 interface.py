from urllib.request import urlopen
from bs4 import BeautifulSoup
from tkinter import Tk, Button, Text


def download():
    c = urlopen('https://www.boc.cn/sourcedb/whpj/').read()
    bs_obj = BeautifulSoup(c, features='lxml')
    alltr = bs_obj.find_all('table')[1].find_all('tr')
    for r in alltr[1:]:
        alltd = r.find_all('td')
        t1.insert('end', f'{alltd[0].text} 卖出价 {alltd[4].text}\n')


def save():
    f = open('d:/currency.txt', 'w')
    f.write(t1.get(1.0, 'end'))
    f.close()


fm_main = Tk()
b1 = Button(fm_main, text='获取外汇牌价', command=download)
b2 = Button(fm_main, text='保存到文件', command=save)
t1 = Text(fm_main)

b1.pack()
b2.pack()
t1.pack()
fm_main.mainloop()
