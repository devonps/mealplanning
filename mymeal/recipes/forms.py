from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, TextAreaField, IntegerField
from wtforms.validators import DataRequired


class RecipeForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    serves = IntegerField('Serves how many people', validators=[DataRequired()])
    description = TextAreaField('Description', validators=[DataRequired()])
    recipe_type = StringField('Recipe Type', validators=[DataRequired()])
    submit = SubmitField('Create')