# Create function SumGeometricElements, determining the sum of the first elements of a decreasing geometric progression
# of real numbers with a given initial element of progression a1 and progression step t

def sum_geometric_elements(a: float, alim: float, step: float):
    """
    :param a: initial value
    :param alim: limit value of the progression (element of the progression can't be less then this value)
    :param step: progression step; 0<step<1
    :return: sum of the elements of geometric progression
    """
    sum = 0
    while a > alim:
        sum += a
        a *= step
    return sum


if __name__ == '__main__':
    try:
        a = float(input('\nInitial real number: '))
        alim = float(input('Limit value of the progression: '))
        t = float(input('Progression step (float number between 0 and 1): '))
    except ValueError:
        print('Ivalid input. Try again..')
        exit()
    if not 0 < t < 1:
        print('Progression step should be a float number between 0 and 1. Try again..')
        exit()
    result = sum_geometric_elements(a, alim, t)
    print(f'\nThe sum of the geometric progression of real numbers with the initial'
          f' element of progression {a}, limit value of {alim} and progression step of {t} is: \n{result: .2f}')
