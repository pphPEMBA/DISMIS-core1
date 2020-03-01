from wtforms import Form, StringField, PasswordField, validators, SubmitField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length, Optional


class SignupForm(Form):
    """User Signup Form."""

    name = StringField('Name', [DataRequired()])
    email = StringField('Email',
                        [DataRequired(),
                         Length(min=6, message=('Please enter a valid email address.')),
                         Email(message=('Please enter a valid email address.'))])
    password = PasswordField('Password',
                             [DataRequired(),
                              Length(min=6, message=('Please select a stronger password.')),
                              EqualTo('confirm', message='Passwords must match')])
    confirm = PasswordField('Confirm Your Password',)
    website = StringField('Website',
                          [Optional()])
    submit = SubmitField('Register')


class LoginForm(Form):
    """User Login Form."""

    email = StringField('Email', [DataRequired(),
                                  Email('Please enter a valid email address.')])
    password = PasswordField('Password', [DataRequired()])
    submit = SubmitField('Log In')