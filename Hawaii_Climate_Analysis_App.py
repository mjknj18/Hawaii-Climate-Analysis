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

app = flask.Flask(__name__)
app.config["DEBUG"] = True

engine = create_engine("sqlite:///Hawaii_Climate_Data/hawaii.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)

Measurement = Base.classes.measurement
Station = Base.classes.station

session = Session(engine)


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Hawaii Climate Data API</h1>
        <h2>Available Static Routes</h2>
        <h3>Precipitation (/api/v1.0/precipitation)</h3>
        <p>Returns Hawaii precipitation data for the most recent year on record (2016-08-24 through 2017-08-23).</p>
        <h3>Stations (/api/v1.0/stations)</h3>
        <p>Returns a list of all Hawaii weather stations.</p>
        <h3>Temperature (/api/v1.0/tobs)</h3>
        <p>Returns Hawaii temperature data for the most active weather station for recent year on record (2016-08-24 through 2017-08-23).</p>'''

@app.route('/api/v1.0/precipitation', methods=['GET'])
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

    return jsonify(precip_dict)

@app.route('/api/v1.0/stations', methods=['GET'])
def api_stations():
    active_stations = engine.execute('SELECT station, name FROM Station')

    station_list = {}

    for occurences in active_stations:
        station_list.update({occurences[0]: occurences[1]})

    return jsonify(station_list)

@app.route('/api/v1.0/tobs', methods=['GET'])
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

    #Query Database to Create Pandas Data Frame of Precipitation Data for Selected Year-Long Period for Most Active Weather Station
    temp_data = pd.read_sql('SELECT date, tobs FROM Measurement WHERE date >= (?) AND station = (?)', engine, params = (prior_date, 'USC00519281',))

    #Drop Rows with Missing Values
    temp_data = temp_data.dropna()

    #Set Date Values as Data Frame Index
    temp_data = temp_data.set_index('date')

    #Sort Data Frame by Date
    temp_data = temp_data.sort_index()

    #Convert Data Frame to Dictionary
    temp_dict = {date_name: date_group['tobs'].tolist() for date_name, date_group in temp_data.groupby('date')}

    return jsonify(temp_dict)

app.run()