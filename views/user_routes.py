from flask import Blueprint, current_app, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from models import User, db
from forms import UserForm
import os

user_views = Blueprint('user_views', __name__)

@user_views.route('/')
@login_required
def view_users():
    users = User.query.all()
    return render_template('user_list.html', users=users)

@user_views.route('/add', methods=['GET', 'POST'])
@login_required
def add_user():
    form = UserForm()
    if form.validate_on_submit():
        image_file = request.files['image']
        if image_file:
            image_path = os.path.join(current_app.config['UPLOAD_FOLDER'], image_file.filename)
            image_file.save(image_path)
        user = User(
            name=form.name.data,
            email=form.email.data,
            gender=form.gender.data,
            role_id=form.role.data,
            created_by=current_user.name,
            image=image_file.filename if image_file else None
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('user_views.view_users'))
    return render_template('add_user.html', form=form)
