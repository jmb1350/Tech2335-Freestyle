# web_app/routes/weather_routes.py

from flask import Blueprint, render_template, request

from app.maps import get_departure_time
from app.flights import get_flight_information

flight_routes = Blueprint("flight_routes", __name__)

# 
@flight_routes.route("/")
def flight_form():
    print("VISITED THE FLIGHT FORM...")
    return render_template("flight_form.html")

@flight_routes.route("/departure_details", methods=["POST"])
def departure_details():
    print("GENERATING DEPARTURE INFORMATION...")

    print("FORM DATA:", dict(request.form)) #> {'zip_code': '20057'}
    f_address = request.form["f_address"]
    f_city = request.form["f_city"]
    f_state = request.form["f_state"]
    f_zip = request.form["f_zip"]
    flight = request.form["flight"]
    airline = request.form["airline"]

    results = get_flight_information(flight, airline) and get_departure_time(f_address, f_city, f_state, f_zip)
    print(results.keys())
    return render_template("flight_data.html", flight=flight, airline=airline, results=results)
    # return("okay")