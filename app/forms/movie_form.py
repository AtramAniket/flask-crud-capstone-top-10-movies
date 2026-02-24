from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField, SubmitField, TextAreaField
from wtforms.validators import DataRequired, NumberRange, URL, Length

class MovieForm(FlaskForm):
    title = StringField("Title", validators=[DataRequired("Title is required")])
    year = IntegerField("Year", validators=[DataRequired("Year is required"), NumberRange(min=1888, max=2100)])
    description = StringField("Description", validators=[DataRequired("Description is required")])
    rating = FloatField("Rating", validators=[DataRequired("Rating is required"), NumberRange(min=0, max=10)])
    ranking = FloatField("Ranking", validators=[DataRequired("Ranking is required"), NumberRange(min=0, max=10)])
    review = TextAreaField("Review", validators=[DataRequired("Review is required"), Length(max=2000, message="Review cannot exceed 2000 characters")])
    img_url = StringField("Image URL", validators=[DataRequired("Image URL is required"), URL("Must be a valid url")])
    submit = SubmitField()  # label will be set dynamically