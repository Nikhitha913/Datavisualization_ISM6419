#!/usr/bin/env python
# coding: utf-8

# Can you make a dataframe from a file you have uploaded and imported on your own? Let's find out. Go to the following website, which contains U.S. Census data (http://census.ire.org/data/bulkdata.html), anddownload the CSV datafile for a state. Now, try to import that data into Python.

# In[6]:


import pandas as pd
#Location = "florida_total_populaion.csv"
df = pd.read_csv("florida_total_population.csv")


# In[7]:


df


# In[ ]:




