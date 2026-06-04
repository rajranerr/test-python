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

# Ex: 
s = [1, 2, 3, 4, 5, 6]
r = map(lambda x: x * 2, s)
print(list(r))