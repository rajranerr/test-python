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