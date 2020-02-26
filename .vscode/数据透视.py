import pandas as pd
import numpy as np
table = pd.read_excel(r'I:\Python\发货商品明细 (8.18-8.27) - 副本.xlsx')
table['year'] = pd.DatetimeIndex(table['支付时间']).year
groups = table.groupby(['品牌','year'])
s = groups['成本金额'].sum()
c = groups['平台单号'].count()
pt2=pd.DataFrame({'sum':s,'count':c})
print(pt2)
pt2.to_excel(r'g:\1.xlsx')
# pt1 = table.pivot_table(index='品牌', columns='year',
#                        values=['成本金额'], aggfunc=np.sum)
# print(pt1)
# print(table.head())
