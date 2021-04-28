#python script to save match data
import datetime
import time
from collections import Counter
import copy
import pandas as pd

players =['Alex', 'Joe', 'Jt','Spezi']




class Game:
    def __init__(self, teams):
        self.teams = teams
        self.size = len(teams)
        self.teamSize = 0
        self.sTime = datetime.datetime.now()
        self.eTime = datetime.datetime.now()
        self.duration = 0
        self.winner = []



        #set Teamsize and check if Teams have equal number of players
        noTeams=False
        for i in teams:
            if len(teams[0]) != len(i):
                noTeams = True
                break
        if noTeams: print("Teamsizes do  not match")
        else: self.teamSize = len(teams[0])

#function to print details of Match
    def details(self):

        for i in self.teams:
            print('Team',self.teams.index(i)+1,end =' ')
            for p in i:
                print(p, end = ' ')
            print()

        print('Number of teams', self.size,'Teamsize',self.teamSize, 'StartTime', self.sTime, 'EndTime', self.eTime, "Duration", self.duration, "Winner", self.winner )

#function to set Endtime and calculate Duration
    def setEndTime(self):
        self.eTime = datetime.datetime.now()
        self.duration = self.eTime - self.sTime

#function to end game and set winning teams
#create row as series, store it in selfe and return a copy
    def endGame(self, winningTeam):
        try:
            self.winner = self.teams[winningTeam]
            self.setEndTime()
            row = {'sTime': self.sTime, 'eTime': self.eTime, 'winner': self.winner, 'teams': self.teams}
            self.series = pd.Series(row)

        except IndexError:
            print('sorry, no Team', winningTeam+1)

        return(copy.deepcopy(self.series))

class Match:
    def __init__(self):
        self.games = pd.DataFrame()


    #add a game to the Match Dataframe
    def addGame(self, game):
        self.games = self.games.append(game,ignore_index=True)

    def endMatch(self):
        self.sTime = self.games['sTime'].min()
        self.eTime = self.games['eTime'].max()
        self.duration = self.eTime - self.sTime
        self.wins = pd.DataFrame(self.games['winner'].value_counts())
        self.winner = self.wins['winner'].idxmax()
        self.teams = self.wins.index.values
        self.points = self.wins['winner'].values

        row = {'sTime': self.sTime, 'eTime': self.eTime, 'winner': self.winner, 'Teams': self.teams, 'Points': self.points}
        self.result = pd.Series(row)

        return(copy.deepcopy(self.result))

    def details(self):
        print(self.result)

class Session:
    def __init__(self):
        self.matches = pd.DataFrame()

    def addMatch(self, match):
        self.matches = self.matches.append(match,ignore_index=True)

#start Session add matches, ... testsection

game = Game([['Alex','Joe'],['Jt','Spezi']])
game1 = game.endGame(0)
time.sleep(0.1)
game2 = game.endGame(0)
time.sleep(0.1)
game3 = game.endGame(1)

match = Match()
match.addGame(game1)
match.addGame(game2)
match.addGame(game3)
#print(match.games)
#print(match.endMatch())

session = Session()
session.addMatch(match.endMatch())
session.addMatch(match.endMatch())
session.addMatch(match.endMatch())
print(session.matches)
print('matches in Sessions not perfect, add games and so on. Acces a sessio with all games,...')
