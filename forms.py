from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired, URL, Optional, NumberRange


class AddCupcakeForm(FlaskForm):
    flavor = StringField("Flavor", validators=[InputRequired(message="Flavor can't be blank")])
    size = StringField("Size", validators=[InputRequired(message="Size can't be blank")])
    rating = IntegerField("Rating", validators=[ NumberRange(min=1, max=10, message="Rating must be between 1 and 10")])
    image = StringField("Image URL", validators=[Optional(), URL(require_tld=False, message="Please enter a valid URL")])
