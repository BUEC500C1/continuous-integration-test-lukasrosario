import os
from flask import Flask, render_template

WOLFRAM_APP_ID = os.environ["WOLFRAM_APP_ID"]
endpoint = f"https://api.wolframalpha.com/v1/result?appid={WOLFRAM_APP_ID}"


def format_question(string):
    return string.strip(" ?&/")


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # a simple page that says hello
    @app.route("/")
    def index():
        return render_template("index.html")

    return app
