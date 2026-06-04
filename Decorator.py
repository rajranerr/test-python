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

# Preserving Function Identity with functools.wraps
# Ex:
from functools import wraps

def preserve_meta(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper

# Decorators That Accept Arguments:To pass arguments directly into a decorator (e.g., @repeat(num_times=3)), you need a third nested layer. The outermost function acts as a "decorator factory" that returns the actual decorator. 
# Ex:
def repeat(num_times):
    def decorator_repeat(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for _ in range(num_times):
                result = func(*args, **kwargs)
            return result
        return wrapper
    return decorator_repeat

@repeat(num_times=2)
def greet(name):
    print(f"Hello {name}")

greet("Maria")