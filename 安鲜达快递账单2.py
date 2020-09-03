# %%
import pandas as pd
import numpy as np
import re
bcf = pd.read_excel(r'G:\工作备份\招联文件\安鲜达对账\账单-201912-三方-百富勤食品专营店.xlsx',
                    sheet_name='包材', index_col='订单流水号', usecols=['订单流水号', '包材辅料总费用'])
psf = pd.read_excel(r'G:\工作备份\招联文件\安鲜达对账\账单-201912-三方-百富勤食品专营店.xlsx',
                    sheet_name='配送', index_col='订单流水号', usecols=['订单流水号', "配送费用", '客户订单号', '重量(kg)', '收货人城市'])
ddf = pd.read_excel(r'G:\工作备份\招联文件\安鲜达对账\账单-201912-三方-百富勤食品专营店.xlsx',
                    sheet_name='订单', index_col='订单流水号', usecols=['订单流水号', '订单操作费', '日期', '仓库', '订单原料详情'])
Table = bcf.join(ddf, how='left').join(psf)
Column_sum = Table.sum(axis=1)
Table.insert(4, '合计', Column_sum)
#order = ['客户订单号', '包材辅料总费用', '订单操作费', '配送费用', '合计']
Table = Table[['日期', '客户订单号', '包材辅料总费用', '订单操作费',
               '配送费用', '合计', '仓库', '订单原料详情', '重量(kg)', '收货人城市']]
Table = Table.reset_index(drop=False)
Sum_weight = []
for i in range(Table.shape[0]):
    Data = Table.at[i, '订单原料详情']
    Data = re.findall(r"\d+\.?\d*", Data)
    Data = list(map(float, Data))
    x = Data[::2]
    y = Data[1::2]
    Produt_weight = list(map(lambda x, y: x*y, x, y))
    Sum_product_weight = sum(Produt_weight)
    Sum_weight.append(Sum_product_weight)
# print(Data)
# print(Sum_product_weight)


# for i in Table.shape[1]:
#    Table.iloc[i,'商品重量']=Table.iloc[i,'包材辅料总费用'].


# 将克数与数量相乘
# print(Table.head())
# Table.to_excel(r'g:\sum.xlsx')


# %%
