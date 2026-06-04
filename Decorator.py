# Decorator:decorator is a design pattern that allows you to modify or extend the behavior of a function or method without changing its actual source code.
# Basic Decorator Structure: For exaThe @decorator_name syntax is a clean shorthand (syntactic sugar) for passing your target function through the decorator function.
# Ex:
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()

# Handling Arguments with *args and **kwargs: If your target functions accept parameters, your inner wrapper function must also accept them. Using *args and **kwargs ensures your decorator can wrap any function, regardless of its arguments. 
# Ex:
def log_decorator(func):
    def wrapper(*arg, **kwargs):
        print(f"Running {func.__name__} with arguments {arg} and {kwargs}")
        result = func(*arg, **kwargs)
        print(f"{func.__name__} finished execution.")
        return result
    return wrapper

@log_decorator
def add_numbers(a, b):
    return a + b
print(add_numbers(20, 50))