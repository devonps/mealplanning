from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired


class IngredientForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    quantity = StringField('Quantity', validators=[DataRequired()])
    myChoices = [('butcher','Butcher'), ('greengrocer', 'Greengrocer'),('supermarket', 'Supermarket')]
    purchased_at = SelectField('Purchased From', choices=myChoices, validators=[DataRequired()])

    submit = SubmitField('Add')