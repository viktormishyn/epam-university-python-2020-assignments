# Write a function that check whether a string is a palindrome or not.

def remove_punctuation(expr) -> str:
    return "".join(i.lower() for i in expr if i.isalpha())


def is_palindrome(expr) -> bool:
    return remove_punctuation(expr) == remove_punctuation(expr)[::-1]


if __name__ == '__main__':
    palindrome = "Dammit, I'm Mad!"
    not_palindrome = "Dammit, I'm not Mad!"

    print(f'\nIs <{palindrome}> a palindrome?')
    print(f'The answer: {is_palindrome(palindrome)}')

    print(f'\nIs <{not_palindrome}> a palindrome?')
    print(f'The answer: {is_palindrome(not_palindrome)}')
