# Object-Oriented programming (OOPs): OOPs is a programming paradigm that structures code by bundling related data and behaviors into individual classes and objects. Instead of writing a pure sequence of instructions (procedural), OOP allows you to model real-world problems through logical software entities.

# Core Concepts: Classes and Objects:
# class: A user-defined blueprint or template used to create objects.
# Object: An actual instance created from a class blueprint that contains concrete data.
# __init__: The constructor method that initializes an object's state automatically upon creation.
# self: A reference pointer pointing directly to the specific object instance currently being processed. 

# Ex: 
class Smartphone:
    # constructor method to assign data attributes
    def __init__(self, brand, model):
        self.brand = brand     # Instance variable
        self.model = model     # Instance variable

    # Instance method showing behavior
    def call(self, number):
        return f"{self.brand} {self.model} is dialing {number}..."
# creating instance (Objects) of the class
phone1 = Smartphone("Apple", "iPhone 16")
phone2 = Smartphone("OnePlus", "Note CE2 Lite")
print(phone1.call("9303514504"))
print(phone2.call("7247535102"))

# The 4 Pillars of OOPs:An effective object-oriented architecture relies entirely on four foundational principles: 

# 1. Inheritance: Inheritance lets a new child class acquire all attributes and methods of an existing parent class to encourage reuse. 
# Ex:
# Parent class
class vehicle:
    def start(self):
        return "Engine started."
    
# Child Class inharits from Vehicle
class ElectricCar(vehicle):
    def charge(self):
        return "Battery charging."

tesla = ElectricCar()
print(tesla.start())   # Inherited method: "Engine started."
print(tesla.charge())  # Child methid: "Battery charging"

# 2. Polymorphism: Polymorphism allows different object classes to share the exact same method names but execute distinct custom actions. 
# Ex:
class Dog:
    def speak(self): return "Moti"
class Cat:
    def speak(self): return "Alice"

# Same interface invocation yields different behaviors
for animal in [Dog(), Cat()]:
    print(animal.speak())

# 3. Encapsulation: Encapsulation restricts direct external modifications by bundling data safely inside a class and using prefix underscores.
# Protected (_variable): Access convention warning for external developers.
# Private (__variable): Strict data hiding through implicit Python name mangling. 
# Ex:
class BankAccount:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance  # Private attribute

    def get_balance(self):        # Getter method to read data securely
        return self.__balance

account = BankAccount("Alex", 19000)
# print(account.__balance)       # Throws an AttributeError
print(account.get_balance())    

# 4. Abstraction: Abstraction hides deep structural backend complexities from users, revealing only clean, essential operational interfaces. It is implemented via Python's built-in abc module. 
# Ex:
from abc import ABC, abstractmethod

class PaymentGateway(ABC): # Abstract Base Class
    @abstractmethod
    def process_transaction(self, amount):
        pass

class Stripe(PaymentGateway):
    def process_transaction(self, amount):
        return f"Processing ${amount} smoothly via stripe API."
    
# gateway = PaymentGateway() # Errors out! cannot instantite abstract classes directly.
payment = Stripe()
print(payment.process_transaction(200))