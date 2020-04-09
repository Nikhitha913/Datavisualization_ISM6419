#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


Location = "datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[3]:


df = df.sort_values(by=['fname','age','grade'],ascending=[True, True, True])
df


# In[ ]:




