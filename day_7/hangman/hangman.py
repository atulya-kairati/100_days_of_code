import art
import random

word = random.choice(art.words)
print(word)
placeholder = len(word) * '_'
lives = len(art.HANGMANPICS)

print(art.banner)


def check_and_give(letter):
    global placeholder
    if letter not in word:
        return None
    else:
        for i in range(len(word)):
            if letter == word[i]:
                placeholder = placeholder[:i] + letter + placeholder[i + 1:]
        return placeholder


while True:
    char = input('\n\nEnter a single alphabet: ')
    if len(char) != 1 or (not char.isalpha()):
        if char == '13':
            print(word)
        continue

    if not check_and_give(char):
        print(art.HANGMANPICS[-lives])
        lives -= 1
        print(f'Lives left: {lives}')

    if not lives:
        print('You got REKT!!!\n')
        print('The Answer is: ' + word)
        break

    if placeholder == word:
        print('\nBooyaahhh!!!')

    print(placeholder)
