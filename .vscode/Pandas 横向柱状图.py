#%%
#水平柱状图
import pandas as pd 
import matplotlib.pyplot as plt
books = pd.read_excel(r'I:\Python\books.xlsx',index_col='id')
books['Totals'] = books['Oct']+books['Nov']+books['Dec']
books.sort_values(by='Totals',inplace=True,ascending=True)
books.plot.barh(x='name',y=['Oct','Nov','Dec'],stacked=True,title='UserView')
plt.tight_layout
plt.show
#%%
