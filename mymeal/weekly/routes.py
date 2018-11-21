from flask import render_template, Blueprint, request, redirect, url_for
from flask_login import login_required
from mymeal.weekly.forms import ThisWeekForm, ThisWeeksIngredients
from mymeal.models import Ingredient

from sqlalchemy import and_, desc, asc

weekly = Blueprint('weekly', __name__)


@weekly.route('/week/new', methods=['GET', 'POST'])
@login_required
def new_week():
    ingredients = ''
    form = ThisWeekForm()
    if request.method == 'POST':
        return redirect(url_for('weekly.week_ingredients'))
    return render_template('thisweek.html', title='This Week', form=form, ingredients=ingredients)


@weekly.route('/week/ingredients', methods=['GET', 'POST'])
@login_required
def week_ingredients():
    if request.method == 'POST':
        r1 = int(request.form['saturdaySelect'])
        r2 = int(request.form['sundaySelect'])

        supermarket = Ingredient.query.filter(and_(Ingredient.purchased_at == "supermarket", Ingredient.recipe_id.in_([r1, r2]))).order_by(asc(Ingredient.name))
        butchers = Ingredient.query.filter(and_(Ingredient.purchased_at == "butcher", Ingredient.recipe_id.in_([r1, r2])))
        greengrocers = Ingredient.query.filter(and_(Ingredient.purchased_at == "greengrocer", Ingredient.recipe_id.in_([r1, r2])))

        form = ThisWeeksIngredients()
        return render_template('weekly_ingredients.html', title='Ingredients', form=form, supermarket=supermarket,
                               butchers=butchers, greengrocers=greengrocers)
