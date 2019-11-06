#import necessary libraries
from flask import Flask, jsonify

# create instance of Flask app
app = Flask(__name__)

#/Home page.
#List all routes that are available.


@app.route("/api/v1.0/precipitation")
def precipitation():

    return jsonify(precipitation)

@app.route("/api/v1.0/stations")
def stations():

    return jsonify(stations)

@app.route("/api/v1.0/tobs")
def stations():

    return jsonify(tobs)


@app.route("/api/v1.0/start")
def start():

    return jsonify(start)

@app.route("/api/v1.0/start/end")
def end():

    return jsonify(end)



@app.route("/")
def welcome():
    return (
        f"Welcome to the weather station API<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs"
        f"/api/v1.0/start"
        f"/api/v1.0/end"
    )

    if __name__ == "__main__":
    app.run(debug=True)