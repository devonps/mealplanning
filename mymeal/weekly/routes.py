from flask import render_template, Blueprint, request
from flask_login import login_required
from mymeal.weekly.forms import NewWeekForm, ThisWeekForm
from mymeal.models import Recipe


weekly = Blueprint('weekly', __name__)


@weekly.route('/week/view', methods=['GET', 'POST'])
@login_required
def view_this_week():
    form = ThisWeekForm()
    recipes = Recipe.query.all()
    if request.method == 'POST':
        pass
    return render_template('thisweek.html', title='This Week', form=form)


@weekly.route('/week/new', methods=['GET', 'POST'])
@login_required
def new_week():
    form = NewWeekForm()
    return render_template('new_week.html', form=form)
