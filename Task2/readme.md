# Task

### Exercise 1

Return the count of negative numbers in next list [4, -9, 8, -11, 8]. Do not use conditionals or loops.

### Exercise 2

You have first 5 best tennis players according APT rankings. 
Set the first-place player to last place and vice versa.
```python
players = ['Ashleigh Barty', 'Simona Halep', 'Naomi Osaka','Karolina Pliskova', 'Elina Svitolina']
```

### Exercise 3

Swap words "reasonable" and "unreasonable" in quote "The reasonable man adapts himself to the world; 
the unreasonable one persists in trying to adapt the world to himself". 
Do not use <string>.replace() function or similar.

# Task Execution

### Exercise 1

My count_negatives function through filter function and lambda expression creates another list with only negative numbers
and then returns the length of this list.

### Exerise 2

In change_position function I simply swap values using the tuple unpacking style.

### Exercise 3

First I splited the quote with split() function.
Then I found the indices of these two words in the list and reassigned values.
Finally, with join() function I joined this modified list into a string.

# Usage

```bash
exercise_1.py
exercise_2.py
exercise_3.py
```
