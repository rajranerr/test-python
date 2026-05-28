# type casting in python: Type casting is the mathode to convert the python variable datatype into a certain data type
#                      in order to perform the required operation by users. In this article, we will see the various
#             techniques for typecasting. There can be two types of Type Casting in Python:
#               
# 1. python implicit type conversion
# 2. python explicit type conversion 

# 1. implicit type conversion: mplicit type conversion occurs when Python automatically converts one data type
#                   to another during an operation to ensure correct and safe evaluation, without
#                 requiring any action from the user.

# ex:
# python automatically converts 'a' to int 
a = 6
print(type(a))

# python automatically converts 'b' to float
b = 4.0
print(type(b))

# pyhton automatically converts 'c' to float as it is a float addition
c = a + b
print(c)
print(type(c))

# Python automatically converts 'd' to float as it is a float multiplication
d = a * b
print(d)
print(type(d))

# Explicit type conversion: Explicit type conversion is when the programmer manually changes a value’s data
#                      type using built-in type casting functions, usually when automatic conversion is
#                  not possible or a specific type is needed.

# Example of Type casting in python:

# Commonly used type casting functions in Python are:

#  Int(): Python Int() function take float or string as an argument and returns int type object.

#  float(): Python float() function take int or string as an argument and return float type object.

#  str(): Python str() function takes float or int as an argument and returns string type object.

# Python convert int to Float

# Converting int to float in python with float() function.

a = 4
n = float(a)

print(n)
print(type(n))

# python convert float to int

# Converting Float to int datatype in python with int() function.

a = 6.8
n = int(n)

print(n)
print(type(n))

# Converting int to String datatype in Python with str() function.

a = 6

# typecast to str
n = str(a)

print(n)
print(type(n))

# Python convert string to int 

a = 6
b = '8'

# explicit conversion of string to int
n = a + int(b)
print(n)
print(type(n))