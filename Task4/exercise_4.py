# For a positive integer n calculate the result, which is equal to the sum of the '1' in the binary representation of n.

def bin_num(n) -> str:
    bin_str = ''
    while n > 0:
        bin_str += str(n%2)
        n //= 2
    return bin_str[::-1]


if __name__ == '__main__':
    try:
        n = int(input('Please, input a positive integer: '))
    except ValueError:
        print('Invalid input. Try again..')
        exit()
    if n <= 0:
        print('The number should not be negative or zero. Try again..')
        exit()
    binary_n = bin_num(n)
    sum_of_1 = str(binary_n).count('1')
    print('Number is ' + str(n) + ', binary representation is ' + binary_n + ', sum is ' + str(sum_of_1))
