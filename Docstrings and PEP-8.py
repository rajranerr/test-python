# Docstrings: Python docstring are the stringb literrals that appear night after the defininmg of a function, method, class or module.
# Ex:
def square(n):
    """"takes in a number n, returns the squer of n"""
    print(n**2)
square(6)
print(square.__doc__)

# Ex:
class Robot:
    """
    A class to represent a simple mobile robot.
    
    Attrributes:
        name (str): The name of the robot.
        battery (int): Remaining battery percentage.
    """
    def __int__(self, name):
        """Initialize the robot with a name and full battery."""
        self.name = "bartin"
        self.battery = 100        
print(Robot.__doc__)

# Ex:
def cube(n):
    """ A number is taking  n, return cube of n"""
    print(n**3)
cube(4)
print(cube.__doc__)

# Ex:
print(print.__doc__)

# Ex:
import pickle
print(pickle.__doc__)

# Ex:
def add_binary(a, b):
    '''
    Return the sum of two decumal number in binary digits.
    
            Parameters:
                    a (int): A decimal integer
                    b (int): Another decimal integer
            Returns:
                    binary_sum (str): Binary string of the sum of a and b 
    '''
    binary_sum = bin(a+b)[2:]
    return binary_sum

print(add_binary.__doc__)

# PEP 8: PEP 8 is the primary style guide for writing clean code, while docstring (governed by PEP 257) are specifically used for documentation.

# PEP 8 (The Style Guide)

# PEP 8 provides recommendations on how to format code to ensure it is readable and consistent across the community.

# Indentation: Always use 4 spaces per level, never tabs.

# Naming Conventions:

# Functions & Variables: Use snake_case.
# Classes: Use PascalCase (CapWords).
# Line Length: Limit code to 79 characters.
# Whitespace: Put spaces around operators (e.g., x = y + 1), but not immediately inside parentheses.

# Ex:

def calculate_area(radius):
    """
    calculate the area of a circle.
    
    Args:
        radius (float): The radius of the circle.
        
    Returns:
        float: The calculated area.
    """
    import math
    return math.pi * (radius ** 2)
print(calculate_area.__doc__)

# EX:
class Person:
    """
    A class to represent a person.
    
    ...
    
    Attributes
    -----------
    name : str
        first name of the porson
    surname : str
        family name of the person 
    age : int 
        age of the person 
        
    methods
    --------
    info(additional=""):
        print the person's name and age.
    """
    def __init__(self, name, surname, age):
        """
        constructs all the necessary attributes for the person object.
        
        parameters
        -----------
            name : str
                first name of the person
            surname : str
                family name of the person
            age : int
                age of the person 
        """
        self.name = "ALice"
        self.surname = "stark"
        self.age = 23
def info(self, additional=""):
    """
    Prints the person's name and age.
    
    If the argument 'additional' is passsed, then it is appended after the main info.
    
    Parameters
    -----------
    addisional : str, optional
        more info to be displayed (dafault is none)
        
    Returns
    --------
    None
    """
    print(f'My name is {self.name} {self.surname}. I am {self.age} years old.' + additional)
    print(info.__doc__)
# PEP 8: PEP 8 is the official Style Guide for Python Code, providing a set of conventions to ensure Python code is readable, consistent, and "Pythonic".
#         Originally written in 2001 by Guido van Rossum, Barry Warsaw, and Nick Coghlan, it centers on the principle that "code is read much more often than it is written".
