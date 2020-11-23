import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify



# Database Setup
engine = create_engine("sqlite:///Resources/hawaii.sqlite")
conn=engine.connect()

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement=Base.classes.measurement
Station=Base.classes.station


# Flask Setup

app = Flask(__name__)



# Flask Routes


@app.route("/")
def welcome():
    #List all available api routes.
    return (
        "Available Routes:<br/>"
        "/api/v1.0/precipitation<br/>"
        "/api/v1.0/stations<br/>"
        "/api/v1.0/tobs<br/>"
        "/api/v1.0/<start><br/>"
        "/api/v1.0/<start>/<end>."


    )


@app.route("/api/v1.0/precipitation")
def prcp():
   return "WIP"


@app.route("/api/v1.0/stations")
def stations():
    return "WIP"

@app.route("/api/v1.0/tobs")
def temps():
    return "WIP"

@app.route("/api/v1.0/<start>")
def date(start):
    return "WIP"

@app.route("/api/v1.0/<start>/<end>")
def date_range(start, end):
    if end<start:
        return("Double check the date range")
    return "WIP"



if __name__ == '__main__':
    app.run(debug=True)