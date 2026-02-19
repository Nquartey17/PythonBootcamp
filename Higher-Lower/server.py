import random

from flask import Flask
app = Flask(__name__)

random_number = random.randint(0, 9)

@app.route("/")
def home_page():
    return ("<h1> Guess a number between 0 to 9. Enter the number in the web address by adding a / followed by the number</h1>"
            "<img src=https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif>"
            )

@app.route("/<int:guess>")
def guess_number(guess):
    if guess > random_number:
        return ("<h1>Guess is too high, try again</h1>" 
               "<img src='https://media1.tenor.com/m/ZaSXLpF36wsAAAAd/mc-donalds-thumbs-down.gif'/>")
    elif guess < random_number:
        return ("<h1>Guess is too low, try again</h1>"
               "<img src='https://media1.tenor.com/m/frxn1MyfUNwAAAAd/shannon-sharpe.gif'/>")
    else:
        return (f"<h1 style='color: green'>You guessed correctly, the number is {guess}</h1>" 
               "<img src='https://media.tenor.com/FZAs03pY_3AAAAAM/dance-monopoly.gif'/>")

if __name__ == "__main__":
    app.run(debug=True) # debug=True: Changes will reflect without having to stop code
