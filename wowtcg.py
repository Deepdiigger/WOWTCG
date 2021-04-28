#python script to save match data
import datetime
import time

players =['Alex', 'Joe', 'Jt','Spezi']




class Match:
    def __init__(self, teams):
        self.teams = teams
        self.size = len(teams)
        self.teamSize = 0
        self.sTime = datetime.datetime.now()
        self.eTime = datetime.datetime.now()
        self.duration = 0
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

        print('Number of teams', self.size,'Teamsize',self.teamSize, 'StartTime', self.sTime, 'EndTime', self.eTime, "Duration", self.duration )

#function to set Endtime and calculate Duration
    def setEndTime(self):
        self.eTime = datetime.datetime.now()
        self.duration = self.eTime - self.sTime

match = Match([['Alex','Joe'],['Jt','Spezi']])

match.details()

# match1 = Match([['Joe'],['Alex']])
# match1.details()
