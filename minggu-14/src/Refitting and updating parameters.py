#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
from sklearn.datasets import load_iris
from sklearn.svm import SVC
X, y = load_iris(return_X_y=True)


# In[2]:


clf = SVC()
clf.set_params(kernel='linear').fit(X, y)


# In[3]:


clf.predict(X[:5])


# In[4]:


clf.set_params(kernel='rbf').fit(X, y)


# In[5]:


clf.predict(X[:5])


# In[ ]:




