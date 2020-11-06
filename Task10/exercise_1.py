# Open file data/unsorted_names.txt. Sort the names and write them into a new file called sorted_names.txt
# Each name should start with a new line
import os


def sort_names(path: str) -> list:
    with open(path, 'r', encoding='utf-8') as f:
        lst = f.readlines()
        # list of lines with \n at the end of line
    return sorted(lst)


def write_names(from_: str, to_: str):
    with open(to_, 'w', encoding='utf-8') as f:
        f.writelines(sort_names(from_))
        # write the items of a list to the file (character by character, line breaks should be at the end of each item)


if __name__ == '__main__':
    from_ = 'data/unsorted_names.txt'
    to_ = 'data/sorted_names.txt'
    print('First 10 lines of the original file: ')
    with open(from_) as f:
        for i in range(10):
            print(f.readline().rstrip())
    print(f'\nWRITING {to_} FILE...')
    write_names(from_, to_)
    print('\nFirst 10 lines of new file: ')
    with open(to_) as f:
        for i in range(10):
            print(f.readline().rstrip())
