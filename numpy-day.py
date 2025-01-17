#!/usr/bin/env python
# coding: utf-8

# In[1]:


#numpy
import numpy as np

#numpy :- array operations

#pandas :- Data manipulation and analysis

#matplotlib :- Graphical analysis

#sklearn :- Mavhine learning algorithms and techniques

#statsmodels :- Statistical analysis

#scipy :- Statistical analysis


# In[2]:


import numpy as np
o = [3,6,9,12]


# In[3]:


d = np.array(o)
print(d)


# In[4]:


tuple(o)


# In[5]:


type(o)


# In[6]:


d.shape


# In[7]:


d.ndim


# In[9]:


d.size


# In[11]:


d = [[12,28,11],[3,6,9],[999,333,666],[11,22,33]]
d


# In[13]:


z = np.array(d)
z


# In[14]:


z.shape


# In[15]:


z.ndim


# In[16]:


z.reshape


# In[25]:


z.reshape(3,3,3,3)


# In[22]:


z.reshape(2,4)


# In[23]:


z.ndim


# In[27]:


#range function
list(range(-9,-3))


# In[28]:


list(range(-3,-9,-3))


# In[29]:


list(range(0,10,))


# In[30]:


#arrange the values in an even and odd based on their index value
j = [30,60,90,36,69,99,66,33]


# In[36]:


x=[]
y=[]
for i in range(len(j)):
    if i%2==0:
        x.append(j[i])
    else:
        y.append(j[i])


# In[37]:


x


# In[38]:


y


# In[ ]:




