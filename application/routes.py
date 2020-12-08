from application import app, db
from application.models import Games

@app.route('/add')
def add():
    new_game = Games(name="New Game")
    if new_game.name == "New Game":
        return " Please enter a unique game title, as this game already exists"
    else:   
        db.session.add(new_game)
        db.session.commit()
        return "Added new game to database"

@app.route('/add/<name>')
def add2(name):
    if name == Games(name="New Game"):
        return "Game already contained within list"
    else:
        new_game2 = Games(name="default")
        new_game2.name = name
        db.session.add(new_game2)
        db.session.commit()
        return new_game2.name

@app.route('/read')
def read():
    all_games = Games.query.all()
    games_string = ""
    for game in all_games:
        games_string += "<br>"+ game.name
    return games_string + " <br> There are " + str(Games.query.count()) + " Games in the database"

@app.route('/update/<nameold>/<namenew>')
def update(nameold,namenew):
    game = Games.query.filter_by(name=nameold).first()
    nameold = game
    nameoldval = nameold.name
    if game is not None:
        game.name = namenew
        db.session.commit()
        return str(nameoldval) + " is now known as " + str(namenew)
    else:
        return "Not available to update"

@app.route('/delete')
def delete():
    last_game = Games.query.first()
    db.session.delete(last_game)
    db.session.commit()
    return "Deleted first game from database"

@app.route('/delete/<name>')
def delete1(name):
    game = Games.query.filter_by(name=name).first()
    if game is not None:
        db.session.delete(game)
        db.session.commit()
        return "Specified game deleted"
    else:
        return "Specified game not available"