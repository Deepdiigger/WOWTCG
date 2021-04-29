#fresh start to save match data
import datetime
import time
import pandas as pd
import os

dirname = os.path.dirname(__file__)
filename = os.path.join(dirname, 'games.csv')



if os.path.exists(filename):
    append_write = 'a' # append if already exists
    append_header = False
    games = pd.read_csv(filename, index_col = 0)

else:
    append_write = 'w' # make a new file if not
    append_header = True



#initialize Datastructure of a row
iGame = {'Team1': 1, 'Team2': 2, 'Points1': 2, 'Points2' :1}

game = pd.Series(iGame)

games = pd.DataFrame(game)
games = games.append (game)



print(games)
