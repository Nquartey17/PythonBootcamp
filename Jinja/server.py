from flask import Flask, render_template
import random
from datetime import date
import requests

app = Flask(__name__)

@app.route("/")
def home():
    random_number = random.randint(1,10)
    year = date.today().year
    # Specify a variable name in the parameter to send to HTML file
    return render_template("index.html", num=random_number,year=year)

@app.route("/guess/<path:name>")
def guess(name):
    age_response = requests.get(f"https://api.agify.io?name={name}")
    age_data = age_response.json()

    gender_response = requests.get(f"https://api.genderize.io?name={name}")
    gender_data = gender_response.json()

    return render_template("guess.html", name=name, age=age_data["age"], gender=gender_data["gender"])

if __name__ == '__main__':
    app.run(debug=True)

