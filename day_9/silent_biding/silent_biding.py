import art
import os


def bid():
    data = {}
    while True:
        name = input('Input your name: ')
        price = int(input('Enter your bidding price: $'))
        data[name] = price
        os.system('cls' if os.name == 'nt' else 'clear')
        choice = input('Enter "end" to end the bidding and "bid" to bid: ')
        if choice == 'end':
            return data


def decide(data):
    max_bid = max(data.values())
    print(max_bid)
    max_bider = dict(filter(lambda element: element[1] == max_bid, data.items()))
    return max_bider


def main():
    data = bid()
    winners = decide(data)
    if len(winners) != 1:
        print('There is a TIE between')
        for name in winners.keys():
            print(name)
    else:
        print('fWinner is {list(winners.keys())[0]}')


if __name__ == '__main__':
    main()
