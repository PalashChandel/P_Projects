#!/usr/bin/env python
# coding: utf-8

# In[2]:


import pandas as pd

df=pd.read_csv("F:\DOWNLOADS\googleplaystore.csv")


# In[3]:


df.head()


# In[4]:


df.info()


# In[5]:


print("\n'Rating' Column Info:")
print(df['Rating'].info())



# In[15]:


print("\nMissing Values in DataFrame:")
print(df.isnull().sum())


df = df.dropna(subset=['Rating'])


df['Reviews'] = df['Reviews'].fillna('0')

df['Reviews'] = pd.to_numeric(df['Reviews'], errors='coerce')




# In[6]:


df['Size'] = df['Size'].apply(lambda x: x.replace('M', '').replace('k', '').replace('+', '').replace(',', '') if isinstance(x, str) else x)
df['Size'] = pd.to_numeric(df['Size'], errors='coerce')


df['Installs'] = df['Installs'].apply(lambda x: x.replace('+', '').replace(',', '') if isinstance(x, str) else x)
df['Installs'] = pd.to_numeric(df['Installs'], errors='coerce')


# In[19]:


df = df[(df['Rating'] >= 1) & (df['Rating'] <= 5)]


df['Category'] = df['Category'].str.lower()


df['Type'] = df['Type'].str.lower()


df['Content Rating'] = df['Content Rating'].str.lower()




# In[20]:


df = df.drop_duplicates()


df['Price'] = df['Price'].apply(lambda x: x.replace('$', '') if isinstance(x, str) else x)
df['Price'] = pd.to_numeric(df['Price'], errors='coerce')


print("\nCleaned DataFrame Info:")
df.info()


print("\nCleaned DataFrame:")
print(df.head())


df.to_csv("F:\\DOWNLOADS\\googleplaystore_cleaned.csv", index=False)


# In[8]:


df.Reviews.unique()


# In[10]:


pd.to_numeric(df.Reviews,errors="coerce")


# In[11]:


df.info()


# In[16]:


df["Content Rating"].isnull().sum()


# In[18]:


df["Type"].isna().sum()


# In[25]:


df["Price"].unique()


# In[26]:


df.info()


# In[27]:


df["Current Ver"].fillna(df["Current Ver"].mode()[0],inplace=True)
df["Android Ver"].fillna(df["Android Ver"].mode()[0],inplace=True)


# In[28]:


df.info()


# In[29]:


df.head()


# In[30]:


df.isna().sum()


# In[38]:


import matplotlib.pyplot as plt


# In[39]:


import seaborn as sns


# In[41]:


plt.figure(figsize=(10,10))
sns.barplot(x=df.Rating,y=df.Category)


# In[ ]:


# above conclusion is events are getting highest rating


# In[43]:


sns.boxplot(x=df.Rating)


# In[46]:


df["Android Ver"].mode()


# In[48]:


sns.distplot(df["Price"])


# In[ ]:


# maximum values are zero from above graph


# In[49]:


df["Genres"].mode()


# In[ ]:




