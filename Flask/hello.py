# File name can't be the same as module name or the program won't work
from flask import Flask
app = Flask(__name__)

@app.route("/") # hello_world will activate if user tries to react home page (/)
def hello_world():
    return ("<h1 style='text=align': center>Hello, World!</h1>"
            "<p>This is a paragraph</p>"
            "<img src=https://media.tenor.com/IN-qCk4y0KgAAAAM/explosion-bombing-explosion.gif>"
            )

@app.route("/bye")
def say_bye():
    return "Bye"

# Using <> to make variable name into url
# Converter (<converter:variable name) will specify the type of the argument
# path works like string but also accepts slashes. String does not
@app.route("/<path:name>/<int:number>")
def greet(name, number):
    return f"Hello {name}: Your number is {number}!"

if __name__ == "__main__":
    app.run(debug=True) # debug=True: Changes will reflect without having to stop code
