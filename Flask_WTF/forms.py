from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField ,SubmitField
from wtforms.validators import DataRequired, Email, Length    

#pip install flask-wtf 
#pip install email-validator

class RegistrationForm(FlaskForm):
    name = StringField(' Full Name', validators=[DataRequired(message="Please enter your full name.")])
    email = StringField('Email', validators=[DataRequired(message="Please enter your email address."), Email()])
    password = PasswordField('Password', validators=[DataRequired(message="Please enter a password."), Length(min=6, message="Password must be at least 6 characters long.")])
    submit = SubmitField('Register')