#!/usr/bin/env python
# coding: utf-8

# In[1]:


def ask_ok(prompt, retries=4, reminder='Please try again!'):
    while True:
        ok = input(prompt)
        if ok in ('y', 'ye', 'yes'):
            return True
        if ok in ('n', 'no', 'nop', 'nope'):
            return False
        retries = retries - 1
        if retries < 0:
            raise ValueError('invalid user response')
        print(reminder)


# In[2]:


i = 5

def f(arg=i):
    print(arg)

i = 6
f()


# In[3]:


def f(a, L=[]):
    L.append(a)
    return L

print(f(1))
print(f(2))
print(f(3))


# In[5]:


def f(a, L=None):
    if L is None:
        L = []
    L.append(a)
    return L


# In[6]:


def parrot(voltage, state='a stiff', action='voom', type='Norwegian Blue'):
    print("-- This parrot wouldn't", action, end=' ')
    print("if you put", voltage, "volts through it.")
    print("-- Lovely plumage, the", type)
    print("-- It's", state, "!")


# In[7]:


parrot(1000)                                          # 1 positional argument
parrot(voltage=1000)                                  # 1 keyword argument
parrot(voltage=1000000, action='VOOOOOM')             # 2 keyword arguments
parrot(action='VOOOOOM', voltage=1000000)             # 2 keyword arguments
parrot('a million', 'bereft of life', 'jump')         # 3 positional arguments
parrot('a thousand', state='pushing up the daisies')  # 1 positional, 1 keyword


# In[8]:


parrot()                     # required argument missing
parrot(voltage=5.0, 'dead')  # non-keyword argument after a keyword argument
parrot(110, voltage=220)     # duplicate value for the same argument
parrot(actor='John Cleese')  # unknown keyword argument


# In[12]:


def function(a):
     pass
    function(0, a=0)
    Traceback (most recent call last):


# In[13]:


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])


# In[14]:


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


# In[15]:


def standard_arg(arg):
     print(arg)

def pos_only_arg(arg, /):
     print(arg)

def kwd_only_arg(*, arg):
     print(arg)

def combined_example(pos_only, /, standard, *, kwd_only):
     print(pos_only, standard, kwd_only)


# In[16]:


standard_arg(2)


# In[17]:


standard_arg(arg=2)


# In[18]:


pos_only_arg(1)


# In[19]:


pos_only_arg(arg=1)


# In[20]:


kwd_only_arg(3)


# In[21]:


combined_example(1, 2, 3)


# In[22]:


combined_example(1, 2, kwd_only=3)


# In[23]:


combined_example(1, standard=2, kwd_only=3)


# In[24]:


combined_example(pos_only=1, standard=2, kwd_only=3)


# In[25]:


def foo(name, **kwds):
    return 'name' in kwds


# In[26]:


foo(1, **{'name': 2})


# In[27]:


def foo(name, /, **kwds):
    return 'name' in kwds
foo(1, **{'name': 2})


# In[28]:


def f(pos1, pos2, /, pos_or_kwd, *, kwd1, kwd2):


# In[29]:


def write_multiple_items(file, separator, *args):
    file.write(separator.join(args))


# In[30]:


def concat(*args, sep="/"):
     return sep.join(args)
concat("earth", "mars", "venus")


# In[31]:


concat("earth", "mars", "venus", sep=".")


# In[32]:


list(range(3, 6))            # normal call with separate arguments


# In[33]:


args = [3, 6]
list(range(*args))            # call with arguments unpacked from a list


# In[34]:


def parrot(voltage, state='a stiff', action='voom'):
     print("-- This parrot wouldn't", action, end=' ')
     print("if you put", voltage, "volts through it.", end=' ')
     print("E's", state, "!")
d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)


# In[35]:


def make_incrementor(n):
     return lambda x: x + n

f = make_incrementor(42)
f(0)


# In[36]:


f(1)


# In[37]:


pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs


# In[38]:


def my_function():
     """Do nothing, but document it.

     No, really, it doesn't do anything.
     """
pass
print(my_function.__doc__)


# In[39]:


def f(ham: str, eggs: str = 'eggs') -> str:
     print("Annotations:", f.__annotations__)
     print("Arguments:", ham, eggs)
     return ham + ' and ' + eggs
f('spam')


# In[ ]:




