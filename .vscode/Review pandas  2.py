# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% [markdown]
# # 新建EXCEL文件并写入数据

#%%
# import pandas as pd

df = pd.DataFrame({'id':[1,2,3,4,5,6,7,8,9,10]})
df.to_excel("i://Python/output.xlsx")
print("done")

#%% [markdown]
# # 读取文件

#%%
import pandas as pd

excercise = pd.read_excel("i://Python/output.xlsx",header = None)
print(excercise.shape)
excercise.columns = ["id","name"]
excercise.set_index("id",inplace=True)
#excercise = excercise.set_index("id")
print(excercise.head(3))
print(excercise.tail(2))
excercise.to_excel("i://Python/excercise.xlsx")
print("done")
df = pd.read_excel("i://Python/excercise.xlsx",index_col = "id")
print(df.head)


#%%



