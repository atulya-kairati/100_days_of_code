import random

cards = list('AKQJ123456789')


def score(deck):
    return sum([10 if card.isalpha() else int(card) for card in deck])


def play():
    comp_cards = [random.choice(cards) for _ in range(2)]
    player_cards = [random.choice(cards) for _ in range(2)]

    print(f'One of the computer\'s card is: {comp_cards[0]}')
    print(f'Your cards are: {", ".join(player_cards)}')

    choice = input('Enter Y/y to pull a new card else Press N/n: ')
    if choice.lower() == 'y':
        player_cards.append(random.choice(cards))

    print(f'Your card: {" ".join(player_cards)}\nComputers cards: {" ".join(comp_cards)}')

    if 21 - score(comp_cards) > 21 - score(player_cards) > -1:
        print('BOOYAAHHH!!!')
    else:
        print("Get REKT!!!")


def main():
    while True:
        play()
        if input('Enter Y/y to Continue else Press N/n: ').lower() == 'n':
            print('Byeeeee!')
            break


if __name__ == '__main__':
    main()
