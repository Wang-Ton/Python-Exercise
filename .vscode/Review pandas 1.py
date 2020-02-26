# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
# ms-python.python added
import os

#%%
#%%
#%%
import pandas as pd

try:
	os.chdir(os.path.join(os.getcwd(), '.ipynb_checkpoints'))
	print(os.getcwd())
except:
	pass

d = {"x":100,"y": 200 ,"z":300,"r":400}
s1 = pd.Series(d)
print (s1)
print (s1.index)


#%%
L1 = [100,200,300]
L2 = ["x","y","z"]
s2 = pd.Series(L1,index = L2)
print(s2)


#%%
s1 = pd.Series([1,2,3],index=[1,2,3],name= "A")
s2 = pd.Series([10,20,30],index=[1,2,3],name= "B")
s3 = pd.Series([100,200,300],index=[1,2,3],name= "C")
df = pd.DataFrame({s1.name:s1,s2.name:s2,s3.name:s3})
pf = pd.DataFrame([s1,s2,s3])
print(df)
print(pf)

#%%
#df = pd.read_excel("I:\Python\excercise.xlsx",header = 0 ,index_col = "id")
#print(df.head(5))
#print(df.tail(5))
gf = pd.read_excel("E:\对账\汇通物流单.xlsx",index_col="订单编号")
print(gf.head(1))
L1 = ([i for i in range(1, 7)])
L2 = [1,2,3,4,5,6]
print(L1)
s1 = pd.Series(L1,index=L2,name="a")
s2 = pd.Series(L2,index=L1,name="b")
print (s1)
print (s2)
df=pd.DataFrame({s1.name:s1,s2.name:s2})
df.set_index("b",inplace = True)
print(df)
#%%
