#%%
import pandas as pd 
df = pd.read_excel(r"I:\Python\books.xlsx",skiprows=3,usecols ='c:f',dtype={'id':str,'instore':str})
for i in range(20):
    df["id"].at[i]=i+1
    df.at[i,'instore']= 'Yes' if i%2==0 else 'No'

#%%
import pandas as pd
from datetime import date
price = pd.read_excel("i:\Python/price.xlsx",index_col = "id")
price['Price']=price['ListPrice']*price['Discount']
price['Price']=price['Price'].apply(lambda x: x+0.2)
price["Date"] = None
start = date(2019,1,1)
for i in price.index:
    price.at[i,"Date"]= date(start.year,start.month,start.day+i)
print(price.head(5))
#for i in price.index:
#   price.at[i,'Price']=price.at[i,'ListPrice']*price.at[i,'Discount']
#%%
