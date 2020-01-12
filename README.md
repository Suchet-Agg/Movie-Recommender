# Movie Recommender System

A web app that suggests movies based on the past ratings and view history of the user using ITEM-ITEM and USER-USER collaborative learning
Website Creator. The project uses data taken from TMdB and stores it in a MongoDB database.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

1. MongoDB
2. Python3

Firstly import the databases into Mongo 

```
mongoimport -d mydb -c movieds --type csv --file /Movie_Recommender/ml-latest-small/movies.csv --headerline

mongoimport -d mydb -c ratingds --type csv --file /Movie_Recommender/ml-latest-small/ratings.csv --headerline

mongoimport -d mydb -c linkds --type csv --file /Movie_Recommender/ml-latest-small/links.csv --headerline

```
Run WebApp.py And Launch yuor Browser and go to : http://127.0.0.1:5000/0 (The Main HomePage)


## Additional Notes

The Project still has some bugs here and there, and may seldom take long for prediction... So please be patient

## Built With

* Python 
* Flask 
* Pandas 
* Pymongo 
* json 
* urllib 
* HTML 
* MongoDB 
* CSS 
* JavaScript 
* TMDB API

## API's Used

* **API KEY** tmdb api key - 78077b8e590c738712916712631f58a3

* **For Images** tmdb - https://image.tmdb.org/t/p/w185/

* **For Movie Data** https://api.themoviedb.org/3/movie/862?api_key=78077b8e590c738712916712631f58a3

## Version Info

Version : 1.0.1

## Authors

* **Suchet Aggarwal** - *IIIT-Delhi* - [Other Work](https://github.com/Suchet-Agg)


## Acknowledgments

* [BootStrap](www.bootStrap.com)
* [PyhtonSpot](https://pythonspot.com/flask-web-app-with-python/)
* [MongoDB](http://api.mongodb.com/python/3.6.0/tutorial.html#counting )
* [Carleton](http://www.cs.carleton.edu/cs_comps/0607/recommend/recommender/itembased.html )
* [JsFiddle](http://jsfiddle.net/ashuslove/zLm4f/6/)

