# Inheritance:Inheritance is a fundamental concept in object-oriented programming (OOP) that allows a class (called a child or derived class) to inherit attributes and methods from another class (called a parent or base class).
# Ex:
class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Animal name:", self.name)

class Dog(Animal):
    def sound(self):
        print(self.name, "barks")

d = Dog("Buddy")
# Inherited method
d.info()     
d.sound()

# super() Function:
# Ex:
# Parent Class: Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def info(self):
        print("Animal name:", self.name)

# Child Class: Dog
class Dog(Animal):
    def __init__(self, name, breed):
        # Calls constructor based on MRO
        super().__init__(name)  
        self.breed = breed

    def details(self):
        print(self.name, "is a", self.breed)

d = Dog("Moti", "Golden Retriever")
d.info()      # Parent method
d.details()   # Child method

# Types of Inheritance:Types of Inheritance depend upon the number of child and parent classes involved. There are four types of inheritance:

# Single Inheritance
# Ex:
# Base class
class Parent:
    def func1(self):
        print("This function is in parent class.")

# Derived class
class Child(Parent):
    def func2(self):
        print("This function is in child class.")

# Driver code
obj = Child()
obj.func1()
obj.func2()

# Multiple Inheritance
# Ex:
# Base class 1
class Mother:
    mothername = ""

    def mother(self):
        print(self.mothername)

# Base class 2
class Father:
    fathername = ""

    def father(self):
        print(self.fathername)

# Derived class
class Son(Mother, Father):
    def parents(self):
        print("Father: ", self.fathername)
        print("Mother: ", self.mothername)

# Driver code
s1 = Son()
s1.fathername = "Rajesh"
s1.mothername = "Kavya"
s1.parents()