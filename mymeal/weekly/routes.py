from flask import render_template, Blueprint, request
from flask_login import login_required, current_user
from mymeal.weekly.forms import ThisWeekForm
from mymeal.models import Mealplan
from mymeal import db

weekly = Blueprint('weekly', __name__)


@weekly.route('/week/new', methods=['GET', 'POST'])
@login_required
def new_week():
    form = ThisWeekForm()
    if request.method == 'POST':
        # write out week choices to Mealplan table
        week = current_user.meal_plan_count + 1
        week_description = 'week ' + str(week)
        dirty_table = False

        if int(form.saturdaySelect.data) != 0:
            dirty_table=True
            saturdaymeal = Mealplan(week=week, day_of_meal='saturday', meal_id=form.saturdaySelect.data,
                                    week_description=week_description, creator=current_user)
            db.session.add(saturdaymeal)

        if int(form.sundaySelect.data) != 0:
            dirty_table = True
            sundaymeal = Mealplan(week=week, day_of_meal='sunday', meal_id=form.sundaySelect.data, week_description=week_description, creator=current_user)
            db.session.add(sundaymeal)

        if int(form.mondaySelect.data) != 0:
            dirty_table = True
            mondaymeal = Mealplan(week=week, day_of_meal='monday', meal_id=form.mondaySelect.data, week_description=week_description, creator=current_user)
            db.session.add(mondaymeal)

        if int(form.tuesdaySelect.data) != 0:
            dirty_table = True
            tuesdaymeal = Mealplan(week=week, day_of_meal='tuesday', meal_id=form.tuesdaySelect.data, week_description=week_description, creator=current_user)
            db.session.add(tuesdaymeal)

        if int(form.wednesdaySelect.data) != 0:
            dirty_table = True
            wednesdaymeal = Mealplan(week=week, day_of_meal='wednesday', meal_id=form.wednesdaySelect.data, week_description=week_description, creator=current_user)
            db.session.add(wednesdaymeal)

        if int(form.thursdaySelect.data) != 0:
            dirty_table = True
            thursdaymeal = Mealplan(week=week, day_of_meal='thursday', meal_id=form.thursdaySelect.data, week_description=week_description, creator=current_user)
            db.session.add(thursdaymeal)

        if int(form.fridaySelect.data) != 0:
            dirty_table = True
            fridaymeal = Mealplan(week=week, day_of_meal='friday', meal_id=form.fridaySelect.data, week_description=week_description, creator=current_user)
            db.session.add(fridaymeal)

        if dirty_table:
            setattr(current_user, 'meal_plan_count', week)
            db.session.commit()

    return render_template('thisweek.html', title='This Week', form=form)


@weekly.route('/week/ingredients', methods=['GET', 'POST'])
@login_required
def week_ingredients():
    return render_template('weekly_ingredients.html', title='Ingredients', form=form, supermarket=supermarket,
                                   butchers=butchers, greengrocers=greengrocers)