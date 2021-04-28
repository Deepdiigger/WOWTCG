#python script to save match data
import datetime

players =['Alex', 'Joe', 'Jt','Spezi']




class Teams:
  def __init__(self, teams):
    self.teams = teams
    self.size = len(teams)
    #check if Teams have equal number of players
    noTeams=False
    for i in teams:
        if len(teams[0]) != len(i):
            noTeams = True
            break
    if noTeams: print("Teamsizes do  not match")


match = Teams([['Alex','Joe'],['Jt','Spezi'],['sjdk']])

print(match.teams)
print(match.size)

# def gametype(teams):
#     nrTeams = len(teams)
#     print("Teams", nrTeams)
#
#     #check if Teams have equal number of players
#     noTeams=False
#     for i in teams:
#         if len(teams[0]) != len(i):
#             noTeams = True
#             break
#     if noTeams: print("Teamsizes do not match")
#
#
# gametype([['Alex','Joe'],['Jt','Spezi']])
