# Getters and Setters: getters and setters are methods used to protect, validate, and control access to an object's internal data. Unlike languages like Java or C++, where you must explicitly write getX() and setX() methods, Python uses the @property decorator to implement them cleanly. This allows you to manage data behind the scenes while keeping standard dot-notation syntax (like obj.value) for the user. 

# The Pythonic way: Using @property :The @property decorator transforms a method into a read-only "getter". To add a "setter", you use the @<attribute_name>.setter decorator.
# Ex:
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary # Single underscore suggests a protected/internal attribute

    # The Getter
    @property
    def salary(self):
        print("Ferching salary...")
        return self._salary
    
    # The Setter
    @salary.setter
    def salary(self, new_salary):
        print("Validating salary update...")
        if new_salary < 0:
            raise ValueError("Salary cannot be negative!")
        self._salary = new_salary

emp = Employee("Alice", 50000)

# 1. Accesses data through the getter smoothly without using parentheses ()
print(emp.salary)  # Triggers the getter logic

# 2. Modifies data through the setter using standard assignment
emp.salary = 60000  # Triggers validation inside the setter
print(emp.salary)
# 3. Triggers validation failure
emp.salary = -1000  # Raises ValueError: Salary cannot be negative!
print(emp.salary)