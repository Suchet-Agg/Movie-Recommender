import pymongo
from pymongo import MongoClient
from math import sqrt

#Global Variables
#Client
client = MongoClient()

#Database
db = client.mydb
#Collections
movies = db.movieds
ratings = db.ratingds
#Size of Dataset
numOfMovies = movies.find().count()
#Similarity Matrix
sim = [[0 for i in range(numOfMovies)] for j in range(numOfMovies)]


#Helper Functions
def square_rooted(x):
	"""Function Computes the denominator for cosine similarity funcition"""
	if x == []:
		return 1
	else:
		a = sqrt(sum([(a)**2 for a in x]))
		if a == 0:
			return 1
		else:
			return a
	
def cosine_similarity(x,y):
	"""Function Computes Cosine Similarity for two Given Movies"""
	numerator = sum((a)*(b) for a,b in zip(x,y))
	denominator = square_rooted(x)*square_rooted(y)
	return numerator/float(denominator)
	
def mean(n):
	"""Function Computes the average rating that a user gives to the movies to calculate normalised ratings"""
	summ=0
	for i in ratings.find({'userId':n}):
		summ+=i['rating']
	return (summ/ratings.find({'userId':n}).count())

#Main Code Starts hers

for m in range(numOfMovies):
	for n in range(m+1,numOfMovies):
		ls1=[]
		ls2=[]
		temp = 0
		s = 0
		usr1 = ratings.find({'movieId':m})
		usr2 = ratings.find({'movieId':n})
		i = 0
		j = 0	

		while(i<usr1.count() and j<usr2.count()):
			if usr1[i]['userId']==usr2[j]['userId']:
				 temp = mean(usr1[i]['userId'])
				 #print(usr1[i]['rating'],usr2[j]['rating'],temp)
				 ls1.append(usr1[i]['rating']-temp)
				 ls2.append(usr2[j]['rating']-temp)
				 i+=1
				 j+=1
			elif usr1[i]['userId']>usr2[j]['userId']:
				j+=1
			else:
				i+=1
		sim[m-2][n-2] = cosine_similarity(ls1,ls2)
		sim[n-2][m-2] = sim[m-2][n-2]

def denominator(mov):
	denim = 0
	for i in range(numOfMovies):
		denim+=sim[mov][i]
	if denim == 0:
		denim = 1
	return denim

#Calculate Rating(Predicted) for Current User

movs= []
user = ratings.find().sort('userId', pymongo.DESCENDING)[0]['userId']
#This Line Wouldn't Work for Now
user += 1
lsofmov =ratings.find( { 'userId': { "$ne": user } } )
for x in lsofmov:
	mov = x['movieId']
	den = denominator(mov)
	rate = 0
	for i in range(numOfMovies):
		rate += (sim[mov][i]*ratings.find({'userId':user,'movieId':i})[0]['rating'] / den)
	movs.append([mov,rate])
movs=movs.sort(key= lambda x :x[1])
print(movs)