# %%
import pymysql
database = pymysql.connect('127.0.0.1', 'root', 'wat263', 'db', charset='utf8')
cursor = database.cursor()  # 初始化指针
# 增
# 格式 insert into
# sql = "INSERT INTO data (ID,Date,Company,Province,Price,Weight) value ('1231231','2019-02-04','武汉仓','湖北','12.5','3.3');"
# cursor.execute(sql)
# database.commit()
# database.close()
# 改
# 格式 UPDATE 表名 SET 字段1=内容1 WHERE 条件;
# sql ="UPDATE data SET Date='2020-02-04' WHERE Date='2019-02-04'"
# cursor.execute(sql)
# database.commit()
# database.close()
#查
#SELECT 字段 FROM 表 WHERE 条件
# sql = "SELECT Company,sum(Weight) FROM data WHERE Province='广东';"
# cursor.execute(sql)
# result = cursor.fetchall()
# print(result)
#删
#DELETE FROM 表名 WHERE 条件；
sql = "DELETE FROM data WHERE ID='1231231';"
cursor.execute(sql)
database.commit()
database.close()

# %%
