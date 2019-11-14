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


@app.route('/', methods=['GET'])
def home():
    return '''<h1>Hawaii Climate Data API</h1>
        <h2>Available Static Routes</h2>
        <h3>Precipitation (/api/v1.0/precipitation)</h3>
        <p>Returns Hawaii precipitation data for the most recent year on record (2016-08-24 through 2017-08-23).</p>
        <h3>Stations (/api/v1.0/stations)</h3>
        <p>Returns a list of all Hawaii weather stations.</p>
        <h3>Temperature (/api/v1.0/tobs)</h3>
        <p>Returns Hawaii temperature data for the most recent year on record (2016-08-24 through 2017-08-23).</p>'''

app.run()