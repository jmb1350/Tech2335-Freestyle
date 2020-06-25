# web_app/routes/weather_routes.py

from flask import Blueprint, render_template, request

# from app.weather_service import get_hourly_forecasts

flight_routes = Blueprint("flight_routes", __name__)

@flight_routes.route("/")
def weather_form():
    print("VISITED THE FLIGHT FORM...")
    return render_template("flight_form.html")

@flight_routes.route("/departure_details", methods=["POST"])
def departure_details():
    print("GENERATING DEPARTURE INFORMATION...")


    print("FORM DATA:", dict(request.form)) #> {'zip_code': '20057'}
    # zip_code = request.form["zip_code"]
    # results = get_hourly_forecasts(zip_code)
    # print(results.keys())
    # return render_template(#"flight_data.html", flight_number=flight_number, results=results)
    return("okay")