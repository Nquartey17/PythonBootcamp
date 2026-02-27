from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
    response = requests.get(url="https://api.npoint.io/2635a81c7b36b9705a5d").json()

    return render_template("index.html", posts=response)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact')
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug=True)
