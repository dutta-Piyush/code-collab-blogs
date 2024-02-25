from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class LoginForm(FlaskForm):
    email = StringField('Email ID', validators=[DataRequired(), Length(max=30), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=3, max=20)])
    submit = SubmitField('Login')
