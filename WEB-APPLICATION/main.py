from flask import Flask,render_template
from flask import request
#importing modules
import pandas as pd
import numpy as np
from scipy.sparse import csr_matrix
from sklearn.neighbors import NearestNeighbors
from matplotlib import pyplot as plt
app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template('index.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
      result = request.form
      for key,value in result.items():
         nameinput=value
      result=recommended_movies(nameinput)  
      return render_template("result.html",result = result)
movies = pd.read_csv("./dataset/movies.csv")
ratings = pd.read_csv("./dataset/ratings.csv")
#making a new dataframe where columns represent users and rows represent movies
new_dataset=ratings.pivot(index='movieId',columns='userId',values='rating')
#replacing the NaN values by 0, here NaN means the user has not rated that movie
new_dataset.fillna(0,inplace=True)
#removing noise
#here main thing is we will filter out movies that were rated very less and we will filter out users that rated only few movies
# To qualify a movie, a minimum of 10 users should have voted a movie.
# To qualify a user, a minimum of 50 movies should have voted by the user.
no_user_voted = ratings.groupby('movieId')['rating'].agg('count')
no_movies_voted = ratings.groupby('userId')['rating'].agg('count')
# DataFrame.loc[] method is a method that takes only index labels and returns row or dataframe if the index label exists in the caller data frame.
#This removes movies that were rated by less than 10 users.
new_dataset = new_dataset.loc[no_user_voted[no_user_voted > 10].index,:]
# DataFrame.loc[] method is a method that takes only index labels and returns row or dataframe if the index label exists in the caller data frame.
#This removes users rated less than 50 movies.
new_dataset = new_dataset.loc[:,no_movies_voted[no_movies_voted>50].index]
#The Compressed Sparse Row, also called CSR for short, is often used to represent sparse matrices in machine learning given the efficient access and matrix multiplication that it supports.
new_less_sparsed_data=csr_matrix(new_dataset)
new_dataset.reset_index(inplace=True)#restoring the new_dataset
#finally using KNN
knn = NearestNeighbors(metric='cosine', algorithm='brute', n_neighbors=20, n_jobs=-1)
knn.fit(new_less_sparsed_data)
#vvimp: your movie must be present in your dataset.
def recommended_movies(your_movie):
  n_movies_to_reccomend=5
  movie_idx = movies[movies['title'] == your_movie]
  movie_idx=movie_idx[['movieId']].iloc[0][0]
  movie_idx1 = new_dataset[new_dataset['movieId'] == movie_idx].index[0]
  distances , indices = knn.kneighbors(new_less_sparsed_data[movie_idx1],n_neighbors=n_movies_to_reccomend+1)#gives us the distances between our movie and other movies with less distances and their indices
  #we will sort the indices by their distances in ascending order
  rec_movie_indices = sorted(list(zip(indices.squeeze().tolist(),distances.squeeze().tolist())),key=lambda x: x[1])[:0:-1]
  #Above list looks like [(index,similarity measure),(),(),....]
  movies_recommended=[]
  for each in rec_movie_indices:
    movie_idx = new_dataset.iloc[each[0]]['movieId']
    movie_name=movies[movies['movieId'] == movie_idx]
    movie_name=movie_name[['title']].iloc[0][0]
    movies_recommended.append(movie_name)
  return movies_recommended
   
if __name__ == '__main__':
   app.run(debug="true")