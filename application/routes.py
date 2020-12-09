from application import app, db
from application.models import Tasks
from flask import Flask, render_template, request, redirect, url_for
from application.forms import TaskForm

@app.route('/', methods=["GET", "POST"])
@app.route('/home', methods=["GET", "POST"])
def home():
    all_tasks = Tasks.query.all()
    output = ""
    return render_template('home.html', title="Home", all_tasks=all_tasks)

@app.route('/create', methods = ["GET", "POST"])
def create():
    form = TaskForm()
    if request.method == "POST":
        if form.validate_on_submit():
            new_task = Tasks(description=form.description.data)
            db.session.add(new_task)
            db.session.commit()
            return redirect(url_for("home"))
    return render_template('add.html', title="Create a Task", form=form)

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
