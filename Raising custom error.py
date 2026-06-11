# Raising Custom errors
# In python, we can raise custom errors by using the raise keyword.

salary = int(input("Enter salary amount: "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")

# In the previous tutorial, we learned about different built-in exceptions in Python and why it is important to handle exceptions. However, sometimes we may need to create our own custom exceptions that serve our purpose.

# 1. Defining Custom Exceptions: We can define custum exceptions by ceating a new class that is derived from the built-in Exception class. 

# Ex:
class MyCustomError(Exception):
    """Exception raised for specific application errors."""
    
    def __init__(self, message, error_code):
        super().__init__(message)
        self.error_code = error_code

    def __str__(self):
        return f"{self.message} (Error code: {self.error_code})"

# Ex: 
class MyCustomError(Exception):
    """Exception raised for custom error scenarios.
    
    Attributes:
        message -- explanation of the error
    """
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

# 2. Raise the Exception: You trigger the exception using the raise keyword followed by an instance of your class. You can optionally pass a custom error message to it.

# Ex:
def check_value(x):
    if x < 0:
        raise MyCustomError("Value cannot be negative!")
    
# Example usege
try:
    check_value(-1)
except MyCustomError as e:
    print(f"Caught an error: {e}")

# 3. Handling Custom Exceptions: Custom exceptions can be handled similar to built-in exceptions using a `try...except` block.

# Ex:
class FileProcessingError(Exception):
    def __init__(self, message, filename, lineno):
        super().__init__(message)
        self.filename = filename
        self.lineno = lineno

    def __str__(self):
        return f"{self.message} in {self.filename} at line {self.lineno}"


try:
    raise FileProcessingError("Syntax error", "example.txt", 13)
except FileProcessingError as e:
    print(f"Caught an error: {e}")