# SQLAlchemy Homework - SqlAlchemy-Hawaii-Climate-Analysis

![surfs-up.png](Images/surfs-up.png)

The goal of this project was to extract, process, and analyze Hawaii climate data contained in a SQLite database, as well as construct an API for the raw climate data. Python with SQLAlchemy was utilized to store, inspect, and manipulate the data, while Python with Pandas, Numpy, and Matplotlib was used to generate meaningful visualizations in a common Jupyter Notebook. The API was developed in VS Code using Python with SQLAlchemy to store and inspect the data, while Python with Flask powered the development of the web interface.

## Questions

#### Climate Analysis

Precipitation Analysis

1. How much total precipitation did Hawaii receive during the last twelve months on record?
2. What are the summary statistics for that precipitation data?

Weather Station Analysis

1. What are the most active weather stations based on observation count?
2. What are the maximum, minimum, and average temperatures for the most active weather station?

Temperature Analysis

1. For the most active weather station, what are the most frequent temperature observations for the last twelve months on record?
2. Are the monthly averages of the recorded June and December temperature observations statistically significant?

Historical Analysis

1. Given a set of start and end dates, what are the maximum, minimum, and average temperatures for the same date range one year prior?
2. Given a set of start and end dates, what is the total precipitation for each weather station for the same date range one year prior?
3. Given a set of start and end dates, what are the daily maximum, minimum, and average temperatures for the same date range for all years on record?

#### Climate API

Static Routes

1. How much total precipitation did Hawaii receive during the last twelve months on record?
2. What weather stations are collecting climate data?
3. For the most active weather station, what is the recorded temperature for each day during the last twelve months on record?

Dynamic Routes

1. Given a start date, what are the maximum, minimum, and average temperatures for that date and all future dates on record?
2. Given a set of start and end dates, what are the maximum, minimum, and average temperatures for those dates and all in-between?

#### Datasets
https://github.com/LolitaDias/SqlAlchemy-Hawaii-Climate-Analysis/blob/master/Resources/hawaii.sqlite
https://github.com/LolitaDias/SqlAlchemy-Hawaii-Climate-Analysis/blob/master/Resources/hawaii_measurements.csv
https://github.com/LolitaDias/SqlAlchemy-Hawaii-Climate-Analysis/blob/master/Resources/hawaii_stations.csv

## Tasks

#### Climate Analysis

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

Query temperature observations for the most active weather station in the aforementioned twelve month date range.
Create twelve equally sized temperature range bins and sort the temperature observations into the appropriate bins.
Plot a histogram of the temperature distribution for the most active weather station in that date range.
Query all June and December temperature observations and create separate Pandas data frames for each dataset.
Perform an independent t-test on the June and December datasets, and analyze the t-statistic and p-value.

#### Historical Analysis

Determine a set of start and end dates, and calculate dates one year prior to those dates.
Query maximum, minimum, and average observed temperature for all records on or within the year prior date range.
Plot a bar chart of the average observed temperature with an error bar reflecting the difference in maximum and minimum observed temperatures.
Query weather station information and the total precipitation recorded by each station for the year prior date range, and sort in descending order.
Query daily maximum, minimum, and average observed temperature for all days from any year matching dates within the year prior date range.
Combine records into a Pandas data frame and set date as the index.
Plot an area chart of the maximum, minimum, and average observed temperatures.

#### Climate API

Define the Flask application environment and establish a connection to the SQLite database.
Automap the database, reflect the tables as classes, and create a session.
Define a path for the API home screen.
Define a function to display API functionality on the home screen.

#### Static Routes

Define a path for the precipitation information API.
Define a function to query precipitation data for the last twelve months on record and display it in JSON format.
Define a path for the weather station information API.
Define a function to query weather station data and display it in JSON format.
Define a path for the temperature information API.
Define a function to query temperature data for the last twelve months on record and display it in JSON format.

#### Dynamic Routes

Define a path for the temperature information API that accepts a start date.
Define a function to import the given start date, query the temperature data on and after that date, calculate the appropriate daily summary values, and display those summary values in JSON format.
Define a path for the temperature information API that accepts start and end dates.
Define a function to import the given start and end dates, query the temperature data for and in-between those dates, calculate the appropriate daily summary values, and display those summary values in JSON format.

##Results