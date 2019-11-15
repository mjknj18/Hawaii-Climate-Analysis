#Import Modules
import flask
from flask import request, jsonify
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from statistics import mean

#Define Flask App Environment
app = flask.Flask(__name__)
app.config["DEBUG"] = True

#Define SQLite Database Engine
engine = create_engine("sqlite:///Hawaii_Climate_Data/hawaii.sqlite")

#Map Database from SQLite File
Base = automap_base()

#Import Tables from Database
Base.prepare(engine, reflect=True)

#Define Classes as Table Names
Measurement = Base.classes.measurement
Station = Base.classes.station

#Create Session Link to SQLite Database
session = Session(engine)

#Define Path for App Home Screen
@app.route('/', methods=['GET'])

#Define Function for Home Screen Content
def home():

    #Display User Information on Home Screen
    return '''<h1>Hawaii Climate Data API</h1>
        <h2>Available Static Routes</h2>
        <h3>Latest Precipitation Information (/api/v1.0/precipitation)</h3>
        <p>Returns Hawaii precipitation data for the most recent year on record (2016-08-24 through 2017-08-23).</p>
        <h3>Weather Station Information (/api/v1.0/stations)</h3>
        <p>Returns a list of all Hawaii weather stations.</p>
        <h3>Latest Temperature Information (/api/v1.0/tobs)</h3>
        <p>Returns Hawaii temperature data for the most active weather station for recent year on record (2016-08-24 through 2017-08-23).</p>
        <h2>Available Dynamic Routes</h2>
        <h3>Temperature Summary by Start Date (/api/v1.0/start)</h3>
        <p>Returns the minimum, maximum, and average temperature for all dates on or after the start date.\nDate must be in YYYY-MM-DD form, and must be between 2010-01-01 and 2017-08-23 inclusive.</p>
        <h3>Temperature Summary by Start and End Dates (/api/v1.0/start/end)</h3>
        <p>Returns the minimum, maximum, and average temperature for all dates between the start and end date inclusive.\nDates must be in YYYY-MM-DD form, and must be between 2010-01-01 and 2017-08-23 inclusive.</p>'''

#Define Path for Precipitation Information Static API
@app.route('/api/v1.0/precipitation', methods=['GET'])

#Define Function for Precipitation Information Static API Content
def api_precip():

    #Extract All Avialable Dates from Measurements Table
    date_list = engine.execute('SELECT date FROM Measurement')

    #Loop Thruough Dates to Find Latest Record
    for date in date_list:
        last_date = date[0]
    
    #Split Lastest Date Record at Dashes to Isolate Year/Month/Day
    date_split = last_date.split('-')

    #Subtract One from Year Index
    date_split[0] = str(int(date_split[0]) - 1)

    #Re-Assemble Date Value & Record as Year Prior Date
    prior_date = date_split[0] + '-' + date_split[1] + '-' + date_split[2]

    #Query Database to Create Pandas Data Frame of Precipitation Data for Selected Year-Long Period
    precip_data = pd.read_sql('SELECT date, prcp FROM Measurement WHERE date >= (?)', engine, params = (prior_date,))

    #Drop Rows with Missing Values
    precip_data = precip_data.dropna()

    #Set Date Values as Data Frame Index
    precip_data = precip_data.set_index('date')

    #Sort Data Frame by Date
    precip_data = precip_data.sort_index()

    #Convert Data Frame to Dictionary
    precip_dict = {date_name: date_group['prcp'].tolist() for date_name, date_group in precip_data.groupby('date')}

    #Display Precipitation Information
    return jsonify(precip_dict)

#Define Path for Station Information Static API
@app.route('/api/v1.0/stations', methods=['GET'])

#Define Function for Station Information Static API Content
def api_stations():
    
    #Extract All Station IDs and Names from Stations Table
    active_stations = engine.execute('SELECT station, name FROM Station')

    #Define Blank Dictionary for Station IDs and Names
    station_list = {}

    #Loop Through Station ID & Name Pairs
    for occurences in active_stations:

        #Create Dictionary of Station IDs & Names
        station_list.update({occurences[0]: occurences[1]})

    #Display Station Information
    return jsonify(station_list)

#Define Path for Temperature Information Static API
@app.route('/api/v1.0/tobs', methods=['GET'])

#Define Function for Temperature Information Static API Content
def api_temp():

    #Extract All Avialable Dates from Measurements Table
    date_list = engine.execute('SELECT date FROM Measurement')

    #Loop Thruough Dates to Find Latest Record
    for date in date_list:
        last_date = date[0]
    
    #Split Lastest Date Record at Dashes to Isolate Year/Month/Day
    date_split = last_date.split('-')

    #Subtract One from Year Index
    date_split[0] = str(int(date_split[0]) - 1)

    #Re-Assemble Date Value & Record as Year Prior Date
    prior_date = date_split[0] + '-' + date_split[1] + '-' + date_split[2]

    #Query Database to Create Pandas Data Frame of Temperature Data for Selected Year-Long Period for Most Active Weather Station
    temp_data = pd.read_sql('SELECT date, tobs FROM Measurement WHERE date >= (?) AND station = (?)', engine, params = (prior_date, 'USC00519281',))

    #Drop Rows with Missing Values
    temp_data = temp_data.dropna()

    #Set Date Values as Data Frame Index
    temp_data = temp_data.set_index('date')

    #Sort Data Frame by Date
    temp_data = temp_data.sort_index()

    #Convert Data Frame to Dictionary
    temp_dict = {date_name: date_group['tobs'].tolist() for date_name, date_group in temp_data.groupby('date')}

    #Display Temperature Information
    return jsonify(temp_dict)

#Define Path for Temperature Information Dynamic API with Start Date
@app.route('/api/v1.0/<start>', methods=['GET'])

#Define Function for Temperature Information Dynamic API with Start Date
def api_start(start):

    #Query Database to Create Pandas Data Frame of Temperature Data for Selected Year-Long Period for Most Active Weather Station
    temp_data = pd.read_sql('SELECT date, tobs FROM Measurement WHERE date >= (?)', engine, params = (start,))

    #Drop Rows with Missing Values
    temp_data = temp_data.dropna()

    #Set Date Values as Data Frame Index
    temp_data = temp_data.set_index('date')

    #Sort Data Frame by Date
    temp_data = temp_data.sort_index()

    #Convert Data Frame to Dictionary
    temp_dict = {date_name: date_group['tobs'].tolist() for date_name, date_group in temp_data.groupby('date')}

    #Define Blank Dictionary for Temperature Summary Data
    summary_dict = {}
    
    #Loop Through Daily Temperature Data
    for index in temp_dict:

        #Calculate Daily Minimum/Maximum/Average Temperatures
        summary_dict.update({index: [min(temp_dict[index]), max(temp_dict[index]), round(mean(temp_dict[index]),1)]})

    #Display Temperature Information
    return jsonify(summary_dict)

#Define Path for Temperature Information Dynamic API with Start & End Dates
@app.route('/api/v1.0/<start>/<end>', methods=['GET'])

#Define Function for Temperature Information Dynamic API with Start & End Date
def api_end(start, end):
    #Query Database to Create Pandas Data Frame of Temperature Data for Selected Year-Long Period for Most Active Weather Station
    temp_data = pd.read_sql('SELECT date, tobs FROM Measurement WHERE date >= (?) AND date <= (?)', engine, params = (start, end,))

    #Drop Rows with Missing Values
    temp_data = temp_data.dropna()

    #Set Date Values as Data Frame Index
    temp_data = temp_data.set_index('date')

    #Sort Data Frame by Date
    temp_data = temp_data.sort_index()

    #Convert Data Frame to Dictionary
    temp_dict = {date_name: date_group['tobs'].tolist() for date_name, date_group in temp_data.groupby('date')}

    #Define Blank Dictionary for Temperature Summary Data
    summary_dict = {}
    
    #Loop Through Daily Temperature Data
    for index in temp_dict:

        #Calculate Daily Minimum/Maximum/Average Temperatures
        summary_dict.update({index: [min(temp_dict[index]), max(temp_dict[index]), round(mean(temp_dict[index]),1)]})

    #Display Temperature Data
    return jsonify(summary_dict)

#Initialize Flask App
app.run()