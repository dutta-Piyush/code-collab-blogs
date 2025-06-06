from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Length


class ContentForm(FlaskForm):
    title = StringField('Blog Title', validators=[DataRequired(), Length(max=100)])
    body = TextAreaField('Blog Body', validators=[DataRequired()])
    submit = SubmitField('Submit')
