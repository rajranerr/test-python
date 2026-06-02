# Import: The import statement  allows your code in one file to access code from another module or package. Under the hood, it performs two distint operations: searching for thr module and binding the results to alocal namespace.

# The Three-step process Behind the scenes

# when you run import abc, python automaticlly triggers a three-step lifecycle:
# 1. checking the cache: Before searching your hard drive, Python checks the sys.modules dictionary.
# If the module was alrady imported earlier, python skips the remaining step and reuses the existing module oject.
# This caching mechanism ensures that a modules is only executed once per program, preventing performance lag and duplicate code executions.
# 2. searching for the module: If the module is not found in the cache, python import machinery searches for the physical file using the directory path listed in sys.path. It scans these locations in strict order.
            # 1. The current directory: The folder where your entry-point script is running.
            # 2. The standard library: A collection of built-in modules that come with python.
            # 3. Third-party packages: If you have installed any external libraries using pip.
            # 4. PYTHONPTH: An optional environment variable cantaining custom user paths.
# 3. Loading, Executing and binding: Once Python finds the corresponding .py file, it builds a module object, runs all the top-level code inside that file, and populates the module's namespace. Finally, it binds this namespace to a variable name in your current file so you can access its contents.

# Common import Syntaxes: You can import elements using different keywords based on your structure needs:
# 1. import module_name: This is the most basic form of import. It imports the entire module and you can access its contents using dot notation.
# Ex:
import math
print(math.sqrt(16))

# 2. from module_name import specific_element: This syntax allows you to import specific functions, classes, or variables directly into your current namespace, eliminating the need for dot notation.
# Ex:
from math import sqrt
print(sqrt(25)) 

# 3. from module_name import *: This syntax imports all public elements from the module into your current namespace. However, it is generally discouraged because it can lead to name clashes and make your code less readable.
# Ex:
from math import *
print(sin(pi/2))

# 4. import module_name as alias: This syntax allows you to give a module a shorter or more convenient name (alias) for easier access.
# Ex:
import numpy as np
array = np.array([1, 2, 3])
print(array)

import pandas as pd
data = pd.DataFrame({'A': [1, 2], 'B': [3, 4]})
print(data)