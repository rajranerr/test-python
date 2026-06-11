# super() function: super() function is a built-in function used to access and call methods from a parent (superclass) inside a child class (subclass). It returns a temporary proxy object of the parent class, allowing you to reuse logic and extend its behavior without hardcoding the parent class name.

# 1. Basic Single Inheritance Usage: The most common use case is calling the parent class constructor (__init__) to initialize inherited attributes.
# Ex:
class Animal:
    def __init__(self,name):
        self.name = name

class Dog(Animal):
    def __init__(self, name, breed):
        # Call the parent class constructor to set the name
        super().__init__(name)
        self.breed = breed

# Create an instance
my_dog = Dog("Moti", "Germon Sheferd")
print(my_dog.name)
print(my_dog.breed)

# 2. Overriding Regular Methods: You can also use super() to extend a regular method that already exists in the parent class instead of completely erasing it.
# Ex:
class Employee:
    def greet(self):
        return "Hello, welcome to the company!"
    
class Manager(Employee):
    def greet(self):
        # Fetch the original message from Employee, then add to it
        original_msg = super().greet()
        return f"{original_msg} As a Manager, let's schedule a meeting."
    
mgr = Manager()
print(mgr.greet())

# 3. Multiple Inheritance & MRO: In multiple inheritance, Python decides which class to check next using the Method Resolution Order (MRO). You can inspect this order using the __mro__ attribute. super() does not simply look "up" to the immediate parent; it looks at the next class lined up in the MRO sequence.

class A:
    def process(self):
        print("Process A")

class B(A):
    def process(self):
        print("Process B")
        super().process()

class C(A):
    def process(self):
        print("Process C")
        super().process()

class D(B, C):
    def process(self):
        print("Process D")
        super().process()
    
# Initialize D
obj = D()
obj.process()