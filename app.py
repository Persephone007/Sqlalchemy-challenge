#import necessary libraries

import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


# create instance of Flask app
app = Flask(__name__)


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station



#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################


#/Home page.
#List all routes that are available.

@app.route("/")
def index():
    return (
        f"Welcome to the Hawaii weather station API<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/temp_obs"
        f"/api/v1.0/start"
        f"/api/v1.0/end"
    )


#/api/v1.0/precipitation
#Convert the query results to a Dictionary using date as the key and prcp as the value.
#Return the JSON representation of your dictionary.


@app.route("/api/v1.0/precipitation")
def precipitation():
     session = Session(engine)
     results = session.query(Measurement.date, Measurement.prcp).all()
     session.close()
     precipitation_data = list(np.ravel(results))


     return jsonify(precipitation_data)


    #Return a JSON list of stations from the dataset.

@app.route("/api/v1.0/stations")
def stations():

     session = Session(engine)
     results = session.query(Station.name).all()
     session.close()
     stations = list(np.ravel(results))

    return jsonify(stations)


#query for the dates and temperature observations from a year from the last data point.
#Return a JSON list of Temperature Observations (tobs) for the previous year.

@app.route("/api/v1.0/temp_obs")
def temp_obs():
    
      session = Session(engine)
      results = (session.query(Measurement.tobs, Measurement.date)
      .filter(Measurement.date > '2016-08-22')
      .order_by(Measurement.date).all())
     
     session.close()
     start = list(np.ravel(results))

    return jsonify(temp_obs)



#Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.

#When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.

#When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.

@app.route("/api/v1.0/start")
def start('2016-08-22', '2016-08-23'):
         session = Session(engine)
         results = (session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs))
        .filter(Measurement.date >= start_date)
        .filter(Measurement.date <= end_date).all())
         session.close()
         start = list(np.ravel(results))
   

@app.route("/api/v1.0/start/end")
def end():
         session = Session(engine)
         results = (session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs))
        .filter(Measurement.date >= start_date)
        .filter(Measurement.date <= end_date).all())
         session.close()
         end = list(np.ravel(results))

    return jsonify(end)





    if __name__ == "__main__":
    app.run(debug=True)