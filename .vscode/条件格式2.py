#%%
import pandas as pd
import seaborn as sns
color_map=sns.light_palette('green',as_cmap=True)
table = pd.read_excel(r'I:\Python\books.xlsx')
table.style.background_gradient(color_map,subset=['Oct','Nov','Dec','Totals'])

# %%
import pandas as pd
table = pd.read_excel(r'I:\Python\books.xlsx')
table.style.bar(color='Orange',subset=['Oct','Nov','Dec','Totals'])


# %%
