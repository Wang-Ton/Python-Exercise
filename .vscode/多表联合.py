#%%
import pandas as pd
students = pd.read_excel(r'I:\Python\join查询.xlsx',sheet_name='Students',index_col='ID')
score = pd.read_excel(r'I:\Python\join查询.xlsx',sheet_name='Score',index_col='ID')
#table = students.merge(score,on='ID',how='left').fillna(0)
#table = students.merge(score,left_on='ID',right_on='ID',how='left').fillna(0)
#table = students.merge(score,on=students.index,how='left').fillna(0)
table = students.join(score,how='left').fillna(0)
table.Score = table.Score.astype(int)
print(table)


#%%
