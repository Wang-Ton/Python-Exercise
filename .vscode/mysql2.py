#%%
import pymysql
import pandas as pd
database = pymysql.connect('127.0.0.1','root','wat263','db',charset ='utf8')
cursor = database.cursor()
sql ="SELECT Company,COUNT(Company),SUM(Weight),SUM(Price),SUM(Price)/SUM(Weight) FROM data GROUP BY Company"
cursor.execute(sql)
result = cursor.fetchall()
data = pd.DataFrame(list(result))
data.columns = ['仓库','单量','重量','金额','单价']
data.to_excel(r'g:\1.xlsx')
# %%
