# List mathods

#  List.sort(): This mathod sorts the ascending order. The original list is updated
print("1. List.sort Examples: ")
# Ex:
colors = ["black", "white", "blue", "orange", "voilet"]
colors.sort()
print(colors)

# Ex:
num = [4,6,2,5,1,2,1,2,8,9,7]
num.sort()
print(num) 

# reverse(): This method reverses the order of the list.
print("2. reverse Examples: ")
# Ex:
colors.reverse()
print(colors)

# Ex:
num.reverse()
print(num)

# index(): This method returns the idex of the first occurrence of the list item.
print("index Example: ")
# Ex:
print(colors.index("black"))

# Ex:
print(num.index(8))

# count(): Returns the count of the number of the items with the given value.
print("count Examples: ")
# Ex:
print(colors.count("white"))

# Ex:
print(num.count("9"))

# copy(): Return copy of the list. This can be done to perform operation on the list without modifying the original list.
print("Examples of copy: ")
# Ex:
newlist = colors.copy()
print(colors)
print(newlist)
# Ex:
newnum = num.copy()
print(num)

print(newnum)

# append(): This methode items to the end of the existing list.
print("Examples of append: ")
# Ex:
colors.append("indigo")
print(colors)

# Ex:
num.append(12)
print(num)

# insert(): This method inserts an item at the given index. User has to specify index and the item to be inserted within the insert() method .
print("Example of insert(): ")
# Ex:
colors = ["voilet", "indigo","blue"]
#            [0]      [1]      [2]

colors.insert(1, "black") # insert item at index
# updated list colors is:
print(colors) # output: ["voilet", "black", "indigo", "blue"]
#                  [0]      [1]         [2]      [3]

# extend(): This mathod adds an entire list or any other collection datatype (set, tuple, dictionary) to the existing list.
print("Example of extebd(): ")
# Ex:
colors = ["voilet", "indigo", "black"]
rainbow = ["red", "blue", "yellow", "orange", "green"]
colors.extend(rainbow)
print(colors)

# Concatenating two lists: You can simply concatenate two list to join two list.
# Ex:
colors = ["yellow", "blue", "black", "white"]
colors2 = ["red", "green", "orange", "voilet", "gray", "silver"]
print(colors + colors2)

# Examples:
# Ex 1:
import math
pie = math.pi
print("The value of pi is: ", pie)

# Ex 2:
import pandas
# Create a simple DataFrame
data = {'Name': ['Alice', 'Bob', 'Charlie'], 'Age': [25, 30, 35]}
df = pandas.DataFrame(data)
print(df)

# Importing specific Functions: Instead of importing the entire module, you can import specific functions, classes, or variables directly into your current namespace using the from keyword. This allows you to use them without the module prefix.
# Ex 1:
from math import sqrt
print("The square root of 16 is: ", sqrt(16))
# Ex 2:
from datetime import datetime
now = datetime.now()
print("Current date and time: ", now)
# Ex 3:
from math import pi
print("The value of pi is: ", pi)

# Importing Modules with Aliases: To avoid naming conflicts or to shorten the module name, you can use the as keyword to create an alias for the imported module.
# Ex 1:
from math import sqrt as square_root
print("The square root of 25 is: ", square_root(25))
# Ex 2:
import numpy as np
array = np.array([1, 2, 3])
print("NumPy array: ", array)   
# Ex 3:
import pandas as pd
data = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
print("Pandas DataFrame: ")
print(data)
# Ex 4:
import math as m
result = m.sqrt(49)
print("The square root of 49 is: ", result)

# Imorting Everything from a Module (*): You can use the from module_name import * syntax to import all public elements from a module into your current namespace. However, this practice is generally discouraged because it can lead to name clashes and make your code less readable.
# Ex 1:
from math import *
print(pi) # Accessing the constant 'pi'
print(factorial(5)) # Accessing the function 'factorial'
print(sin(pi/2)) # Accessing the function 'sin'
# Ex 2: 
from datetime import *
now = datetime.now()
print("Current date and time: ", now)

# Handling Import Errors: When you try to import a module that doesn't exist or has a typo in its name, Python raises an ImportError. You can handle this error using a try-except block to provide a more user-friendly message or to take alternative actions.
# Ex 1:
# try:
    # import mathematics # Incorrect module name
    # print(mathematics.pi)
# except ImportError:
    # print("The module 'mathematics' could not be found. Please check the module name and try again.")