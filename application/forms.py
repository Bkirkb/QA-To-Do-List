from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,IntegerField
from wtforms.validators import DataRequired

class TaskForm(FlaskForm):
    description = StringField('Description of Task', validators=[DataRequired()])
    submit = SubmitField('Add Task')
    