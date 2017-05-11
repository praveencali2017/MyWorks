import sqlite3
import pandas as pd
import json
import numpy as np

'''
Author: Praveen
Module Purpose: To perform CRUD operations
'''


class DataBaseWorker:
    conn = sqlite3.connect("movielens.db")
    cursor = conn.cursor()

    def CreateTables(self):
        try:
            df = pd.read_csv("csv/movies.csv")
            df.to_sql("Movie", con=self.conn, if_exists="append", index=False)
            df = pd.read_csv("csv/ratings.csv")
            df.to_sql("Rating", con=self.conn, if_exists="append", index=False)
            df = pd.read_csv("csv/links_url.csv")
            df.to_sql("Link", con=self.conn, if_exists="append", index=False)
            return True
        except:
            return False

    def loadMovies(self, isInitial, keys=0, ratingData=None):
        movies = []
        if isInitial:
            selectMoviesQuery = "SELECT * FROM Movie"
            movies = pd.read_sql_query(selectMoviesQuery, self.conn)
        else:
            myquery = "select * from Movie where movieId in (%s)" % ",".join(map(str, keys))
            # for key in keys:
            # selectMoviesQuery="SELECT * FROM Movies WHERE movieId={key}".format(key=key)
            # movies.append(pd.read_sql_query(selectMoviesQuery,self.conn))
            movies = pd.read_sql_query(myquery, self.conn)
        data = []
        for movie in movies.values:
            temp = {}
            temp[movies.columns[0]] = movie[0]
            temp[movies.columns[1]] = movie[1]
            temp[movies.columns[2]] = movie[2]
            temp['image_url'] = self.getImgUrl(movie[0])
            if ratingData is None:
                data.append(temp)
            else:
                temp['ratings'] = self.getRating(movie[0], ratingData)
                data.append(temp)
        return json.dumps(data)

    def getRating(self, movieID, data):
        rating = ''
        for movie in data:
            if movieID == int(movie['movieID']):
                return movie['rating']

        return 'Not-Rated'

    def loadUsersIDs(self):
        selectUnique = "Select distinct userId from Rating order by userId"
        users = pd.read_sql_query(selectUnique, self.conn)
        data = []
        for user in users.values:
            jsonObj = {}
            jsonObj['userId'] = np.int(user[0])
            data.append(jsonObj)
        return json.dumps(data)

    def getImgUrl(self, movieID):
        try:
            tmdbQuery = "SELECT imgUrl FROM Link where movieId={}".format(movieID)
            imgUrl = pd.read_sql_query(tmdbQuery, self.conn)
            cc = imgUrl._values[0]
            imgUrl = str(cc[0])
            print(imgUrl)
        except:
            print("error{}".format(movieID))
        return imgUrl
