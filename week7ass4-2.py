#!/usr/bin/env python
# coding: utf-8

# Can you create a column for timemgmt that shows busy if a student exercises more than three hours per week AND studies more 
# than seventeen hours per week?

# In[1]:


import pandas as pd
Location = "Desktop/Data Visualization/python/datasets/datasets/gradedata.csv"
df = pd.read_csv(Location)
df.head()


# In[7]:


import numpy as np
df['timemgmt'] = np.where((df['exercise']>3) & (df['hours'] > 17),'busy', 'not busy')
df.tail(10)


# In[ ]:




