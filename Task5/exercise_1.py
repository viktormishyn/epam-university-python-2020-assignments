# Create function IsSorted, determining whether a given array of integer values is sorted in a given order

# Test cases:
# array = [4, 5, 7, 12, 45, 66]
# array = [2, 4, 1, 55, 32, 44]
# array = [44, 34, 21, 18, 4, 2, 1]
array = [128, 54, 39, 3, -33, -178, -224]


def is_sorted(array, order) -> bool:
    array = array
    itr = iter(array)

    next(itr)
    try:
        for num in array:
            if num <= next(itr) and order == 'ASC':
                continue
            elif num >= next(itr) and order == 'DESC':
                continue
            else:
                return False
    except StopIteration:
        return True


def check(array):
    if is_sorted(array, 'ASC'):
        print(f'The array {array} is sorted in ascending order')
    elif is_sorted(array, 'DESC'):
        print(f'The array {array} is sorted in descending order')
    else:
        print(f'The array {array} is unsorted')


if __name__ == '__main__':
    check(array)
