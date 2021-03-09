import pandas

data = pandas.read_csv('nato.csv')

nato_dict = {frame.letter: frame.code for (index, frame) in data.iterrows()}

print([nato_dict[alphabet] for alphabet in input('Enter a Word:').upper() if alphabet.isalpha()])