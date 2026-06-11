# Lambda function: , a lambda function is a small, anonymous function that is defined without a name and contains only a single expression. You use them for short-lived, quick operations where defining a full function using def is unnecessary.

# Ex: Here is a side-by-side comparison of a regular function vs lambda function.
# Regular Function
def square(x):
    return x * x

# Lambda function equivalent
square_lambda = lambda x: x * x
print(square(20))
print(square_lambda(10))

# 1.Custom Sorting with sorted(): You can use a lambda function to customize how a collection is sorted, such as sorting a list of tuples by their second element. 
# Ex:
pairs = [(1, 'One'), (3, 'Three'), (2, 'Two'), (4, 'Four')]
# Sort based on the second item in each tuple
sorted_pairs = sorted(pairs, key=lambda item: item[1])
print(sorted_pairs)

# 2. Transferming data with map():The map() function applies a transformation to every item in an iterable. 
# Ex:
numbers = [1, 2, 3, 4 , 5, 6]
doubled =list(map(lambda x: x * 2, numbers))
print(doubled)

# 3. filtering data with filter(): The filter() function extracts elements from an iterable based on whether a condition evaluates to True.
# Ex:
nums = [1, 2, 3, 4, 5, 6, 7, 8]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)

# 4. inline conditional logic (if-else): You can include an if-else statement inside a lambda function, provided it remains a single expression. 
check_age = lambda age: "Adult" if age >= 18 else "Minor"
print(check_age(21))