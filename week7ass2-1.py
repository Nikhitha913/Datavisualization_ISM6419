#!/usr/bin/env python
# coding: utf-8

# In the datasets/weekly_call_data folder, there are 104 files of weekly call data for two years. Your task is to try to load
# all of that data into one dataframe.

# In[1]:


import pandas as pd
import numpy as np
import glob


# In[32]:


all_data = pd.DataFrame()
for f in glob.glob("Desktop/Data Visualization/python/datasets/datasets/weekly_call_data/weekdata*.xlsx"):
    df = pd.read_excel(f)
    all_data = all_data.append(df,ignore_index=True)


# In[33]:


all_data.head()


# In[34]:


all_data.describe()


# In[ ]:




