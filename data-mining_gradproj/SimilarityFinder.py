import numpy as np
import pandas as pd
import operator
import csv
from scipy.stats import pearsonr

checkFrame = pd.read_csv("csv/user-ratings.csv")
'''
Author: Praveen
Functionality: Find Similarity between selected user and selected user cluster.
Ultimately return the user reviewed movies and movies being recommended for the user.
'''


def getsimilarMovies(user_selected, similar_cluster):
    selectedUser = checkFrame.ix[user_selected - 1, :]
    users = {}
    for index, row in checkFrame.iterrows():
        if selectedUser[0] == row[0]:
            continue
        else:
            users['{}'.format(row[0])] = pearsonr(selectedUser, row)[0]
    users_sort = sorted(users.items(), key=operator.itemgetter(1), reverse=True)
    selected_ids = [userID[0] for userID in users_sort[:int(similar_cluster)]]
    recommended_movies = {}
    defaultUserMovies = {}
    defaultUserMovies_list = []
    counter = 0
    for i in range(0, len(selected_ids)):
        row = checkFrame.ix[int(float(selected_ids[i])) - 1]
        selected_movies = []
        for index, item in row.iteritems():
            otheruser_mov = int(row[index])
            if otheruser_mov >= 3 and int(selectedUser[index]) == 0:
                selected_movies.append(index)
            if counter == 0:
                if int(selectedUser[index]) > 0 and index != 'Unnamed: 0':
                    temp = {}
                    temp['movieID'] = index;
                    temp['rating'] = selectedUser[index];
                    defaultUserMovies_list.append(temp);
        recommended_movies["{}".format(selected_ids[i])] = selected_movies
        defaultUserMovies["{}".format(selectedUser[0])] = defaultUserMovies_list
        counter += 1
    return defaultUserMovies, recommended_movies
