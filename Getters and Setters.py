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
# emp.salary = -1000  # Raises ValueError: Salary cannot be negative!
# print(emp.salary)

# Alternative Method: The Traditional Way (Not Recommended)
# Ex:
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary

    def get_salary(self):
        return self._salary
    def set_salary(self, value):
        if value >= 0:
            self._salary = value


# Getter:  The getter method is used to retrieve the value of a private attribute. It allows controlled access to the attribute.

# Setter: The setter method is used to set or modify the value of a private attribute. It allows you to control how the value is updated, enabling validation or modification of the data before it’s actually assigned.

# Using normal function:
# Ex:
class Geek: 
	def __init__(self, age = 0): 
		self._age = age 
	
	# getter method 
	def get_age(self): 
		return self._age 
	
	# setter method 
	def set_age(self, x): 
		self._age = x 

raj = Geek() 

# setting the age using setter 
raj.set_age(21) 

# retrieving age using getter 
print(raj.get_age()) 

print(raj._age)

# Using property() function
# Ex:
class Geeks: 
	def __init__(self): 
		self._age = 0
	
	# function to get value of _age 
	def get_age(self): 
		print("getter method called") 
		return self._age 
	
	# function to set value of _age 
	def set_age(self, a): 
		print("setter method called") 
		self._age = a 

	# function to delete _age attribute 
	def del_age(self): 
		del self._age 
	
	age = property(get_age, set_age, del_age) 

mark = Geeks() 

mark.age = 18

print(mark.age)

# Using @property decorators
# Ex:
class Geeks: 
	def __init__(self): 
		self._age = 0
	
	# using property decorator 
	# a getter function 
	@property
	def age(self): 
		print("getter method called") 
		return self._age 
	
	# a setter function 
	@age.setter 
	def age(self, a): 
		if(a < 18): 
			raise ValueError("Sorry you age is below eligibility criteria") 
		print("setter method called") 
		self._age = a 

mark = Geeks() 

mark.age = 21

print(mark.age)