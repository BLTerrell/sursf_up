
import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify
# Set up the database
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)
Measurement = Base.classes.measurement
Staion = Base.classes.station
session = Session(engine)


# Set up flask
app = Flask(__name__)


@app.route("/")
def welcome():
    return(
        '''
    Welcome to the Climate Analysis API!  </br>
    Available Routes: </br>
    /api/v1.0/precipitation </br>
    /api/v1.0/stations </br>
    /api/v1.0/tobs </br>
    /api/v1.0/temp/start/end </br>
    ''')


@app.route("/api/v1.0/precipitation")
def precipitation():
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    precipitation = session.query(Measurement.date, Measurement.prcp).filter(
        Measurement.date >= prev_year).all()
    precip = {date: prcp for date, prcp in precipitation}

    return jsonify(precip)


@app.route("/api/v1.0/stations")
# @app.route("/api/v1.0/tobs")
# @app.route("api/v1.0/temp/start/end")
