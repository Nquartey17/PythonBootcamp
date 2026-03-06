from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
#Secret key is required, randomly generate it yourself
app.config['SECRET_KEY'] = ''

class LoginForm(FlaskForm):
    email = StringField('Email')
    password = StringField('Password')
    submit = SubmitField('Log In')

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=['GET','POST'])
def login():
    form = LoginForm()
    return render_template("login.html",form=form)


if __name__ == '__main__':
    app.run(debug=True)