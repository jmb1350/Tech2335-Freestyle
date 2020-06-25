# web_app/routes/weather_routes.py

from flask import Blueprint, render_template, request

from app.weather_service import get_hourly_forecasts

weather_routes = Blueprint("weather_routes", __name__)

@flight_routes.route("/")
def weather_form():
    print("VISITED THE FLIGHT FORM...")
    return render_template("flight_form.html")

@flight_routes.route("/departure_details", methods=["GET", "POST"])
def departure_details():
    print("GENERATING DEPARTURE INFORMATION...")

    if request.method == "POST":
        print("FORM DATA:", dict(request.form)) #> {'zip_code': '20057'}
        zip_code = request.form["zip_code"]
    elif request.method == "GET":
        print("URL PARAMS:", dict(request.args))
        zip_code = request.args["zip_code"] #> {'zip_code': '20057'}

    results = get_hourly_forecasts(zip_code)
    print(results.keys())
    return render_template("weather_forecast.html", zip_code=zip_code, results=results)