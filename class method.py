# Class Method: A class method  in Python is a method that is explicitly bound to the class itself rather than to individual instances of that class. It receives the class namespace as its implicit first argument, allowing it to modify or access class-level data across all instances. 

# Basic Code Example:

class Book:
    # Class-level attribute shared by all instances
    total_books = 0

    def __init__(self, title):
        self.title = title
        # Accessing class variable to track objects
        Book.total_books += 1

    @classmethod
    def get_total_books(cls):
        # 'cls' refers to the Book class namespace
        return f"Total books in library: {cls.total_books}"

# Creating class instances
book1 = Book("Python Basics")
book2 = Book("Advanced OOP")

# Calling the class method directly on the class
print(Book.get_total_books())

# Primary Use Cases
# 1. Alternative Constructors (Factory Methods): Class methods are heavily used in Python to instantiate objects using different types or formats of input data.
# 2. Maintaining Class State: Tracking statistics, registries, or shared global configurations that affect all instances equally. 

# Example: Creating an Alternative Constructor

class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, data_string):
        """Parses a hyphenated string to construct a User instance."""
        name, age_str = data_string.split("-")
        # cls(...) dynamically calls the __init__ constructor
        return cls(name, int(age_str))

# Standard instantiation
user1 = User("Kavya", 18)
print(user1.name)
print(user1.age)

# Factory method instantiation from raw string data
user2 = User.from_string("kritika-19")
print(user2.name)
print(user2.age)

# Ex:

class Geeks:
    course = 'DSA'
    list_of_instances = []

    def __init__(self, name):
        self.name = name
        Geeks.list_of_instances.append(self)

    @classmethod
    def get_course(cls):
        return f"Course: {cls.course}"

    @classmethod
    def get_instance_count(cls):
        return f"Number of instances: {len(cls.list_of_instances)}"

    @staticmethod
    def welcome_message():
        return "Welcome to classes!"

# Creating instances
g1 = Geeks('Kritika')
g2 = Geeks('Raj')

# Calling class methods
print(Geeks.get_course())  
print(Geeks.get_instance_count())  

# Calling static method
print(Geeks.welcome_message())

# Ex:

class Student:

    # create a variable
    name = "Kritika"

    # create a function
    def print_name(obj):
        print("The name is : ", obj.name)


# create print_name classmethod
# before creating this line print_name()
# It can be called only with object not with class
Student.print_name = classmethod(Student.print_name)

# now this method can be called as classmethod
# print_name() method is called a class method
Student.print_name()

# Ex:

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def from_string(cls, date_string):
        year, month, day = map(int, date_string.split('-'))
        return cls(year, month, day)
    

date = Date.from_string('2010-10-09')
print("Day: ", date.day)
print("Month: ", date.month)
print("Year: ", date.year)