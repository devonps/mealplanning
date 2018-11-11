from flask import render_template, request, Blueprint
from mymeal.models import Recipe


main = Blueprint('main', __name__)


@main.route('/')
@main.route('/home')
def home():
    page = request.args.get('page', 1, type=int)
    recipes = Recipe.query.order_by(Recipe.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', title='Home', recipes=recipes)


@main.route('/about')
def about():
    return render_template('about.html', title='About')