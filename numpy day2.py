#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


h = [30,20,3,6,9]
h


# In[8]:


a=[]
for i in h:
    a.append(i+7)
print(a)


# In[9]:


#tuple
s = (3,6,9)
s


# In[10]:


type(s)


# In[14]:


a = list(s)
b = []
for i in a:
    b.append(i**2)
s = tuple(b)
s


# In[16]:


z = []
for i in s:
    if i>50:
        z.append(i)
print(i)


# In[17]:


#appending in an array / in an array loops and statements are not required
arr = np.array([3,6,9,36,69])
arr


# In[18]:


arr+7


# In[19]:


x = arr**2
x


# In[20]:


arr>90


# In[21]:


arr<90


# In[22]:


arr>36


# In[23]:


arr[3:9:6]


# In[24]:


arr [arr>36]


# In[25]:


s


# In[38]:


type(s)


# In[40]:


index = []
for i in range(len(b)):
    if b[i]>20:
        index.append(i)
    index


# In[ ]:




