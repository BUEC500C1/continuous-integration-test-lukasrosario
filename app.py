import os
from flask import Flask, render_template

app = Flask(__name__)

WOLFRAM_APP_ID = os.environ["WOLFRAM_APP_ID"]
endpoint = f"https://api.wolframalpha.com/v1/result?appid={WOLFRAM_APP_ID}"

print(endpoint)


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
