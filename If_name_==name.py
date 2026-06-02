# if __name__ == "__main__": is a conditional statement used to ensure that a block of code runs only when the script is executed directly, and not when it is imported as a module into another file.
# How it works: Before executing the code, the python interpreter defines a few special variables. One of these is __name__:

# Running a script directly: When you run a python file directly (e.g., python my_script.py), the interpreter sets __name__ to "__main__". This indicates that the script is being executed as the main program.
# Importing a script as a module: When you import a python file as a module (e.g., import my_script), the interpreter sets __name__ to the name of the module (e.g., "my_script"). This indicates that the script is being used as a library or component in another program.

# Code Example:
def add(a, b):
    return a + b

# This block acts as a test or demo environment
if __name__ == "__main__":
    print("Running math_helper.py directly")
    result = add(5, 3)
    print(f"Test result: {result}")

# Scenario 1: Running the script directly
# If you execute the file from your terminal:
# python math_helper.py
# Output:   Running math_helper.py directly!
#           Test result: 8

# Scenario 2: Importing into another file
# If you have another file, say main.py, that imports math_helper.py:
# import math_helper
# print("Running main_add.py!")
# print(math_helper.add(10, 20))
# Output:   Running main_add.py!
#           30

# Examples:
# Ex 1:
def main():
    print("Application started.")
if __name__ == "__main__":
    main()
# Ex 2:
print("Always executed")
if __name__ == "__main__":
    print("Executed when invoked directly")
else:
    print("Executed when imported as a module")
# Ex 2:
def my_function():
    print("I am inside my_function.")
if __name__ == "__main__":
    my_function()