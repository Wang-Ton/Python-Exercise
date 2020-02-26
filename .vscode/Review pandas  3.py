#%%
import pandas as pd
from datetime import date,timedelta
def add_month(d,md):
    yd = md // 12
    m = d.month + md % 12
    if m != 12:
        yd += m//12
        m = m % 12
    return date(d.year+yd,m,d.day)
books = pd.read_excel(r"I:\Python\books.xlsx",skiprows=3,usecols="c:f",index_col=None,
        dtype={"id":str,'instore':str,'date':str})
start = date(2018,1,1)
for i in books.index:
    books["id"].at[i] = i+1  
    books['instore'].at[i] = 'Yes' if i%2==0 else 'No'
    books['date'].at[i] = add_month(start,i)
    #books['date'].at[i] = date(start.year+i,start.month,start.day)
print(books)
#%%
