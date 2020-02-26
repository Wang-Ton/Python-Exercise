#%%
import pandas as pd

df = pd.read_excel(r'I:\Python\duplication.xlsx')
#df.drop_duplicates(subset='name',inplace=True,keep='first')
#print(df)
dupe=df.duplicated(subset='name')
#print(dupe)
#print(dupe.any())
dupe = dupe[dupe==True] #等同于 dupe = dupe[dupe] 
print(dupe.index)
print(df.iloc[dupe.index])



#%%
