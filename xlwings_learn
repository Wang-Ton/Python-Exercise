#%%
import tushare as tushare
import xlwings as xw
excel = xw.App()
excel.books.add()
wb = excel.books.open(r'G:\1.xlsx')
ws = wb.sheets.add()
ws.name = '我的工作表'
ws = wb.sheets[0]
r = ws.range('A2')
print(r.value)
#%%
import tushare
import pandas as pd
s =tushare.get_today_all()
s.to_excel(r'g:\2.xlsx')


# %%
