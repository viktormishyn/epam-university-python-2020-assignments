# For a positive integer n calculate the result value which is equal to the sum of the first n Fibonacci numbers

def fib_sequence(n) -> list:
    lst = [1]
    fib_num = 1
    for i in range(n-1):
        lst.append(fib_num)
        fib_num += lst[-2]
    return lst


if __name__ == '__main__':
    try:
        n = int(input('Please, input the length of sequence: '))
    except ValueError:
        print('Invalid input. Try again..')
        exit()
    if n <= 0:
        print('The number should not be negative or zero. Try again..')
        exit()
    fib_list = fib_sequence(n)
    print(f'Fibonacci sequence is {fib_list}')
    print(f'Sum of elements in Fibonacci sequence is {sum(fib_list)}')
