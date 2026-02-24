from flask import Flask, render_template
import requests

app = Flask(__name__)
blog_url = requests.get(url="https://api.npoint.io/c790b4d5cab58020d391").json()

@app.route('/')
def home():
    return render_template("index.html", posts=blog_url)

@app.route('/post/<int:card_id>')
def post(card_id):
    return render_template("post.html",posts=blog_url, card_id=card_id)

if __name__ == "__main__":
    app.run(debug=True)
