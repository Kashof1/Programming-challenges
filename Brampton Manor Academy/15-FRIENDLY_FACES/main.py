from operator import index
from pathlib import Path
import csv

#IMPORTANT NOTICE:
#the program definitely works, however the 3rd and 5th link were faulty (at least on my device)
#when I opened the 3rd link directly to see the image, i got a blank image back. 
#when i opened the 5th link directly, I was blocked from accessing the site as the connection was not private
#in order to make sure that the code does truly work, I would recommend swapping out the image links in the csv file for some other images

def read_csv(csv_path):
    csv_contents = []
    with open(csv_path) as csvfile:
        reader = csv.reader(csvfile, delimiter=",")
        for row in reader:
            csv_contents.append(row)
    return csv_contents

def read_html(path):
    with open (path, 'r') as file:
        htmlFile = file.read()
        return htmlFile

def process(csv, html):
    indexNameList = [[0,'link'], [1, 'initials'], [2, 'name']]
    for currentItem in indexNameList:
        for x in range (5):
            Name = currentItem[1] + str(x+1)
            html = html.replace (Name, csv[x][currentItem[0]])
    return html

def write_html(path, html):
    with open (path, 'w') as htmlfile:
        htmlfile.write(html)

if __name__ == "__main__":   
    csv = read_csv(csv_path='south.csv')
    html = read_html(path='south.html')
    html = process(csv, html)
    write_html(path="south_final.html", html=html)


