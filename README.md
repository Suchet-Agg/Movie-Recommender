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
**[UPDATE]: See Version History**

## Built With

* Python 
* Pandas, numpy
* keras
* sklearn

* Flask 
* Pymongo 
* json 
* urllib 
* HTML 
* MongoDB 
* CSS 
* JavaScript 

## API's Used

* **API KEY** tmdb api key - 78077b8e590c738712916712631f58a3
[UPDATE]: TMdB no longer works

## Version Info

Version : 1.0.1

[UPDATE] : Version 1.1.1 : 
**added ipynb and updated model**
The earlier implementation was slow, the new one uses keras as base and is quite efficient and accurate. Also the new implementation directly uses data from the csv using pandas instead of first loading it in MongoDB (was quite slow actually)
PS: This is not yet incorporated in the Web app so the web app may be broken ; (

## Authors

* **Suchet Aggarwal** - *IIIT-Delhi* - [Other Work](https://github.com/Suchet-Agg)

## Acknowledgments
* [Data Set Used](https://grouplens.org/datasets/movielens/latest/)

