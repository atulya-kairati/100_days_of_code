# FileNotFoundError
# with open('hi.txt') as file:
#     print(file.read())

# KeyError:
# d = {'key': 'value'}
# print(d['key1'])

# IndexError:
# l = [1, 2]
# print(l[2])

d = {'key': 'value'}

try:  # warp around something which can blow up
    file = open('data.txt')
    print(d['key1'])

except FileNotFoundError as exp:  # will get triggered for this exception only
    print(exp)
    file = open('data.txt', 'w')
    file.write('Hey')

except KeyError as exp:
    print(f"This key doesn't exist: {exp}")

except Exception as exp:  # this will get executed if try block blows up (there was an exception) // not recommended
    print(f'Something went wrong {exp}')
else:  # executed if there was no problem
    print(file.read())

finally:  # Will always get Executed
    file.close()
    print('file closed')


print("The End :)")
