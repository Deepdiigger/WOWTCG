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
        self.gamerow = pd.DataFrame()

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
    def endGame(self, winningTeam):

        try:
            self.winner = self.teams[winningTeam]
            self.setEndTime()
        except IndexError:
            print('sorry, no Team', winningTeam+1)

#start Session add matches, ... testsection

game = Game([['Alex','Joe'],['Jt','Spezi']])
game.endGame(1)
game.details()
