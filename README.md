# Hawaii-Climate-Analysis

The goal of this project was to extract, process, and analyze Hawaii climate data contained in a SQLite database, as well as construct an API for the raw climate data. Python with SQLAlchemy was utilized to store, inspect, and manipulate the data, while Python with Pandas, Numpy, and Matplotlib was used to generate meaningful visualizations in a common Jupyter Notebook. The API was developed in VS Code using Python with SQLAlchemy to store and inspect the data, while Python with Flask powered the development of the web interface. 

## Questions

### Climate Analysis

#### Precipitation Analysis

1. How much total precipitation did Hawaii receive during the last twelve months on record?
2. What are the summary statistics for that precipitation data?

#### Weather Station Analysis

1. What are the most active weather stations based on observation count?
2. What are the maximum, minimum, and average temperatures for the most active weather station?

#### Temperature Analysis

1. For the most active weather station, what are the most frequent temperature observations for the last twelve months on record?
2. Are the monthly averages of the recorded June and December temperature observations statistically significant?

#### Historical Analysis

1. Given a set of start and end dates, what are the maximum, minimum, and average temperatures for the same date range one year prior?
2. Given a set of start and end dates, what is the total precipitation for each weather station for the same date range one year prior?
3. Given a set of start and end dates, what are the daily maximum, minimum, and average temperatures for the same date range for all years on record?

### Climate API

#### Static Routes

1. How much total precipitation did Hawaii receive during the last twelve months on record?
2. What weather stations are collecting climate data?
3. For the most active weather station, what is the recorded temperature for each day during the last twelve months on record?

#### Dynamic Routes

1. Given a start date, what are the maximum, minimum, and average temperatures for that date and all future dates on record?
2. Given a set of start and end dates, what are the maximum, minimum, and average temperatures for those dates and all in-between?

## Datasets

1. https://github.com/mjknj18/Hawaii-Climate-Analysis/blob/master/Hawaii_Climate_Data/hawaii.sqlite
2. https://github.com/mjknj18/Hawaii-Climate-Analysis/blob/master/Hawaii_Climate_Data/hawaii_measurements.csv
3. https://github.com/mjknj18/Hawaii-Climate-Analysis/blob/master/Hawaii_Climate_Data/hawaii_stations.csv

## Tasks

### Climate Analysis

1. Define the SQLAlchemy environment and establish a connection to the SQLite database.
2. Automap the database, reflect the tables as classes, and create a session.

#### Precipitation Analysis

1. Calculate the latest twelve month date range from the last available record in the database.
2. Query precipitation data for dates within that range and sort records from oldest to newest.
3. Plot the precipitation data for that date range.
4. Calculate the summary statistics for the precipitation data.
5. Create a Pandas data frame of the calculated statistical values.

#### Weather Station Analysis

1. Query weather station information and the number of records tied to each station, and sort by the latter in descending order.
2. Query maximum, minimum, and average observed temperature for all records from the most active weather station.

#### Temperature Analysis

1. Query temperature observations for the most active weather station in the aforementioned twelve month date range.
2. Create twelve equally sized temperature range bins and sort the temperature observations into the appropriate bins.
3. Plot a histogram of the temperature distribution for the most active weather station in that date range.
4. Query all June and December temperature observations and create separate Pandas data frames for each dataset.
5. Perform an independent t-test on the June and December datasets, and analyze the t-statistic and p-value.

#### Historical Analysis

1. Determine a set of start and end dates, and calculate dates one year prior to those dates.
2. Query maximum, minimum, and average observed temperature for all records on or within the year prior date range.
3. Plot a bar chart of the average observed temperature with an error bar reflecting the difference in maximum and minimum observed temperatures.
4. Query weather station information and the total precipitation recorded by each station for the year prior date range, and sort in descending order.
5. Query daily maximum, minimum, and average observed temperature for all days from any year matching dates within the year prior date range.
6. Combine records into a Pandas data frame and set date as the index.
7. Plot an area chart of the maximum, minimum, and average observed temperatures.

### Climate API

1. Define the Flask application environment and establish a connection to the SQLite database.
2. Automap the database, reflect the tables as classes, and create a session.
3. Define a path for the API home screen.
4. Define a function to display API functionality on the home screen.

#### Static Routes

1. Define a path for the precipitation information API. 
2. Define a function to query precipitation data for the last twelve months on record and display it in JSON format.
3. Define a path for the weather station information API.
4. Define a function to query weather station data and display it in JSON format.
5. Define a path for the temperature information API.
6. Define a function to query temperature data for the last twelve months on record and display it in JSON format.

#### Dynamic Routes

1. Define a path for the temperature information API that accepts a start date.
2. Define a function to import the given start date, query the temperature data on and after that date, calculate the appropriate daily summary values, and display those summary values in JSON format.
3. Define a path for the temperature information API that accepts start and end dates.
4. Define a function to import the given start and end dates, query the temperature data for and in-between those dates, calculate the appropriate daily summary values, and display those summary values in JSON format.

## Results

### Climate Analysis

#### Precipitation Analysis

<img src = https://github.com/mjknj18/Hawaii-Climate-Analysis/blob/master/Images/Precipitation_History.png>

<img src = https://github.com/mjknj18/Hawaii-Climate-Analysis/blob/master/Images/Precipitation_Summary.PNG>

#### Weather Station Analysis

<img src = https://github.com/mjknj18/Hawaii-Climate-Analysis/blob/master/Images/Weather_Station_Activity.PNG>

<img src = https://github.com/mjknj18/Hawaii-Climate-Analysis/blob/master/Images/Busiest_Weather_Station_Stats.PNG>

#### Temperature Analysis

<img src = https://github.com/mjknj18/Hawaii-Climate-Analysis/blob/master/Images/Temperature_Frequency.png>

<img src = https://github.com/mjknj18/Hawaii-Climate-Analysis/blob/master/Images/Temperature_T_Test.PNG>

#### Historical Analysis

<img src = https://github.com/mjknj18/Hawaii-Climate-Analysis/blob/master/Images/Historical_Temperature.png>

<img src = https://github.com/mjknj18/Hawaii-Climate-Analysis/blob/master/Images/Historical_Precipitation_Totals.PNG>

<img src = https://github.com/mjknj18/Hawaii-Climate-Analysis/blob/master/Images/Daily_Normals.png>

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

#### Precipitation Analysis

1. For the majority of days in the most recent twelve month period, the total daily precipitation amounts in Hawaii were at or below two inches, with occasional days seeing anywhere up to nearly seven inches.
2. In the most recent twelve month period, there were 2021 recorded precipitation amounts, with a mean of 0.177 inches, a standard deviation of 0.461 inches, and a maximum of 6.7 inches.

#### Weather Station Analysis

1. The most active weather station was Waihee (2772 observations), closely followed by Waikiki (2724 observations) and Kaneohe (2709 observations).
2. The maximum, minimum, and average temperatures for the most active weather station (Waihee) were 85, 54, and 71.7 degrees Fahrenheit respectively.

#### Temperature Analysis

1. For the most active weather station (Waihee) in the most recent twelve month period, the majority of temperatures were between 69 and 79 degrees Fahrenheit, with occasional days seeing temperatures as high as 83 degrees Fahrenheit and as low as 59 degrees Fahrenheit.
2. The t-test of the June and December temperature data produced a p-value of 3.902e-191. This is far below the accepted cutoff of 0.05 and indicates that the averages of the two datasets are statistically significant. 

#### Historical Analysis

1. For a date range of 2017-12-18 to 2018-01-17, the average temperature for the same period one year prior was approximately 70 degrees Fahrenheit, with an error window of approximately 20 degrees Fahrenheit.
2. For a date range of 2017-12-18 to 2018-01-17, the Manoa Lyon Arbo weather station had the highest recorded precipitation amount of 10.93 inches for the same period one year prior. All other weather stations recorded less than 3.25 inches of precipitation in that prior year period.
3. For a date range of 2017-12-18 to 2018-01-17, the daily maximum, minimum, and average temperatures for the same days in all prior years were between 75 and 81 degrees Fahrenheit, 55 and 67 degrees Fahrenheit, and 68 and 73 degrees Fahrenheit respectively.

### Climate API

#### Static Routes

1. The URL for the precipitation information API correctly displays all of the recorded precipitation amounts for each day during the latest year on record. 
2. The URL for the weather station information API correctly displays all of weather stations that contributed obsere daily vations to the baseline climate data.
3. The URL for the temperature information API correctly displays the observed temperatures for the most active weather station during the latest year on record.

#### Dynamic Routes

1. For a given start date of 2016-01-01, the URL for the temperature information API returns the maximum, minimum, and average temperatures for all dates on or after that start date.
2. for a given start and end date pair of 2016-01-01 and 2016-12-31, the URL for the temperature information API returns the maximum, minimum, and average temperatures for all dates on or between those start and end dates.

## Disclaimer

The baseline data used for this analysis was provided by a third party source and its accuracy in relation to actual Hawaii climate data is unknown.