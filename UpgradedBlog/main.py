from flask import Flask, render_template, request
import requests


app = Flask(__name__)
response = requests.get(url="https://api.npoint.io/2635a81c7b36b9705a5d").json()

@app.route('/')
def home():
    return render_template("index.html", posts=response)

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)

@app.route('/post/<int:card_id>')
def post(card_id):
    return render_template("post.html", posts=response, card_id=card_id)

@app.route('/form-entry', methods=['POST'])
def receive_data():
    return "<h1>Successfully sent your message</h1>"

if __name__ == "__main__":
    app.run(debug=True)
