#!/usr/bin/env python
# coding: utf-8

# In[1]:


tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
tel


# In[2]:


tel['jack']


# In[3]:


del tel['sape']
tel['irv'] = 4127
tel


# In[4]:


list(tel)


# In[5]:


sorted(tel)


# In[6]:


'guido' in tel


# In[7]:


'jack' not in tel


# In[8]:


dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])


# In[9]:


{x: x**2 for x in (2, 4, 6)}


# In[10]:


dict(sape=4139, guido=4127, jack=4098)


# In[ ]:




