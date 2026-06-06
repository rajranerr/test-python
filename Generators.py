# Generator: Generator is a special type of function that returns an iterator object, allowing you to produce a sequence of values over time on demand (lazily) instead of computing them all at once and saving them in memory. Unlike standard functions that use return to terminate and hand back a single value, generators use the yield keyword to temporarily pause execution, save their current state, and emit a value.

# Example:
def function(max):
    cnt = 1
    while cnt <= max:
        yield cnt
        cnt += 1

ctr = function(10)
for n in ctr:
    print(n)

# Creating a Generator
# Ex:
def function():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5
    yield 6

for val in function():
    print(val)

# Ex:
# Yield vs Return
# Ex:
def function():
    return 10 + 28 + 42
res = function()
print(res)

# Generator expression

# Ex:
sq = (x*x for x in range(1, 8))
for i in sq:
    print(i)