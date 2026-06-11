# Constructor: In Python, a constructor is a special method that runs automatically when you create a new instance of a class, primarily used to initialize an object's state. While the __init__() method is commonly called the constructor because it initializes the object's attributes, Python technically separates object creation via __new__() from object initialization via __init__(). 
# Core Syntax of a Constructor: You define a constructor inside a class using the def __init__(self) keyword structure. The self parameter is a mandatory reference to the current object instance being created.
# Ex:
class Robot:
    # The constructor method
    def __init__(self, name, color):
        self.name = name # Instance variable
        self.color = color # Instance variable

# creating an instance (object) of the class
my_robot = Robot("Alex", "Silver")

print(my_robot.name)
print(my_robot.color)

# Types of Constructors:
# 1. Parameterized Constructor: A parameterized constructor accepts arguments to initialize the object's attributes with specific values.
# Ex:
class Bike:
    def __init__(self, make, model, year):
      
        #Initialize the Bike with specific attributes.
        self.make = make
        self.model = model
        self.year = year

# Creating an instance using the parameterized constructor
bike = Bike("Royal Enfield", "Hunter 350", 2025)
print(bike.make)
print(bike.model)
print(bike.year)

# 2. Default (Non-Parameterized) Constructor: A default constructor does not take any parameters other than self. It initializes the object with default attribute values.
# Ex:
class Bike:
    def __init__(self):
        
        # Initialize the Bike with default attributes
        self.make = "Royal Enfield"
        self.model = "Interseptor 650"
        self.year = 2025

# Creating an instance using the default constructor
bike = Bike()
print(bike.make)
print(bike.model)
print(bike.year)

# Example:
class SystemCheck:
    # Default / Non-parameterized constructor
    def __init__(self):
        self.status = "Healthy"

sys = SystemCheck()
print(sys.status)  

# Handling "Multiple" Constructors
# 1: Using Default Arguments: You can assign default fallback values to your parameters.
# Ex:
class User: 
    def __init__(self, username, role="Student"):
        self.username = username
        self.role =  role