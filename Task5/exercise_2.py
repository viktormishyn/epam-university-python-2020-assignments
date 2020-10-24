# Create function Transform, replacing the value of each element of an integer array with the sum of this element value
# and its index, only if the given array in the given order.

from exercise_1 import is_sorted

# Test cases:
# array = [4, 5, 7, 12, 45, 66]
# array = [2, 4, 1, 55, 32, 44]
# array = [44, 34, 21, 18, 4, 2, 1]
array = [15, 10, 3]
order = 'DESC'


def transform(array, order):
    if is_sorted(array, order):
        zipped_array = zip(range(len(array)), array)
        t_array = [i[0] + i[1] for i in zipped_array]
        return t_array
    else:
        return array


if __name__ == '__main__':
    result = transform(array, order)
    print(f'\nThe order {order}; The original array {array}')
    print(f'The transformed array {result}')
