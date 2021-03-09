import pandas


new_data = {'Fur color': ['Gray', 'Cinnamon', 'Black'], 'count': []}
data = pandas.read_csv('squirrel_data.csv')

print(len(data))

new_data['count'].append(len(data[data['Primary Fur Color'] == 'Gray']))
new_data['count'].append(len(data[data['Primary Fur Color'] == 'Cinnamon']))
new_data['count'].append(len(data[data['Primary Fur Color'] == 'Black']))

print(new_data)

fur_data = pandas.DataFrame(new_data)
print(fur_data)
# fur_data.to_csv('new_data.csv')

