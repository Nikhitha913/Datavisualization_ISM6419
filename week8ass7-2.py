#!/usr/bin/env python
# coding: utf-8

# In[10]:


import matplotlib.pyplot as plt
import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
status = ['Senior','Freshman','Sophomore','Senior','Junior']
grades = [76,95,77,78,99]
GradeList = zip(status,grades)
df = pd.DataFrame(data = GradeList, columns=['Status', 'Grades'])
get_ipython().run_line_magic('matplotlib', 'inline')
df = df.set_index(df['Status'])
df.plot(kind='bar')


# In[ ]:




