#%%
import numpy as np
import matplotlib as npl
import matplotlib.pyplot as plt

# %%
x= np.linspace(0,10,100)

# %%
y=np.sin(x)

# %%
plt.plot(x,y)
plt.show()
# %%
cosy=np.cos(x)
# %%
siny = y.copy()
# %%
plt.plot(x,siny,linestyle =':',label = 'sinx')
plt.plot(x,cosy,color='red',linestyle ='--',label = 'cosx')
plt.xlabel('sinx')
plt.ylabel('cosy')
plt.legend()
plt.title('ML World')
plt.show()

# %%
plt.scatter(x,siny)
plt.scatter(x,cosy)
plt.show
# %%
x=np.random.normal(0,1,10000)
y=np.random.normal(0,1,10000)
plt.scatter(x,y,alpha = 0.1)
plt.show()
# %%
