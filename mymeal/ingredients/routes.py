from flask import render_template, url_for, flash, redirect, request, Blueprint
from mymeal.models import Ingredient, Recipe
from mymeal.ingredients.forms import IngredientForm
from flask_login import login_required
from mymeal import db


ingredients = Blueprint('ingredients', __name__)


@ingredients.route('/ingredient/new', methods=['GET', 'POST'])
@login_required
def new_ingredient():
    recipe_id = request.args.get('recipe_id', default=None, type=int)
    form = IngredientForm()
    if form.validate_on_submit():
        ingredient = Ingredient(name=form.name.data, quantity=form.quantity.data,
                                purchased_at=form.purchased_at.data, recipe_id=recipe_id)
        db.session.add(ingredient)
        db.session.commit()
        flash('Your ingredient has been added!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_ingredient.html', title='New ingredient', form=form, legend='New ingredient')


@ingredients.route('/ingredient/<int:ingredient_id>/update', methods=['GET', 'POST'])
@login_required
def update_ingredient(ingredient_id):
    ingredient = Ingredient.query.get_or_404(ingredient_id)
    recipe = Recipe.query.get(ingredient.recipe_id)
    form = IngredientForm()
    if form.validate_on_submit():
        ingredient.name = form.name.data
        ingredient.quantity = form.quantity.data
        ingredient.purchased_at = form.purchased_at.data
        db.session.commit()
        flash('Your ingredient has been updated!','success')
        return redirect(url_for('recipes.recipe', recipe_id=recipe.id))
    elif request.method == 'GET':
        form.name.data = ingredient.name
        form.quantity.data = ingredient.quantity
        form.purchased_at.data = ingredient.purchased_at
    return render_template('create_ingredient.html', title='Update Ingredient', legend='Update Ingredient',
                           ingredient=ingredient, form=form)