#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from sklearn import kernel_approximation


# In[2]:


rng = np.random.RandomState(0)
X = rng.rand(10, 2000)
X = np.array(X, dtype='float32')
X.dtype


# In[3]:


transformer = kernel_approximation.RBFSampler()
X_new = transformer.fit_transform(X)
X_new.dtype


# In[4]:


from sklearn import datasets
from sklearn.svm import SVC
iris = datasets.load_iris()
clf = SVC()
clf.fit(iris.data, iris.target)


# In[5]:


list(clf.predict(iris.data[:3]))


# In[6]:


clf.fit(iris.data, iris.target_names[iris.target])


# In[7]:


list(clf.predict(iris.data[:3]))


# In[ ]:




