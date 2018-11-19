from flask import render_template, Blueprint, request
from flask_login import login_required
from mymeal.weekly.forms import ThisWeekForm


weekly = Blueprint('weekly', __name__)


@weekly.route('/week/new', methods=['GET', 'POST'])
@login_required
def new_week():
    form = ThisWeekForm()
    if request.method == 'POST':
        pass
    return render_template('thisweek.html', title='This Week', form=form)
