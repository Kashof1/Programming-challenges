from pathlib import Path
import csv
import codecs

csvPath = Path('south.csv')
htmlPath = Path('south.html')

def check_file_exists(file):
    return file.is_file()

def read_csv(csv_path):
    csv_contents = []
    if check_file_exists(csv_path):
        with open(csv_path) as csvfile:
            reader = csv.reader(csvfile, delimiter=",")
            for row in reader:
                csv_contents.append(row)
    return csv_contents

def read_html(path):
    if check_file_exists(path):
        with open (path, 'r') as file:
            htmlFile = file.read()
            return htmlFile

def link_replace(csv, html):
    currentStringIndex = 0
    for x in range (5):
        linkName = 'link' + str(x+1)
        print (linkName)
        print(x)
        print (csv[x][0])
        html.replace (linkName, csv[x][0])
    
    return html


def process(csv, html):
    linked_html = link_replace(csv, html)
    return linked_html

def write_html():
    pass

if __name__ == "__main__":
    csv = read_csv(csv_path=csvPath)
    html = read_html(path=htmlPath)
    html = process(csv, html)
    print (html)
    #html = process(csv=csv, html=html)
    #write_html(path="south_final.html", html=html)