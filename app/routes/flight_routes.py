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
    address = request.form["f_address"]
    city = request.form["f_city"]
    state = request.form["f_state"]
    zip_code = request.form["f_zip"]
    flight_number = request.form["flight_number"]
    airline = request.form["airline"]

    results = get_flight_information(flight_number, airline)+get_departure_time(address, city, state, zip_code)
    print(results.keys())
    return render_template("flight_data.html", flight=flight, airline=airline, results=results)
    # return("okay")