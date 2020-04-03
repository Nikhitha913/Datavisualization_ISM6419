#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd
Location = "Desktop/Data Visualization/python/datasets/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[14]:


bins = [0, 80, 100]


# In[17]:


result_names = ['Fail', 'Pass']


# In[18]:


df['result'] = pd.cut(df['grade'], bins, labels=result_names)
df.head()


# In[ ]:




