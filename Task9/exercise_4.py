# Implement a brunch of functions which receive a changeable number of strings
# and return next parameters:
# 1) characters that appear in all strings;
# 2) characters that appear in at least one string;
# 3) characters that appear at least in two strings;
# 4) characters of alphabet, that were not used in any string.

import string
import itertools


def test_1_1(*args):
    """
    Characters that appear in all strings;
    :param args: list of strings
    :return: the intersection of the sets from the list of sets where each set consists of the
    characters from each string in the list of strings
    """
    list_of_sets = []
    for arg in args:
        s = set()
        for char in arg:
            s.add(char)
        list_of_sets.append(s)
    return set.intersection(*list_of_sets)


def test_1_2(*args):
    """
    Characters that appear in at least one string;
    :param args: list of strings
    :return: the union of the sets from the list of sets where each set consists of the
    characters from each string in the list of strings
    """
    list_of_sets = []
    for arg in args:
        s = set()
        for char in arg:
            s.add(char)
        list_of_sets.append(s)
    return set.union(*list_of_sets)


def test_1_3(*args):
    """
    Characters that appear at least in two strings;
    :param args: list of strings
    :return: a set that contains the characters which appear at least in two strings
    """
    list_of_sets = []
    for arg in args:
        s = set()
        for char in arg:
            s.add(char)
        list_of_sets.append(s)
    double_sets = itertools.combinations(list_of_sets, 2)
    # double_sets - this iterator object consists of tuples, each tuple contains two sets

    list_of_instersections = [set.intersection(*tpl) for tpl in double_sets]
    final_set = set.union(*list_of_instersections)
    return final_set


def test_1_4(*args):
    """
    Characters of alphabet, that were not used in any string;
    :param args: list of strings
    :return:
    """
    s = set()
    for char in string.ascii_letters:
        if char not in test_1_2(*args):
            s.add(char.lower())
    return s


if __name__ == '__main__':
    test_strings = ["hello", "world", "python"]
    print(f"Test strings: {test_strings}")
    print(f"1) characters that appear in all strings: {test_1_1(*test_strings)}")
    print(f"2) characters that appear in at least one string: {test_1_2(*test_strings)}")
    print(f"3) characters that appear at least in two strings: {test_1_3(*test_strings)}")
    print(f"4) characters of alphabet, that were not used in any string: {test_1_4(*test_strings)}")

# **Example:**
# ```python
# test_strings = ["hello", "world", "python"]
# print(test_1_1(*test_strings))
# >>> {'o'}
# print(test_1_2(*test_strings))
# >>> {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
# print(test_1_3(*test_strings))
# >>> {'h', 'l', 'o'}
# print(test_1_4(*test_strings))
# >>> {'a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'}
# ```
