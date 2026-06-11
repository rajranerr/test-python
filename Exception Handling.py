# Exception Handling: Exception handling is the process of responding to unwanted or unexepted events when a computer program runs. Exception handling deals with these events to avoid the program pr system crashing, and without this process, exception would disrupt the normal operatiom of a program.

# Exceptions: python has many built-in exceptions that are raised when your program encounters an error (somethong in the program goes wrong).

#  When these exceptions occur, the python interpreter stops the current process and passes it to the calling program until it is handled. if not handled the program will crash.

#  Python try...except:

# try..... except blocks are used in python to handle error and exceptions. The code in try block runs when there is no error. If the try block catches the error, then the except block is executed.

# Syntex:
# try: 
    # statements which could generate 
    # exception
# except:
    # soloution of generated exception

# Ex:
try:
    num = int(input("Enter an integer: "))
except ValueError:
    print("Number entered is not an integer.")

# Ex:
# try:
#     num = int(input("Enter an integer: "))
#     a = [6, 4]
#     print(a[num])
# except ValueError:
#     print("Number entered is not an integer.")
# except ImportError:
#     print("Index Error") # output: IndexError: list index out of range

# Finally keyword
# finally Clause:The finally code block is also a part of exception handling. When we handle exception using the try and except block, we can include a finally block at the end. The finally block is always executed, so it is generally used for doing the concluding tasks like closing file resources or closing database connection or may be ending the program execution with a delightful message.

# Syntax:
# try:
#     # statements which could generate
#     # exception
# except:
#     # solution of generated evception
# finally:
    # block of code which is going to 
    # execute in any situstion

# The finally block is executed irrespective of the outcome of try ...... except ..... else blocks
# One of the important use cases of finally block is in a function which returns a value.

# Ex:
def func1():
    try:
        l = [1, 3, 6, 8, 4]
        i = int(input("Enter the index: "))
        print(l[i])
        return 1
    except:
        print("Some error occurred")
        return 0
    
    finally:
        print("I am always executed")

x = func1()
print(x)

# Examples:

# 1. Catching Specific Exceptions: Catching specific exceptions makes code to respond to different exception types differently. It precisely makes your code safer and easier to debug. It avoids masking bugs by only reacting to the exact problems you expect.

# Ex: This code handles ValueError and ZeroDivisionError with different messages.
try:
    # This will cause ValueError
    x = int("str")
    inv = 1 / x # Inverse calculation

except ValueError:
    print("Not Valid")

except ZeroDivisionError:
    print("Zero has no inverse!")

# 2. Catching Multiple Exceptions: We can catch multiple exceptions in a single block if we need to handle them in the same way or we can separate them if different types of exceptions require different handling.

# Ex:  This code attempts to convert list elements and handles ValueError, TypeError and IndexError.
a = ["10", "twenty", 30]
try:
    # 'twenty' cannot be converted to int
    total = int(a[0]) + int(a[1])

except (ValueError, TypeError) as e:
    print("Error", e)

except ImportError:
    print("Index out of range.")

# 3. Catch-All Handlers and Their Risks: Catch-all handler is used to call to catch any exception (similar to else statement). Use only except keyword to define it:

# Ex: This code tries dividing a string by a number, which causes a TypeError.
try:
    # Risky operation: dividing string by number
    res = "200" / 10

except ArithmeticError:
    print("Arthmetic problem.")

except:
    print("Something went wrong!")

# Raise an Exception: We raise an exception in Python using the raise keyword followed by an instance of the exception class that we want to trigger. We can choose from built-in exceptions or define our own custom exceptions by inheriting from Python's built-in Exception class.

# Basic Syntax:
#       raise ExceptionType("Error message")

# Ex: This code raises a ValueError if an invalid age is given.
def set(age):
    if age < 0:
        raise ValueError("Age cannot be negative.")
    print(f"Age set to {age}")

try:
    set(-5)
except ValueError as e:
    print(e)