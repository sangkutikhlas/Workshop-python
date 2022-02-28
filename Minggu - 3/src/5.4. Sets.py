#!/usr/bin/env python
# coding: utf-8

# In[1]:


basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed


# In[3]:


'orange' in basket                 # fast membership testing


# In[4]:


'crabgrass' in basket


# In[5]:


# Demonstrate set operations on unique letters from two words
a = set('abracadabra')
b = set('alacazam')
a


# In[7]:


a - b                              # letters in a but not in b


# In[8]:


a | b                              # letters in a or b or both


# In[9]:


a & b                              # letters in both a and b


# In[10]:


a ^ b                              # letters in a or b but not both


# In[11]:


a = {x for x in 'abracadabra' if x not in 'abc'}
a


# In[ ]:




