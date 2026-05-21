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

def fun( x ):
    if (x % 2 == 0):
        print("enen")
    else:
        print("odd")

fun(int(input("Enter any number: "))) # function calling


# Parameterized functions:
# EX:

def fun(name):
    print("hello", name)

fun(str(input("Enter name: ")))

# Function with default argument
# Ex:

def fun(x, y=70):
    print("x:",x)
    print("y:",y)

fun(int(input("Enter number: ")))
    
#  Keyword argument functions:
# Ex:
def fun(name, age):
    print(name, "is", age, "year old.")

fun(age=18,name="kulalux")

#  User-Defined functions Example:

# We define our oen function to greet a user

def greet_user(username):
    return f"Hello, {username} wellcome back."

# we call our custume function
message = greet_user("kulalux")

print(message) # output:









     