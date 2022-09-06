#RICHTER CHALLENGE, IBRAHIM KASHIF
richtervalueslist = [1.0, 5.0, 9.1, 9.2, 9.5]

def richter_to_joule(richter):
    return 10**((1.5*richter)+4.8)

def joule_to_tnt(joule):
    return joule/(4.184*(10**9))

def preset_calculations():
    print (f'Richter            Joules          TNT')
    for count in (richtervalueslist):
        current_richter = count
        current_joule = richter_to_joule(current_richter)
        current_TNT = joule_to_tnt(current_joule)
        print (f'{current_richter}             {current_joule}             {current_TNT}')


def user_input():
    user_richter = float(input(f'Please enter a Richter scale value: '))
    user_joule = richter_to_joule(user_richter)
    user_tnt = joule_to_tnt(user_joule)
    print (f'Richter value: {user_richter}')
    print (f'Equivalence in joules: {user_joule}')
    print (f'Equivalence in tons of TNT: {user_tnt}')

def run():
    preset_calculations()
    user_input()

#run()
