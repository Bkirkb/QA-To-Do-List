from application import app, db
from application.models import Tasks
from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import Form, BooleanField,StringField,SubmitField, DateField, IntegerField, DecimalField, SelectField
from wtforms.validators import DataRequired, Length, ValidationError


@app.route('/', methods=["GET", "POST"])
@app.route('/home', methods=["GET", "POST"])
def home():

    all_tasks = Tasks.query.all()
    output = []
    newoutput = {}
    for task in all_tasks:
        taskid = str(task.id)
        taskdesc = str(task.description)
        taskcomplete = str(task.complete)
        output += [" Task name:  " + taskdesc + "       Complete?    " + taskcomplete + "     Id of task is: " + taskid]
    return render_template('home.html',output=output)


@app.route('/create')
def add():
    new_todo = Tasks(description="New Task")
    db.session.add(new_todo)
    db.session.commit()
    return "New Task Added"


@app.route('/complete/<int:id>')
def complete(id):
    task = Tasks.query.filter_by(id=id).first()
    task.complete = True
    db.session.commit()
    return "Task " + str(id) + " Is now complete"

@app.route('/incomplete/<int:id>')
def incomplete(id):
    task = Tasks.query.filter_by(id=id).first()
    task.complete = False
    db.session.commit()
    return "Task " + str(id) + " Is now incomplete"

@app.route('/update/<new_description>')
def update(new_description):
    task = Tasks.query.order_by(Tasks.id.desc()).first()
    task.description = new_description
    db.session.commit()
    return "Most recent task was updated with the description " + str(new_description)

@app.route('/delete/<int:id>')
def delete(id):
    task = Tasks.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit()
    return "Task ", str(id) , " Was deleted."
