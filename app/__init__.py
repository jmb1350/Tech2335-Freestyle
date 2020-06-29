
# app/__init__.py

import os
from dotenv import load_dotenv
from flask import Flask

# from app.routes.flight_routes import flight_routes
from app.routes.home_routes import home_routes
load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY", default="super secret") # use "production" on a remote server

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = SECRET_KEY

    app.register_blueprint(home_routes)
    # app.register_blueprint(flight_routes)

    return app

# def start():
#     from app.departure import get_flight_information, get_departure_time

if __name__ == "__main__":
    my_app = create_app()
    my_app.run(debug=True)