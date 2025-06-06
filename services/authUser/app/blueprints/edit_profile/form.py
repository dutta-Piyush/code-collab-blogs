from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField


class EditForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    email = StringField('Email ID')
    submit = SubmitField('Submit')

