from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import login_required
from mymeal import db


weekly = Blueprint('weekly', __name__)


@weekly.route('/week/view')
@login_required
def view_this_week():
    return render_template('thisweek.html', title='This Week')
