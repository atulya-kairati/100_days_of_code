# raise ValueError('I made up this Error LOL')

accn = float(input('Input acceleration: '))
mass = float(input('Input Mass: '))

if mass < 0:
    raise ValueError('Mass Cannot be -ve')

force = mass * accn

print(f'Force Applied was: {force} Newtons')

# add exception handling in password manager
