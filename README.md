# MRS
Movie Recommender System


***THE PROJECT DOESN'T WORK COMBINED AS A UNIT FOR NOW, BUT THE BACKEND AND FRONTEND WORK INDIVIDUALLY***
-------------------------------------------------------------------------------------
------------This is a Simple Implementation of a Movie Recommender System------------
-------------------------------------------------------------------------------------

Tools I Used:
-------------
1. Python
	Flask
	Pandas
	Pymongo
	json
	urllib
2.HTML
3.MongoDB
4.CSS
5.A bit of JavaScript
6.TMDB API

Resources Used:
---------------
1.BootStrap.com
2.https://pythonspot.com/flask-web-app-with-python/
3.http://api.mongodb.com/python/3.6.0/tutorial.html#counting
4.http://www.cs.carleton.edu/cs_comps/0607/recommend/recommender/itembased.html
5.http://jsfiddle.net/ashuslove/zLm4f/6/ (Star Rating System)

What I couldn't do:
-------------------
1. Reduce the running time of the algorithm, because of which the server often gives TimeOutError
2. Host the app on Heroku
3. Rating system is Broken 

To Run the App on a Local Machine:
----------------------------------
1. Firstly import the databases into Mongo
	mongoimport -d mydb -c movieds --type csv --file <LocationOfYourDirectory>/Movie_Recommender/ml-latest-small/movies.csv --headerline

	mongoimport -d mydb -c ratingds --type csv --file <LocationOfYourDirectory>/Movie_Recommender/ml-latest-small/ratings.csv --headerline

	mongoimport -d mydb -c linkds --type csv --file <LocationOfYourDirectory>/Movie_Recommender/ml-latest-small/links.csv --headerline

2. Run WebApp.py And Launch yuor Browser and go to : http://127.0.0.1:5000/0 (The Main HomePage)


API Keys Used:
--------------
tmdb api key - 78077b8e590c738712916712631f58a3

tmdb - https://image.tmdb.org/t/p/w185/<ImagePath>

https://api.themoviedb.org/3/movie/862?api_key=78077b8e590c738712916712631f58a3
