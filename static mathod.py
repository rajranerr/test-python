# Static Method: A static method  in Python is a method that belongs to a class but does not have access to any class-specific state or instance-specific data. It is defined using the @staticmethod decorator and behaves exactly like a plain, regular function, except that it lives inside a class's namespace. 

# Unlike instance methods or class methods, a static method does not receive an implicit first argument like self or cls. 

# Code Example:
# You can call a static method directly using the class name, without instantiating an object. 

class MathUtils:
    @staticmethod
    def is_even(number):
        # Operates independently of class or instance data
        return number % 2 == 0

# Calling the static method directly on the class
result = MathUtils.is_even(8)
print(result)  
