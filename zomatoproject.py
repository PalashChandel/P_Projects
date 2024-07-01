#!/usr/bin/env python
# coding: utf-8

# In[ ]:


"F:\DOWNLOADS\zomatoarchive (1)\zomato.csv"


# In[14]:


import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import seaborn as sns
get_ipython().run_line_magic('matplotlib', 'inline')


# In[2]:


df = pd.read_csv("F:\DOWNLOADS\zomatoarchive (1)\zomato.csv")


# In[3]:


df.drop(["url","address","phone","menu_item"],axis=1,inplace = True)


# In[4]:


df.head()


# In[7]:


df.shape


# In[6]:


df.isna().sum()


# In[11]:


#Data cleaning
feature_na=[i for i in df.columns if df[i].isnull().sum()>0]
feature_na


# In[16]:


for i in feature_na:
    print(f"{i} has {np.round((df[i].isnull().sum()/len(df[i])*100),4)}% null values")


# In[18]:


df.rate.unique()


# In[19]:


df.dropna(subset=['rate'],axis=0,inplace=True)


# In[20]:


def split(x):
    return x.split('/')[0].strip()


# In[22]:


df['rate']=df['rate'].apply(split)


# In[23]:


df['rate']


# In[25]:


df.rate.unique()


# In[26]:


df['rate'].replace(['NEW','-'],0,inplace=True)


# In[27]:


df.info()


# In[28]:


df['rate']=df['rate'].astype(float)


# In[29]:


df.info()


# In[31]:


rating=pd.pivot_table(df,index='name',values='rate')
rating


# In[32]:


rating=rating.sort_values(['rate'],ascending=False)
rating[0:15]


# In[35]:


plt.figure(figsize=(10,8))
sns.barplot(x=rating[0:20].rate,y=rating[0:20].index,orient="h")
plt.show()


# In[36]:


sns.set_style('whitegrid')
sns.distplot(df['rate'])
plt.show()


# In[38]:


from scipy.stats import normaltest
Datatotest=df['rate']
stat,p=normaltest(Datatotest)

print("stat =%0.2f,p=%0.30f"%(stat,p))

if p>0.05:
    print("Normal distribution")
else:
    print("Not a normal distribution")


# In[39]:


df['name'].value_counts()


# In[42]:


plt.figure(figsize=(10,7),dpi=110)
chains=df['name'].value_counts()[0:15]

sns.barplot(x=chains,y=chains.index,palette='deep')
plt.xlabel("no. of outlets")

plt.show()


# In[44]:


x=df.online_order.value_counts()
labels=['accepted','not-accepted']
plt.pie(x,labels=labels,explode=[0.0,0.1],autopct='%1.1f%%')

plt.show()


# In[45]:


x=df.book_table.value_counts()
labels=['accepted','not-accepted']
plt.pie(x,labels=labels,explode=[0.0,0.1],autopct='%1.1f%%')


# In[47]:


df.head(5) #ananlysis on type of resturatnt


# In[48]:


df.rest_type.unique()


# In[49]:


len(df.rest_type.unique())


# In[50]:


df.rest_type.value_counts()


# In[53]:


plt.figure(figsize=(20,12))
rest_type=df.rest_type.value_counts()[0:15]
plt.bar(rest_type.index,rest_type)

plt.show()


# In[55]:


df.head() #which restaurant had the highest voting? meas count of rating given


# In[56]:


voting=df.groupby('name')[['votes']].mean()
voting


# In[57]:


voting['votes'].describe()


# In[58]:


high_vot=voting[voting['votes']>5000]


# In[64]:


plt.figure(figsize=(20,12),dpi=100)
plt.barh(high_vot.index,high_vot['votes'])
plt.show()


# In[66]:


df.head(3) #highly rated and worst rest on ratings


# In[68]:


sns.distplot(df['votes'])
plt.show()


# In[69]:


voting_rating=df.groupby('name')[['votes']].mean().sort_values('votes',ascending=False)
voting_rating


# In[70]:


voting_rating['name']=voting_rating.index


# In[71]:


voting_rating=voting_rating.reset_index(drop=True)
voting_rating.head()


# In[72]:


voting_rating=pd.merge(voting_rating,df[['rate','name']])
voting_rating


# In[73]:


vote_top=voting_rating[voting_rating['votes']>5000]
vote_top.head()


# In[74]:


vote_top=vote_top.groupby('name')[['rate']].mean().sort_values('rate',ascending=False)
vote_top


# In[76]:


plt.figure(figsize=(20,8),dpi=100)
sns.barplot(x=vote_top['rate'],y=vote_top.index,orient='h')
plt.show()


# In[77]:


bad_count=voting_rating[(voting_rating['rate']<3)&(voting_rating['rate']>0)]
bad_count


# In[79]:


bad_resturants=bad_count[bad_count['votes']>500].groupby('name')[['rate']].mean()
bad_resturants


# In[81]:


plt.figure(figsize=(20,8))
sns.barplot(x=bad_resturants['rate'],y=bad_resturants.index)
plt.show()


# In[82]:


df.head()


# In[83]:


location_restro=df[['location']].value_counts()[0:20]
location_restro


# In[85]:


plt.figure(figsize=(25,8))
sns.countplot(x=df['location'])

plt.xticks(rotation=90)
plt.show()


# In[86]:


df.head()


# In[88]:


df.rest_type.value_counts()


# In[92]:


cusin=df.cuisines.value_counts()[0:10]
print(cusin)
sns.barplot(x=cusin.index,y=cusin)
plt.xticks(rotation=75)
plt.show()


# In[93]:


df['approx_cost(for two people)'].isna().sum()


# In[94]:


df.dropna(axis=0,subset=['approx_cost(for two people)'],inplace=True)


# In[95]:


df['approx_cost(for two people)']


# In[ ]:




