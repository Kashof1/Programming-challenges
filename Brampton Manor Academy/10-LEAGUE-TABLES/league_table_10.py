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

def windecider(row):
    if row[5] == "H":
        return row[1]
    elif row[5] == "A":
        return row[2]
    else:
        return 'Draw'

def drawadder(currentrow, leaguetable): # work in progress
    team_1 = currentrow[1]
    team_2  = currentrow[2]
    for leaguetablerow in leaguetable:
        if leaguetablerow[0] == team_1:
            leaguetablerow[1] += 1 
        elif leaguetablerow[0] == team_2:
            leaguetablerow[1] += 1



def leaguetablemaker(teamlist, filecontents):
    header = ['Team Name', 'Wins', 'Draws', 'Losses', 'Goal Difference', 'Total Points']
    leaguetable = []
    for currentitem in teamlist:
        leaguetable.append([currentitem,0,0,0,0,0])
    for currentrow in filecontents:
        winner = windecider(currentrow)
        if winner == "Draw":
            team_1 = currentrow[1]
            team_2  = currentrow[2]
            for leaguetablerow in leaguetable:
                if leaguetablerow[0] == team_1:
                    leaguetablerow[1] += 1 
                elif leaguetablerow[0] == team_2:
                    leaguetablerow[1] += 1



def run():
    filestate = check_file_exists(csv_file)
    if filestate == True:
        filecontents = read_csv(csv_file)
        teamlist = teamlistmaker(filecontents)
        print (teamlist)
    else:
        print ('File not found. Code terminating')


if __name__ == "__main__":
    run()