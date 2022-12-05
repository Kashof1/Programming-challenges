import json
def fibonacci_generator(end):
    array = [1,2]
    for current in range (2, end):
        array.append((array[current-1] + array[current-2]))
    return array

def writetofile(fibarray):
    with open ('fibs.json', 'w') as fibs:
        json.dump(fibarray, fibs)

def openfile():
    with open ('fibs.json', 'r') as fibs:
        final = json.load(fibs)
    return final


def largest(n, fibs):
    current = fibs[0]
    while n > fibs[current]:
        current+=1
    return fibs[current-1]

def zeckendorf(number, fibs):
    finarray = []
    while number >= 1:
        largestn = largest(number, fibs)
        number = number - largestn
        finarray.append(largestn)
    print (finarray)

fibs = openfile()
zeckendorf(4, fibs)