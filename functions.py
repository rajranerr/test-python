# Functions: functions are self-contained blocks of code designed to perfom specific tast,
#          allowing you to write cleaner, reusable, and more efficient code. 
#         They help organize large programs into smaller, manageable sections by following the "DRY" (Don't Repeat Yourself) principle.

#   functions are defined using the def keyword, followed by a name and parentheses.

#  Definition:The syntex includes def function_name(): followed by an indented block of code.
#  Execution: A function only runs when it is "called" or "invoked" by writing its name 
#           followed by parentheses: function_name() .

# Type of Functions:

# 1. Built-in functions:  Pre-defined functions like print(), len(), and input().
# 2. User-Defined Functions: Functions created by developers to perform custom tasks specific to their programs.

# Argument Types:

#  Python supports several ways to pass data to functions:

#  Positional Arguments: Assigned based on their order in the call.

#  Keyword Arguments: Passed using the parameter name (e.g., name="Alice"), allowing any order.

#  Default Arguments: Pre-set values used if no argument is provided during the call.

#  Arbitrary Arguments: Used when you don't know how many arguments will be passed, typically denoted by *args or **kwargs.

# Ex:
def my_function():
    print("My fevorite bike is interseptor 650 \n colour: black")

my_function()

# Ex:

def get_greeting():
    return "Hello i am raj"

message = get_greeting()
print(message)

# Ex:
def my_function():
    print("Hello i am raj")

my_function()

# Examples:

#  functions ex:

def number( x ):
    if (x % 2 == 0):
        print("enen")
    else:
        print("odd")

number(6) # function calling

# Types of Function Arguments


#  default argument: Default argument use a predefined value when no value is passed during the function call.

# Ex:

def my_function(x, y=70):
    print("x:",x)
    print("y:",y)

my_function(40)
    
#  Keyword argument : pass valyes using parameter names, so argument order does not matter'

# Ex:
def myfunction(name, age):
    print(name, "is", age, "year old.")

myfunction(age=18,name="kulalux")

# Positional Arguments: Value are assigned to parameters based on their order in the function call.

# Ex: 

def nameAge(name, age):
    print("Hi, I am", name)
    print("My age is", age)

print("Case-1:")
nameAge("stark",21)

print("Case-2")
nameAge(21, "stark")

# Arbitrary Arguments: allow functions to accept multiple values. This is done using two special symbols:
# *args collects extra positional arguments aa a tuple.
# **kwargs collects extra keyword arguments as a dictionary.
# Ex:
def my_function(*args, **kwargs):
    print("Non-Keyword Arguments (*args):")
    for arg in args:
        print(arg)

    print("Keyword Arguments (**kaargs):")
    for key, value in kwargs.items():
        print(f"{key} == {value}")
my_function('Hey', 'Welcome', first='geeks', mid='for', last='geeks')

# Functions within Functions

# A function defined inside another function is called an inner function (or nested function).
#  It is used to organize related logic and access variables from the outer function. 
# Ex:
def f1():
    s = 'I love kulaluxfornature' 
    def f2():
        print(s)
    f2()
f1()

# Return Statement: Return is used to end a function and send a value back to the caller.
#  It can return any data type. multiple values (packed into tuple), or None if no value is given.

# Syntax
#        return(expression)

#  Parameters: expression is the value returned by the function. If no value is retuned, it returns None by default.
def sq_value(num):
    return num**2
print(sq_value(2))
print(sq_value(-4))

# Pass by Reference and Pass by Value: Variables refer to objects. function behavior depends on whether the object is mutable or immutable.

# Mutable objects like list can be modified inside functions.
# Immutable objects like integers and strings remain unchanged.

def myfunction(x):
    x[0] = 20

b = [10, 11, 12, 13, 14]
myfunction(b)
print(b)

def myfunction2(x):
    x = 20

a = 10
myfunction2(a)
print(a)

#  User-Defined functions Example:
# We define our own function to greet a user

def greet_user(username):
    return f"Hello, {username} wellcome back."

# we call our custume function
message = greet_user("kulalux")

print(message) # output:

# 1. Simple Function (No Arguments)
    #  A basic function that perform a single action without requiring any input.
# Ex:
def greet():
    print("Hello! Welcomee to python.")

# calling the function
greet()
  
# 2. Function with parameters and Return value
    # This function taken numbers, adds them, and returns the result for furthr use.
# Ex:
def add_numbers(a,b):
    sum_result = a + b
    return sum_result

# Using the returned value
result = add_numbers(20, 8)
print(f"The sum is: {result}")

# Function with Default Arguments
 # You can provide default values for parameters. if value isn't provided during the call, the default is used.
# Ex:
def describe_pet(name, animal_type="dog"):
    print(f"I have a {animal_type} named {name}.")

describe_pet("moti")              # User default "dog"
describe_pet("whiskers", "cat")   # Overrides with "cat"

# 4. Function with keyword Arguments
    # Arguments can be passed by name, allowing you to ignor the order of parameters.
# Ex:
def student_info(name, age):
    print(f"student: {name}, age: {age}")
        
# Order doesn't matter when keyword are used 
student_info(age=17, name="Aline")  

# Example of a user- defined function

# Program to illustrate
# the use of user-defined functions

def add_numbers(x,y):
   sum = x + y
   return sum

num1 = 5
num2 = 6

print("The sum is", add_numbers(num1, num2))

# Ex:
def cube_volume(side_length):
    volume = side_length ** 3
    return volume
# Use the function 
result = cube_volume(3)
print(f"The volume of the cube is: {result}")