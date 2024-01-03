# Foundations of Python - Part 3

**1. Nest list comprehensions**

Write a function `nested_prime()` to generate a list of prime numbers upto $n$ using only a nested list comprehension

**2. Reverse a string**

Write a function `old_school_reverse()` that reverses a string or number without using `.reverse()` or `[::-1]` slicing and returns any other value passed to the function as is.

```python
def old_school_reverse(n):
    return n
```

**3. Dictionary Comprehension with Conditional Logic**

Write a function `dict_a_noodle()` that ingests a dictionary and returns a dictionary such that `key: value` becomes the `value: key` if the key is a string and is unchanged if the key is anything other than a string.

```python
def dict_a_noodle(a):
    return a
```

**4. Fibonacci Squares**

Write a function `fib_squares()` that returns a list of numbers where each element is the number if the number is not a fibonacci number and the square of the number if the number is a fibonacci number for a given range of numbers.

```python
def fib_squares(a, b):
    return list(range(a, b+1))
```

```python
>>> fib_squares(2, 5):
[4, 9, 4, 25]
```

**5. Cataloging a list of lists**

Write a function `dict_of_lists()` that...
1. takes a deeply nested list of lists and flattens it out,
2. ignores any dict elements, and
3. returns a dictionary where the key is value and the value is the count of each item in the flattened list.

Use recursion to flatten the list.

```python
def dict_of_lists(data):
    return data
```

```python
>>> data = [[[1, 2, 3], [4, [5, 6]], 6, [7, 8, 9], [8, [8, 9, "a"], {5: 6}, ["b"], "ab"]], [5, 2, 1], 1]
>>> list_of_lists(data)
{1: 3, 2: 2, 3: 1, 4: 1, 5: 2, 6: 2, 7: 1, 8: 3, 9: 2, "a": 1, "b": 1, "ab": 1}
```

**6. Flattening a list of lists**

Write a function `list_of_lists()` that
1. takes a deeply nested list of lists and flattens it out,
2. ignores any dict elements, and
3. returns a sorted list of unique values of the combined list. 

Use recursion to flatten the list.

```python
def list_of_lists(data):
    return data
```

```python
>>> data = [[[1, 2, 3], [4, [5, 6]], 6, [7, 8, 9], [8, [8, 9, "a"], {5: 6}, ["b"], "ab"]], [5, 2, 1], 1]
>>> list_of_lists(data)
[1, 2, 3, 4, 5, 6, "a", "ab", "ab"]
```

