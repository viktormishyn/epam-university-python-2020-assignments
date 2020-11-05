# Usage
```bash
exercise_1.py
exercise_2.py
exercise_3.py
exercise_4.py
exercise_5.py
```

# Tasks

### Task 1:  
Implement a function which receives a string and replaces all `"` symbols 
with `'` and vise versa.  

### Task 2:  
Write a function that check whether a string is a palindrome or not. To check 
your implementation you can use strings from here: 
[https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes](https://en.wikipedia.org/wiki/Palindrome#Famous_palindromes)  

### Task 3:    
Implement a function `get_shortest_word(s: str) -> str` which returns the 
shortest word in a given string. The word can contain any symbols except 
whitespaces (` `, `\n`, `\t` and so on). If there are multiple shortest words 
in the string with a same length return the word that occurs first. Usage of 
any split functions is forbidden.  
**Example:**  
```python
>>> get_shortest_word('Python is simple and effective!')
'is'
>>> get_shortest_word('Any pythonista like namespaces a lot, a? O')
'a'
```  

### Task 4:  
Implement a brunch of functions which receive a changeable number of strings 
and return next parameters:  
1) characters that appear in all strings;  
2) characters that appear in at least one string;  
3) characters that appear at least in two strings;  
4) characters of alphabet, that were not used in any string.  
  
Note: use `string.ascii_lowercase` for list of alphabet letters   
**Example:**  
```python
test_strings = ["hello", "world", "python"]
print(test_1_1(*test_strings))
>>> {'o'}
print(test_1_2(*test_strings))
>>> {'d', 'e', 'h', 'l', 'n', 'o', 'p', 'r', 't', 'w', 'y'}
print(test_1_3(*test_strings))
>>> {'h', 'l', 'o'}
print(test_1_4(*test_strings))
>>> {'a', 'b', 'c', 'f', 'g', 'i', 'j', 'k', 'm', 'q', 's', 'u', 'v', 'x', 'z'}
```  

### Task 5:  
Implement a function, that takes string as an argument and returns a 
dictionary, that contains letters of given string as keys and number of their 
occurrence as values.  
**Example:**  
```python
print(count_letters("stringsample"))
>>> {'s': 2, 't': 1, 'r': 1, 'i': 1, 'n': 1, 'g': 1, 
     'a': 1, 'm': 1, 'p': 1, 'l': 1, 'e': 1}
```

# Solutions

### task 1  
To solve this task I used third swap variable and `replace` method:  
```python
    def replace_quote(expr: str) -> str:
        single_quote = "'"
        double_quote = '"'
        swappp = 'swappp'
        expr = expr.replace(single_quote, swappp)
        expr = expr.replace(double_quote, single_quote)
        expr = expr.replace(swappp, double_quote)
        return expr
```  

### task 2
I use `remove_punctuation` function in order to create a string without non-whitespace characters.  
Then I check if the string equal to itself reversed.
```python
    def remove_punctuation(expr) -> str:
        return "".join(i.lower() for i in expr if i.isalpha())
    
    
    def is_palindrome(expr) -> bool:
        return remove_punctuation(expr) == remove_punctuation(expr)[::-1]
```  

### task 3  
I use regular expression '\S+' (which returns 1 or more non-whitespace characters) and `findall` method 
from `re` library to make a list of words.  
Then I use min function to find the minimal value, where the key is the length of words.
```python
    import re

    def get_shortest_word(s: str) -> str:
        lst = re.findall(r'\S+', s)
        return min(lst, key=lambda word: len(word))
```  

### task 4  
* In order to find characters that appear in all strings I use `set.intersection` method applied to all the arguments
```python
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
```  
  
* Characters that appear in at least one string can be found using `set.union` method applied to all the arguments  
```python
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
```  
  
* First I transformed all the strings into a list of sets.  
Then using `itertools.combinations` method I created an iterator which contains all posible pairs of given sets 
represented as tuples.  
Finally, I made a list of sets were each set is the intersection beween that pairs (combinations) of sets, and
applied `set.union` method to this list of sets.
```python
    import itertools

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
```  

* To find characters of alphabet that were not used in any string I use the `string.ascii_letters` sequence, 
iterating through it and checking if the letter appears in the set of all characters (`test_1_2` function).  
If the letter wasn't used it will be added to the final set as a lowercase alphabet ascii symbol.  

```python
    import string
    
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
```  

### task 5  
We are iterating through the characters, adding the letter as a key to the vocabulary with the count of 1 or 
incrementing the value if the letter exists in the dictionary as a key.  
If the character is not a letter `except KeyError` will continue iteration through the sequence of string characters.  

```python
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
```
