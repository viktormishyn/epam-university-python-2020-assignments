def check_number(i):
    if not 0 < i < 100:
        return 'The number should be from 1 to 100\n'
    if i % 3 == 0 and i % 5 == 0:
        return 'FizzBuzz\n'
    elif i % 3 == 0:
        return 'Fizz\n'
    elif i % 5 == 0:
        return 'Buzz\n'
    else:
        return f'{i}\n'


if __name__ == '__main__':
    while True:
        i = input("Enter the number from 1 to 100 ('q' for Quit): ")
        if i == 'q':
            break
        try:
            i = int(i)
        except ValueError:
            print('Input is not valid. Should be an integer number')
        print(check_number(i))
