#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
names = ['Bob','Jessica','Mary','John','Mel']
grades = [76,-2,77,78,101]
GradeList = zip(names,grades)
df = pd.DataFrame(data = GradeList,columns=['Names', 'Grades'])
df


# Using the dataset from this section, can you replace all the subzero grades
# with a grade of zero?

# In[2]:


df.loc[(df['Grades'] <= 0,'Grades')] = 0


# In[3]:


df


# In[ ]:




