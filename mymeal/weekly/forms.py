from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from mymeal.models import Recipe


class NewWeekForm(FlaskForm):
    recipe = StringField('Meal', validators=[DataRequired()], render_kw={'placeholder': 'Name of meal'})
    submit = SubmitField('Add meal')


class ThisWeekForm(FlaskForm):
    aSelect = StringField('Meal', validators=[DataRequired()], render_kw={'placeholder': 'Name of meal'})
    mondaySelect = SelectField('Monday')
    tuesdaySelect = SelectField('Tuesday')
    wednesdaySelect = SelectField('Wednesday')
    thursdaySelect = SelectField('Thursday')
    fridaySelect = SelectField('Friday')
    saturdaySelect = SelectField('Saturday')
    sundaySelect = SelectField('Sunday')
    submit = SubmitField('Create Ingredients List')

    def __init__(self, *args, **kwargs):
        super(ThisWeekForm, self).__init__(*args, **kwargs)
        default_message = 'Select Meal'
        recipes = Recipe.query.all()
        self.mondaySelect.choices = [(0, default_message)] + [(recipe.id, recipe.title) for recipe in recipes]
        self.tuesdaySelect.choices = [(0, default_message)] + [(recipe.id, recipe.title) for recipe in recipes]
        self.wednesdaySelect.choices = [(0, default_message)] + [(recipe.id, recipe.title) for recipe in recipes]
        self.thursdaySelect.choices = [(0, default_message)] + [(recipe.id, recipe.title) for recipe in recipes]
        self.fridaySelect.choices = [(0, default_message)] + [(recipe.id, recipe.title) for recipe in recipes]
        self.saturdaySelect.choices = [(0, default_message)] + [(recipe.id, recipe.title) for recipe in recipes]
        self.sundaySelect.choices = [(0, default_message)] + [(recipe.id, recipe.title) for recipe in recipes]


class ThisWeeksIngredients(FlaskForm):
    submit = SubmitField('Home Page')