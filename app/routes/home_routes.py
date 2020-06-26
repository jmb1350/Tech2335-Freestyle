# web_app/routes/home_routes.py

from flask import Blueprint, render_template, redirect, request, flash


home_routes = Blueprint("home_routes", __name__)

@home_routes.route("/")
def index():
    print("VISITED THE HOME PAGE")
    #return render_template("dashboard.html")
    # return "Welcome Home (TODO)"
    return render_template("flight_form.html")

@home_routes.route("/departure_details", methods=["POST"])
def create_user():
    print("FORM DATA:", dict(request.form))
    # FYI: we are able to access the form data via the "request" object we import from flask
    # ... these keys correspond with the "name" attributes of each <input> element in the form!
    #> {'full_name': 'Example User', 'email_address': 'me@example.com', 'country': 'US'}

    user_details = dict(request.form)
    # todo: store in a database or google sheet!

    # FYI: "warning", "primary", "danger", "success", etc. are bootstrap color classes
    # ... see https://getbootstrap.com/docs/4.3/components/alerts/
    # ... and the flash messaging section of the "bootstrap_layout.html" file for more details
    flash("okay!", "success")
    return redirect("/")