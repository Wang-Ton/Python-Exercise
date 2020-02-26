# %%
import os
import pandas as pd
filename = os.listdir('d:/')
data = pd.DataFrame(filename)
data.columns = ['文件名']
data.to_excel(r'd:\1.xlsx', index=False)


# %%
