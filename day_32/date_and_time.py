import datetime as dt

print(f'Current Time: {dt.datetime.now()}')
print(f'Current Year: {dt.datetime.now().year}')
print(f'Current Month: {dt.datetime.now().month}')
print(f'Current weekday: {dt.datetime.now().weekday()}')

my_bday = dt.datetime(year=1999, month=7, day=8)
print(my_bday)