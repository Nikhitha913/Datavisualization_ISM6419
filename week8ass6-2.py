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


import statsmodels.formula.api as sm 
result = sm.ols(formula='grade ~ exercise + hours',data=df).fit()
result.summary()


# In[4]:


df['gendernumeric'] = np.where(df['gender']=='female',1, 0 )
df.head()


# In[5]:


import statsmodels.formula.api as sm 
result = sm.ols(formula='grade ~ gendernumeric + exercise + hours',data=df).fit()
result.summary()


# The R squared value is 0.664 and 0.665 in both cases. The adjusted R square has not been changed in both cases. So gender can be removed from this regression as it doesn't add any value

# In[ ]:




