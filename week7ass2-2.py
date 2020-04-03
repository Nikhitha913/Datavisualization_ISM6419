#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd


# In[18]:


from sqlalchemy import create_engine
# Connect to sqlite db 
db_file = r'Desktop/Data Visualization/python/datasets/salesdata.db' 
engine = create_engine(r"sqlite:///{}"
                       .format(db_file)) 


# In[19]:


sql = "select name from sqlite_master"    
"where type = 'table';"


# In[20]:


test = pd.read_sql(sql, engine) 


# In[15]:


print(test.iloc[0])


# In[16]:


sql = 'SELECT * from {};'.format(test.iloc[0].iloc[0])


# In[21]:


sales_data_df = pd.read_sql(sql, engine)


# In[22]:


sales_data_df


# In[ ]:




