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


@app.route('/change/<int:id>', methods=["GET","POST"])
def change(id):
    form=TaskForm()
    all_tasks = Tasks.query.all()
    task = Tasks.query.filter_by(id=id).first()
    if task.complete == True:
        task.complete = False
        db.session.commit()
    elif task.complete == False:
        task.complete = True
        db.session.commit()
    else:
        task.complete = task.complete
    return render_template("home.html", form=form, task=task, all_tasks=all_tasks)

@app.route('/update/<int:id>', methods=["GET", "POST"])
def update(id):
    form = TaskForm()
    task = Tasks.query.order_by(Tasks.id.desc()).first()
    if request.method == "POST":
        task.description = form.description.data
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("update.html", form=form, title="Update Task",task=task)

@app.route('/delete/<int:id>', methods=["GET"])
def delete(id):
    task = Tasks.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit()
    return redirect(url_for("home"))
