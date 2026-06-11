# 'is' vs '==': The core difference is that == checks for value equality (whether two objects contain the same data), while is checks for object identity (whether two variables point to the exact same object in memory). 

# Example 1: Working with List
a = [1, 2, 3, 4, 5]
b = [1, 2, 3, 4, 5]
c = a
print(a == b)
print(a is b)
print(a is c)

# Ex 2: The Integer Caching Trap

#  Variable within the cached range (-5 to 256)
x = 200
y = 200
print(x == y)
print(x is y)

# Variables outside the cached range
x = 600
y = 600
print(x == y)
print(x is y)

# == operator(equality operator):
# Ex:
x = [2, 3, 4, 6]
y = [2, 3, 4, 6]
z = x 
if x == y:
    print("x and y have the same values")
else:
    print("x and y do not have the same values")

# is operator (identity operator):
# Ex:
x = [2, 3, 4, 6]
y = [2, 3, 4, 6]
z = x 
# case 1: x and y
if x is y:
    print("x and y are the same object")
else:
    print("x and y are not the same object")
# case 2: x and z
if x is z:
    print("x and z are the same object")
else:
    print("x and z are not the same object")