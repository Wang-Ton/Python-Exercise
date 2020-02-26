import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
sales = pd.read_excel(r'I:\Python\sales.xlsx', dtype={'Month': str})
print(sales)
slope,intercept,r,p,stderr = linregress(sales.index,sales.Revenue)
exp=sales.index*slope+intercept
#plt.bar(sales.index, sales.Revenue)
plt.scatter(sales.index, sales.Revenue)
plt.plot(sales.index,exp,color ='Orange')
plt.title(f'{slope}*x+{intercept}')
plt.xticks(sales.index, sales.Month, rotation=90)
plt.tight_layout()
plt.show()
