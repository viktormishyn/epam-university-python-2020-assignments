# Implement a function, that takes string as an argument and returns a
# dictionary, that contains letters of given string as keys and number of their
# occurrence as values.

def count_letters(s: str):
    """
    :param s: string
    :return: dictionary that contains letters of given string as keys and number of their occurence as values
    """
    dict = {}
    for char in s:
        try:
            if char not in dict and char.isalpha():
                dict[char] = 1
            else:
                dict[char] += 1
        except KeyError:
            continue
    return dict


if __name__ == '__main__':
    print(count_letters("stringsample"))

# **Example:**
# ```python
# print(count_letters("stringsample"))
# >>> {'s': 2, 't': 1, 'r': 1, 'i': 1, 'n': 1, 'g': 1,
#      'a': 1, 'm': 1, 'p': 1, 'l': 1, 'e': 1}
# ```
