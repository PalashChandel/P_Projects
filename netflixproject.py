#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np 
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns
import plotly.express as px
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


data = pd.read_csv("F:\\netflix\\netflix_titles.csv")
data.head()


# In[4]:


data.info()


# In[5]:


data.drop(columns=['show_id', 'cast', 'director', 'description'], inplace=True)

# Replacments
data['country'] = data['country'].fillna(data['country'].mode()[0])

# Drop the rest
data.dropna(inplace=True)


# In[ ]:


data["date_added"] = pd.to_datetime(data['date_added'])


# In[ ]:


data['principal_country'] = data['country'].apply(lambda x: x.split(",")[0])


# In[ ]:


ratings_ages = {
    'TV-PG': 'Older Kids',
    'TV-MA': 'Adults',
    'TV-Y7-FV': 'Older Kids',
    'TV-Y7': 'Older Kids',
    'TV-14': 'Teens',
    'R': 'Adults',
    'TV-Y': 'Kids',
    'NR': 'Adults',
    'PG-13': 'Teens',
    'TV-G': 'Kids',
    'PG': 'Older Kids',
    'G': 'Kids',
    'UR': 'Adults',
    'NC-17': 'Adults'
}

# Replace Rating values with age targets, they are based on
data['ages'] = data['rating'].replace(ratings_ages)
data['ages'].unique()


# In[ ]:


data.head()


# In[ ]:




