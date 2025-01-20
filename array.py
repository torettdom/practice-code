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


# In[3]:


import numpy as np
arr = np.array([3,6,9,36,69,11,28,12,369])
arr


# In[4]:


arr[-2:-7:-1]


# In[5]:


arr.ndim


# In[14]:


arr =(3,6,9,36,69,11,28,12,369,36,66,99)
arr


# In[19]:


import numpy as np  # Import numpy

np.random.seed(96)  # Set the seed for reproducibility
arr = np.random.randint(3, 6, size=(12, 28))  # Generate random integers in the range [3, 6) with size (12, 28)
print(arr)

#This code will correctly generate a 12x28 array of random integers between 3 and 5 (inclusive of 3, exclusive of 6).


# In[24]:


#[6:10] is the rows from where we want the data
#[5:18] is the coloms from where we want the data
arr[6:10,5:18]


# In[25]:


arr[3:6:9]


# In[22]:


#3 is the row which we selected 5 is the start and 20 is the stop
arr[3,5:20]


# In[7]:


arr[1:6:2,1:6]


# In[8]:


print(arr)


# In[10]:


import numpy as np
arr = np.array([3,6,9,36,69,11,28,12,369])
arr


# In[13]:


import numpy as np  # Import numpy

np.random.seed(96)  # Set the seed for reproducibility
arr = np.random.randint(3, 9, size=(12, 28))  # Generate random integers in the range [3, 6) with size (12, 28)
print(arr)


# In[14]:


arr[1:6:2,1:6:2]


# In[ ]:




