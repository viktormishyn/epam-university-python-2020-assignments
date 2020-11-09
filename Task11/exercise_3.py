# Implement a decorator call_once which runs a function or method once and caches the result.
# All consecutive calls to this function should return cached result no matter the arguments

initial_arguments = None


def call_once(original_function):
    def wrapper_function(*args):
        global initial_arguments
        if initial_arguments is None:
            initial_arguments = [*args]
        return original_function(*initial_arguments)
    return wrapper_function


@call_once
def sum_of_numbers(a, b):
    return a+b


if __name__ == '__main__':
    print('print(sum_of_numbers(13, 42))')
    print(sum_of_numbers(13, 42))

    print('print(sum_of_numbers(999, 100))')
    print(sum_of_numbers(999, 100))

    print('print(sum_of_numbers(134, 412))')
    print(sum_of_numbers(134, 412))
