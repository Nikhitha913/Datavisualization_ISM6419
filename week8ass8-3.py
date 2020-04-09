#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
Location = "datasets/gradedata.csv"
df = pd.read_csv(Location) 
df.head()


# In[9]:


plt.scatter(df['hours'], df['grade'],color= 'red', alpha =0.1)
plt.xlabel("Hours")
plt.ylabel("Grades of students")
plt.title("Scatter plot")


# There is a pattern present in the data. As the number of hours increases the grades of the students also increased.

# In[ ]:




