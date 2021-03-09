from flask_wtf import FlaskForm
from wtforms import (
    StringField,
    SelectField,
    SubmitField
)

from wtforms.validators import (
    URL,
    DataRequired
)


class CafeForm(FlaskForm):
    name = StringField(label='Cafe Name', validators=[DataRequired()])
    location = StringField(label='Cafe Location on Maps (Link)', validators=[DataRequired(), URL()])
    open_time = StringField(label='Open Time e.g. 8AM', validators=[DataRequired()])
    close_time = StringField(label='Close Time e.g. 8PM', validators=[DataRequired()])
    coffee_rating = SelectField(label='Choose Coffee Quality', choices=['☕' * i for i in range(1, 6)])
    wifi_rating = SelectField(label='Choose Wifi Quality', choices=['✘'] + ['💪' * i for i in range(1, 6)])
    power_rating = SelectField(label='Choose Power Quality', choices=['✘'] + ['🔌' * i for i in range(1, 6)])
    add_button = SubmitField(label='Add')
