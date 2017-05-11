from flask import Flask, render_template, request

app = Flask(__name__)
import DatabaseHelper as dh
import SimilarityFinder as sf
import flask
from collections import Counter
import json

'''
Author: Praveen
Functionality: Renders Page dashboard.html along with neccesary users being passed to the Page

Note: If movielens.db has been deleted uncomment the result=db.CreateTables() for first time
and comment back for the following runs. Make sure the database file is created.
'''
@app.route('/')
def index():
    db = dh.DataBaseWorker()
    # result=db.CreateTables()
    usersId = db.loadUsersIDs()
    return render_template("dashboard.html", userIDs=usersId)

'''
Author: Praveen
Functionality: Return the recommended and reviewed movies for the User to the Front-End
Web page.
'''
@app.route('/getUser', methods=['GET', 'POST'])
def loadMoviesOnUser():
    db = dh.DataBaseWorker()
    value = int(request.json['value'])
    selected_cluster = int(request.json['selected_cluster'])
    defaultUserMovies, recommendedMovies = sf.getsimilarMovies(value, selected_cluster)
    movies_list = []
    for users_movie in recommendedMovies.keys():
        [movies_list.append(movie) for movie in recommendedMovies.get(users_movie)]
    unique_movies = sorted(set(movies_list))
    user_key = list(defaultUserMovies.keys())[0]
    ggg = defaultUserMovies.get(user_key);
    def_movies = []
    ratings = []
    for g in ggg:
        def_movies.append(g['movieID'])
        ratings.append(g);
    default_user_movies = sorted(set(def_movies))
    recommendedMovies = db.loadMovies(isInitial=False, keys=unique_movies)
    defaultUserMovies = db.loadMovies(isInitial=False, keys=default_user_movies, ratingData=ratings)
    return flask.jsonify(defaultMovies=defaultUserMovies, recommended=recommendedMovies)


if __name__ == "__main__":
    app.run()
