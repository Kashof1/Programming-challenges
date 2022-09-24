from calendar import c
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
    for currentIndex in range (1, len(leaguetable)):
        calculatedPoints = 0
        winPoints = (leaguetable[currentIndex][1]) * 3
        drawPoints = (leaguetable[currentIndex][2]) * 1
        calculatedPoints = winPoints + drawPoints
        leaguetable[currentIndex][5] = calculatedPoints
    return leaguetable

def goal_difference_calculator(teamlist, leaguetable):  #INVESTIGATE PERSISTENT ERRORS IN THE COMPARISON OF TEAM NAMES
    goalstable = [] #team name, goals scored, goals conceded, difference
    for currentTeam in teamlist:
        goalstable.append([currentTeam,0,0,0])
    with open(csv_file) as table:
        reader = csv.reader(table, delimiter=",")
        for tablerow in reader:
            for currentrow in goalstable:
                if currentrow[0] == tablerow[1]:
                    currentrow[1] += int(tablerow[3])
                    currentrow[2] += int(tablerow[4])

                elif currentrow[0] == tablerow[2]:
                    currentrow[1] += int(tablerow[4])
                    currentrow[2] += int(tablerow[3])

        for currentrow in goalstable:
            currentrow[3] =int(currentrow[1]) - int(currentrow[2])
            for leaguetablerow in leaguetable:
                if leaguetablerow[0] == currentrow[0]:
                    leaguetablerow[4] = currentrow[3]

    return leaguetable
    
def league_table_sort(leaguetable):
    countingnumber = 0
    while countingnumber < len(leaguetable):
        for x in range (6):
            if type(leaguetable[countingnumber][x]) is str:
                if leaguetable[countingnumber][x].isnumeric():
                    leaguetable[countingnumber][x] = int(leaguetable[countingnumber][x])
        countingnumber+=1
    
    leaguetable.sort(key=lambda x:x[5], reverse=True)
    for currentindex in range (1, len(leaguetable)-1):
        if currentindex!= (len(leaguetable)-1):
            if leaguetable[currentindex][5] == leaguetable[currentindex+1][5]:
                if leaguetable[currentindex][4] < leaguetable[currentindex+1][4]:
                    leaguetable[currentindex],leaguetable[currentindex+1] = leaguetable[currentindex+1], leaguetable[currentindex]
    return leaguetable

def league_table_print(leaguetable):
    # header = ['Team Name', 'Wins', 'Draws', 'Losses', 'Goal Difference', 'Total Points']
    print(f"{'Team':26}{'Wins':10}{'Draws':10}{'Losses':10}{'Goal Difference':20}{'Total Points':20}")
    print('****************************************************************************************')
    for currentrow in leaguetable:
        print (f'{currentrow[0]:20}{currentrow[1]:10}{currentrow[2]:10}{currentrow[3]:10}{currentrow[4]:^20}{currentrow[5]:>10}')

def leaguetablemaker(teamlist, filecontents):
    leaguetable = []
    for currentitem in teamlist:
        leaguetable.append([currentitem,0,0,0,0,0])
    leaguetable_WLD = leagueTable_WinDrawLoss_Function(filecontents, leaguetable) #leaguetable_WLD is the leaguetable with the win, loss and draw data added
    leaguetable_withPoints = totalPointsCalculator(leaguetable_WLD)
    leaguetable_withGoalDiff = goal_difference_calculator(teamlist, leaguetable_withPoints)
    sortedLeagueTable = league_table_sort(leaguetable_withGoalDiff)
    return sortedLeagueTable


def run():
    filestate = check_file_exists(csv_file)
    if filestate == True:
        filecontents = read_csv(csv_file)
        teamlist = teamlistmaker(filecontents)
        leaguetable = leaguetablemaker(teamlist, filecontents)
        league_table_print(leaguetable)
    else:
        print ('File not found. Code terminating')


if __name__ == "__main__":
    run()