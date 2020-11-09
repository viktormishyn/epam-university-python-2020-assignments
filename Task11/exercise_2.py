# Implement a decorator remember_result which remembers last result of function and prints it before next call

result = None


def remember_result(original_function):
    def wrapper_function(*args):
        global result
        print(f"Last result = '{result}'")
        result = original_function(*args)
        print(f"Current result = '{result}'")
        return original_function(*args)
    return wrapper_function


@remember_result
def sum_list(*args):
    result = ""
    for item in args:
        result += str(item)
    return result


if __name__ == '__main__':
    lst = ['a', 'b']
    print('\nsum_list("a", "b")')
    sum_list(*lst)

    lst = ['abc', 'cde']
    print('\nsum_list("abc", "cde")')
    sum_list(*lst)

    lst = [3, 4, 5]
    print('\nsum_list(3, 4, 5)')
    sum_list(*lst)
