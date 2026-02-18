# File name can't be the same as module name or the program won't work
from flask import Flask
app = Flask(__name__)

@app.route("/") # hello_world will activate if user tries to react home page (/)
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/bye")
def say_bye():
    return "Bye"

if __name__ == "__main__":
    app.run(debug=True)
