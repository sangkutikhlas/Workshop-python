#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import LabelBinarizer


# In[2]:


X = [[1, 2], [2, 4], [4, 5], [3, 2], [3, 1]]
y = [0, 0, 1, 1, 2]


# In[3]:


classif = OneVsRestClassifier(estimator=SVC(random_state=0))
classif.fit(X, y).predict(X)


# In[4]:


y = LabelBinarizer().fit_transform(y)
classif.fit(X, y).predict(X)


# In[5]:


from sklearn.preprocessing import MultiLabelBinarizer
y = [[0, 1], [0, 2], [1, 3], [0, 2, 3], [2, 4]]
y = MultiLabelBinarizer().fit_transform(y)
classif.fit(X, y).predict(X)


# In[ ]:




