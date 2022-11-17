#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
import pandas as pd


# In[4]:


column_names = ['user_id','item_id','rating','timestamp']
df = pd.read_csv("C:/Users/90507/Desktop/Dersler/users.data" , sep='\t' , names=column_names)


# In[5]:


df.head()


# In[6]:


#To see how many records there are in total
len(df)


# In[8]:


#Now lets download other files

movie_titles = pd.read_csv("C:/Users/90507/Desktop/Dersler/movie_id_titles.csv")
movie_titles.head()


# In[9]:


len(movie_titles)


# In[10]:


df = pd.merge(df, movie_titles, on='item_id')
df.head()


# In[11]:


moviemat = df.pivot_table(index='user_id',columns='title',values='rating')
moviemat.head()


# In[12]:


starwars_user_ratings = moviemat['Star Wars (1977)']
starwars_user_ratings.head()


# In[13]:


#Our goal is to find movies similar to STARWARS.
similar_to_starwars = moviemat.corrwith(starwars_user_ratings)


# In[14]:


similar_to_starwars


# In[15]:


corr_starwars = pd.DataFrame(similar_to_starwars, columns=['Correlation'])
corr_starwars.dropna(inplace=True)
corr_starwars.head()


# In[16]:


corr_starwars.sort_values('Correlation',ascending=False).head(10)


# In[17]:


#As you can see, there were irrelevant results. Let's eliminate movies with less than 100 votes to avoid irrelevant results.
#Let's find the average value of each movie.
ratings = pd.DataFrame(df.groupby('title')['rating'].mean())
ratings.sort_values('rating',ascending=False).head()


# In[ ]:




