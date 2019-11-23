import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func


from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station=Base.classes.station



#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

# 1.  Home Page
# i.  / 
# ii. List all routes that are available.
@app.route("/")

def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start day<br/>"
        f"Enter the start date in 'YYYY-MM-DD' format<br/>"
        f"/api/v1.0/start and end day<br/>"   
        f"Enter the dates in 'YYYY-MM-DD/YYYY-MM-DD' format<br/>"
        
    )

# 2.   Precipitation Page
# i.   /api/v1.0/precipitation
# ii.  Convert the query results to a Dictionary using date as the key and prcp as the value.
# iii. Return the JSON representation of your dictionary.

@app.route("/api/v1.0/precipitation")

def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    latest_date=session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    date_one_year_ago=dt.date(2017,8,23) - dt.timedelta(days=365)
    prcp_data=session.query(Measurement.date,Measurement.prcp).filter(Measurement.date>=date_one_year_ago).all()
    # Create a dictionary from the row data and append to a list of all_prcp_data
    all_prcp_data = []
    for d,p in prcp_data:
        prcp_dict = {}
        prcp_dict["date"] = d
        prcp_dict["prcp"] = p
        all_prcp_data.append(prcp_dict)

    return jsonify(all_prcp_data)
    session.close()


# 2.   Stations Page
# i.   /api/v1.0/stations
# ii.  Return a JSON list of stations from the dataset.

@app.route("/api/v1.0/stations")

def stations():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    stations_data = session.query(Station.station, Station.name).all()
    all_stations=[]
    for s,n in stations_data:
        station_dict={}
        station_dict["station"]=s
        station_dict["name"]=n
        all_stations.append(station_dict)
    return jsonify(all_stations)
    session.close()

# 3.   Temperature Page
# i.   /api/v1.0/tobs
# ii.  query for the dates and temperature observations from a year from the last data point.
# iii. Return a JSON list of Temperature Observations (tobs) for the previous year.

@app.route("/api/v1.0/tobs")

def temperatures():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    latest_date=session.query(Measurement.date).order_by(Measurement.date.desc()).first()
    date_one_year_ago=dt.date(2017,8,23) - dt.timedelta(days=365)
    temp_data = session.query(Measurement.date, Measurement.tobs).\
                filter(Measurement.date >= date_one_year_ago).\
                order_by(Measurement.date).all()
    all_temps=[]
    for t in temp_data:
        temp_dict={}
        temp_dict["temperature"]=t
        all_temps.append(temp_dict) 
    return jsonify(all_temps)
    session.close()

# 4.   Start and End Date
# i.   /api/v1.0/<start> and /api/v1.0/<start>/<end>
# ii.  Return a JSON list of the minimum temperature, the average temperature, and the max temperature for a given start or start-end range.
# iii. When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than and equal to the start date.
# iv.  When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates between the start and end date inclusive.

@app.route("/api/v1.0/start day/<start_date>")

def start_day(start_date):
    # Create our session (link) from Python to the DB
    session = Session(engine)
    results_1 = session.query(Measurement.date, func.min(Measurement.tobs), func.max(Measurement.tobs),func.avg(Measurement.tobs)).\
                filter(Measurement.date >= start_date).\
                group_by(Measurement.date).all()
    all_results=[]
    for v1,v2,v3,v4 in results_1:
        all_result_dict={}
        all_result_dict["Date"]=v1
        all_result_dict["Minimum Temperature"]=v2
        all_result_dict["Maximum temperature"]=v3
        all_result_dict["Average Temperature"]=v4
        all_results.append(all_result_dict)
    return jsonify(all_results)
    session.close()

@app.route("/api/v1.0/start and end day/<start_date>/<end_date>")

def start_end_day(start_date, end_date):
    # Create our session (link) from Python to the DB
    session = Session(engine)
    results_2 = session.query(Measurement.date, func.min(Measurement.tobs), func.max(Measurement.tobs),func.avg(Measurement.tobs)).\
            filter(Measurement.date >= start_date).\
            filter(Measurement.date <= end_date).\
            group_by(Measurement.date).all()
    all_results_2=[]
    for v1,v2,v3,v4 in results_2:
        all_result2_dict={}
        all_result2_dict["Date"]=v1
        all_result2_dict["Minimum Temperature"]=v2
        all_result2_dict["Maximum temperature"]=v3
        all_result2_dict["Average Temperature"]=v4
        all_results_2.append(all_result2_dict)
        return jsonify(all_results_2)
        session.close()

if __name__ == '__main__':
    app.run(debug=True)

