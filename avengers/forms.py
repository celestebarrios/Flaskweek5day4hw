from flask_wtf import FlaskForm

from wtforms import StringField, PasswordField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Email

class UserInfoForm(FlaskForm):
    username = StringField("Birth Name",validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    number = StringField("Phone Number",validators=[DataRequired()])
    confirm_pass = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
   
    submit = SubmitField()

class LoginForm(FlaskForm):
    email = StringField('Email',validators=[DataRequired(),Email()])
    password = PasswordField('Password', validators = [DataRequired()])
    number = StringField("Phone Number",validators=[DataRequired()])

    submit=SubmitField()
class NumberForm(FlaskForm):
    number = StringField("Phone Number",validators=[DataRequired()])
    updated_number = StringField("New Number",validators=[DataRequired()])
    submit=SubmitField()