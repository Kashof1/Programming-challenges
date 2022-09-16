import csv 
from pathlib import Path 

csv_file = Path("Premier 16-17.csv")

def check_file_exists(csv_file): 
    return csv_file.is_file()
        
def read_csv(csv_file):
    csv_contents = []
    if check_file_exists(csv_file):
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            next(reader)
            for row in reader:
                csv_contents.append(row)
    return csv_contents

def teamlistmaker(csv_contents):
    teamlist = []
    for currentrow in csv_contents:
        currentitem = currentrow[1]
        if currentitem not in teamlist:
            teamlist.append(currentitem)

    return teamlist



def drawadder(currentrow, leaguetable): 
    team_1 = currentrow[1]
    team_2  = currentrow[2]
    for leaguetablerow in leaguetable:
        if leaguetablerow[0] == team_1:
            leaguetablerow[2] += 1 
        elif leaguetablerow[0] == team_2:
            leaguetablerow[2] += 1
    return leaguetable

def winAndLossAdder(winningTeamName, losingTeamName, leaguetable):
    for currentIndex in range (0, len(leaguetable)):
        if leaguetable[currentIndex][0] == winningTeamName:
            leaguetable[currentIndex][1] += 1
        elif leaguetable[currentIndex][0] == losingTeamName:
            leaguetable[currentIndex][3] += 1
    return leaguetable

def leagueTable_WinDrawLoss_Function(filecontents, leaguetable):
    for currentrow in filecontents:
        winner = currentrow[5]
        if winner == "D":
            leaguetable = drawadder(currentrow, leaguetable)
        elif winner == "H":
            leaguetable = winAndLossAdder(currentrow[1], currentrow[2], leaguetable)
        elif winner == "A":
            leaguetable = winAndLossAdder(currentrow[2], currentrow[1], leaguetable)
    return leaguetable

def totalPointsCalculator(leaguetable):
    for currentIndex in range (0, len(leaguetable)):
        calculatedPoints = 0
        winPoints = (leaguetable[currentIndex][1]) * 3
        drawPoints = (leaguetable[currentIndex][2]) * 1
        calculatedPoints = winPoints + drawPoints
        leaguetable[currentIndex][5] = calculatedPoints
    return leaguetable



def leaguetablemaker(teamlist, filecontents):
    header = ['Team Name', 'Wins', 'Draws', 'Losses', 'Goal Difference', 'Total Points']
    leaguetable = []
    leaguetable.append(header)
    for currentitem in teamlist:
        leaguetable.append([currentitem,0,0,0,0,0])
    leaguetable_WLD = leagueTable_WinDrawLoss_Function(filecontents, leaguetable) #leaguetable_WLD is the leaguetable with the win, loss and draw data added
    leaguetable_withPoints = totalPointsCalculator(leaguetable_WLD)
    return leaguetable_withPoints



def run():
    filestate = check_file_exists(csv_file)
    if filestate == True:
        filecontents = read_csv(csv_file)
        teamlist = teamlistmaker(filecontents)
        leaguetable = leaguetablemaker(teamlist, filecontents)
        print (leaguetable)
    else:
        print ('File not found. Code terminating')


if __name__ == "__main__":
    run()