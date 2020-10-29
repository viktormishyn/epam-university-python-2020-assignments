# Implement a function, that receives changeable number of dictionaries (keys - letters, values - numbers)
# and combines them into one dictionary.

def combine_dicts(*args) -> dict:
    combined_dict = {}
    for arg in args:
        for k, v in arg.items():
            combined_dict.setdefault(k, 0)
            combined_dict[k] += v
    return combined_dict


if __name__ == '__main__':
    dict1 = {'a': 100, 'b': 200}
    dict2 = {'a': 200, 'c': 300}
    dict3 = {'a': 300, 'd': 100}
    combined_dict = combine_dicts(dict1, dict2, dict3)
    print(f'\nDictionaries given:\n{dict1}\n{dict2}\n{dict3}\n')
    print(f'Result: {combined_dict}')
