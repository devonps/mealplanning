from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField, SelectField
from wtforms.validators import DataRequired


class RecipeForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    serves_choices = [('1','1'), ('2', '2'),('3', '3'),('4', '4'),('5', '5'),('6', '6'),('7', '7'),('8', '8'),('9', '9')]
    serves = SelectField('Serves How Many', choices=serves_choices, validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    recipe_type_choices = [('snack', 'Snack'), ('lunch', 'Lunch'),('dinner', 'Dinner'),('desert', 'Desert')]
    recipe_type = SelectField('Recipe Type', choices=recipe_type_choices, validators=[DataRequired()])
    recipe_book = StringField('Recipe Book')
    recipe_book_page = IntegerField('Page Number')
    submit = SubmitField('Create')