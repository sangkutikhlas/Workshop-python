#!/usr/bin/env python
# coding: utf-8

# In[1]:


from sklearn import datasets
iris = datasets.load_iris()
digits = datasets.load_digits()


# In[2]:


print(digits.data)


# In[3]:


digits.target


# In[4]:


digits.images[0]


# In[5]:


from sklearn import svm
clf = svm.SVC(gamma=0.001, C=100.)


# In[6]:


clf.fit(digits.data[:-1], digits.target[:-1])


# In[8]:


clf.predict(digits.data[-1:])


# In[9]:


# Code source: Gaël Varoquaux
# Modified for documentation by Jaques Grobler
# License: BSD 3 clause

from sklearn import datasets

import matplotlib.pyplot as plt

# Load the digits dataset
digits = datasets.load_digits()

# Display the last digit
plt.figure(1, figsize=(3, 3))
plt.imshow(digits.images[-1], cmap=plt.cm.gray_r, interpolation="nearest")
plt.show()

