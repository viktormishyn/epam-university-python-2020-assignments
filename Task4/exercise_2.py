# calculate the factorial for positive number n

# 1. using recursion. NOT RECOMMENDED!!!
# def fac(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fac(n-1)


# 2. using loops. RECOMMENDED!!!
def fac(n):
    f = 1
    for i in range(1, n+1):
        f *= i
    return f


if __name__ == '__main__':
    try:
        n = int(input('Enter the number: '))
    except ValueError:
        print('Invalid input. Try again..')
        exit()
    if n <= 0:
        print('The number should not be negative or zero. Try again..')
        exit()
    f = fac(n)
    print(f'The factorial of {n} is {f}')
