# Implement a function `get_shortest_word(s: str) -> str` which returns the
# shortest word in a given string. The word can contain any symbols except
# whitespaces (` `, `\n`, `\t` and so on). If there are multiple shortest words
# in the string with a same length return the word that occurs first. Usage of
# any split functions is forbidden.

import re


def get_shortest_word(s: str) -> str:
    lst = re.findall(r'\S+', s)
    return min(lst, key=lambda word: len(word))


if __name__ == '__main__':
    expr = '\tExample. The re.findall method is the most important part of this solution.\n ' \
           'It does not simply find a match. It finds all matches within a string.\n'
    shortest_word = get_shortest_word(expr)
    print(f'Original expression:\n {expr}')
    print(f'Shortest word: {shortest_word}')
