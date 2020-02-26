import pandas as pd
df=pd.read_excel(r'I:\Python\books.xlsx',index_col ='id')
table=df.transpose()
print(table)