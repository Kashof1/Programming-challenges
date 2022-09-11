def userinput():
    while True:
        input_rods = input('Enter the number of rods that you want to convert')
        try:
            input_rods = float(input_rods)
        except:
            pass
        else:
            if input_rods>=0:
                break
            else:
                print ('You must enter a number and it must be greater than 0. Please try again')
    print (f'Your input is {input_rods} rods \n')
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
    input_rods = userinput()
    meters = meterscalc(input_rods)
    furlong = furlongcalc(input_rods)
    miles = milescalc(meters)
    feet = feetcalc(meters)
    time = minutes_to_walkcalc(miles)

    print ('Conversions')
    print (f'Meters = {meters}')
    print (f'Feet = {feet}')
    print (f'Miles = {miles}')
    print (f'Furlongs = {furlong}')


run()