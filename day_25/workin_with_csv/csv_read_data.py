import csv

with open('weather_data.csv') as file:
    data = csv.reader(file)
    for row in data:
        print(row[1])
