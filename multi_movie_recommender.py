# a421_multi_movie_recommender.py
# A basic movie recommendation code with normalization.

import numpy as np 

# define the movies, users, and different ratings
movies = ["Back to the Future", "Guardians of the Galaxy", "Avatar", "Trolls", "Black Panther"]
genres = ["Action", "Adventure", "Science Fiction", "Comedy"]

# Users
users = ["Student1", "Student2", "Student3"]

# Ratings: rows = users, columns = movies
movie_ratings = [
    [5, 4, 5, 2, 4],  # Student1
    [3, 3, 4, 5, 3],  # Student2
    [4, 5, 5, 3, 5]   # Student3
]

# User preferences: rows = users, columns = genres
user_preferences = [
    [5, 4, 5, 1],  # Student1
    [3, 3, 4, 5],  # Student2
    [4, 5, 5, 2]   # Student3
]

# Movie genre weights: rows = movies, columns = genres
movie_genre = [
    [0.6, 0.0, 0.3, 0.1], 
    [0.2, 0.3, 0.3, 0.2], 
    [0.3, 0.3, 0.4, 0.0], 
    [0.7, 0.0, 0.0, 0.3], 
    [0.1, 0.6, 0.3, 0.0]
]

# Your ratings (column vector: 5 movies x 1 user)
your_ratings = np.zeros((5, 1))
your_ratings[0] = 0  # Back to the Future
your_ratings[1] = 0  # Guardians of the Galaxy
your_ratings[2] = 0  # Avatar
your_ratings[3] = 0  # Trolls
your_ratings[4] = 0  # Black Panther

# --- Convert to numpy arrays ---
# Transpose so shape becomes (movies x users)
ratings = np.array(movie_ratings).T
movie_features = np.array(movie_genre)
user_prefs = np.array(user_preferences)

# Append your ratings as a new user (column)
ratings = np.append(your_ratings, ratings, axis=1)

# Matrix showing whether a movie was rated (1 = rated, 0 = not rated)
did_rate = (ratings != 0) * 1

# Function to normalize ratings
def normalize_ratings(ratings, did_rate):
    num_movies = ratings.shape[0]
    
    ratings_mean = np.zeros((num_movies, 1))
    ratings_norm = np.zeros(ratings.shape)
    
    for i in range(num_movies): 
        idx = np.where(did_rate[i] == 1)[0]
        
        if len(idx) > 0:
            ratings_mean[i] = np.mean(ratings[i, idx])
            ratings_norm[i, idx] = ratings[i, idx] - ratings_mean[i]
    
    return ratings_norm, ratings_mean

# Normalize the ratings
ratings_norm, ratings_mean = normalize_ratings(ratings, did_rate)

# --- Output predictions ---
print("\nPredicted ratings for each movie:\n")

for index in range(len(movies)):
    print("%.2f is predicted for the movie %s" % (ratings_mean[index], movies[index]))