values = {'2': 2, '3': 3, '4': 4,
          '5': 5, '6': 6, '7': 7,
          '8': 8, '9': 9, '10': 0,
          'J': 0, 'Q': 0, 'K': 0, 'A': 1}


def play(c1, c2):
    if c1.lower() == 'joker':
        return 'Do not cheat!'
    total = values[c1] + values[c2]
    if total > 9:
        total -= 10
    return total


if __name__ == '__main__':
    c1 = input('Play first card: ')
    c2 = input('Play second card: ')
    if c1 not in values or c2 not in values:
        print('Input invalid. Please try again!')
        exit()
    result = play(c1, c2)
    print(f'Your result: {result}')
