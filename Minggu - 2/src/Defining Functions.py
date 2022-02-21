#!/usr/bin/env python
# coding: utf-8

# In[1]:


def fib(n):    # write Fibonacci series up to n
     """Print a Fibonacci series up to n."""
     a, b = 0, 1
     while a < n:
         print(a, end=' ')
         a, b = b, a+b
     print()
# Now call the function we just defined:
fib(2000)


# In[2]:


fib


# In[3]:


f = fib
f(100)


# In[4]:


fib(0)
print(fib(0))


# In[5]:


def fib2(n):  # return Fibonacci series up to n
     """Return a list containing the Fibonacci series up to n."""
     result = []
     a, b = 0, 1
     while a < n:
         result.append(a)    # see below
         a, b = b, a+b
     return result
f100 = fib2(100)    # call it
f100                # write the result


# In[ ]:




