# Hawaii-Climate-Analysis

The goal of this project was to extract, process, and analyze Hawaii climate data contained in a SQLite database, as well as construct an API for raw climate data. For the analysis portion, Python with SQLAlchemy was utilized to store and inspect the data, while Python with Pandas, Numpy, and Matplotlib was used to generate meaningful visualizations in a common Jupyter Notebook. The API was developed in VS Code using Python with SQLAlchemy to store and inspect the data, while Python with Flask powered the development of the web interface. 

## Questions

### Climate Analysis

#### Precipitation Analysis

1. How much total precipitation did Hawaii receive during the last twelve months on record?
2. What are the summary statistics for that precipitation data?

#### Weather Station Analysis

1. What are the most active weather stations by observation count?
2. What are the maximum, minimum, and average temperatures for the most active weather station?

#### Temperature Analysis

1. For the most active weather station, what are the most common temperature observations for the last twelve months on record?
2. Are the averages of the recorded June temperature data and December temperature data statistically significant?

#### Historical Analysis

1. Given a set of start and end dates, what are the historical maximum, minimum, and average temperatures for the same date range one year prior?
2. Given a set of start and end dates, what is the total precipitation for each weather station for the same date range one year prior?
3. Given a set of start and end dates, what are the daily normal maximum, minimum, and average temperatures for the same date range for all years on record?

### Climate API

#### Static Routes

1. How much total precipitation did Hawaii receive during the last twelve months on record?
2. What are the weather stations collecting climate data?
3. What are the temperatures observed by all Hawaii weather stations during the last twelve months on record?

#### Dynamic Routes

1. For a given start date, what are the maximum, minimum, and average temperatures for all dates on and beyond that date?
2. For a given start and end date combination, what are the maximum, minimum, and average temperatures for all dates on and between those dates?

## Datasets

1. https://github.com/mjknj18/Hawaii-Climate-Analysis/blob/master/Hawaii_Climate_Data/hawaii.sqlite
2. https://github.com/mjknj18/Hawaii-Climate-Analysis/blob/master/Hawaii_Climate_Data/hawaii_measurements.csv
3. https://github.com/mjknj18/Hawaii-Climate-Analysis/blob/master/Hawaii_Climate_Data/hawaii_stations.csv

## Tasks

### Climate Analysis



### Climate API



## Results

### Climate Analysis



### Climate API

#### Static Routes

1. http://127.0.0.1:5000/api/v1.0/precipitation
2. http://127.0.0.1:5000/api/v1.0/stations
3. http://127.0.0.1:5000/api/v1.0/tobs

#### Dynamic Routes

1. http://127.0.0.1:5000/api/v1.0/2016-01-01
2. http://127.0.0.1:5000/api/v1.0/2016-01-01/2016-12-31

## Observations

### Climate Analysis



### Climate API



## Disclaimer

The baseline data used for this analysis was provided by a third party source and its accuracy in relation to actual Hawaii climate data is unknown.