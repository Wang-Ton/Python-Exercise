# %%
import pandas as pd
table_1 = pd.read_excel(r'I:\Python\books.xlsx', sheet_name='Sheet1')
table_2 = pd.read_excel(r'I:\Python\books.xlsx', sheet_name='Sheet2')
#多表追加
books = table_1.append(table_2).reset_index(drop=True)
#追加一行
newbook = pd.Series({'id': 41, 'name': 'Nature',
                     'Nov': 11, 'Dec': 33, 'Oct': 67})
books = books.append(newbook, ignore_index=True)
#修改单个值或者修改一行
#books.at[39,'name']='Red & Black'
# books.at[39,'Oct']=55
newbook = pd.Series({'id': 39, 'name': 'Red & Black',
                     'Nov': 31, 'Dec': '', 'Oct': 37})
books.iloc[39] = newbook
#插入一行：先生成一行，然后切片原表，再拼接
newbook = pd.Series({'id': 101, 'name': 'Faith',
                     'Nov': 31, 'Dec': 32, 'Oct': 37})
Part1 = books[:20]
Part2 = books[20:]
books = Part1.append(newbook, ignore_index=True).append(
    Part2, ignore_index=True)
#批量删除含空值的行或者Nan值的行
#books.drop(index=[0,1,3],inplace=True)
#books.drop(index=range(0,10),inplace=True)
#books.drop(books[0:10].index,inplace=True)
missing = books.loc[books['Dec']=='']
books.drop(index=missing.index,inplace = True)
print(books)
#books=books.dropna(axis=0)

# %%
