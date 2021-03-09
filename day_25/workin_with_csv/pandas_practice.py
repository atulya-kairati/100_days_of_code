import pandas

data = pandas.read_csv('weather_data.csv')

print(data)  # a dataframe

print(data.condition)  # a series

# attributes of a series
print(f'Avg. temperature: {data.temp.mean()}')
print(f'Max temperature: {data["temp"].max()}')

# Accessing a row
print(data[data.condition == 'rainy'])
print(data[data.temp == data.temp.max()])

# Create dataframe from sratch

names = {
    'name': ['hanumaan', 'Shankar', 'Ram'],
    'nickname': ['Bajrangbali', 'Mahadev', 'Ramu']
}

namet = pandas.DataFrame(names)
print(namet)
namet.to_csv('names.csv')
