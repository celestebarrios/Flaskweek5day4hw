from flask_wtf import FlaskForm

from wtforms import StringField, SubmitField, TextAreaField
from wtforms.validators import DataRequired 

class Form(FlaskForm):
    names = StringField("Birth Name",validators=[DataRequired()])
    number = StringField("Phone Number",validators=[DataRequired()])
    submit = SubmitField()