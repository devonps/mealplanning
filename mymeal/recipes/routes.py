from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from mymeal.models import Recipe, Ingredient
from mymeal.recipes.forms import RecipeForm
from flask_login import current_user, login_required
from mymeal import db

recipes = Blueprint('recipes', __name__)


@recipes.route('/recipe/new', methods=['GET', 'POST'])
@login_required
def new_recipe():
    form = RecipeForm()
    if form.validate_on_submit():
        recipe = Recipe(title=form.title.data, serves=form.serves.data, description=form.description.data,
                        recipe_type = form.recipe_type.data,author=current_user)
        db.session.add(recipe)
        db.session.commit()
        flash('Your recipe has been added!', 'success')
        return redirect(url_for('main.home'))
    return render_template('create_recipe.html', title='New Recipe', form=form, legend='New Recipe')


@recipes.route('/recipe/<int:recipe_id>')
@login_required
def recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    ingredients = Ingredient.query.filter_by(recipe_id=recipe_id)
    ingredient_count = Ingredient.query.filter_by(recipe_id=recipe_id).count()
    if ingredient_count == 0:
        ingredient_button_text = 'Add the first ingredient'
    else:
        ingredient_button_text = 'Add another ingredient'

    return render_template('recipe.html', title=recipe.title, recipe=recipe, ingredients=ingredients,
                           count=ingredient_count, ingredient_button_text=ingredient_button_text)


@recipes.route('/recipe/<int:recipe_id>/update', methods=['GET', 'POST'])
@login_required
def update_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    if recipe.author != current_user:
        abort(403)
    form = RecipeForm()
    if form.validate_on_submit():
        recipe.title = form.title.data
        recipe.serves = form.serves.data
        recipe.description = form.description.data
        recipe.recipe_type = form.recipe_type.data
        db.session.commit()
        flash('Your recipe has been updated!','success')
        return redirect(url_for('recipes.recipe', recipe_id=recipe.id))
    elif request.method == 'GET':
        form.title.data = recipe.title
        form.serves.data = recipe.serves
        form.description.data = recipe.description
        form.recipe_type.data = recipe.recipe_type
    return render_template('create_recipe.html', title='Update Recipe', legend='Update Recipe', recipe=recipe, form=form)


@recipes.route('/recipe/<int:recipe_id>/delete', methods=['POST'])
@login_required
def delete_recipe(recipe_id):
    recipe = Recipe.query.get_or_404(recipe_id)
    if recipe.author != current_user:
        abort(403)

    db.session.delete(recipe)
    db.session.commit()
    flash('Your recipe has been deleted!', 'success')
    return redirect(url_for('main.home'))
