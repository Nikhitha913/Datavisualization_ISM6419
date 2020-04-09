#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[8]:


import numpy as np
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[10]:


df1 = df.take(np.random.permutation(len(df))[:500])
df1


# In[ ]:




