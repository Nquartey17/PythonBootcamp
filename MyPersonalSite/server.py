from flask import Flask, render_template
app = Flask(__name__)

@app.route("/") # hello_world will activate if user tries to react home page (/)
def home():
    return render_template("index.html")

if __name__ == '__main__':
    app.run(debug=True)