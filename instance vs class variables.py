# Instance Variable: 1. instance variables hold data unique to each specific object instance.
# 2. tied to a specific object.
# 3. Defined inside method (usually __init__) using self.
# 4 New copy created for every object.
# 5. Unique attributes (e.g., names, IDs).

# Class Variable: 1.class variable are shared by all instances of a class.
# 2. Tied to the class itself.
# 3. Defined directly inside the class body.
# 4. Only one copy shared across all objects.
# 5. Shared data/constants (e.g., configurations).

# Code Example:
class Employee:
    # class variable (Shared by all employees)
    company_name = "TechCorp"

    def __init__(self, name, salary):
        # Instance Variables (Unique to each employee)
        self.name = name
        self.salary = salary

# Create two separate instances
emp1 = Employee("kavya", 80000)
emp2 = Employee("Ramesh", 100000)

# 1. Accessing Instance Variable
print(emp1.name)
print(emp2.name)
print(emp1.salary)
print(emp2.salary)

# 2. Accessing Class Variables
print(emp1.company_name)
print(emp2.company_name)
print(Employee.company_name)

# Pitfalls with Modification

# 1. Modifying via the class Name (Affects Everyone)

# Ex:
Employee.company_name = "AWS"
print(emp1.company_name)
print(emp2.company_name)

# 2. Modifying via an Instance (Creates a Shadow Copy)
emp2.company_name = "Rajesh"
print(emp1.company_name)
print(emp2.company_name)

# 3. mutable Class Variable (The Danger Zone)

class ShareData:
    items = [] # Mutable class variable

obj1 = ShareData()
obj2 = ShareData()

obj1.items.append("Apple") # Modifies the shared list in-place
print(obj2.items)