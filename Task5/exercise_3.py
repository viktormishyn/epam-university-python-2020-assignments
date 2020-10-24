# Create function MultArithmeticElements, which determines the multiplication of the first n elements of arithmetic
# progression of real numbers with a given initial element of progression a1 and progression step t.

def mult_arithmetic_elements(a: float, n: int, step: float):
    """
    :param a: initial value
    :param n: number of elements
    :param step: progression step
    :return: multiplication of the elements of arithmetic progression
    """
    mult = 1
    for i in range(n):
        mult *= a
        a += step
    return mult


if __name__ == '__main__':
    try:
        a = float(input('\nInitial real number: '))
        n = int(input('Number of elements: '))
        t = float(input('Progression step: '))
    except ValueError:
        print('Ivalid input. Try again..')
        exit()
    result = mult_arithmetic_elements(a, n, t)
    print(f'\nThe multiplication of the first {n} elements of arithmetic progression of real numbers with the initial'
          f' element of progression {a} and progression step of {t} is: \n{result: .2f}')
