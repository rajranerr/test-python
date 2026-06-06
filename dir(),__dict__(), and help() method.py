# dir(), __dict__, and help() method: dir(), __dict__, and help() are built-in introspection tools used to examine the attributes, methods, and documentation of objects.

# The dir() Function
# 1. dir() : The dir() function returns a list of all the attributes and methods (including dunder methods) available for an object. It is a useful tool for discovering what you can do with an object.

# Example:
# Check method available for a regular list
numbers = [1, 2, 3, 4, 5, 6]
print(dir(numbers))

# The __dict__ attribute
# 2. __dict__: _dict _: The __dict__ attribute return a dictionary representation of an object's attributes. It is a useful tool for introspection.
# Example:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person("Kyara", 18)
print(p1.__dict__)
# Check user-defined attributes

# The help() Function
# help(): The help() function is used to get help documentation for an object, including a description of its attributes and methods.
# Example: 
help(list.append)

# Ex:
print(help(str))

# Ex:
print(help(Person))