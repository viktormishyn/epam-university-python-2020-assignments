def validate_point(x: float, y: float) -> bool:
    return y >= abs(x) and y <= 1


if __name__ == '__main__':
    x = float(input('Enter x: '))
    y = float(input('Enter y: '))

    print('Is point in shadow area:', validate_point(x, y))



