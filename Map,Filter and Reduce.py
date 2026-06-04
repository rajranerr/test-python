# Map(),Filter(),and Reduce(): map(),filter(),and reduce() are higher-order function in python used to process and transform data collection without explicit loops. While map() transforms each item and filter() extracts items matching a condition, reduce() aggregates all items into a single final value.

# map(): The map() function executes a specified function for each item in an iterable sequence.

# Syntax: map(function, iterable)
# Example 1: Squaring a list of numbers.

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

# Using a lambda function to square each item
squared = map(lambda x: x ** 2, numbers)

print(list(squared))

# Ex 2: Built-in function

cities = [" India ", " Paris ", " New York " " Tokyo "]

# pass the built-in str.strip function
clean_cities = list(map(str.strip, cities))

print(clean_cities)

# Ex 3: Multiple Iterables:
a = [2, 4, 6, 8]
b = [10, 20, 30, 40]

# Add element from a and b positionally
sums = map(lambda x, y: x + y, a, b)
print(list(sums))

# Ex 4: 
s = [1, 2, 3, 4, 5, 6]
r = map(lambda x: x * 2, s)
print(list(r))

# Ex 5:
text = [" my name is raj rane"]
upper_text = map(str.upper, text)
print(list(upper_text))

# fiter(): The filter() function evaluates each element in an iterable against a condition (a function that returs True or False) and keeps only the item that pass.
# Syntax: finter(function, iterable)
# Ex 1:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# Extract only the even numbers
evens = filter(lambda x: x % 2 == 0, numbers)
print(list(evens))
b = filter(lambda x: x % 3 == 0, numbers)
print(list(b))

# Ex 2:
ages = [12, 14, 15, 17, 18, 19, 20, 21, 22, 24, 25, 26]
#  Filter out element under 18 using a shorthand lambda expression
adults = filter(lambda age: age >= 18, ages)
print(list(adults))
minor = filter(lambda age: age <= 17, ages)
print(list(minor))

# Ex 3:
mixed_data = ["apple", "", False, "banana", 0, None, "cherry", "orange"]
# Removes all empty/falsy items
clean_data = filter(None, mixed_data)
print(list(clean_data))

# reduce(): The reduce() function applies a binary function cumulatively to elements from left to right, reducing the entire collection to a single terminal value. 
# Syntex: reduce(function, iterable[, initializer])
# Ex 1:
from functools import reduce
numbers = [1, 2, 3, 4, 5, 6]
# Compute the product of all elements (1 * 2 * 3 * 4 * 5 * 6)
product = reduce(lambda x, y: x * y, numbers)
print(product)

# Ex 2: Finding the Maximum Value in a List
from functools import reduce
numbers = [5, 12, 3, 16, 21, 8, 9, 18, 36, 54]
# Track and return the higher number at each step
max_value = reduce(lambda x, y: x if x > y else y, numbers)
print(max_value)

# Ex 3: Using the initializer parameter

from functools import reduce
numbers = [2, 4, 5, 6, 8, 10]
# Starts at 100, then adds 2, 4, 5, 6, 8, and 10
total = reduce(lambda x,y: x + y, numbers, 100)
print(total)

# Example: Combining All Three 
from functools import reduce
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# Pipline: filter even-> square them -> sum them up
result = reduce(lambda x, y: x + y, map(lambda x: x**2, filter(lambda x: x % 2 == 0, numbers)))
print(result)