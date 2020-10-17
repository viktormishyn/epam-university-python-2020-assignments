lst = [4, -9, 8, -11, 8]

# return the count of negative numbers. Do not use conditionals or loops


def count_negatives(numbers: list) -> int:
    only_negatives = list(filter(lambda x: x < 0, numbers))
    count = len(only_negatives)
    return count


if __name__ == '__main__':
    print(f'There are {count_negatives(lst)} negative numbers in list {lst}')
