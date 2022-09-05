def input():
    input_rods = float(input('Input rods:'))
    print (f'Your input is {input_rods} rods')
    print('')
    return input_rods

def meterscalc(rods):
    return rods * 5.0292

def furlongcalc(rods):
    return rods/40

def milescalc(meters):
    return meters/1609.34

def feetcalc(meters):
    return meters/0.3048

def minutes_to_walkcalc(miles):
    avg_walking_speed = 3.1/60
    return miles/avg_walking_speed

def run():
    input_rods = input()
    meters = meterscalc(input_rods)
    furlong = furlong(input_rods)
    miles = miles(meters)
    feet = feet(meters)
    time = minutes_to_walk(miles)

    print ('Conversions')
    print (f'Meters = {meters}')
    print (f'Feet = {feet}')
    print (f'Miles = {miles}')
    print (f'Furlongs = {furlong}')

