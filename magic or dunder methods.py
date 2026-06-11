# Magic or Dunder Methods: Magic methods, also known as dunder methods (short for double underscore), are special built-in methods in Python that start and end with two underscores (e.g., __init__). They are not meant to be called directly; instead, they are invoked automatically by the Python interpreter to handle specific built-in operations, functions, or operators. 

# 🔑 The 3 Most Critical Dunder Methods

# Almost every custom Python class benefits from implementing these three baseline methods: 
#  1. __init__(self, ...) — Object Initialization: The initializer method called automatically when a new instance of a class is created.
#  2. __str__(self) — User-Friendly String: Controls what is returned when str(obj) or print(obj) is called.
#  3. __repr__(self) — Developer Debug String: Returns an unambiguous, machine-readable string representation of the object, which is vital for logging and debugging.

# Ex:
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}')"
    
my_book = Book("1997", "Harry Potter")
print(my_book)
print(repr(my_book))

# 🗂️ Categorized Cheat Sheet of Common Dunder Methods

# ⚙️ Object Creation & Lifecycle

#  1. __new__(cls, ...) — Allocates memory and creates the actual object instance before __init__ is run.
#  2. __del__(self) — The destructor method; invoked right before an object's memory is garbage collected. 

# ⚖️ Comparison Operators

# These allow you to use standard mathematical comparison operators directly on your custom objects:

#  1. __eq__(self, other) — Implements equality (==).
#  2. __ne__(self, other) — Implements inequality (!=).
#  3. __lt__(self, other) — Implements less than (<).
#  4. __gt__(self, other) — Implements greater than (>).
#  5. __le__(self, other) — Implements less than or equal to (<=).
#  6. __ge__(self, other) — Implements greater than or equal to (>=). 

# Ex:
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price
    
p1 = Product("Shirt", 800)
p2 = Product("Jeans", 800)
p3 = Product("Shoes", 1200)

print(p1 == p2)
print(p1 < p3)

# ➕ Arithmetic & Math Operators

# These manage how your objects behave when used with standard arithmetic calculations: 

#  1. __add__(self, other) — Implements addition (+).
#  2. __sub__(self, other) — Implements subtraction (-).
#  3. __mul__(self, other) — Implements multiplication (*).
#  4. __truediv__(self, other) — Implements standard float division (/).
#  5. __floordiv__(self, other) — Implements integer floor division (//).

#  📦 Container & Sequence Types
#  Use these to make your objects work exactly like lists, tuples, or dictionaries: 
 
#  1.__len__(self) — Invoked when calling len(obj) to return the size of the object.
#  2.__getitem__(self, key) — Allows indexing and key lookups, like obj[key].
#  3.__setitem__(self, key, value) — Handles index/key assignments, like obj[key] = value.
#  4.__contains__(self, item) — Implements the in operator to check membership. 
 
# Ex:
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        # Enables adding two Vector objects together
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
v1 = Vector(69, 92)
v2 = Vector(95, 74)
print(v1 + v2) 

#  🔄 Iterables & Context Managers
#  1. __iter__(self) — Returns an iterator object when your object is passed into a for loop.
#  2. __next__(self) — Fetches the next item in an iteration cycle.
#  3. __enter__(self) / __exit__(self, ...) — Defines setup and breakdown rules for using your object inside a with block (context manager). 

# Example:
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # custom official string representation for debugging
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"
    
    # Overloading the addition (+) operator
    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented
    
    # Overloading the equality (==) operator
    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y
        return False
    
# Usage:
v1 = Vector(62, 80)
v2 = Vector(36, 93)

# 1. Triggers __add__ automatically behind the scenes
v3 = v1 + v2
print(v3)

# 2. Trigger __eq__ automatically behind the scenes
print(v1 == v2)
print(v1 == Vector(62, 80))