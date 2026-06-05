# Static Method: A static method  in Python is a method that belongs to a class but does not have access to any class-specific state or instance-specific data. It is defined using the @staticmethod decorator and behaves exactly like a plain, regular function, except that it lives inside a class's namespace. 

# Unlike instance methods or class methods, a static method does not receive an implicit first argument like self or cls. 

# Code Example:
# You can call a static method directly using the class name, without instantiating an object. 

class Check:
    @staticmethod
    def is_even(n):
        return n % 2 == 0
    
print(Check.is_even(8))

# Ex:
class Calculate:
    @staticmethod
    def add(a, b):
        return a + b
    
result = Calculate.add(62, 20)
print(result)

# Ex:
class Temperature:
    @staticmethod
    def to_fahrenheit(c):
        return (c * 9/5) + 32
    
print(Temperature.to_fahrenheit(30))

# Ex:
class Person:
    @staticmethod
    def is_adult(age):
        return age >= 18

print(Person.is_adult(17))
print(Person.is_adult(21))