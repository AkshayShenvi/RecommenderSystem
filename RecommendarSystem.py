# -*- coding: utf-8 -*-
"""
Created on Sat Apr 27 14:57:15 2019

@author: akshay
"""

import pandas as pd



# Load movies Metadata
metadata = pd.read_csv('movie_metadata.csv')
metadata.head(3)

#Calculate C

C = metadata['imdb_score'].mean()
print(C)


# Minimum number of votes required to be  in the chart, m

m= metadata['num_voted_users'].quantile(0.90)
print(m)

# Filter out all the qualified movies

qualified_movies = metadata.copy().loc[metadata['num_voted_users'] >= m]
qualified_movies.shape

def weighted_ratings(x,m=m,C=C):
    v= x['num_voted_users']
    R = x['imdb_score']
    return (v/(v+m)* R)+ (m/(m+v)*C)

qualified_movies['score']=  qualified_movies.apply(weighted_ratings,axis=1)
qualified_movies =qualified_movies.sort_values('score',ascending=False)
qualified_movies[['movie_title','num_voted_users','imdb_score','score']].head(15)

