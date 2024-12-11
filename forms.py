from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectMultipleField, RadioField, SelectField, DateField, FileField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class TaskForm(FlaskForm):
    name = StringField('Task Name', validators=[DataRequired(), Length(max=100)])
    description = StringField('Task Description', validators=[DataRequired(), Length(max=200)])
    task_type = SelectMultipleField(
        'Task Type',
        choices=[
            ('a-task', 'A Task'),
            ('b-task', 'B Task'),
            ('c-task', 'C Task'),
            ('d-task', 'D Task'),
            ('e-task', 'E Task'),
        ],
        validators=[DataRequired()],
        coerce=str
    )
    start_date = DateField('Start Date', validators=[DataRequired()], format='%Y-%m-%d')
    end_date = DateField('End Date', validators=[DataRequired()], format='%Y-%m-%d')
    submit = SubmitField('Submit Task')

class UserForm(FlaskForm):
    name = StringField('User Name', validators=[DataRequired(), Length(max=100)])
    image = FileField('User Image')
    email = StringField('Email', validators=[DataRequired(), Email(), Length(max=120)])
    gender = RadioField(
        'Gender',
        choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')],
        validators=[DataRequired()]
    )
    role = SelectField(
        'Role',
        choices=[
            ('super-admin', 'Super Admin'),
            ('admin', 'Admin'),
            ('manager', 'Manager'),
        ],
        validators=[DataRequired()],
        coerce=str
    )
    submit = SubmitField('Submit User')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')
