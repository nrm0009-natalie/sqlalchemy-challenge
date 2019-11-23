import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///../sqlalchemy-challenge/hawaii.sqlite")

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

@app.route("/")
def home_page():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
    )


@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    """Return a list of all precipitation values"""
    # Query all values
    sel = [Measurement.date, Measurement.prcp]
    date_prcp = session.query(*sel).\
    filter(Measurement.date >= '2016-08-23').\
    order_by(Measurement.date).all()

    session.close()

    #create a dataframe and group by date, then add date and precipitation to a dictionary 
    date_prcp_df = pd.DataFrame(date_prcp, columns=["Date", "Precipitation"])
    date_prcp_df.set_index("Date", inplace=True)
    date_prcp_df.sort_values("Date", inplace=True)
    date_prcp_df.dropna(inplace=True)
    date_prcp_grouped = date_prcp_df.groupby("Date")

    #create an empty dictionary to set date(key) and precipitation values in
    date_prcp_dict = {}

    for date, precipitation in date_prcp_grouped:
        date_prcp_dict[date] = precipitation["Precipitation"].tolist()

    return jsonify(date_prcp_dict)


@app.route("/api/v1.0/stations")
def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # Query all stations
    stations = session.query(Station.station).all()

    session.close()

    # Create a dictionary from the row data and append to a list of all_passengers
    all_stations = []
    for item in stations:
        all_stations.append(item)

    return jsonify(all_stations)

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # from Measurements query dates and temps from the past year
    year_of_temps = engine.execute('SELECT date, tobs FROM measurement WHERE strftime("%Y-%m-%d", date) BETWEEN "2016-08-23" AND "2017-08-23" AND station="USC00519281"').fetchall()

    session.close()

    #append all tempatures from the past year to a list
    temps = []
    for date, tobs in year_of_temps:
        temps.append(tobs)
    return jsonify(temps) 

@app.route("/api/v1.0/<start>")
def start(start):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # from Measurements query temps from a chosen start date
    #find the max, min, and avg out of these temps
    average_temps_2016 = session.query(func.avg(Measurement.tobs)).filter(Measurement.date >= '2016-01-01').all()
    max_temps_2016 = session.query(func.max(Measurement.tobs)).filter(Measurement.date >= '2016-01-01').all()
    min_temps_2016 = session.query(func.avg(Measurement.tobs)).filter(Measurement.date >= '2016-01-01').all()
    session.close()

    #print above data
    return f"After January 2016 the average for temp was {average_temps_2016}, the max temp  was {max_temps_2016}, and the min temp was {min_temps_2016}."

@app.route("/api/v1.0/<start>/<end>")
def start_end(start, end):
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # from Measurements query temps from a chosen start date to an end date
    #find the max, min, and avg out of these temps
    tavg = session.query(func.avg(Measurement.tobs)).filter(Measurement.date >= '2016-01-01').filter(Measurement.date <= '2016-12-31').all()
    tmin = session.query(func.min(Measurement.tobs)).filter(Measurement.date >= '2016-01-01').filter(Measurement.date <= '2016-12-31').all()
    tmax = session.query(func.max(Measurement.tobs)).filter(Measurement.date >= '2016-01-01').filter(Measurement.date <= '2016-12-31').all()

    session.close()

    #print above data
    return f"For the year of 2016 the average temp was {tavg}, the max temp  was {tmax}, and the min temp was {tmin}."



if __name__ == '__main__':
    app.run(debug=True)
