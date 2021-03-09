from flask_wtf import FlaskForm
from wtforms import DecimalField, StringField, SubmitField
from wtforms.validators import DataRequired


class EditForm(FlaskForm):
    rating = DecimalField(label='Enter New Rating (e.g. 7.6)', validators=[DataRequired()])
    review = StringField(label='Enter New Review', validators=[DataRequired()])
    submit = SubmitField(label='Submit')


class AddMovieForm(FlaskForm):
    movie = StringField(label='Enter Movie Name', validators=[DataRequired()])
    submit = SubmitField(label='Search')
