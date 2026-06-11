# local and global: Local variables are defined inside a function and can only be accessed within that specific function, while global variables are defined outside of all functions and are accessible throughout the entire program.

# global variable: Declared outside of all functions. Exists until the entire program ends. Accesseble anywherw in the program. Shared across all functions easily.
# local variable: Declered inside a specific function. Created on function call; destroyed on return. Accessible only within its own function. Not shared with other function.

# Local Variables: A local varible is isolated inside its function environment. if yo try to access a local variable from outside its function, Python will raise a NameError.
# Example:
# Ex 1:
def my_function():
    local_val = "I am loacl!" # local variable
    print(local_val)
my_function()

# This will caesh the program:
# print(Local_val)
# Error: NameError: name 'Local_val' is no defined

# Ex 2:
def my_function():
    # This is a Local variable
    massage = "Hello from inside the function!"
    print(massage) # works perfectly here

# call the function
my_function()

# Trying to access the local variable outside the function
# print(message) # output: NameError: name 'message' is not defined

# Ex 3:
def greet():
    msg = "Hello!"
    print("Inside function: ", msg)

greet()
# print("Outside function:",msg) # NameError: 'msg' is not defined

# Global variable: Global variables are declared outside all functions and can be accessed anywhere in the program, including inside functions.

# Example:
# Ex 1:
msg = "python is awesome!"

def display():
    print("Inside function:",msg)
display()
print("Outside function:",msg)

# Ex 2:
# This is a global variible
counter = 20

def update_countee():
    global counter # Declares that we want change the global variable
    counter = 40 # Modified the global variable

print("Before:", counter) # prints 20
update_countee()
print("After:",counter) # prints 40

# Use of Local and Global variables: If a variable is defined both globally and locally with the same name, local variable shadows the global variable inside the function. Changes to the local variable do not affect the global variable unless explicitly declare variable as global.
# Example:
# Ex 1:
def function():
    s = "I like."
    print(s)
s = "I am also love."
function()
print(s)

# Modifying Global Variables Inside a function:By default, one cannot modify a global variable inside a function without declaring it as global. If you try, Python will raise an error because it treats variable as local. To modify a global variable use the global keyword.
# Example:
# Without global (causes error):
# def function():
#     s += 'GFG' # Error: python thinks s is local
#     print(s)
# s = "I like interseptor"
# function() # Output: UnboundLocalError: cannot access local variable 's' where it is not associated with a value

# Ex 2:
# With global (works correctly)
s = "Interseptor 650 is my favorite bike"

def function():
    global s
    s += "Hunter also" # Modify global variable
    print(s)
    s = "My favorite bike is Interseptor 650 and Hunter 350" # Reassign global
    print(s)

function()
print(s)

# Ex 3:
# Global vs Local with Same Name:
a = 2 # Global variable

def f():
    print("f():",a) # User global a

def g():
    a = 6 # Local shadows global
    print("g():",a)

def h():
    global a
    a = 8 # Modifies global a
    print("h():",a)

print("global:",a)
f()
print("global:",a)
g()
print("global:",a)
h()
print("global:",a)

# Ex 4:
x = 30

def my_function():
    y = 74
    print(y)

my_function()
print(x)