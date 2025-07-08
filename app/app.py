from flask import Flask, render_template
from config import Config
from database import Database
from crud import CRUD


def create_app():
    app = Flask(__name__)

    @app.route("/")
    def index():
        print(">>> Home route /")
        # temperature_data = get_temperature_df()
        # return temperature_data.to_html()
        temperatures = get_current_temperatures()
        return render_template("index.html", temperatures=temperatures)

    return app


def get_current_temperatures():
    crud = CRUD(db)
    temperatures = crud.get_all_temperatures()
    print(temperatures)
    return temperatures


def get_temperature_df():
    crud = CRUD(db)
    return crud.get_temp_df()


db = Database(
    host=Config.DATABASE_HOST,
    db_name=Config.DATABASE_NAME,
    username=Config.DATABASE_USER,
    password=Config.DATABASE_PASSWORD,
)

app = create_app()
