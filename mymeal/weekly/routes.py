from flask import render_template, Blueprint, request, redirect, url_for, flash
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
    form = ThisWeeksIngredients()
    r1 = int(request.form['saturdaySelect'])
    r2 = int(request.form['sundaySelect'])
    r3 = int(request.form['mondaySelect'])
    r4 = int(request.form['tuesdaySelect'])
    r5 = int(request.form['wednesdaySelect'])
    r6 = int(request.form['thursdaySelect'])
    r7 = int(request.form['fridaySelect'])

    if request.method == 'POST':

            supermarket = get_all_ingredients_for_shopping_location('supermarket', r1, r2, r3, r4, r5, r6, r7)
            butchers = get_all_ingredients_for_shopping_location('butcher', r1, r2, r3, r4, r5, r6, r7)
            greengrocers = get_all_ingredients_for_shopping_location('greengrocer', r1, r2, r3, r4, r5, r6, r7)

            return render_template('weekly_ingredients.html', title='Ingredients', form=form, supermarket=supermarket,
                                   butchers=butchers, greengrocers=greengrocers)
    elif request.method == 'GET':
        flash('Ingredients email has been sent', 'success')
        return redirect(url_for('main.home'))


def get_all_ingredients_for_shopping_location(location, r1, r2, r3, r4, r5, r6, r7):
    return Ingredient.query.filter(
            and_(Ingredient.purchased_at == location, Ingredient.recipe_id.in_([r1, r2, r3, r4, r5, r6, r7]))).order_by(
            asc(Ingredient.name))