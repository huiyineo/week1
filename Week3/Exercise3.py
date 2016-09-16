
# Exercise 3.1 (numpy):
# Write a script which reads a matrix from a file like this one and 
# solves the linear matrix equation Ax=b 
# where b is the last column of the input-matrix and A is the other columns. 
# It is okay to use the solve()-function from numpy.linalg.
# Does the result make sense?

import numpy as np
def solveMatrix(filename):
	# load file into an 2d array with "," as separator between cols
	mat = np.loadtxt(filename, delimiter=',')
	a = mat[:,:-1]
	b = mat[:,-1]
	return np.linalg.solve(a, b)

# print(solveMatrix('XAhwshXe.txt'))
# Output: [-5.09090909  1.18181818  2.24242424]
# Traverse of b
# check soln
# np.allclose(np.dot(a, x), b) #where x is the output


# Exercise 3.2 (scipy):
# Write a script that reads in this list of points (x,y), fits/interpolates them with a polynomial of degree 3. 
# Solve for the (real) roots of the polynomial numerically using Scipy’s optimization functions (not the root function in Numpy). 
# Does the result make sense (plot something to check).

import scipy.optimize
import matplotlib.pyplot as plt
# load file into an 2d array
mat = np.loadtxt("ENyYffaq.txt")
x = mat[:,0]
y = mat[:,1]
coef = np.polyfit(x,y,3)
func = np.poly1d(coef)
print(scipy.optimize.brentq(func, x[0], x[-1]))

# graphical check
# x_new = np.linspace(x[0], x[-1], 5000) #calculate evenly spaced numbers over a x interval
# y_new = func(x_new)
# plt.plot(x,y,'o', x_new, y_new)
# plt.axhline(0, color='black')
# axes = plt.gca()
# axes.set_ylim([-1,1])
# axes.set_xlim([-2,-1])
# plt.show()


# Exercise 3.3 (pandas):
# Qns 1
# Using the movie-lens 1M data and pandas.read_table read in all three files (users, ratings, movies) into pandas DataFrames. 
# Use the data combining tools discussed above to combine these three objects into a single object named movie_data
import pandas
users = pandas.read_table("users.dat", delimiter= "::", names=["user_id", "gender", "age", "occp_code", "zip"], engine='python')
ratings = pandas.read_table("ratings.dat", delimiter= "::", names=["user_id", "movie_id", "rating", "timestamp"], engine='python')
movies = pandas.read_table("movies.dat", delimiter= "::", names=["movie_id", "title", "genre"], engine='python')
movie_data = users.merge(ratings, how="inner", on="user_id")
movie_data = movie_data.merge(movies, how="inner", on="movie_id")
# movie_data.to_csv("out.csv", "\t")

# Qns 2
# Use the movie_data object from the previous exercise and compute the following things:
# The 5 movies with the most number of ratings
# sorted in descending order by default
rate_count = movie_data['title'].value_counts()
top5 = rate_count.index.tolist()[:5]

# A new object called active_titles that is made up of movies each having at least 250 ratings
active_titles = rate_count[rate_count >= 250].index.tolist()
active_movies = movie_data[movie_data['title'].isin(active_titles)]

# For the subset of movies in the active_titles list compute the following:
# The 3 movies with the highest average rating for females. Do the same for males.
f_active_movie = active_movies.query('gender == "F"')[['title', 'rating']]
f_active_rating = f_active_movie.groupby(['title']).mean().sort_values('rating', ascending=False)
f_top3 = f_active_rating.index.tolist()[:3]

m_active_movie = active_movies.query('gender == "M"')[['title', 'rating']]
m_active_rating = m_active_movie.groupby(['title']).mean().sort_values('rating', ascending=False)
m_top3 = m_active_rating.index.tolist()[:3]

# The 10 movies men liked much more than women and the 10 movies women liked more than men 
# (use the difference in average ratings and sort ascending and descending).
# merge by index as titles are now in the index
b_active_rating = f_active_rating.merge(m_active_rating, right_index=True, left_index=True, how="inner", suffixes=('_f', '_m'))
b_active_rating['diff'] = b_active_rating['rating_f'] - b_active_rating['rating_m'].shift(-1)
print(b_active_rating.sort_values('diff', ascending=False).index.tolist()[:10]) #women more than men
print(b_active_rating.sort_values('diff', ascending=True).index.tolist()[:10]) #men more than women

# The 5 movies that had the highest standard deviation in rating.
sd = active_movies[['title', 'rating']].groupby(['title']).apply(lambda x: x.std())
sd_top5 = sd.sort_values('rating', ascending=False).index.tolist()[:5]
print(sd_top5)


#Exercise 3.4 (scikit-learn):
import json
import string
import random
import math
from sklearn import linear_model
from sklearn.metrics import accuracy_score

# open json file
with open('pizza-train.json') as data_file:    
    data = json.load(data_file)

random.shuffle(data)
textList = [] #textList will contain list of the text in bag-of-words form
wordList = [] #wordList will contain all the words in request_text in the whole json file

for i in range(len(data)):
    #remove punctuation and change all to lowercase
    words = "".join(l for l in data[i]['request_text'] if l not in string.punctuation).lower().split()
    textList.append(words)
    wordList += words
#ensure only unqiue words in list by using set
wordList = list(set(wordList))

bag_of_words = []
for text in textList:
    textCount = []
    for word in wordList:
        textCount.append(text.count(word))
    bag_of_words.append(textCount)

mark = math.ceil(len(bag_of_words)*0.9)
train_bag = bag_of_words[:mark]
test_bag = bag_of_words[mark:]

res = pandas.DataFrame(data)['requester_received_pizza'].values
train_res = res[:mark]
test_res = res[mark:]

lr = linear_model.LogisticRegression()
lr.fit(train_bag, train_res)
print(accuracy_score(test_res, lr.predict(test_bag)))


# Exercise 3.5 (cython):
import timeit
def sumFun():
	res = 0
	for i in range(10000):
		res += 1/(i+1)
	return res

def fast_sumFun():
	cdef double res = 0
	cdef int i
	for i in range(10000):
		res += 1/(i+1)
	return res

print timeit.Timer(sumFun()).timeit()

#http://cython.readthedocs.io/en/latest/src/tutorial/cython_tutorial.html



