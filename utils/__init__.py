from flask import Flask
from flask import Flask,render_template


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'


# @app.route("/")
# def hello():
# 	render_template("hi")

from utils import routes
