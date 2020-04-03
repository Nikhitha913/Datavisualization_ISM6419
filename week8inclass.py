#!/usr/bin/env python
# coding: utf-8

# In[79]:


import pandas as pd 
import matplotlib.pyplot as plt
Location = "C:/Users/nikhi/Desktop/Data Visualization/03-11-2020.csv" 
df = pd.read_csv(Location)


# In[82]:


df_3 = df.groupby('Country/Region')['Confirmed'].sum()


# In[86]:


df1 = df_3.to_frame()


# In[87]:


df1.loc['Total'] = pd.Series(df1['Confirmed'].sum(), index = ['Confirmed'])


# In[89]:


def color_red(value):

  if value > 500:
    color = 'red'
  else:
    color = 'black'

  return 'color: %s' % color


# In[90]:


df1.style.applymap(color_red)


# In[ ]:




