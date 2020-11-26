from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Length, Email, EqualTo,ValidationError
from wtforms import StringField,SubmitField

class InputForm(FlaskForm):
	tag = StringField('tag')
	submit = SubmitField('Sentiments')