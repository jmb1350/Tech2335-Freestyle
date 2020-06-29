# web_app/routes/weather_routes.py

from flask import Blueprint, render_template, request

# from app.departure import get_departure_time, get_flight_information

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

    results = departure.get_flight_information(flight, airline) and departure.get_departure_time(f_address, f_city, f_state, f_zip)
    print(results.keys())
    flash(f"Information submitted successfully", "success")
    return render_template("flight_data.html", flight=flight, airline=airline, results=results)
    # return("okay")