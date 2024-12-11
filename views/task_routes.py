from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from models import Task, db
from forms import TaskForm

task_views = Blueprint('task_views', __name__)

@task_views.route('/')
@login_required
def view_tasks():
    tasks = Task.query.all()
    return render_template('task_list.html', tasks=tasks)

@task_views.route('/add', methods=['GET', 'POST'])
@login_required
def add_task():
    form = TaskForm()
    if form.validate_on_submit():
        task = Task(
            name=form.name.data,
            description=form.description.data,
            task_type=','.join(form.task_type.data),
            created_by=current_user.name,
            start_date=form.start_date.data,
            end_date=form.end_date.data
        )
        db.session.add(task)
        db.session.commit()
        return redirect(url_for('task_views.view_tasks'))
    return render_template('add_task.html', form=form)
