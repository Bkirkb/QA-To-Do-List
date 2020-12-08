from application import app, db
from application.models import Tasks



@app.route('/')
@app.route('/home')
def home():
    all_tasks = Tasks.query.all()
    output = " "
    for task in all_tasks:
        output = task.description + "<br>"
    return output


@app.route('/create')
def add():
    new_todo = Tasks(description="New Task")
    db.session.add(new_todo)
    db.session.commit()
    return "New Task Added"

##@app.route('/add/<name>')
##def add2(name):
    #if task == Task(description="New "):
        #return "Game already contained within list"
    #else:
        #new_game2 = Games(name="default")
        #new_game2.name = name
        #db.session.add(new_game2)
        #db.session.commit()
        #return new_game2.name

@app.route('/complete/<int:id>')
def complete(id):
    task = Tasks.query.filter_by(id=id).first()
    task.completed = True
    db.session.commit()
    return "Task ", str(id), " Is now complete"

@app.route('/incomplete/<int:id>')
def incomplete(id):
    task = Tasks.query.filter_by(id=id).first()
    task.completed = False
    db.session.commit()
    return "Task ", str(id), " Is now incomplete"

@app.route('/update/<new_description>')
def update(newdescription):
    task = Tasks.query.order_by(Tasks.id.desc()).first()
    task.description = new_description
    db.session.commit()
    return "Most recent tasks was updated with the description " , str(new_description)

@app.route('/delete/<int:id>')
def delete(id):
    task = Tasks.query.filter_by(id=id).first()
    db.session.delete(task)
    db.session.commit()
    return "Task ", str(id) , " Was deleted."




# """ @app.route('/read')
# def read():
#     all_games = Games.query.all()
#     games_string = ""
#     for game in all_games:
#         games_string += "<br>"+ game.name
#     return games_string + " <br> There are " + str(Games.query.count()) + " Games in the database"

# @app.route('/update/<nameold>/<namenew>')
# def update(nameold,namenew):
#     game = Games.query.filter_by(name=nameold).first()
#     nameold = game
#     nameoldval = nameold.name
#     if game is not None:
#         game.name = namenew
#         db.session.commit()
#         return str(nameoldval) + " is now known as " + str(namenew)
#     else:
#         return "Not available to update"

# @app.route('/delete')
# def delete():
#     last_game = Games.query.first()
#     db.session.delete(last_game)
#     db.session.commit()
#     return "Deleted first game from database"

# @app.route('/delete/<name>')
# def delete1(name):
#     game = Games.query.filter_by(name=name).first()
#     if game is not None:
#         db.session.delete(game)
#         db.session.commit()
#         return "Specified game deleted"
#     else:
#         return "Specified game not available" 