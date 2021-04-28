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

        #check if Teams have equal number of players
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

#function to set winning teams
    def setWinner(self, winningTeam):

        try:
            self.winner = self.teams[winningTeam]
            self.setEndTime()
        except IndexError:
            print('sorry, no Team', winningTeam+1)


class Match:
    def __init__(self):
        self.sTime = datetime.datetime.now()
        self.eTime = datetime.datetime.now()
        self.games = []
        self.size = 0


    def details(self):
        print('Start', self.sTime, 'End', self.eTime, 'Matches', self.size)

    def addGame(self, game):
        self.games.append(copy.deepcopy(game))
        self.size = len(self.games)


    def showGames(self):
            for i in self.games:
                i.details()

    def endMatch(self):
        self.eTime = datetime.datetime.now()
        #add winners
        #for i in self.games:
            #i.details()



#start Session add matches, ... testsection
match = Match()
game = Game([['Alex','Joe'],['Jt','Spezi']])
time.sleep(0.1)
game.setWinner(1)
match.addGame(game)

time.sleep(0.1)
game.setWinner(0)
match.addGame(game)

time.sleep(0.1)
game.setWinner(1)
match.addGame(game)

time.sleep(0.1)
match.endMatch()

#match.showGames()
match.details()
