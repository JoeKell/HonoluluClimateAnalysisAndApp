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
        "Available Routes:<br/><br/>"

        "/api/v1.0/precipitation<br/>"
        "On this page you will find a JSON representation of a dictionary "
        "of dates and precipitation from the Waihee station in Hawaii.<br/><br/>"

        "/api/v1.0/stations<br/>"
        "On this page you will find a JSON representation of a list of the Hawaii stations.<br/><br/>"

        "/api/v1.0/tobs<br/>"
        "On this page you will find a JSON representation of a dictionary of"
        " dates and temperature from the last year of the most active station.<br/><br/>"

        "/api/v1.0/enter_start_date<br/>"
        "On this page you will find a JSON representation of a dictionary of the lowest temperature,"
        " average temperature, and highest temperature from the last year of the most active station. "
        "Enter the date in the format YYYY-MM-DD and use a start date between "
        "2016-08-18 and 2017-08-18. <br/><br/>"

        "/api/v1.0/enter_start_date/enter_end_date.<br/>"
        "On this page you will find a JSON representation of a dictionary of the lowest temperature,"
        " average temperature, and highest temperature from the last year of the most active station. "
        "Enter the dates in the format YYYY-MM-DD, use a start date between "
        "2016-08-18 and 2017-08-17, and use an end date that is greater than the start date "
        "and less than 2017-08-18"

    )


@app.route("/api/v1.0/precipitation")
        # "On this page you will find a JSON representation of a dictionary "
        # "of dates and precipitation from the Waihee station in Hawaii.<br/><br/>"
def prcp():
    precip = engine.execute("SELECT date, prcp FROM measurement WHERE station = 'USC00519281' ORDER BY date").fetchall()
    pre_dict={}
    for x in precip:
        pre_dict[x[0]]=x[1]
    return jsonify(pre_dict)


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
    if end<=start:
        return (
        f"{start}<br/>"
        "Double check the date range<br/>"
        
        )
    return "WIP"



if __name__ == '__main__':
    app.run(debug=True)