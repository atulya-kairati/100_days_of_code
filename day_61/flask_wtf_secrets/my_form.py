from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    PasswordField,
    SubmitField
)
from wtforms.validators import (
    Email,
    Length
)


class MyLoginForm(FlaskForm):
    email = StringField(label='Email', validators=[Email()])
    pswd = PasswordField(label='Password', validators=[Length(min=8)])
    submit = SubmitField(label='Log In')
