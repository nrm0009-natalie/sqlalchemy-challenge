# sqlalchemy-challenge

The goal of this project was to extract, process, and analyze Hawaii climate data contained in a SQLite database, as well as construct an API for the raw climate data. 

## Technologies

Python with SQL-alchemy was utilized to store, inspect, and manipulate the data, while Python with Pandas, Numpy, and Matplotlib was used to generate meaningful visualizations in a common Jupyter Notebook. The API was developed in VS Code using Python with SQLAlchemy to store and inspect the data, while Python with Flask powered the development of the web interface. 

## Climate Analysis

* Define the SQLAlchemy environment and establish a connection to the SQLite database.
* Automap the database, reflect the tables as classes, and create a session.
* Create numerous pandas dataframes using queried data - 
    * The most active weather stations based on observation count
    * Maximum, minimum, and average temperatures for the most active weather station
    * Total precipitation Hawaii received during the last twelve months on record
    * Given a set of start and end dates, the daily maximum, minimum, and average temperatures for the same date range for all years on record.


### Climate API

* Define the Flask application environment and establish a connection to the SQLite database.
* Automap the database, reflect the tables as classes, and create a session.
* Define a path for the API home screen.
* Define several functions to display API functionality on the home screen.


### Climate API Routes
(Run https://github.com/nrm0009-natalie/sqlalchemy-challenge/blob/master/climate-app.py in local server)

1. How much total precipitation did Hawaii receive during the last twelve months on record?
    * /api/v1.0/precipitation
2. What weather stations are collecting climate data?
    * /api/v1.0/stations
3. For the most active weather station, what is the recorded temperature for each day during the last twelve months on record?
    * /api/v1.0/tobs
4. Given a start date, what are the maximum, minimum, and average temperatures for that date and all future dates on record?
    * /api/v1.0/start
5. Given a set of start and end dates, what are the maximum, minimum, and average temperatures for those dates and all in-between?
    * /api/v1.0/start and /api/v1.0/start/end

## Datasets

1. https://github.com/nrm0009-natalie/sqlalchemy-challenge/blob/master/hawaii.sqlite
2. https://github.com/nrm0009-natalie/sqlalchemy-challenge/blob/master/hawaii_measurements.csv
3. https://github.com/nrm0009-natalie/sqlalchemy-challenge/blob/master/hawaii_stations.csv



## Visualizations

<img src = https://github.com/nrm0009-natalie/sqlalchemy-challenge/blob/master/Precipitation_2016-1017.png>

## 
<img src = https://github.com/nrm0009-natalie/sqlalchemy-challenge/blob/master/sqlalchemy_histogram.png>


## 
<img src = https://github.com/nrm0009-natalie/sqlalchemy-challenge/blob/master/sqlalchemy_bargraph.png>


## Results and Analysis

It can be gathered from the above data that the most active weather station on Hawaii - that is, the station with the highest quantity of recorded weather data - is USC00519281 in the city of WAIHEE. After further analysis of the data from this station we can confirm that the variance in temperature throughout the seasons is incredibly small. There is only a 30 degree difference in the highest and lowest recorded temperatures within a year.
As can be viewed on the above bar chart, we can also deduce that all 9 stations in the dataset are located within cities that have moderate to heavy rainfall year round. In fact, much of the precipitation data that was gathered showed rainfall measurement taken several times per day. 
These results tend to agree with the assumptions regarding weather in Hawaii. Islands located in the pacific on the equator do indeed tend to receive massive amounts of rain, and enjoy mild temperatures all year.