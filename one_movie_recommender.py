#   a421_one_movie_recommender.py
#   A basic movie recommendation code using average for a single user and single movie.
#   This code is based on the netflix-style-recommender project shared on GitHub.
#   It was written by Nikhil22.
#   The code has been modified from its original version.
import numpy as np 

# define the movies, users, and different ratings
movies = ["Back to the Future", "Guardians of the Galaxy", "Avatar", "Trolls", "Black Panther"]
genres = ["Action", "Adventure", "Science Fiction", "Comedy"]

#TODO 1 change these values to the names of the students in your group
users = ["Student1", "Student2", "Student3"]

#TODO 2 paste your ratings tables here
movie_ratings = [
    [5, 4, 5, 2, 4],  # Student1
    [3, 3, 4, 5, 3],  # Student2
    [4, 5, 5, 3, 5]   # Student3
]
user_preferences = [
    [5, 4, 5, 1],  # Student1
    [3, 3, 4, 5],  # Student2
    [4, 5, 5, 2]   # Student3
]
movie_genre = [[0.6, 0.0, 0.3, 0.1], 
               [0.2, 0.3, 0.3, 0.2], 
               [0.3, 0.3, 0.4, 0.0], 
               [0.7, 0.0, 0.0, 0.3], 
               [0.1, 0.6, 0.3, 0.0]]

# Single user's rating 
# change these values to compare the ratings of different users and different movies
rating = 0 # a starting rating
user = 2 # represents the third user in the list of users
movie = 3 # represents the fourth movie in the list of movies

# get the estimated rating for a specific movie and a specific user
for genre in range(len(genres)):
    rating += user_preferences[user][genre] * movie_genre[movie][genre]
print(users[user]+"'s", movies[movie], "recommended rating: ", rating) 

