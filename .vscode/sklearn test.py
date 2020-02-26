# %%
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
from sklearn import datasets
# %%
iris = datasets.load_iris()
# %%
iris.keys()
# %%
print(iris.DESCR)
# %%
iris.data

# %%
iris.data.shape
# %%
iris.feature_names
# %%
# %%
iris.target
iris.target.shape
# %%
iris.target_names
# %%
X = iris.data[:, :2]
X.shape
# %%
plt.scatter(X[:, 0], X[:, 1])
plt.show()

# %%
y = iris.target
plt.scatter(X[y == 0, 0], X[y == 0, 1], marker='o')
plt.scatter(X[y == 1, 0], X[y == 1, 1], marker='x')
plt.scatter(X[y == 2, 0], X[y == 2, 1], marker='+')

# %%
X = iris.data[:, 2:]
X.shape
# %%
y = iris.target
plt.scatter(X[y == 0, 0], X[y == 0, 1], marker='o')
plt.scatter(X[y == 1, 0], X[y == 1, 1], marker='x')
plt.scatter(X[y == 2, 0], X[y == 2, 1], marker='+')

# %%
