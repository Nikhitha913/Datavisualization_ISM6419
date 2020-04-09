#!/usr/bin/env python
# coding: utf-8

# In[16]:


import pandas as pd


# In[17]:


names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,95,77,78,99]
bsdegrees = [1,1,0,0,1]
msdegrees = [2,1,0,0,0]
phddegrees = [0,1,0,0,0]


# In[18]:


GradeList = zip(names,grades,bsdegrees,msdegrees,phddegrees)
columns = ['Names','Grade','BS','MS','PhD'] 
df = pd.DataFrame(data = GradeList, columns=columns)
df


# In[19]:


print("Number of values of given data")
df.count()


# In[20]:


print("Arithmetic average")
df.mean()


# In[21]:


print("standard deviation")
df.std()


# In[22]:


print("Minimum values")
df.min()


# In[23]:


print("Maximum values")
df.max()


# In[24]:


print("First quartile")
df.quantile(.25)


# In[25]:


print("Second quartile")
df.quantile(.5)


# In[26]:


print("Third quartile")
df.quantile(.75)


# In[27]:


print("Median of the data")
df.median()


# In[28]:


print("Mode of the data")
df.mode()


# In[29]:


print("Variance of the data")
df.var()


# In[ ]:




