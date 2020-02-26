#%%
import pandas as pd
import matplotlib.pyplot as plt 
sells = pd.read_excel('I:\Python\sells.xlsx',index_col='name')
#sells['2017'].sort_values(ascending=False).plot.pie(fontsize=8,startangle=-270)
sells['2017'].plot.pie(fontsize=8,counterclock=True,startangle=-270,autopct='%2.1f%%',labels=None)
plt.title("sells counts",fontsize=12,fontweight='bold')
plt.ylabel('2017',fontsize=12,fontweight='bold',labelpad=35.5)
plt.legend(sells.index,bbox_to_anchor=(1.2,1.1))
plt.show
print(sells.iloc[:,[0]])
#%%
