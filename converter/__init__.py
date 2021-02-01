import os
import requests
from flask import Flask, render_template, request

WOLFRAM_APP_ID = os.environ["WOLFRAM_APP_ID"]
endpoint = f"https://api.wolframalpha.com/v1/result?appid={WOLFRAM_APP_ID}&i="


def format_question(string):
    question = " ".join(string.split())
    question = question.strip(" ?&/\\")
    return question.replace(" ", "+")


def create_app():
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    # a simple page that says hello
    @app.route("/", methods=["GET", "POST"])
    def index():
        if request.method == "POST":
            if request.headers["Content-Type"] == "application/json":
                question = format_question(request.json["question"])
                answer = requests.get(endpoint + question).text
                return answer
            question = format_question(request.form["question"])
            answer = requests.get(endpoint + question).text
            return render_template("index.html", answer=answer)
        return render_template("index.html")

    return app
